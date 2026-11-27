# LAB3 · Đóng gói Docker và đo hiệu năng API

> Đề mẫu nhóm tự viết để chạy thử (`synthetic`), tham khảo kiểu bố cục nhiều phần (quy định chung, từng checkpoint, tiêu chí chấm & nộp bài) của các bài lab L3, không chép nội dung đề khoá. Mỗi dòng yêu cầu có một mã.

## 0. Quy định & luật chung

- [LAB3-0.1] Khai báo cấu hình qua `.env.example`; tuyệt đối không commit `.env`, `API_KEY` thật hoặc thông tin cá nhân vào repo hay lịch sử git.
- [LAB3-0.2] Mọi lệnh Docker Compose trong bài phải dùng chung tên project `-p lab3-<ma-hoc-vien>` để tránh trùng container và xem đúng log.
- [LAB3-0.3] Không được sửa bộ câu đo chuẩn `bench/workload.json` và script kiểm tra `scripts/check_lab3.py`.
- [LAB3-0.4] Mọi số đo hiệu năng ghi trong báo cáo phải lấy từ file JSON/CSV do lệnh chạy thật sinh ra trong `outputs/`, không chép mẫu hay ước lượng.

## 1. CP1 · Đóng gói Docker Compose và kiểm tra sức khoẻ

- [LAB3-1.1] Có `Dockerfile` (ưu tiên multi-stage, dung lượng image dưới 500 MB) và `docker-compose.yml` khởi chạy API bằng `docker compose -p lab3-<ma-hoc-vien> up -d --build`.
- [LAB3-1.2] Tách rõ 2 đường dẫn: `GET /health` trả mã 200 khi tiến trình sống; `GET /ready` trả 200 khi kết nối dịch vụ phụ thuộc sẵn sàng và trả 503 khi mất kết nối.
- [LAB3-1.3] Cổng ứng dụng đọc từ biến môi trường `APP_PORT`, không ghi cứng trong mã nguồn; ghi kích thước image đo thật bằng `docker images` vào `outputs/cp1-image.txt`.

## 2. CP2 · Đo hiệu năng (benchmark) theo kịch bản chuẩn

- [LAB3-2.1] Chạy `python bench/run_bench.py --requests 200 --concurrency 20 --out outputs/cp2-bench.json` vào container đang chạy ở CP1.
- [LAB3-2.2] Ghi đủ 4 chỉ số trong `outputs/cp2-bench.json`: `p50_ms`, `p95_ms`, `rps` và `error_rate`.
- [LAB3-2.3] Đối chiếu ngưỡng SLO của bài đo: `p95_ms <= 300` và `error_rate < 0.01` (dưới 1%); ghi rõ trạng thái `PASS` hoặc `FAIL` cho từng ngưỡng.

## 3. CP3 · Truy vết log có cấu trúc và đối chiếu

- [LAB3-3.1] Mọi phản hồi HTTP trả thêm header `X-Request-Id` duy nhất cho mỗi lượt gọi.
- [LAB3-3.2] Log ứng dụng xuất định dạng JSON mỗi dòng gồm tối thiểu: `timestamp`, `request_id`, `path`, `status_code`, `latency_ms`.
- [LAB3-3.3] Chép ít nhất 1 dòng log JSON có `request_id` trùng với một phản hồi thật vào `outputs/cp3-trace-sample.json` trước khi dọn container.

## 4. Tiêu chí chấm & quy định nộp bài

- [LAB3-4.1] Đối với CP1: kèm ảnh chụp `screenshots/cp1-healthy.png` kết quả `docker compose -p lab3-<ma-hoc-vien> ps` thấy trạng thái `healthy` và đầu ra lệnh `docker images` đo thật.
- [LAB3-4.2] Đối với CP2: điền bảng 4 chỉ số vào `BENCHMARK_REPORT.md` và copy `outputs/cp2-bench.json` ra thư mục `reports/` ở gốc repo; số liệu lệch file JSON sẽ bị 0 điểm CP2.
- [LAB3-4.3] Đối với CP3: chỉ chạy lệnh dọn container (`docker compose -p lab3-<ma-hoc-vien> down -v`) sau khi đã lưu đủ log JSON và chụp ảnh minh chứng.
- [LAB3-4.4] Ghi chú phạm vi chấm: không yêu cầu deploy lên cloud trong bài lab này; mọi kiểm tra đều chạy local bằng Docker.
- [LAB3-4.5] README ghi lệnh dựng stack, lệnh chạy benchmark và danh mục tự rà đủ file trước khi nộp repo Public.
