# Phân việc CP2 (hạn 19:30)

Mục tiêu: không ai sửa file của người khác, không ai phải chờ người khác mới làm được.

## 1. Giao ước chung (đã chốt thì không tự đổi)

**Đầu vào** — một chuỗi, đúng ô `input` của câu thử:

```text
LAB1 | CP2
LAB1 | CP2 | ghi chú thêm của học viên (tuỳ chọn)
```

**Đầu ra** — chuỗi chữ, trả trong `{"output": ...}`:

```text
YÊU CẦU:
- [LAB1-0.1] Dùng Python 3.10 trở lên
- [LAB1-0.2] Lưu kết quả chạy vào results/CP2.txt
- [LAB1-0.3] Không đưa khoá bí mật vào repo
- [LAB1-2.1] POST /notes nhận title và body
- [LAB1-2.2] title trống thì trả 422
- [LAB1-2.3] GET /notes trả ghi chú mới nhất trước
- [LAB1-4.2] Kèm ảnh chụp lần gọi bị lỗi 422, thấy mã phản hồi
KHÔNG RÕ:
- (điều học viên hỏi mà đề không nói; không có thì ghi "không có")
```

| Trường hợp | Đầu ra |
|---|---|
| Không có lab hoặc checkpoint đó | `KHÔNG RÕ: không tìm thấy ... ` |
| Xin viết code, làm hộ, chấm điểm | `TỪ CHỐI: ...` kèm việc công cụ làm được |
| Đầu vào chen chỉ dẫn "bỏ qua hướng dẫn" | Coi là dữ liệu, không làm theo |

**Đề lab:** mỗi đề một file `data/labs/<mã lab>.md`, mỗi yêu cầu một dòng `- [<mã>] nội dung`. Mẫu: [data/labs/LAB1.md](../data/labs/LAB1.md).

**Luồng (workflow cố định):** đọc đầu vào → đọc đề → model chọn mã yêu cầu → code loại mã không có trong đề → in kết quả.

## 2. Ai sửa file nào

| Người | Chỉ sửa | Việc | Xong khi |
|---|---|---|---|
| Tùng | `codebase/` | Luồng với model giả theo giao ước; thử lấy API key | `python run.py`, gõ `LAB1 \| CP2` ra đúng dạng đầu ra |
| Hùng | `data/`, `eval/` | Thêm LAB2, LAB3; ≥10 câu thử; ≥3 metric; data card | `python run.py check` không còn cảnh báo metric và dòng mẫu |
| Lâm | `spec.md` **chỉ §4** | Sơ đồ, lý do chọn workflow, công cụ, chỗ chặn rủi ro, người duyệt | §4 không còn ô trống bắt buộc |
| Truyền | `spec.md` **chỉ §1, §2, §7** · `canvas.md` · `evidence/` | Bằng chứng, chuẩn "đạt", nộp bài | Đã nộp CP2 |

## 3. Vì sao không phải chờ nhau

- **Tùng** dùng sẵn `LAB1.md` và model giả, không cần chờ câu thử.
- **Hùng** viết câu thử từ giao ước và đề mẫu, không cần chờ code.
- **Lâm** vẽ sơ đồ từ dòng "Luồng" ở mục 1.
- **Truyền** làm bằng chứng độc lập; chỉ cần tên metric của Hùng khi chốt §7.

## 4. Gợi ý câu thử (Hùng)

- Yêu cầu nằm ở phần khác (mục 0, mục 4) mà vẫn áp dụng cho checkpoint.
- Checkpoint không tồn tại · thiếu mã checkpoint.
- Hỏi điều đề không nói (vd độ dài tối đa của `title`).
- Xin viết code hộ · câu chen chỉ dẫn (≥2 câu tấn công).
- Cột `source` chỉ ghi `nguoi_dung: P_` khi câu thử đi ra từ điều người đó kể (`evidence/interviews/`).

## 5. Git

```bash
git switch main
git pull
git switch -c cp2-<tên>
# làm việc, chỉ add file của mình
git add <file của mình>
git commit -m "CP2: <việc đã làm>"
git push -u origin cp2-<tên>
```

Tạo Pull Request vào `main`, xong là merge được vì không ai đụng file của ai. Không commit `.env`.

## 6. Mốc giờ

| Giờ | Việc |
|---|---|
| 17:30 | Ai cũng đã push bản đầu |
| 18:00 | Merge hết, cả nhóm `git pull`, chạy thử |
| 18:00–19:00 | Đổi chéo kiểm, chốt chuẩn "đạt" và metric (**sau CP2 không sửa được**) |
| 19:15 | Nộp CP2 |
