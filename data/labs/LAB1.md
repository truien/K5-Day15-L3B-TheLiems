# LAB1 · API ghi chú nhỏ

> Đề mẫu nhóm tự viết để chạy thử (`synthetic`), không chép đề lab của khoá. Mỗi dòng yêu cầu có một mã.

## 0. Quy định chung

- [LAB1-0.1] Dùng Python 3.10 trở lên.
- [LAB1-0.2] Mỗi checkpoint phải lưu kết quả chạy vào `results/<mã checkpoint>.txt`.
- [LAB1-0.3] Không đưa khoá bí mật vào repo; để trong `.env`.

## 1. CP1 · Chạy được API

- [LAB1-1.1] Có đường dẫn `GET /health` trả về trạng thái "ok".
- [LAB1-1.2] Cổng đọc từ biến môi trường `PORT`.

## 2. CP2 · Thêm và liệt kê ghi chú

- [LAB1-2.1] `POST /notes` nhận `title` và `body`.
- [LAB1-2.2] `title` trống thì trả mã 422.
- [LAB1-2.3] `GET /notes` trả danh sách, ghi chú mới nhất đứng trước.

## 3. CP3 · Giới hạn số lần gọi

- [LAB1-3.1] Mỗi địa chỉ gọi tối đa 10 lần mỗi phút; quá thì trả mã 429.
- [LAB1-3.2] Giới hạn này không áp dụng cho `GET /health`.

## 4. Nộp bài

- [LAB1-4.1] README ghi lệnh chạy.
- [LAB1-4.2] Kèm ảnh chụp một lần gọi `POST /notes` bị lỗi 422 ở CP2, thấy được mã phản hồi.
- [LAB1-4.3] README ghi phần nào chưa làm xong.
