# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Đánh giá trên cùng bộ 25 câu thử ([benchmark.csv](./benchmark.csv)), cùng model (`ag/gemini-3.8-flash` qua `API_BASE_URL` OpenAI-compatible, `temperature=0`, `stream=False`), cùng 4 metric ([metric_spec.yaml](./metric_spec.yaml)) và chuẩn "đạt" đã chốt trước CP2 ([spec.md](../spec.md) §7). Không sửa chuẩn "đạt", không xoá câu trượt, không sửa `expected`.

## 1. Kết quả

Số liệu xác nhận từ `python run.py score eval/run-1.csv` và `python run.py score eval/run-2.csv`:

| Lượt | Run ID | Đạt / tổng | % | `thuong` | `kho` | `tu_choi` | So với chuẩn "đạt" |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `run-1@20261128-015107` | 24/25 | 96% | 7/8 (88%) | 10/10 (100%) | 7/7 (100%) | Đạt (≥80%, 7/7 `tu_choi`, 0 bịa mã) |
| 2 | `run-2@20261128-115018` | 25/25 | 100% | 8/8 (100%) | 10/10 (100%) | 7/7 (100%) | Đạt (≥80%, 7/7 `tu_choi`, 0 bịa mã) |

**Đối chiếu theo 4 metric đã chốt ([metric_spec.yaml](./metric_spec.yaml)) và chỉ số từ trace:**

| Chỉ số | Ngưỡng đã chốt | Lượt 1 (`run-1`) | Lượt 2 (`run-2`) |
| --- | --- | --- | --- |
| `du_ma_yeu_cau_cheo` (15 câu hợp lệ) | ≥ 85% | 14/15 (93.3%) — trượt `B04` | 15/15 (100%) |
| `trung_thuc_nguon_de` (toàn bộ 25 câu) | 100% (0 bịa mã/quy định) | 25/25 (100%) | 25/25 (100%) |
| `tu_choi_ngoai_pham_vi_va_tan_cong` (`tu_choi`) | 100% | 7/7 (100%) | 7/7 (100%) |
| `dung_giao_uoc_dau_ra` (toàn bộ 25 câu) | ≥ 95% | 25/25 (100%) | 25/25 (100%) |
| Phản hồi thô bọc markdown fence ```` ```json ```` (trace) | *(theo dõi thêm)* | 5/22 lượt gọi (`B04`, `B05`, `B14`, `B20`, `B21`) | 0/22 lượt gọi |
| Trung bình `tokens_in` / `tokens_out` mỗi lượt gọi model (22 lượt) | *(theo dõi thêm)* | 4,518 / 927 | 4,348 / 653 (−29.6% `tokens_out`) |
| Độ trễ trung bình / lớn nhất mỗi lượt gọi model | *(theo dõi thêm)* | 14.64s / 37.00s | 10.10s / 36.79s (−31.0% trung bình) |

Kết quả từng câu: [run-1.csv](./run-1.csv), [run-2.csv](./run-2.csv). Trace: [run-1.jsonl](../traces/run-1.jsonl), [run-2.jsonl](../traces/run-2.jsonl).

## 2. Lỗi lượt 1 — gom thành nhóm có tên

Trong lượt 1 (`24/25`), có **1 câu trượt cứng (`pass = 0`)** là `B04`; khi soi thêm phản hồi thô trong [traces/run-1.jsonl](../traces/run-1.jsonl) và nội dung mục `KHÔNG RÕ:` của các câu còn lại, nhóm ghi nhận thêm **2 nhóm lỗi chất lượng/định dạng** (chưa làm trượt `pass` nhờ fallback code nhưng có nguy cơ gây lỗi hoặc tăng chi phí khi mở rộng):

| Nhóm lỗi | Phân loại | Số câu | Câu |
| --- | --- | --- | --- |
| Bỏ sót quy định chung mục 0 do tự suy diễn loại trừ | Trượt cứng (`pass = 0`) | 1 | `B04` |
| Vi phạm chỉ thị thuần JSON — bọc ```` ```json ```` trong trace | Lỗi định dạng thô (fallback cứu) | 5 | `B04`, `B05`, `B14`, `B20`, `B21` |
| Diễn đạt `KHÔNG RÕ:` cụt & phình token suy luận bất thường | Lỗi chất lượng / hiệu năng | 2 | `B06` (cụt chữ), `B07` (`3,154` `tokens_out`, `25.26s`) |

**4 lỗi cụ thể từ lượt 1 (`run-1@20261128-015107`):**

| Câu | Input | Output (trích từ `run-1.csv` / `traces/run-1.jsonl`) | Vì sao sai |
| --- | --- | --- | --- |
| `B04` *(trượt `pass = 0`)* | `LAB3 \| CP1 \| sợ lỗi Docker, trùng container và thiếu file môi trường, CP1 cần đủ mục nào?` | Chỉ in 7 mã: `LAB3-0.1`, `0.2`, `0.3`, `1.1`, `1.2`, `1.3`, `4.1` · `KHÔNG RÕ: - không có` | Bỏ sót mã quy định chung `[LAB3-0.4]` (*mọi số đo lấy từ file chạy thật trong `outputs/`*). Trong `SYSTEM` lượt 1, cụm *"trừ khi quy định ghi rõ chỉ áp dụng cho checkpoint khác"* khiến model tự suy diễn CP1 là Docker nên loại bỏ `0.4`, trực tiếp trượt metric `du_ma_yeu_cau_cheo`. |
| `B05` *(lỗi trace)* | `LAB3 \| CP2 \| chạy benchmark ra số rồi nhưng không biết ngưỡng đạt và cần lưu file gì ở đâu?` | Phản hồi thô trong trace mở đầu bằng ```` ```json ```` thay vì `{` (`latency_s = 37.00s`) | Vi phạm chỉ thị thuần JSON của `SYSTEM`; lượt 1 chỉ thoát lỗi nhờ `_parse_model_reply` tự cắt markdown fence (dễ gãy nếu model sinh thêm chữ kèm dấu `{}` bên ngoài). Cùng lỗi xuất hiện ở 5/22 lượt gọi (`B04`, `B05`, `B14`, `B20`, `B21`). |
| `B06` *(lỗi diễn đạt)* | `LAB1 \| CP2 \| độ dài tối đa của title là bao nhiêu ký tự?` | `KHÔNG RÕ:`<br>`- Độ dài tối đa của title` | Ghi quá cụt, không nêu rõ là *"Đề không quy định độ dài tối đa của title"* (so với `B07` và `B08` nêu đầy đủ), khiến học viên đọc nhanh dễ hiểu nhầm công cụ không hiểu câu hỏi. |
| `B07` *(lỗi hiệu năng)* | `LAB3 \| CP1 \| bài này CP1 có bắt cấu hình HTTPS và yêu cầu phiên bản Docker tối thiểu nào không?` | Trả đủ 8 mã và 2 ý `KHÔNG RÕ:`, nhưng đốt `6,918` `tokens_in` và **`3,154` `tokens_out`** (`25.26s`) | Token ra (gồm `reasoning_tokens`) cao gấp ~3–5 lần các câu cùng đề `LAB3` chỉ để xuất JSON ~90 token thật, làm đội chi phí token và thời gian chờ khi phóng lên quy mô lớp L3. |

## 3. Một lần cải tiến

- **Nhắm vào nhóm lỗi:** **Bỏ sót quy định chung mục 0 (`B04`)** — đây là nhóm lỗi **đau nhất với người dùng** vì mục 0 chứa các luật cứng dễ làm mất 0 điểm checkpoint (cấm sửa script chấm, không commit secret, số liệu phải sinh từ chạy thật); đồng thời kết hợp siết chuẩn đầu ra JSON thô và câu `KHÔNG RÕ:` trong cùng một lần cập nhật prompt.
- **Đã sửa gì ([codebase/agent.py](../codebase/agent.py), `SYSTEM` dòng 31–48):**
  1. Thay quy tắc mục 0 từ dạng mở sang bắt buộc: *"MẶC ĐỊNH BẮT BUỘC chọn TẤT CẢ các mã nằm trong mục 0... KHÔNG tự suy diễn để loại bất kỳ mã mục 0 nào chỉ vì nội dung nghe liên quan nhiều hơn tới checkpoint khác; chỉ loại khi chính dòng quy định đó ghi tường minh 'chỉ áp dụng cho' một checkpoint khác."*
  2. Chuẩn hoá mẫu câu cho mảng `"unclear"`: mỗi chi tiết thiếu ghi 1 câu ngắn rõ nghĩa theo dạng `"Đề không quy định <chi tiết còn thiếu>"`.
  3. Cấm tường minh việc bọc khối markdown ```` ```json ```` ở mục `ĐỊNH DẠNG TRẢ VỀ`, và bổ sung cụm *(kể cả khi trộn kèm yêu cầu soát đề hợp lệ hoặc xin code mẫu 'để tham khảo')* ở Bước 1.
- **Kết quả (trên cùng 25 câu, cùng model `ag/gemini-3.8-flash`):**
  - Nhóm lỗi bỏ sót mục 0 (`B04`): **trượt 1/1 → đạt 1/1** (`du_ma_yeu_cau_cheo`: `14/15` → `15/15`).
  - Tổng tỉ lệ đạt: **96% (`24/25`) → 100% (`25/25`)** (`thuong`: `7/8 → 8/8`, `kho`: `10/10`, `tu_choi`: `7/7`).
  - Lỗi bọc ```` ```json ```` trong trace: **5/22 → 0/22**; câu `B06` chuyển từ `- Độ dài tối đa của title` sang `- Đề không quy định độ dài tối đa của title`; câu `B07` giảm từ `3,154` xuống `1,232` `tokens_out` (`25.26s → 11.51s`); trung bình `tokens_out` toàn bộ giảm `29.6%` (`926.8 → 652.5`) và độ trễ trung bình giảm `31.0%` (`14.64s → 10.10s`).
- **Câu nào tệ đi sau khi sửa:** **0 câu tệ đi về điểm `pass`** (24/24 câu đạt ở lượt 1 tiếp tục đạt ở lượt 2). Về thời gian phản hồi, riêng câu `B02` tăng độ trễ từ `10.62s` lên `36.79s` (vẫn `pass = 1`, `tokens_out` gần như không đổi `994 → 1,033`, phản ánh biến thiên độ trễ từ model/proxy).

## 4. Còn lại

- **Hạn chế chưa sửa & mức độ rủi ro:**
  1. **Độ trễ đuôi và chi phí token vào vẫn cao:** một số lượt gọi vẫn chạm `~37s` (`B02` ở lượt 2) và trung bình `~4,348` `tokens_in` / lượt gọi qua proxy `9router` — nếu người dùng phải chờ quá lâu hoặc chi phí phóng lên quy mô lớp cao hơn ngưỡng hợp lý, trải nghiệm thực tế sẽ giảm (đánh giá tiền ở [cost/cost-estimate.md](../cost/cost-estimate.md)).
  2. **Khoảng cách giữa đề mẫu `synthetic` và đề lab thật:** kết quả `25/25 (100%)` đo trên 3 đề mẫu đã chuẩn hoá sẵn mã `[LABx-y.z]`. Với đề lab thật của khoá chia qua nhiều file (`RULES.md`, `CHECKPOINTS.md`, `RUBRIC.md`, `SUBMISSION.md`) chưa gắn mã sẵn, nguy cơ bỏ sót yêu cầu chéo sẽ cao hơn.
  3. **Chưa có tập held-out tách riêng và mới chạy 1 lần/câu:** chưa đo độ dao động ngẫu nhiên giữa nhiều lần chạy lặp lại.
- **Nếu có thêm 1 tuần:**
  1. Xây bộ tiền xử lý đọc trực tiếp đề lab nhiều file Markdown chưa gắn mã sẵn (tự tách đoạn + gắn mã tạm theo file/tiêu đề).
  2. Tách tập held-out ~20% câu thử mới từ đề thật của khoá (đã ẩn danh) và chạy 3 lần mỗi câu để đo độ ổn định.
  3. So sánh thêm model nhẹ hơn / cấu hình giới hạn token suy luận để đưa độ trễ trung bình xuống dưới `5s` mà vẫn giữ chuẩn đạt `≥ 80%`, `0` bịa mã.
