# LAB2 · Hàng đợi xử lý tác vụ đồng thời

> Đề mẫu nhóm tự viết để chạy thử (`synthetic`), tham khảo kiểu bố cục nhiều phần (quy định chung, từng checkpoint, tiêu chí chấm & nộp bài) của các bài lab L3, không chép nội dung đề khoá. Mỗi dòng yêu cầu có một mã.

## 0. Quy định & luật chung

- [LAB2-0.1] Dùng Python 3.10 trở lên; mọi lệnh chạy từ thư mục gốc repo (không `cd src`), tương thích cả PowerShell (Windows) và bash (Linux/macOS).
- [LAB2-0.2] Không commit `.env`, API key hay thông tin cá nhân (email, SĐT); chỉ commit `.env.example`.
- [LAB2-0.3] Không được sửa file tự kiểm `scripts/verify_queue.py` và bộ kịch bản mẫu `tests/fixtures.json` (sửa để lấy PASS sẽ bị 0 điểm checkpoint tương ứng).
- [LAB2-0.4] Mọi file kết quả trong `artifacts/` phải được sinh từ lệnh chạy thật của mã nguồn, không tạo tay hay chỉnh số liệu sau khi chạy.

## 1. CP1 · Nhận tác vụ và chạy song song

- [LAB2-1.1] `POST /jobs` nhận JSON có trường `task` (chuỗi không rỗng) và trả mã 202 kèm `job_id`.
- [LAB2-1.2] Xử lý đồng thời tối đa `MAX_WORKERS` tác vụ (đọc từ biến môi trường, mặc định `3`); tác vụ vượt ngưỡng phải xếp chờ trong hàng đợi.
- [LAB2-1.3] `GET /jobs/{job_id}` trả trạng thái `queued`, `running`, `done` hoặc `failed`; `job_id` không tồn tại trả mã 404.
- [LAB2-1.4] Tự kiểm CP1: chạy `python scripts/verify_queue.py --cp 1` báo `PASS` và tự động sinh `artifacts/cp1-check.json`.

## 2. CP2 · Tắt dịch vụ an toàn (graceful shutdown)

- [LAB2-2.1] Khi nhận tín hiệu dừng (`SIGINT` hoặc `SIGTERM`), dịch vụ ngừng nhận việc mới và trả mã 503 cho mọi lệnh `POST /jobs` mới.
- [LAB2-2.2] Các tác vụ đang ở trạng thái `running` phải hoàn tất trước khi tiến trình thoát, trong giới hạn thời gian chờ `SHUTDOWN_TIMEOUT` giây.
- [LAB2-2.3] Nhật ký tắt dịch vụ lưu vào `artifacts/cp2-shutdown.log`, ghi rõ số tác vụ đã hoàn tất và số tác vụ còn trong hàng đợi lúc thoát.

## 3. CP3 · Thử tải ngắn và xuất thống kê

- [LAB2-3.1] Script thử tải gửi đồng thời 20 yêu cầu tới `POST /jobs` và đợi toàn bộ xử lý xong.
- [LAB2-3.2] Xuất `artifacts/cp3-summary.json` gồm: `total`, `succeeded`, `failed`, `max_duration_ms`.

## 4. Tiêu chí chấm & quy định nộp bài

- [LAB2-4.1] README ghi rõ lệnh cài đặt, lệnh chạy trên cả Windows PowerShell và bash, cùng mục các phần chưa hoàn thành (nếu có).
- [LAB2-4.2] Đối với CP2: kèm đoạn log hoặc ảnh chụp `screenshots/cp2-shutdown.png` chứng minh tác vụ đang chạy hoàn tất sau tín hiệu dừng và yêu cầu mới bị từ chối với mã 503 (che toàn bộ token/biến bí mật nếu xuất hiện trên màn hình).
- [LAB2-4.3] Đối với CP3: đưa bảng tổng hợp từ `artifacts/cp3-summary.json` vào `REPORT.md`; số liệu trong `REPORT.md` phải khớp chính xác với file JSON (lệch số sẽ bị 0 điểm CP3).
- [LAB2-4.4] Ghi chú phạm vi chấm: giao diện web quản trị hàng đợi là phần mở rộng không tính điểm, không bắt buộc làm ở bất kỳ checkpoint nào.
- [LAB2-4.5] Đảm bảo repo ở chế độ Public trước khi nộp link.
