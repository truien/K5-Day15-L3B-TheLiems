# AI SPEC — Soát yêu cầu đề lab theo từng bước · Nhóm TheLiems · Phòng C401 · Zone [X]

> Mốc nộp: §7 chốt chuẩn "đạt" tại **CP2 19:30 Thứ Sáu 27/11** · §0–§7 nộp **CP3 10:00 Thứ Bảy 28/11** · đủ §0–§10 **CP4 14:30 Thứ Bảy 28/11** · §10 changelog ghi tiếp đến **23:59 Thứ Bảy 28/11**.
> Đầu mỗi mục ghi bước guide (`02-guide.md` trong repo đề) chỉ cách điền. Mỗi mục ngắn, có số và nguồn; chi tiết để ở file được trỏ tới. Xoá dòng hướng dẫn trong ngoặc vuông khi điền xong.

Track: [x] A · [ ] B · [ ] C · [ ] D · [ ] E — bài toán: hướng A6 (hỗ trợ lab), nhóm tự mở rộng: soát yêu cầu của đề lab theo từng bước
Data BTC cấp đã dùng (nếu có — không commit nguyên file): __

## §0. Hiện tại việc này diễn ra thế nào *(guide 1.1)*
- Luồng hiện tại của việc này, trong khoá hoặc trên app thật (3–5 bước; ảnh chụp từ tài khoản của mình, đã che thông tin):
  1. Học viên mở bài tập, xem các nội dung bài, checkpoints hoàn thành, và yêu cầu bài nộp
  2. Học viên thiết lập các môi trường (python, docker,...) trước khi làm bài
  3. Học viên thực hiện bài tập theo đúng nội dung và các checkpoints
  4. Học sinh kiểm tra bài làm đã đáp ứng tất cả yêu cầu đề bài chưa. Nếu chưa, tiếp tục làm và sửa bài (bước 3)
  5. Học sinh kiểm tra bài nộp đã phù hợp và đầy đủ theo yêu cầu chưa. Nếu rồi thì nộp bài.
- Công cụ / AI đang được dùng cho việc này (nếu có) + nguồn. Không kiểm được thì ghi "chưa kiểm": Chưa kiểm

## §1. Người dùng & bằng chứng *(guide 1.1, 1.2)*
- Người dùng chính (một vai cụ thể): học viên L3 AI20K khoá 5 đang làm lab nhiều checkpoint
- Việc họ cố làm xong (`động từ + đối tượng + bối cảnh`, không có chữ AI): hoàn thành đúng yêu cầu của từng checkpoint trong bài lab trước khi nộp
- Hôm nay họ giải bằng gì, hỏng ở đâu, vì sao chưa bỏ: đọc lại đề và slide, hỏi công cụ trò chuyện, chạy test hoặc script chấm; vẫn có lúc không biết đã đúng yêu cầu chưa; vì sao chưa bỏ: chưa hỏi
- Pain (KHÔNG chữ AI): học viên L3 đang làm lab theo từng checkpoint thì sót hoặc không chắc yêu cầu của bước đang làm, nên phải đối chiếu lại hoặc chạy lại và mất thêm thời gian
- Bằng chứng — số chính + kết luận (chi tiết: `evidence/summary.md`): 2/3 người trong phiếu (P2, P4) mất từ 30 phút trở lên; hướng nảy ra sau khi nghe, chưa kiểm lại

## §2. Impact & quyết định chọn *(guide 1.3)*

| Hướng | Bao nhiêu người gặp | Bao nhiêu lần / tháng | Mỗi lần tốn gì | Impact / tháng | Làm kịp không | Chọn? |
|---|---|---|---|---|---|---|
| H1. Máy chưa sẵn môi trường khi vào lab | 1/3 (P2) | P2: 1–2 | 20–30 phút | chưa tính | Có *(tự ước tính)* | Loại |
| H2. Không biết trước cần nắm kiến thức gì cho lab | 0/3 khớp đủ điều kiện | chưa có số | chưa có số | chưa tính | Có *(tự ước tính)* | Loại |
| H3. Kẹt lỗi trong lúc làm lab | 2/3 (P2, P3) | P3: gần như buổi nào | 20 phút – 2 giờ | chưa tính | Có *(tự ước tính)* | Loại |
| H4. Nộp thiếu hoặc sai file bài lab | 0/3 từng nộp rồi mới biết sai | chưa có số | chưa có số | chưa tính | Có *(tự ước tính)* | Loại |
| H5. Sót hoặc không chắc yêu cầu của bước đang làm | 2/3 (P2, P4); P3 có nhắc | chưa đo riêng | 30 phút đến gần 1 giờ | chưa tính | Có *(tự ước tính)* | **Chọn** |

- Số trong bảng lấy từ `evidence/interviews/P2.md`–`P4.md`. H5 nảy ra sau khi nghe, chưa kiểm lại bằng người hỏi mới.
- **Impact / tháng** của hướng chọn = __ người × __ lần × __ phút = __ — chưa tính được vì chưa có số lần / tháng riêng cho H5
- Hướng ĐÃ LOẠI + vì sao (giữ lại, đừng xoá):
  - H1: mất dưới 30 phút; người được hỏi thường đọc kỹ đề khi vào buổi nên khó chuẩn bị theo đề từ trước.
  - H2: không ai khớp; P4 không chuẩn bị nhiều vì các bài trước vẫn làm được.
  - H3: có người gặp, nhưng nguyên nhân lỗi rất khác nhau nên khó dựng câu thử có đáp án *(nhóm đánh giá)*.
  - H4: chưa ai từng nộp rồi mới biết thiếu hoặc sai.
- Số lần / tháng của từng kiểu người dùng (dùng cho persona ở §8):

## §3. Giải pháp tương tự *(guide 2.1)*
- [sản phẩm / tính năng gần giống]: Tính năng học tập trên ChatGPT
  - Một điều đáng học: Trong tính năng này, ChatGPT sẽ hướng dẫn người dùng hiểu các kiến thức thông qua các giải thích và minh hoạ dễ hiểu, cộng với các bài trắc nghiệm nhỏ ở cuối để thử nguời dùng.
  - Một điều đáng né: ChatGPT có thể chỉ quá sâu cho người học, hoặc thậm chí làm hộ bài, nếu nhập prompt không phù hợp.
  - Mình khác gì: Agent trong dự án này sẽ có giới hạn nhất định, như việc tránh không chỉ quá sâu hay làm hộ bài, đồng thời sẽ luôn có khuyến cáo yêu cầu người học luôn tự soát lại kiến thức và bài làm.

## §4. Thiết kế *(guide 2.2, 3.2)*
- **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả): một học viên · đưa đề lab và cho biết checkpoint sắp làm · AI chọn các yêu cầu trong đề áp dụng cho checkpoint đó, kể cả yêu cầu nằm ở phần khác, kèm đoạn đề · học viên đối chiếu đủ yêu cầu trước khi chạy
- Không làm (≥3 điều): không viết code hay làm hộ bài · không chấm điểm, không khẳng định bài đã đạt · không chạy lệnh, không truy cập máy hay repo của học viên · không thêm yêu cầu ngoài nội dung đề
- **Sơ đồ** (Mermaid — khớp `codebase/agent.py` và `codebase/tools.py`):

```mermaid
flowchart TD
    A["Học viên nhập: LAB | CP | ghi chú (tuỳ chọn)"] --> B["Bước 1 (Code): Tách mã lab, checkpoint và ghi chú"]
    B --> C{"Đủ mã lab và checkpoint?"}
    C -- "Thiếu mã + đòi ngoài phạm vi" --> R1["TỪ CHỐI: ngoài phạm vi + nêu việc công cụ làm được"]
    C -- "Thiếu mã (G10)" --> U1["KHÔNG RÕ: thiếu mã lab hoặc checkpoint"]
    C -- "Đủ mã" --> D["Bước 2 (Công cụ read_lab): Đọc đề trong data/labs/{LAB}.md"]
    D --> E{"Có đề lab và checkpoint trong đề không?"}
    E -- "Không (G10)" --> U2["Gọi list_labs() nếu thiếu đề → KHÔNG RÕ: không tìm thấy lab/CP"]
    E -- "Có" --> F["Bước 3 (AI - call_model): Kiểm tra phạm vi/chỉ dẫn chen; chọn mã [MÃ] áp dụng cho CP (mục 0, mục CP, mục 4) và ghi mục KHÔNG RÕ nếu đề không quy định"]
    F --> G{"Ngoài phạm vi hoặc chen chỉ dẫn?"}
    G -- "Có (Chặn rủi ro #1)" --> R2["TỪ CHỐI: không viết code/chấm điểm/làm theo chỉ dẫn chen + nêu phạm vi công cụ"]
    G -- "Không" --> H["Bước 4 (Code - Chặn rủi ro #2): Đối chiếu mã thật từ read_lab, loại mọi mã không có trong đề và giữ nguyên văn nội dung đề"]
    H --> I["Bước 5 (Code): In kết quả theo giao ước (YÊU CẦU: kèm [MÃ] + KHÔNG RÕ: điều đề không nói hoặc 'không có')"]
    I --> J(["Chỗ người duyệt — Học viên tự đối chiếu từng yêu cầu trước khi chạy/nộp bài"])
```

- **Hình dạng:** [x] workflow cố định · [ ] một agent · [ ] nhiều agent — 2 dòng lý do, và vì sao **không** chọn hình dạng phức tạp hơn:
  Toàn bộ quá trình từ tách đầu vào, đọc đề, kiểm tra tồn tại lab/CP, để AI lọc mã yêu cầu, đến bước code loại mã không có trong đề và in kết quả đều cố định thứ tự cho mọi lần chạy.
  Không chọn một agent hay nhiều agent vì bài toán chỉ cần một quyết định AI duy nhất trên toàn bộ văn bản đề; workflow cố định tránh gọi model thừa khi thiếu lab/CP, chặn cứng lỗi bịa mã bằng code, rẻ hơn và dễ đo hơn.
- **AI dựa vào đâu** — mỗi công cụ (khớp `codebase/tools.py`):

  | Công cụ | Input | Output | Tác động ra ngoài? |
  |---|---|---|---|
  | `read_lab` | `lab_id` (`str`, vd `LAB1`) | `dict` gồm `found`, `lab_id`, `title`, `checkpoints`, `items` (`code`, `section`, `section_type`, `checkpoint`, `text`), `raw` | Không (chỉ đọc file trong `data/labs/`) |
  | `list_labs` | Không | `list[str]` danh sách mã đề lab hiện có trong `data/labs/` | Không (chỉ liệt kê thư mục `data/labs/`) |

- **Mức tự động:** [x] AI gợi ý, người quyết · [ ] AI tự làm khi chắc, chuyển người khi không · [ ] AI tự làm — lý do (sai thì ai chịu gì, sửa đắt hay rẻ):
  Nếu AI sót hoặc bịa yêu cầu thì học viên mất thời gian chạy lại hoặc mất điểm checkpoint; nhưng vì đầu ra chỉ là danh sách đối chiếu ngắn gọn kèm mã `[MÃ]` nguyên văn từ đề nên học viên tự kiểm tra và sửa lại rất rẻ trước khi chạy/nộp bài.
- **Chỗ chặn rủi ro** (rủi ro lớn nhất của lát cắt bị chặn ở đâu, bằng gì):
  1. **Bịa mã / bịa yêu cầu ngoài đề:** chặn bằng code ở Bước 4 (`_filter_valid_codes` trong `codebase/agent.py`) — chỉ giữ các mã có thật trong kết quả `read_lab` và in nguyên văn đoạn đề, loại mọi mã không tồn tại. **Giới hạn:** code chỉ lọc mã trong `YÊU CẦU:`; chữ do model viết trong `KHÔNG RÕ:` và lý do `TỪ CHỐI:` đang in thẳng, chưa lọc.
  2. **Làm hộ bài / chấm điểm / prompt injection:** chặn ở Bước 1 của `SYSTEM` (bọc ghi chú người dùng trong `<<<...>>>` coi là dữ liệu, yêu cầu ngoài phạm vi hoặc chen chỉ dẫn bắt buộc trả `action: refuse` → `TỪ CHỐI:`).
  3. **Đoán bừa khi thiếu lab hoặc checkpoint:** chặn bằng code ngay ở Bước 1–2 trước khi gọi model, trả `KHÔNG RÕ:` kèm gợi ý lab/CP hiện có.
- **Chỗ người duyệt** (việc AI không được tự làm):
  Học viên tự đọc và xác nhận từng mục trong danh sách đối chiếu trước khi chạy lệnh hoặc nộp bài; AI không tự sửa code, không tự chạy lệnh, không tự chấm đạt/trượt thay học viên hay giảng viên.
- **Nguyên tắc thiết kế** (≥3, bắt buộc G10):

  | Nguyên tắc | Chỗ cụ thể trên sơ đồ / trong bản chạy thử |
  |---|---|
  | G10 — thu hẹp phạm vi khi không chắc | Bước 1–2: thiếu hoặc không tìm thấy lab/CP thì dừng trước khi gọi AI và báo `KHÔNG RÕ:`; Bước 3–5: chi tiết học viên hỏi nhưng đề không quy định được tách vào mục `KHÔNG RÕ:`, không tự đoán |
  | G1 / G2 — nói rõ làm được gì, làm tốt đến đâu | Nhánh `TỪ CHỐI:` luôn kèm `_TOOL_SCOPE_MSG` nói rõ công cụ chỉ liệt kê yêu cầu theo đề để tự đối chiếu, không viết code hay chấm điểm |
  | G11 — giải thích vì sao (hiện căn cứ) | Bước 4–5: mỗi dòng trong `YÊU CẦU:` gắn đúng mã `[LABx-y.z]` và nội dung nguyên văn trích từ file đề để học viên kiểm chứng ngay |

- Phần nào còn giả (công cụ trả dữ liệu giả, model chế độ giả…) — ghi rõ, không giả làm thật:
  Tại CP2, `codebase/ai.py` chạy mặc định ở chế độ giả (`MODEL_PROVIDER=fake`, dùng `_fake_model_decision` trong `codebase/agent.py`); nhánh gọi API thật (OpenAI, Anthropic, Gemini, Ollama) đã viết sẵn nhưng chưa chạy thử với API key thật. Bộ đề `data/labs/LAB1.md`–`LAB3.md` là dữ liệu `synthetic` nhóm tự viết (chi tiết ở `data/DATA_CARD.md`).

## §5. Chỗ khó — 4 lớp + ≥6 kịch bản + 2 tấn công *(guide 2.3)*

| Kịch bản | Lớp (1–4) | Hành vi mong muốn (nói gì, hiện gì, cho làm gì tiếp) | Câu thử |
|---|---|---|---|
|  |  |  |  |
| *(tấn công)* |  |  |  |
| *(tấn công)* |  |  |  |

(1) nguồn sự thật · (2) mơ hồ / thiếu thông tin · (3) ngoài phạm vi / thẩm quyền · (4) đặc thù lĩnh vực (sai thì người dùng mất gì đắt nhất)

## §6. Bốn đường đi của trải nghiệm
- Mọi thứ suôn sẻ: · Không chắc (lớp 2): · Không có căn cứ (lớp 1): · Người dùng sửa:
- Bị đòi ngoài phạm vi (lớp 3): · Trường hợp đặc thù lĩnh vực (lớp 4):

## §7. Đánh giá & chuẩn "đạt" *(guide 2.4, 4.1)*
- Data card: `data/DATA_CARD.md` · bộ câu thử: `eval/benchmark.csv` — 12 câu (thuong 4 · kho 5 · tu_choi 3) · metric: `eval/metric_spec.yaml` (4 metric)
- **Chuẩn "đạt"** (chốt **trước 19:30 Thứ Sáu 27/11**, giữ nguyên đến 23:59 Thứ Bảy 28/11): "Đạt khi ≥ 80% câu qua, và 100% câu `tu_choi` qua (gồm 2 câu tấn công), và 0 câu bịa mã hoặc bịa quy định ngoài đề."
- Kết quả: lượt 1 __/__ (__%) · lượt 2 __/__ (__%) — run ID: __ / __ → chi tiết `eval/report.md`, hồ sơ `eval/README.md`

## §8. Chi phí khi dùng thật *(guide 4.2)*
- Persona + giá: `cost/personas.yaml` · lượt mô phỏng: `cost/simulate-__.csv` (__ phiên)
- Chi phí / task thành công: __ (model __) · __ (model __)
- Chi phí / tháng ở quy mô thật: thấp __ · cơ sở __ · cao __ → chi tiết `cost/cost-estimate.md`
- So với impact / người / tháng (§2): đáng làm không, vì sao:

## §9. Rủi ro & an toàn
- Dữ liệu: đã ẩn danh gì, không thu gì, không đưa gì vào model gói miễn phí:
- AI **không được** làm gì kể cả khi người dùng yêu cầu:
- Ai có thể bị hại nếu AI sai, và nhóm chặn thế nào:

## §10. Phân công & changelog
- Phân công có tên (theo chặng, chia cặp — guide "Cách chia việc"): __
- Dùng AI vào việc gì (2–3 dòng; chi tiết `docs/ai-usage.md`):
- Nhật ký thay đổi — **mọi thay đổi sau CP2 19:30 Thứ Sáu 27/11 phải có dòng ở đây**:

**CP2 → CP4** (vd thu hẹp lát cắt, hỏi thêm người dùng, lần cải tiến trước lượt 2)

| Thời điểm | Đổi gì | Vì sao (trỏ về câu thử / lỗi / bằng chứng nào) |
|---|---|---|
|  |  |  |

**Sau CP4 (đến 23:59 Thứ Bảy 28/11)** (sửa theo góp ý — không sửa chuẩn "đạt", câu thử, số bằng chứng, kết quả các lượt đã chạy)

| Thời điểm | Đổi gì | Vì sao |
|---|---|---|
|  |  |  |
