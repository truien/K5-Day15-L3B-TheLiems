# Chi phí khi dùng thật

> CP4, 28/11. Số lấy từ [simulate-1-summary.md](simulate-1-summary.md) và [simulate-1.csv](simulate-1.csv). Giá tính theo gói trả phí.

## 1. Đầu vào

- **Persona** ([personas.yaml](personas.yaml)):

  | Kiểu | Tỉ lệ | Phiên / người / tháng | Câu hỏi / phiên |
  |---|---:|---:|---:|
  | `chua_hieu_kien_thuc` | 30% | 20 | 8 |
  | `khong_chac_yeu_cau_de` | 35% | 16 | 6 |
  | `loi_ky_thuat` | 35% | 12 | 4 |

  Nhóm persona dựa trên khảo sát; **tỉ lệ làm tròn, số phiên và số câu hỏi là *(tự ước tính)***, khảo sát không hỏi số lần dùng công cụ.
- **Số người dùng:** thấp 300 · cơ sở 700 · cao 1.000. Cơ sở theo fanpage "Đào tạo Nhân tài AI thực chiến" (link trong `personas.yaml`); thấp, cao *(tự ước tính)*.
- **Giá** (USD / 1 triệu token, vào · ra), nguồn https://ai.google.dev/gemini-api/docs/pricing, xem 28/11/2026:
  - `gemini-3.8-flash`: 0,75 · 3,75 (áp dụng đến 31/12/2026; từ 01/01/2027 là 1,50 · 7,50)
  - `gemini-4-hydrogen`: 1,50 · 7,50
- **Tỉ lệ đạt:** 25/25 (100%), lượt `run-2@20261128-115018`.
- Token đo trên `ag/gemini-3.8-flash` qua proxy; tính giá theo hai model trên.

## 2. Kết quả mô phỏng

Run ID `simulate-1@20261128-122154` · 50 phiên · seed 42 · 0 phiên lỗi.

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp | / tháng — cơ sở | / tháng — cao | / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|
| `gemini-3.8-flash` | $0.0399 | $0.0399 | $188.87 | $440.69 | $629.55 | $0.63 |
| `gemini-4-hydrogen` | $0.0798 | $0.0798 | $377.73 | $881.37 | $1,259.10 | $1.26 |

- Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt. Trung bình 6,2 câu hỏi / phiên, tức **$0.0065 / câu hỏi đạt** (`flash`) hoặc $0.0130 (`hydrogen`).
- Bản tóm tắt do máy sinh ghi tên model rẻ là `gemini-3.8-flash-lite`. Tên đó sai (trang giá không có model này); mức giá đã dùng là của `gemini-3.8-flash`, nên số tiền không đổi. `personas.yaml` đã sửa, file mô phỏng đã chạy giữ nguyên.

**Giới hạn của số này**
- Tỉ lệ đạt 100% là trên 25 câu thử của đề tự dựng, không phải tỉ lệ khi dùng thật. Lấy 96% của lượt 1 thì chi phí / task thành công là $0.0416 (`flash`) và $0.0831 (`hydrogen`).
- Mô phỏng chạy lúc 12:21, trước khi gộp bản prompt lượt 2 với thay đổi code lúc 12:43. Token ra mỗi lần gọi trong mô phỏng khoảng 1.150, cao hơn lượt 2 (653), nên chi phí có thể đang ước cao.
- Giá `flash` tăng gấp đôi từ 01/01/2027.

**Độ nhạy theo mức dùng** *(tự ước tính)*: persona trên tương đương khoảng 98 câu hỏi / người / tháng, khá cao cho công cụ soát yêu cầu. Nếu mỗi người chỉ hỏi 12 câu / tháng (4 bài lab × 3 checkpoint), `flash` còn khoảng $0.08 / người / tháng, tức khoảng $55 / tháng cho 700 người.

## 3. So với impact

- Impact (`spec.md` §2, *tự ước tính* từ khảo sát): 4 trong 20 người mất ít nhất khoảng 420 phút / tháng cộng lại, tức khoảng 105 phút / người bị ảnh hưởng, hoặc 21 phút / người nếu chia đều cho cả 20.
- Chi phí cơ sở, `flash`: $0.63 / người / tháng.
- Hoà vốn nếu công cụ tiết kiệm được toàn bộ 21 phút đó và một giờ của học viên đáng giá khoảng $1.80; tiết kiệm được một nửa thì khoảng $3.60.
- **Kết luận một dòng:** chi phí model thấp so với thời gian bị mất, **nhưng chưa đo công cụ tiết kiệm được bao nhiêu** và chỉ 4/20 coi đây là chỗ tốn nhất, nên đáng thử tiếp ở quy mô nhỏ, chưa đủ để triển khai cả khoá.

## 4. Chưa tính

Hosting, phí proxy, công người cập nhật và gắn mã đề lab.
