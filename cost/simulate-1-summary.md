# Tóm tắt mô phỏng simulate-1@20261128-122154

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| chua_hieu_kien_thuc | 22 | 8 | 31992 | 7651 | 6.8 | 7.8 |
| khong_chac_yeu_cau_de | 10 | 6 | 22004 | 5267 | 4.7 | 6.1 |
| loi_ky_thuat | 18 | 4 | 15351 | 3940 | 3.2 | 4.1 |

Tỉ lệ đạt dùng để tính: 25/25 (100%) — lượt run-2@20261128-115018

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (300 người) | Chi phí / tháng — cơ sở (700 người) | Chi phí / tháng — cao (1.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gemini-3.8-flash-lite (vào 0.75 · ra 3.75 $/1M) | $0.0399 | $0.0399 | $0.0065 | $188.87 | $440.69 | $629.55 | $0.6296 |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0798 | $0.0798 | $0.0130 | $377.73 | $881.37 | $1,259.10 | $1.26 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (6.2) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: ag/gemini-3.8-flash. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
