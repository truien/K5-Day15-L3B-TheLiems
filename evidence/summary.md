# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Mạnh nhất: đào data ra insight → hỏi người dùng để kiểm lại (hoặc ngược lại).

**Trạng thái (28/11, 08:43): khảo sát đạt ngưỡng nguồn (20 người hợp lệ). Giả thuyết 3 không đạt.**

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☐ không dùng cho hướng này | — |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☐ có 3 phiếu, còn thiếu (xem mục 5) | `evidence/interviews/P2.md`–`P4.md` |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☑ 20 người hợp lệ (22 phản hồi, loại 2 lab coach) | `evidence/survey/questions.md`, `results.csv` |

## 2. Số chính

- Đào data: không dùng. Data pre-class không ghi buổi lab trên lớp.
- Phỏng vấn: **2/3 người** (P2, P4) kể mất từ 30 phút trở lên khi không biết kết quả đã đúng yêu cầu chưa. P3 nói tài liệu chia nhiều file nên tìm mất công, không nêu thời gian cho việc đó; chỗ P3 tốn nhất là lỗi Docker và deploy (1–2 giờ).
- Khảo sát, N = 20 (học viên L3 khoá 5, làm lab trong 1 tháng qua). Cách đếm viết trước ở `survey/questions.md`:
  - **Pain chính: 4/20 (20%)**: chỗ tốn thời gian nhất là sót hoặc không chắc yêu cầu, và mất từ 30 phút. Giả thuyết cần ≥ 2/3, **không đạt**.
  - Từng gặp trong 1 tháng: không chắc đề yêu cầu gì 10/20 · không chắc kết quả đã đạt 9/20 · sót yêu cầu 4/20.
  - Trong 15 người trả lời được yêu cầu bị sót nằm đâu: 6/15 ở mục khác hoặc file khác.
  - Đếm thêm (không định trước): 16/20 gặp ít nhất một trong ba ý về yêu cầu.
  - Đếm thêm, chỗ tốn nhất (trong đó mất ≥ 30 phút): yêu cầu (gộp 3 ý) 7 (4) · kiến thức 5 (4) · Docker/deploy 4 (0) · cài đặt máy 3 (2) · không gặp 1.

| | Vai | Gặp pain? | Số lần / 1 tháng qua | Lần gần nhất mất | Đang xoay xở bằng |
|---|---|---|---|---|---|
| P2 | người làm lab | Có | 3–4 lần gộp nhiều nguyên nhân, trong đó 1–2 do môi trường | 30–45 phút | đọc lại đề, xem lại code, hỏi AI, chạy test |
| P3 | người làm lab | Một phần | chưa có số riêng | chưa có số riêng (lỗi cấu hình: 1–2 giờ) | đọc log, tài liệu, hỏi AI |
| P4 | người làm lab | Có (gốc là chưa hiểu chỉ số) | khoảng 3–4 buổi phải dừng tìm hiểu thêm | gần 1 giờ | slide, hỏi AI, đọc lại code |

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

1. "chạy được rồi mà không biết kết quả đã đúng yêu cầu chưa." — P2
2. "Mình đọc lại yêu cầu đề bài, xem lại logic code rồi nhờ AI phân tích xem có bỏ sót trường hợp nào không." — P2
3. "chạy được nhưng không biết đúng chưa. Tầm gần 1 tiếng." — P4
4. "Có lần chuẩn bị nộp mới thấy thiếu kết quả chạy." — P4
5. "Mấy bài trước vẫn làm được bình thường nên cũng không chuẩn bị gì nhiều." — P4
6. "Tài liệu chia nhiều file nên tìm cũng hơi mất công." — P3
7. "Lâu nhất là phần Docker với deploy, tầm 1–2 tiếng." — P3

## 4. Các nguồn có khớp nhau không

Có hai nguồn: phỏng vấn (trước) và khảo sát (kiểm lại).

- **Khớp:** có người gặp chuyện không chắc yêu cầu hoặc không chắc kết quả đã đạt.
- **Lệch:** phỏng vấn 2/3 người mất từ 30 phút, khảo sát chỉ 4/20 coi đó là chỗ tốn nhất và mất từ 30 phút. Cách giải thích *(nhóm suy đoán)*: phỏng vấn chỉ 3 người, hướng nảy ra sau khi nghe họ; khảo sát hỏi "tốn nhất" nên kiến thức, cài đặt, deploy cạnh tranh trực tiếp.
- **Giới hạn khảo sát:** người trả lời tự chọn tham gia, có quà bốc thăm, chưa ghi kênh gửi; một số phiếu trả lời không nhất quán (vẫn giữ nguyên); không ai viết câu 10 nên khảo sát không cho trích dẫn; phản hồi rải đều suốt đêm.

## 5. Kết luận

- Giả thuyết 1 (chuẩn bị trước lab): **phải đổi**. Không phiếu nào khớp đủ điều kiện (P2 một phần, P3 và P4 không khớp).
- Giả thuyết 2 (kiểm bài trước khi nộp): **chưa đạt**. P2 là người gợi ra nên không tính; P3 không khớp, P4 khớp một phần.
- Hướng chọn (giả thuyết 3, sót hoặc không chắc yêu cầu của đề): đã kiểm bằng khảo sát, **không đạt** ngưỡng đặt trước (4/20, cần ≥ 2/3). Pain có thật ở nhiều người nhưng thường không phải chỗ tốn nhất. Sau CP2 chỉ được thu hẹp lát cắt; nhóm chưa quyết có thu hẹp không.
- Điều còn thiếu: giờ hỏi chính xác (phiếu chỉ ghi giờ muộn nhất đã nhận câu trả lời) và người hỏi; P2 chưa xác nhận người trả lời tự viết; chưa rõ các người này có phải học viên L3; chưa hỏi người nào sau khi viết giả thuyết 3.

## Lịch hẹn (dùng cho CP2 — chỉ ghi vai và giờ, không tên)

| Vai | Giờ hẹn | Đã xong? |
|---|---|---|
| | | |
