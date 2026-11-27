# Mini Hackathon AI — AI20K khoá 5 · L3

> **[README]** → [01-challenge-brief](01-challenge-brief.md) → [tracks/](tracks/README.md) → [02-guide](02-guide.md) → [03-rubric](03-rubric.md)

**Tìm một chỗ đau thật của người dùng, thiết kế một giải pháp AI cho nó, rồi chứng minh bằng số.**

> **Trang hackathon:** https://ai20k-hackathon.pages.dev — đăng ký nhóm, tìm đồng đội, nộp checkpoint, đồng hồ đếm giờ, side quest.

Bài của nhóm phải cân bằng hai nửa: **tư duy sản phẩm** (đúng người dùng, đúng chỗ đau, đáng làm) và **giải pháp AI** (thiết kế công nghệ ra sao, AI dựa vào dữ liệu và công cụ nào, chạy thật được). Ba câu phải trả lời, mỗi câu bằng số:

1. **Pain & impact:** ai đang đau, đau thế nào, bao nhiêu người, mỗi tháng mất bao nhiêu?
2. **Giải pháp AI:** AI quyết định gì, dựa trên dữ liệu và công cụ nào, chọn workflow hay agent và vì sao, chặn rủi ro ở đâu, người duyệt ở đâu? Bản chạy thử phải gọi AI thật.
3. **Đánh giá & chi phí:** giải pháp đúng được bao nhiêu trên bộ câu thử? Dùng thật ở quy mô thật của sản phẩm thì tốn bao nhiêu mỗi tháng?

- Nhóm **3–5 người**, tự ghép, bầu một đội trưởng. Chưa có nhóm: mục **Đồng đội** trên trang hackathon.
- Khoảng **10 giờ làm thật**: chiều tối Thứ Sáu 27/11 và sáng Thứ Bảy 28/11.
- **6 track:** A EdTech (chính khoá AI20K) · B Y tế · C Du lịch · D Thương mại điện tử · E Tài chính · F Làn khác (lĩnh vực bất kỳ, có insight từ người dùng thật).
- BTC **không cấp API key** cho mọi nhóm. Nhóm dùng gói miễn phí hoặc tài khoản của nhóm (một số credit API là quà của side quest trên trang hackathon).
- Mọi kỹ thuật cần dùng, nhóm đã học trong 15 ngày giai đoạn 1. [02-guide.md](02-guide.md) chỉ rõ bước nào ôn lại ngày nào.

---

## Đọc theo thứ tự này

| # | File | Đọc khi nào | Trong đó có gì |
|---|---|---|---|
| 1 | **README.md** *(file này)* | Đầu buổi Zoom | Tổng quan · checkpoint · chấm điểm · luật |
| 2 | [01-challenge-brief.md](01-challenge-brief.md) | Lúc chọn track | Đề bài: bối cảnh, 6 track, 7 hạng mục bắt buộc, dữ liệu |
| 3 | [tracks/](tracks/README.md): **file của track nhóm chọn** | Ngay sau file 2 | Bối cảnh · người dùng · định hướng ý tưởng · data · công cụ gợi ý |
| 4 | [**02-guide.md**](02-guide.md) | **Mở suốt hai ngày** | Làm từng bước: câu hỏi phải trả lời → làm gì → ra file nào → nộp mốc nào |
| 5 | [03-rubric.md](03-rubric.md) | Trước mỗi checkpoint | Chấm từng phần thế nào |

Đi kèm:
- [starter-repo/](starter-repo/README.md): khung repo nộp bài. Có sẵn thư mục, file mẫu, và lệnh `run.py` chạy bộ câu thử và mô phỏng chi phí.
- [data/](01-challenge-brief.md#data): dữ liệu BTC cấp cho track A (EdTech). Track B–F nhóm tự tìm data.
- [further-reading/](further-reading/README.md): JTBD, phỏng vấn người dùng, HAX, PAIR, bảng giá model.

---

<a id="checkpoint"></a>
## CHECKPOINT

**Mỗi checkpoint nộp trên [trang hackathon](https://ai20k-hackathon.pages.dev), thay cả nhóm.** Đội trưởng đăng ký nhóm một lần (tên nhóm + PIN + mã học viên đội trưởng); ai trong nhóm có PIN cũng nộp thay được. Trang ghi giờ nộp và commit của repo lúc nộp, agent tự kiểm đủ phần trong vài phút.
- Đúng hạn và đủ phần → đủ điểm mốc. Muộn hoặc thiếu → 0 điểm mốc đó.
- Vẫn nộp phần đã có và khai thật phần còn thiếu.
- Tự soát trước khi nộp: bước guide ghi ở từng mốc.

### CP1 · 17:00 Thứ Sáu 27/11 · 3 điểm

- `TEAMS.md` điền đủ thành viên + mã học viên, **đúng format** (đội trưởng ở dòng 1).
- Track (A–F) + bài toán của nhóm trong 1–2 câu: ai, đang làm gì, vướng ở đâu. Không viết chữ AI. Track F kèm thẻ đề.
- Lát cắt dự kiến (1 câu).
- Canvas 7 dòng (`canvas.md`).
- Link repo GitHub công khai, mở được bằng cửa sổ ẩn danh.

Tự soát: [guide 1.4](02-guide.md#b1-4) · **Nộp CP1:** [trang hackathon → Nộp checkpoint](https://ai20k-hackathon.pages.dev/#submit)

### CP2 · 19:30 Thứ Sáu 27/11 · 4 điểm

- Canvas cập nhật + 1–3 dòng "đã đổi gì so với CP1".
- Nguồn bằng chứng đang làm (đào data / phỏng vấn / khảo sát) và đã làm đến đâu.
- Link `spec.md`, trong §4 có sơ đồ kiến trúc giải pháp.
- Link `eval/benchmark.csv`, ≥10 câu thử. Đã có `eval/metric_spec.yaml` và `data/DATA_CARD.md` bản đầu.
- **Chuẩn "đạt" bằng số**, chép từ `spec.md` §7. **Chốt tại mốc này, không sửa về sau.**
- Bản chạy thử dạng khung: `python run.py` đi hết luồng với AI giả.

Tự soát: [guide 2.5](02-guide.md#b2-5) · **Nộp CP2:** [trang hackathon → Nộp checkpoint](https://ai20k-hackathon.pages.dev/#submit)

### CP3 · 10:00 Thứ Bảy 28/11 · 4 điểm

- Bằng chứng pain đạt ngưỡng ở ≥1 nguồn + ≥5 trích dẫn / ví dụ nguyên văn. Link `evidence/summary.md`.
- Bộ câu thử 20–30 câu: ≥5 câu `kho`, ≥2 câu `tu_choi`.
- **Video 30 giây:** bản chạy thử gọi AI thật. YouTube để "Không công khai", hoặc Google Drive để "Bất kỳ ai có đường liên kết". Mở thử bằng cửa sổ ẩn danh.
- Kết quả lượt 1 (x/N câu đạt) + run ID.
- Link `spec.md` đã có §0–§7.
- Phần chưa xong, nếu có.

Tự soát: [guide 3.4](02-guide.md#b3-4) · **Nộp CP3:** [trang hackathon → Nộp checkpoint](https://ai20k-hackathon.pages.dev/#submit)

### CP4 · 14:30 Thứ Bảy 28/11 · 4 điểm

- Phòng demo + link repo.
- Tích 7 hạng mục bắt buộc đã có ([01-challenge-brief](01-challenge-brief.md#7-hang-muc)).
- Kết quả lượt 1 → lượt 2 (ví dụ 14/24 → 18/24).
- Chi phí / task thành công ở kịch bản cơ sở, kèm tên model.
- Slide, định dạng nào cũng được (PDF, PPTX, HTML, Keynote…): file trong repo **hoặc** link slide nộp ở form CP4 (Drive, Canva, Google Slides…, ai có link cũng xem được) · link video demo dự phòng.
- Phần chưa xong, nếu có.

Tự soát: [guide 4.4](02-guide.md#b4-4) · **Nộp CP4:** [trang hackathon → Nộp checkpoint](https://ai20k-hackathon.pages.dev/#submit)

### Hạn chót · 23:59 Thứ Bảy 28/11 · không nộp form

Khoá repo bản cuối:
- Sửa theo góp ý ở buổi demo, mọi thay đổi sau 14:30 ghi vào `spec.md` §10.
- Mỗi người 1 file `reflection/`.

Hướng dẫn: [guide 5.3](02-guide.md#b5-3).

---

## Lịch hai ngày

| Khi nào | Ở đâu | Việc |
|---|---|---|
| Sáng Thứ Sáu 27/11 | Zoom | Khai mạc. **Sau buổi:** ghép nhóm · chọn track · nháp Canvas · hẹn người phỏng vấn / gửi khảo sát |
| 16:00–19:30 Thứ Sáu 27/11 | L3A: H209 + H210 · L3B: C401 | Làm tại lớp · **CP1 17:00** · **CP2 19:30** |
| Tối Thứ Sáu → 10:00 Thứ Bảy 28/11 | Nhóm tự làm | Nối model thật, nên xong trước khi ngủ · **CP3 10:00**. Sáng Thứ Bảy không có lớp |
| 14:00 Thứ Bảy 28/11 | L3A: H209 + H210 + H201 · L3B: C401 + E403 | Vào phòng · **CP4 14:30** |
| 14:30–16:00 | Theo zone | **Demo Zone:** mọi nhóm demo trong zone của mình |
| 16:00–18:00 | Cả phòng | **Demo Phòng:** các nhóm top của mỗi zone demo trước cả phòng |
| 23:59 Thứ Bảy 28/11 | — | **Hạn chót** |

---

## Chấm điểm

**100 = 15 điểm nộp (4 checkpoint) + 85 điểm chấm bài + 5 điểm bonus**, tổng tối đa 100.

| Phần | Điểm |
|---|---|
| Bằng chứng pain (data / phỏng vấn / khảo sát) | 14 |
| Impact có số | 11 |
| **Giải pháp AI: thiết kế + bản chạy thử** | **16** |
| Định nghĩa "tốt": bộ câu thử + metric | 14 |
| Báo cáo đánh giá | 8 |
| Mô phỏng chi phí khi dùng thật | 12 |
| Slide & demo | 10 |
| *Bonus:* người dùng thử | +5 |

- **Không xét giải** nếu thiếu: bản chạy thử gọi AI thật · bằng chứng pain ≥1 nguồn · bộ câu thử ≥20 câu có % đạt · slide PDF.
- **Kết quả thấp mà trung thực vẫn được đủ điểm.** Số bị sửa hoặc giấu (ví dụ đổi chuẩn "đạt" sau CP2, bỏ câu thử trượt) → phần đó 0 điểm.
- Chi tiết từng tiêu chí: [03-rubric.md](03-rubric.md).

## Thể thức và giải

Công bố sau.

---

## Luật chung

1. **Dùng AI để build thoải mái**, nhưng mỗi người phải giải thích được phần có tên mình. Không giải thích được thì phần đó 0 điểm. Ghi 2–3 dòng "dùng AI vào việc gì" trong `docs/ai-usage.md`.
2. **Chuẩn "đạt" chốt tại CP2**, giữ nguyên đến hạn chót.
3. **Sau CP4** được sửa code, báo cáo, slide, và ghi changelog (`spec.md` §10). **Không** sửa chuẩn "đạt", câu thử trong bộ, số liệu bằng chứng, kết quả các lượt đã chạy. Chạy thêm thì ghi thành lượt mới.
4. **Giải** xét trên bản CP4 + phần demo. **Điểm lab** chấm trên commit cuối trước 23:59 Thứ Bảy 28/11.
5. **Đổi track** được trước CP2: báo lab coach và ghi trong lần nộp CP2. Sau CP2 chỉ được thu hẹp lát cắt.
6. **Không commit API key** (để trong `.env`). Repo có API key hoặc dữ liệu cá nhân thật → **trừ 10 điểm**, gỡ ngay. Thông tin thành viên trong `TEAMS.md` là bắt buộc, không tính vào lỗi này. Luật dùng dữ liệu: [01-challenge-brief → Dữ liệu](01-challenge-brief.md#data).

## Nộp bài

1. **Tạo repo công khai, chép thư mục [starter-repo/](starter-repo/README.md) vào.**
2. **Tên repo:** `K5-Day15-<lớp>-<tên nhóm>`, ví dụ `K5-Day15-L3A-StudyPulse`. Tên nhóm viết liền, không dấu.
3. **Kiểm công khai:** mở link repo bằng cửa sổ ẩn danh, mở được mới đúng.
4. **`TEAMS.md` ở thư mục gốc repo:** ghi đầy đủ thành viên, mã học viên, vai trò, phần việc, theo đúng mẫu có sẵn trong [starter-repo/TEAMS.md](starter-repo/TEAMS.md). **Khi chấm và đánh giá, BTC quét file này để ghép điểm cho từng người, nên phải làm đúng format.** Kiểm bằng `python run.py check`.

## Kẹt thì hỏi ai

- Tại lớp (chiều Thứ Sáu, buổi demo Thứ Bảy): **lab coach của zone**.
- Ngoài giờ lớp, kể cả sáng Thứ Bảy: kênh hỗ trợ, BTC thông báo lúc khai mạc.
- Kẹt kỹ thuật quá **20 phút** thì hỏi ngay, đừng ngồi một mình.
- Câu hỏi hay gặp: [02-guide → Hỏi nhanh](02-guide.md#hoi-nhanh).

---

**Đọc tiếp:** [01-challenge-brief.md](01-challenge-brief.md) → chọn track ở [tracks/](tracks/README.md) → làm theo [02-guide.md](02-guide.md).
