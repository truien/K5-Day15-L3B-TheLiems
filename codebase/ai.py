"""Nối model — chỗ DUY NHẤT trong bản chạy thử gọi model AI.

Hợp đồng (giữ nguyên để khung đo được token):
    call_model(system: str, user: str) -> dict với 4 khoá:
        "text":       str   chữ model trả về
        "model":      str   tên model đã gọi (để tra giá ở bảng giá model)
        "tokens_in":  int   số token vào, lấy từ trường usage trong phản hồi API — KHÔNG ước lượng
        "tokens_out": int   số token ra, gồm cả token suy luận / suy nghĩ nếu API tính riêng
    @model_call (từ tracing.py) tự ghi mỗi lần gọi vào trace.

Hỗ trợ qua thư viện chuẩn (urllib), đọc cấu hình từ .env:
    MODEL_PROVIDER = fake | openai | anthropic | gemini | ollama
    MODEL_NAME     = mã gọi API của model
    API_KEY        = khoá API (không cần với fake / ollama)
    API_BASE_URL   = (tuỳ chọn) URL thay thế cho endpoint tương thích OpenAI / Ollama
"""
import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request

from tracing import model_call

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_env(path=os.path.join(ROOT, ".env")):
    """Đọc file .env (KEY=VALUE mỗi dòng) vào biến môi trường, không ghi đè biến đã có."""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env()
MODEL_PROVIDER = (os.environ.get("MODEL_PROVIDER") or "fake").strip().lower()
MODEL_NAME = (os.environ.get("MODEL_NAME") or "").strip()
API_KEY = (os.environ.get("API_KEY") or "").strip()
API_BASE_URL = (os.environ.get("API_BASE_URL") or "").strip()

SHOW_RAW = False  # đổi thành True để in nguyên phản hồi JSON của API khi debug

URL_OPENAI = "https://api.openai.com/v1/chat/completions"
URL_CLAUDE = "https://api.anthropic.com/v1/messages"
URL_OLLAMA = "http://localhost:11434/api/chat"
URL_GEMINI_TMPL = "https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent"


def post_json(url: str, headers: dict, body: dict, timeout: int = 60) -> dict:
    """Gửi POST JSON, trả về JSON phản hồi. Chỉ dùng thư viện chuẩn (urllib)."""
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        method="POST",
        headers=dict({"Content-Type": "application/json"}, **headers),
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise RuntimeError("HTTP %d: %s" % (e.code, e.read().decode("utf-8", "replace")[:300]))
    if SHOW_RAW:
        print(json.dumps(data, ensure_ascii=False, indent=2)[:3000])
    return data


def _require_config(need_key: bool = True):
    if not MODEL_NAME:
        raise RuntimeError("Thiếu MODEL_NAME trong .env (MODEL_PROVIDER=%s)" % MODEL_PROVIDER)
    if need_key and not API_KEY:
        raise RuntimeError("Thiếu API_KEY trong .env (MODEL_PROVIDER=%s)" % MODEL_PROVIDER)


def call_openai(system: str, user: str) -> dict:
    _require_config(need_key=True)
    url = API_BASE_URL or URL_OPENAI
    messages = ([{"role": "system", "content": system}] if system else []) + [
        {"role": "user", "content": user}
    ]
    body = {"model": MODEL_NAME, "messages": messages}
    if not re.match(r"^(o[134]|gpt-5)", MODEL_NAME, re.IGNORECASE):
        body["temperature"] = 0
    data = post_json(url, {"Authorization": "Bearer " + API_KEY}, body)
    u = data["usage"]
    choices = data.get("choices") or []
    content = ((choices[0].get("message") or {}).get("content") or "") if choices else ""
    return {
        "text": content,
        "tokens_in": int(u["prompt_tokens"]),
        "tokens_out": int(u["completion_tokens"]),
    }


def call_claude(system: str, user: str) -> dict:
    _require_config(need_key=True)
    url = API_BASE_URL or URL_CLAUDE
    data = post_json(
        url,
        {"x-api-key": API_KEY, "anthropic-version": "2023-06-01"},
        {
            "model": MODEL_NAME,
            "max_tokens": 1024,
            "system": system or "",
            "messages": [{"role": "user", "content": user}],
        },
    )
    text = "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")
    u = data["usage"]
    return {
        "text": text,
        "tokens_in": int(u["input_tokens"]),
        "tokens_out": int(u["output_tokens"]),
    }


def call_gemini(system: str, user: str) -> dict:
    _require_config(need_key=True)
    url = API_BASE_URL or (URL_GEMINI_TMPL % urllib.parse.quote(MODEL_NAME, safe=""))
    body = {
        "contents": [{"role": "user", "parts": [{"text": user}]}],
        "generationConfig": {"temperature": 0},
    }
    if system:
        body["systemInstruction"] = {"parts": [{"text": system}]}
    data = post_json(url, {"x-goog-api-key": API_KEY}, body)
    candidates = data.get("candidates") or []
    parts = (candidates[0].get("content") or {}).get("parts") or [] if candidates else []
    text = "".join(p.get("text", "") for p in parts if not p.get("thought"))
    u = data.get("usageMetadata") or {}
    tokens_in = int(u.get("promptTokenCount", 0))
    tokens_out = int(u.get("candidatesTokenCount", 0)) + int(u.get("thoughtsTokenCount", 0))
    return {"text": text, "tokens_in": tokens_in, "tokens_out": tokens_out}


def call_ollama(system: str, user: str) -> dict:
    _require_config(need_key=False)
    url = API_BASE_URL or URL_OLLAMA
    messages = ([{"role": "system", "content": system}] if system else []) + [
        {"role": "user", "content": user}
    ]
    data = post_json(
        url,
        {},
        {"model": MODEL_NAME, "messages": messages, "stream": False},
        timeout=300,
    )
    return {
        "text": (data.get("message") or {}).get("content", ""),
        "tokens_in": int(data.get("prompt_eval_count", 0)),
        "tokens_out": int(data.get("eval_count", 0)),
    }


@model_call
def call_model(system: str, user: str) -> dict:
    if MODEL_PROVIDER == "fake":
        last = (user.strip().splitlines() or [""])[-1]
        return {
            "text": "[câu trả lời giả — chưa nối model] " + last[:60],
            "model": "fake",
            "tokens_in": 0,
            "tokens_out": 0,
        }

    if MODEL_PROVIDER == "openai":
        r = call_openai(system, user)
    elif MODEL_PROVIDER in ("anthropic", "claude"):
        r = call_claude(system, user)
    elif MODEL_PROVIDER == "gemini":
        r = call_gemini(system, user)
    elif MODEL_PROVIDER == "ollama":
        r = call_ollama(system, user)
    else:
        raise NotImplementedError(
            "Chưa hỗ trợ MODEL_PROVIDER=%s trong codebase/ai.py — chọn fake/openai/anthropic/gemini/ollama"
            % MODEL_PROVIDER
        )

    return {
        "text": r["text"],
        "model": MODEL_NAME,
        "tokens_in": int(r["tokens_in"]),
        "tokens_out": int(r["tokens_out"]),
    }
