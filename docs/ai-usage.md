# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Antigravity (Gemini) | Hỗ trợ viết khung `codebase/tools.py` (`read_lab`, `list_labs`), `codebase/agent.py` (workflow cố định 5 bước, `parse_input` linh hoạt, `_filter_valid_codes`, `_sanitize_free_text`) và `codebase/ai.py` (kết nối OpenAI/9router, Claude, Gemini, Ollama bằng `urllib`) | Tự kiểm tra từng hàm, rà lỗ hổng path traversal / lộ key / đếm `reasoning_tokens`, chạy kiểm thử `run.py`, `eval --try`, `simulate --try` và chạy lượt 1 (`eval/run-1.csv`, 24/25 đạt) | Nguyễn Thanh Tùng |
| Prompt / thiết kế lời gọi mô hình | Antigravity (Gemini) | Đối chiếu `SYSTEM` prompt trong `codebase/agent.py` với 25 câu thử & 4 metric; kiểm tra cấu hình `.env` và mã lỗi kết nối | Kiểm trực tiếp mã nguồn `codebase/ai.py` & `codebase/agent.py`, chạy thử `python run.py eval --try` và ghi 3 đề xuất chỉnh prompt gửi Tùng | Đoàn Anh Hùng (phối hợp Tùng) |
| Đào data (viết script đếm, gợi ý nhãn) | | | Kiểm tay __ dòng, khớp __ | |
| Rà câu hỏi phỏng vấn / khảo sát | | Chỉ rà câu dẫn dắt | | |
| Viết câu thử (benchmark) | Antigravity (Gemini) | Hỗ trợ soạn nháp 25 câu thử (`B01`–`B25`) theo 4 lớp chỗ khó, lưới độ phủ 4 chiều và `pass_criterion` nhị phân; soạn nháp 4 metric (`eval/metric_spec.yaml`) và mục 1–2 của `eval/README.md` | Tự rà từng mã `[LABx-y.z]` đối chiếu file đề, đảm bảo 10/25 câu `nguoi_dung` bám đúng phiếu `P2`–`P4` (không bịa nguồn), giữ bất biến `B01`–`B12` sau CP2 và chạy `python run.py check` sạch cảnh báo | Đoàn Anh Hùng |
| Sinh data `synthetic` (nếu có) | Antigravity (Gemini) | Hỗ trợ viết 2 đề mẫu `data/labs/LAB2.md` (18 yêu cầu) và `data/labs/LAB3.md` (18 yêu cầu) theo bố cục nhiều mục của lab L3 (không chép đề khoá) và điền `data/DATA_CARD.md` | Không dùng script sinh ngẫu nhiên (không có seed); kiểm tay và kiểm regex 49/49 dòng yêu cầu (`LAB1`–`LAB3`), không trùng mã, không chứa nội dung đề thật hay dữ liệu cá nhân | Đoàn Anh Hùng |
| Chấm cột `pass` bằng LLM (nếu có) | Không sử dụng | — | Nhóm chấm bằng `code` và `nguoi` theo `eval/metric_spec.yaml` (đã có 2 người chấm thử khớp 5/5 ở `eval/README.md` mục 3) | Đoàn Anh Hùng |
| Slide, văn bản | Claude Code | Soạn khảo sát và script tạo form, tổng hợp số khảo sát, dựng slide, viết `cost/cost-estimate.md`, `spec.md` §8–§10; viết script tự gõ đầu vào và quay video demo | Đội trưởng chịu trách nhiệm đọc lại; số trên slide trỏ về file nguồn ở chân trang | Nguyễn Trọng Truyền |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
