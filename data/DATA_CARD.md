# Data card — dữ liệu bản chạy thử dùng

> Bản đầu CP2 (27/11/2026) — sẽ cập nhật khi mở rộng bộ đề/bộ câu thử ở CP3. Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp.

## Dataset 1 · Bộ đề lab mẫu (`LAB1`–`LAB3`)

| Hạng mục | Chi tiết |
| --- | --- |
| Dùng để làm gì | Nguồn đọc đề cho công cụ trong [codebase/tools.py](../codebase/tools.py) và làm căn cứ đáp án cho bộ câu thử [eval/benchmark.csv](../eval/benchmark.csv) |
| Từ đâu | Nhóm tự viết mới (`synthetic`), không chép nội dung đề lab của khoá: [LAB1.md](./labs/LAB1.md) do nhóm dựng mẫu ở CP2; [LAB2.md](./labs/LAB2.md) và [LAB3.md](./labs/LAB3.md) do Đoàn Anh Hùng viết thêm theo kiểu bố cục rải nhiều mục của lab L3 và bối cảnh người dùng kể ở `P2`–`P4` |
| Xử lý những bước gì | Chuẩn hoá mỗi đề thành 5 phần (quy định & luật chung, `CP1`–`CP3`, tiêu chí chấm & nộp bài); gắn mã định danh duy nhất dạng `- [LABx-y.z]` cho từng dòng yêu cầu; kiểm tự động bằng regex không trùng mã và không chứa thông tin cá nhân hay trích nguyên văn đề khoá |
| Số dòng / số đoạn | 3 file đề lab · tổng **49 dòng yêu cầu** (`LAB1`: 13 · `LAB2`: 18 · `LAB3`: 18) |
| Phiên bản / ngày lấy | v0.1 (CP2) · 27/11/2026 |
| Nhãn | `synthetic` |
| Giới hạn | Ngắn hơn và đã chuẩn hoá mã sẵn so với đề lab thật của khoá (vốn rải qua nhiều file `RULES.md`, `CHECKPOINTS.md`, `RUBRIC.md`, `SUBMISSION.md`); hiện mới có 3 đề mẫu |

**Chi tiết data `synthetic`:** Tự viết tay bởi thành viên nhóm theo giao ước tại [docs/cp2-phan-viec.md](../docs/cp2-phan-viec.md), không dùng script sinh ngẫu nhiên (không có seed). Người kiểm: Đoàn Anh Hùng đã rà tay và kiểm regex 49/49 dòng yêu cầu (chờ thành viên khác review chéo trước 19:00 ngày 27/11). **Data tự dựng này chỉ dùng để chạy thử và đánh giá kỹ thuật, không phải bằng chứng pain.**

## Dataset 2 · Phiếu phỏng vấn người dùng (`P2`–`P4`)

| Hạng mục | Chi tiết |
| --- | --- |
| Dùng để làm gì | Nguồn bối cảnh thực tế để xây các câu thử có `source = nguoi_dung: P2/P3/P4` trong [eval/benchmark.csv](../eval/benchmark.csv) (đồng thời là đầu vào bằng chứng pain tổng hợp tại [evidence/summary.md](../evidence/summary.md)) |
| Từ đâu | 3 phiếu phỏng vấn người ngoài nhóm ([P2.md](../evidence/interviews/P2.md), [P3.md](../evidence/interviews/P3.md), [P4.md](../evidence/interviews/P4.md)) do nhóm thu thập ngày 27/11/2026 |
| Xử lý những bước gì | Ẩn danh hoàn toàn (bỏ họ tên, SĐT, email, mã học viên, thay bằng mã `P2`–`P4`); chỉ rút ra tình huống vướng thực tế (chạy đa luồng/tắt server trên Windows, Docker/file môi trường, đối chiếu chỉ số benchmark và thiếu file kết quả chạy) để chuyển hoá thành câu hỏi thử nghiệm, không đưa thông tin nhận dạng vào prompt hay model |
| Số dòng / số đoạn | 3 phiếu phỏng vấn (7 trích dẫn nguyên văn chính tại [evidence/summary.md](../evidence/summary.md)) |
| Phiên bản / ngày lấy | v0.1 (CP2) · 27/11/2026 |
| Nhãn | thật |
| Giới hạn | Cỡ mẫu hiện nhỏ (`n = 3`), thiếu thông tin xác nhận giờ hỏi chính xác và vai L3 của từng phiếu (đã ghi rõ tại [evidence/summary.md](../evidence/summary.md) mục 5); sẽ cập nhật bản mới khi nhóm bổ sung phỏng vấn/khảo sát trước CP3 |
