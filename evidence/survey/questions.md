# Khảo sát: những lúc mất thời gian khi làm lab

- Soạn: 27/11/2026 17:38, trước khi có câu trả lời nào.
- Kênh đã gửi: ____
- Giờ mở / giờ chốt: phản hồi đầu 27/11 17:51 / chốt số liệu 28/11 08:43 (22 phản hồi, cuối cùng 08:26).
- Kết quả: [results.csv](results.csv), đã bỏ cột email. Đội trưởng xác nhận các phản hồi đều do người thật ngoài nhóm tự điền.
- Khác bản soạn: form thật có thêm một câu email không bắt buộc ở cuối (để nhận quà), chưa ai điền.
- Không thu tên, mã học viên. Thành viên nhóm không điền.
- Quà: bốc thăm ngẫu nhiên 1 slot ge. Email để ở **form riêng** (không bắt buộc), không gắn với câu trả lời, không đưa vào repo, xoá sau khi trao. Hạn chế: có quà thì có thể có người tích cho nhanh.

## Câu hỏi (câu 1–9 chỉ tích, bắt buộc; câu 10 tuỳ chọn)

1. Bạn là: Học viên L3 AI20K khoá 5 · Học viên khoá hoặc lớp khác · Lab coach / TA / giảng viên · Khác
2. Lần gần nhất bạn làm một bài lab chia nhiều bước (checkpoint) là khi nào? Trong 7 ngày qua · 8–30 ngày trước · Hơn 1 tháng trước · Chưa từng
3. Trong 1 tháng qua khi làm lab, bạn đã gặp chuyện nào? *(chọn nhiều)* Danh sách A
4. Trong các chuyện đó, chuyện nào làm bạn mất nhiều thời gian nhất? *(chọn một)* Danh sách A
5. Lần gần nhất gặp chuyện ở câu 4, bạn mất khoảng bao lâu? Dưới 15 phút · 15 đến dưới 30 phút · 30 đến dưới 60 phút · Từ 60 phút trở lên · Không gặp
6. Trong 1 tháng qua, mấy lần bạn phải sửa, chạy lại hoặc nộp lại vì sót hay hiểu nhầm yêu cầu? 0 · 1 · 2–3 · Từ 4 lần
7. Lần gần nhất sót hoặc không chắc một yêu cầu, yêu cầu đó nằm ở đâu? Ngay mục của bước đang làm · Mục khác trong đề (quy định chung, nộp bài…) · File khác · Ngoài đề (Discord, lời giảng) · Không nhớ · Chưa gặp
8. Lần gần nhất gặp chuyện ở câu 4, bạn đã làm gì? *(chọn nhiều)* Đọc lại đề · Hỏi ChatGPT hoặc AI khác · Hỏi bạn · Hỏi lab coach / TA · Chạy test hoặc script chấm · Đọc log, tài liệu · Bỏ qua · Không gặp · Khác
9. Lần đó kết thúc thế nào? Xong đúng hạn · Xong nhưng trễ · Nộp thiếu · Bỏ phần đó · Không gặp
10. *(tuỳ chọn, gõ)* Kể 1 câu về lần đó.

**Danh sách A:** Lỗi cài đặt, cấu hình máy · Lỗi Docker hoặc deploy · Chưa hiểu kiến thức, khái niệm · Không chắc đề yêu cầu gì ở bước đang làm · Sót một yêu cầu của đề, sau mới biết · Không chắc kết quả đã đạt yêu cầu chưa · Không gặp chuyện nào · Khác

## Cách đếm (viết trước khi xem kết quả)

- **N** = người chọn "Học viên L3 AI20K khoá 5" ở câu 1 **và** "Trong 7 ngày qua" hoặc "8–30 ngày trước" ở câu 2.
- **Pain chính** = trong N, câu 4 là một trong ba ý "Không chắc đề yêu cầu gì…", "Sót một yêu cầu…", "Không chắc kết quả đã đạt…" **và** câu 5 từ 30 phút trở lên.
- **Đúng giả thuyết 3** nếu pain chính ≥ 2/3 của N (giữ đúng ngưỡng ở [hypothesis.md](../hypothesis.md)). Không đạt thì ghi là không đạt.
- Báo thêm: số người từng gặp từng ý ở câu 3; câu 7 chọn "Mục khác" hoặc "File khác" là bao nhiêu trên số người đã gặp.
- Người đã được phỏng vấn trước 13:03 ngày 27/11 không điền lại.
- Ngưỡng của đề: ≥20 người ngoài nhóm, đúng người dùng. N dưới 20 thì ghi là chưa đạt ngưỡng.

## Lưu kết quả

Google Form → Câu trả lời → tải CSV → lưu thành `results.csv` trong thư mục này. Đọc lại cột câu 10, xoá tên người, tên nhóm nếu có.
