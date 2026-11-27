# Guide — làm từng bước, 5 giai đoạn, bám 4 mốc

> [README](README.md) → [01-challenge-brief](01-challenge-brief.md) → [tracks/](tracks/README.md) → **[02-guide]** → [03-rubric](03-rubric.md)

**Đây là file nhóm mở suốt hai ngày.** Đứng ở bước nào, đọc bước đó. Giờ, mốc và luật nằm ở [README](README.md); điểm nằm ở [03-rubric](03-rubric.md) — file này chỉ dạy **làm thế nào**.

Mỗi giai đoạn mở đầu bằng **câu hỏi nhóm phải tự trả lời** — đó là phần quan trọng nhất. Mẫu và bảng chỉ để chốt lại câu trả lời. Mẫu không chọn hộ nhóm người dùng, lát cắt, metric hay ngưỡng: giám khảo sẽ hỏi đúng vào những quyết định đó.

---

## Bản đồ một trang

| Giai đoạn | Bước | Ra file (trong repo nhóm) | Mốc |
|---|---|---|---|
| <a id="giai-doan-1"></a>**1 · Khám phá** | [1.0 Ghép nhóm, tạo repo](#b1-0) · [1.1 Năm câu hỏi](#b1-1) · [1.2 Tìm bằng chứng pain](#b1-2) · [1.3 Bảng impact](#b1-3) · [1.4 Canvas](#b1-4) | `README.md` · `evidence/` · `spec.md` §1–2 · `canvas.md` | **CP1** 17:00 Thứ Sáu 27/11 |
| **2 · Thiết kế** | [2.1 Câu hỏi thiết kế](#b2-1) · [2.2 Kiến trúc & mức tự động](#b2-2) · [2.3 Chỗ khó → câu thử](#b2-3) · [2.4 Định nghĩa "tốt" và bộ câu thử](#b2-4) · [2.5 Tự soát](#b2-5) | `spec.md` §3–7 · `data/DATA_CARD.md` · `eval/benchmark.csv` · `eval/metric_spec.yaml` | **CP2** 19:30 Thứ Sáu 27/11 |
| **3 · Build** | [3.1 Câu hỏi định hướng](#b3-1) · [3.2 Bản chạy thử làm trọn lát cắt](#b3-2) · [3.3 Nối model & an toàn](#b3-3) · [3.4 Lượt 1 & tự soát](#b3-4) | `codebase/` · `eval/run-1.csv` | **CP3** 10:00 Thứ Bảy 28/11 |
| **4 · Đo & tính tiền** | [4.1 Đánh giá: lượt 1 → lượt 2](#b4-1) · [4.2 Mô phỏng chi phí](#b4-2) · [4.3 Người dùng thử *(bonus)*](#b4-3) · [4.4 Tự soát](#b4-4) | `eval/README.md` · `eval/report.md` · `cost/` · `validation/` | **CP4** 14:30 Thứ Bảy 28/11 |
| **5 · Demo & nộp** | [5.1 Slide](#b5-1) · [5.2 Checklist](#b5-2) · [5.3 Demo & hạn chót](#b5-3) | `demo-slides.pdf` · `reflection/` | Demo Zone · Demo Phòng · **23:59 Thứ Bảy 28/11** |

Phụ lục: [Bản đồ 15 ngày — bước nào ôn lại ngày nào](#phu-luc) · [Hỏi nhanh](#hoi-nhanh)

### Cách chia việc: cả nhóm cùng đi, chia cặp trong chặng

Pain, impact, giải pháp, đánh giá, chi phí là **một câu chuyện**. Ai cũng phải kể lại được cả câu chuyện — giám khảo hỏi bất kỳ ai.

1. **Hiểu người dùng: cả nhóm cùng làm.** Mỗi người tự hỏi ≥1 người dùng hoặc tự đào ≥1 câu hỏi trên data. Tổng hợp làm chung.
2. **Chia theo cặp, không chia theo người**, và chỉ chia trong một chặng. Hết chặng thì đổi cặp hoặc đổi việc.
3. **15 phút trước mỗi checkpoint, cả nhóm đi lại câu chuyện:** Pain → Impact → Giải pháp → Đánh giá → Chi phí. Chỗ nào lệch thì sửa.
4. **Ai cũng chạy được** `run.py eval` và `run.py simulate`, và giải thích được một câu thử trượt.

| Chặng | Giờ | Cả nhóm cùng làm | Chia cặp | Bước |
|---|---|---|---|---|
| 1 · Ghép nhóm + người dùng | Zoom sáng Thứ Sáu 27/11 | Ghép nhóm, bầu đội trưởng · chọn track · ai là người dùng · giả thuyết pain | Mỗi người hẹn ≥1 người / chia nhau gửi khảo sát / mở data xem thử | 1.0–1.2 |
| 2 · Canvas | 16:00–17:00 Thứ Sáu 27/11 | Hoàn thiện Canvas | — | 1.3–1.4 → **CP1** |
| 3 · Pain trước, rồi khung | 17:00–19:30 Thứ Sáu 27/11 | Mỗi người 1 cuộc hỏi / 1 câu đào → **20 phút tổng hợp chung** → chốt lát cắt + sơ đồ cùng nhau | Cặp X: khung bản chạy thử · Cặp Y: data card + 10 câu thử + metric spec → **đổi chéo review** | 2.1–2.5 → **CP2** |
| 4 · Chạy thật | Tối Thứ Sáu 27/11 → 10:00 Thứ Bảy 28/11 | Sáng Thứ Bảy 28/11, 30 phút: chốt bằng chứng + bảng impact · chạy lượt 1 **cùng nhau** | Cặp X: nối model thật + chặn rủi ro · Cặp Y: mở rộng 20–30 câu thử | 3.1–3.4 → **CP3** |
| 5 · Đo & tính tiền | 10:00–13:00 Thứ Bảy 28/11 | **Ngồi chung đọc các câu trượt** → chọn 1 cải tiến | Cặp X: cải tiến → lượt 2 · Cặp Y: mô phỏng chi phí · *(bonus)* mỗi người 1 người dùng thử | 4.1–4.4 |
| 6 · Kết luận | 13:00–14:30 Thứ Bảy 28/11 | Go / iterate / stop · tập demo, ai cũng nói 1 phần | Một cặp làm slide, một cặp quay video dự phòng | 5.1–5.2 → **CP4** |

Nhóm 3 người: một cặp + một người lẻ. Nhóm 5 người: hai cặp + một người lẻ giữ mạch câu chuyện Pain → Impact. Người lẻ đổi sang cặp khác ở chặng sau.

### Mỗi bước viết theo một khuôn

> **Câu hỏi** nhóm phải tự trả lời · **Input** cần có trước · **Làm** · **Output** (file) · **Nhóm tự quyết** · **Xong khi** · **Ôn lại** (ngày học, lab) · **Tham khảo**

---

# Giai đoạn 1 · KHÁM PHÁ *(sáng Thứ Sáu 27/11, sau buổi Zoom → 17:00 Thứ Sáu 27/11 · CP1)*

<a id="b1-0"></a>
## 1.0 Ghép nhóm, tạo repo *(cả nhóm · 20 phút · trong buổi Zoom)*

- **Làm:**
  1. Tự ghép nhóm **3–5 người**. Bầu **đội trưởng** — người nộp form cả 4 mốc bằng một mã học viên.
  2. Mỗi người ghi 1 dòng: mạnh gì (hỏi người dùng · code · dữ liệu · trình bày) — để chia cặp ở giai đoạn 2–4.
  3. Tạo repo nhóm từ [starter-repo/](starter-repo/README.md) (đặt tên theo [README → Nộp bài](README.md#nộp-bài)). Điền **`TEAMS.md`** đúng format: BTC quét file này để ghép điểm cho từng người.
- **Output:** repo công khai, có `TEAMS.md` đúng format.
- **Xong khi:** mở link repo bằng cửa sổ ẩn danh được · `python run.py check` không báo gì ở phần "Kiểm TEAMS.md".

<a id="b1-1"></a>
## 1.1 Năm câu hỏi — theo đúng thứ tự *(cả nhóm · 20 phút)*

- **Input:** file track đã chọn trong [tracks/](tracks/README.md).
- **Câu hỏi:**
  1. **Ai** trực tiếp làm việc này? Một vai cụ thể — "học viên L3 đi làm, tối mới xem bài pre-class", không phải "học viên nói chung".
  2. Họ đang cố **hoàn thành việc gì**? Viết một câu `động từ + đối tượng + bối cảnh`, không có chữ AI. Tự kiểm: bỏ AI đi, việc đó còn tồn tại không? Không còn = đang tìm chỗ nhét AI, chọn lại.
  3. Hôm nay họ giải bằng gì (tua video · hỏi bạn · hỏi trợ giảng · ChatGPT riêng · bỏ qua)? **Nó hỏng ở đâu, và vì sao họ chưa bỏ nó?**
  4. **Bằng chứng nào** cho thấy họ đau thật — số đếm được, hay lời nguyên văn của họ? Cảm nhận của nhóm chưa phải bằng chứng.
  5. Nhóm thấy **≥3 hướng** — vì sao chọn hướng này? Trả lời bằng số ở [1.3](#b1-3).
- **Làm:** mỗi người viết 3 lần gần nhất **chính mình** vướng ở việc này (học bài gì, kẹt đâu, hỏi ai, mất bao lâu). Đây là để hiểu việc — **người trong nhóm không tính là bằng chứng**.
- **Output:** câu trả lời 1–3 vào `spec.md` §1; giả thuyết hai dòng vào `evidence/hypothesis.md`: *"Mình nghĩ… / Mình đúng nếu thấy…"*.
- **Nhóm tự quyết:** người dùng chính là vai nào.
- **Ôn lại:** ngày 2 · lab ngày 2.

> **Tham khảo — Jobs to be done (JTBD).** Câu 1–3 chính là JTBD rút gọn: *người làm việc* (câu 1) → *job statement* (câu 2) → *cách đang làm và chỗ hỏng* (câu 3). Muốn rõ hơn, viết 2–3 **job story**: `Khi [tình huống], tôi muốn [động lực], để [kết quả]` — lấy tình huống từ chuyện thật. Đọc thêm: [further-reading/jtbd-full-worksheet.md](further-reading/jtbd-full-worksheet.md).

<a id="b1-2"></a>
## 1.2 Tìm bằng chứng pain *(cả nhóm · bắt đầu ngay sau Zoom · xong trước CP3)*

- **Câu hỏi:** Pain này có thật không, ở bao nhiêu người, và vì sao?
- **Ba nguồn bằng chứng, ngang nhau.** Tối thiểu **≥1 nguồn đạt ngưỡng**. Mạnh nhất: **đào data ra insight → hỏi người dùng để kiểm lại** (hoặc nghe người dùng kể → vào data đếm xem có bao nhiêu người như vậy).

| Nguồn | Ngưỡng tối thiểu | Ghi ở |
|---|---|---|
| **Đào data** — Track A: data BTC cấp trong [data/](data/) (vd [data/preclass/](data/preclass/README.md)), kênh công khai của khoá. Track B–F: **review công khai** (Google Play, App Store, Google Maps…), số liệu công khai có nguồn | Đếm được: **x/N và %** · cách chọn mẫu và cách đếm ghi trước, người khác chạy lại được · ≥5 ví dụ cụ thể | `evidence/data-mining.md` + script / công thức |
| **Phỏng vấn** | **≥3 người ngoài nhóm**, đúng người dùng · 10–15 phút / người · hỏi chuyện **1 tháng qua** · mỗi người 1 file ghi chép | `evidence/interviews/P1.md`… |
| **Khảo sát** | **≥20 người ngoài nhóm**, đúng người dùng · giữ log đủ câu hỏi và từng câu trả lời | `evidence/survey/` |

Cả ba nguồn: tổng **≥5 trích dẫn hoặc ví dụ nguyên văn**, có nguồn, bỏ tên.

**Đào data — cách làm, không phải đào cái gì:**
1. **Đọc trước, đếm sau.** Mở 30–50 dòng đầu, đọc từ điển cột, hiểu một dòng là gì. Ghi ra các *kiểu* hành vi thấy được rồi mới định nghĩa thứ cần đếm.
2. **Viết cách đếm trước khi chạy:** đếm gì · trên tập nào · lọc gì · mẫu số là gì. Mẫu số sai là lỗi hay gặp nhất.
3. **Đếm được mới là bằng chứng:** "x/N (y%) …" ✓ · "nhiều bạn…" ✗. Ghi giới hạn của data (thiếu gì, từ ngày nào).
4. Data chỉ cho biết người ta **làm gì**. Muốn biết **vì sao** → hỏi người dùng.

**Đào review công khai (track B–F):**
1. **Chọn nguồn và ghi cách chọn mẫu trước khi đọc.** Ví dụ: "N review mới nhất của app X trên Google Play, từ ngày … đến ngày …, mọi mức sao". Lọc riêng 1–3 sao cũng được, nhưng phải ghi rõ, vì như vậy mẫu nghiêng về phía phàn nàn.
2. **Đọc thử khoảng 30 review, rồi mới đặt nhãn** theo loại vấn đề. Mỗi nhãn có một câu định nghĩa, để người khác gắn nhãn cũng ra giống mình.
3. **Gắn nhãn từng review vào một bảng:** nguồn · ngày · số sao · trích tối đa 2 câu · nhãn. Không chép tên người viết.
4. **Đếm x/N và %.** N là số review đã đọc và gắn nhãn, kể cả review không liên quan. Ghi link nguồn và ngày xem.
5. **Biết giới hạn:** người viết review thường là người đang bực, nên % trong review không phải % của mọi người dùng. Kiểm lại bằng vài cuộc phỏng vấn hoặc một khảo sát ngắn thì bằng chứng mạnh hơn hẳn.

**Phỏng vấn — 3 quy tắc, 3 phản xạ:**
- **Quy tắc:** (1) nói về cuộc sống của họ, không giới thiệu ý tưởng của mình · (2) hỏi chuyện cụ thể **đã xảy ra**, không hỏi họ sẽ làm gì · (3) nói ít, nghe nhiều.
- **Phản xạ khi nghe:** được khen → cảm ơn rồi quay lại chuyện thật · nghe "mình thường… / mình sẽ…" → hỏi *"lần gần nhất là khi nào?"* · nghe đề xuất tính năng → hỏi *"cái đó giúp bạn làm được gì?"*
- **Nên hỏi:** *"Lần gần nhất bạn [làm việc này], bạn đã làm gì? Mất bao lâu?"* · *"Bạn đã thử cách nào khác — vì sao vẫn chưa bỏ?"* · **Tránh:** *"Bạn có muốn tính năng X không?"* (ai cũng trả lời có).
- n = 3 **không ghi %** — viết "2/3 người" và liệt kê từng người.
- Mẫu ghi chép và tin nhắn hẹn: `evidence/interviews/TEMPLATE.md` trong repo nhóm.

**Khảo sát:** 8–10 câu, hỏi **hành vi đã xảy ra** (lần gần nhất, bao nhiêu lần / tuần, mất bao lâu), không hỏi "có thích không". Mẫu form để chép sang Google Form: `evidence/survey/TEMPLATE.md`.

- **Nhóm tự quyết:** nguồn nào chính, nguồn nào để kiểm lại.
- **Xong khi:** đủ ngưỡng ≥1 nguồn · ≥5 trích dẫn / ví dụ · `evidence/summary.md` có số chính + kết luận "giả thuyết đúng / sai / phải đổi".
- **Ôn lại:** ngày 2, ngày 6 · lab ngày 2, lab ngày 6.
- **Tham khảo:** [further-reading/mom-test-summary.md](further-reading/mom-test-summary.md) (phỏng vấn).
- **Không tính là bằng chứng:** người trong nhóm · dữ liệu **giả lập** · trò chuyện với nhân vật AI.

<a id="b1-3"></a>
## 1.3 Bảng impact — chọn bài toán bằng số *(cả nhóm · 20 phút · cập nhật đến CP3)*

- **Câu hỏi:** Trong ≥3 hướng, hướng nào đáng làm nhất — và vì sao, bằng số?
- **Làm:** mỗi hướng một dòng:

  | Hướng | Bao nhiêu người gặp | Bao nhiêu lần / tháng | Mỗi lần tốn gì (phút / điểm / niềm tin) | Impact / tháng | Làm kịp không | Chọn? |
  |---|---|---|---|---|---|---|

  Mỗi số **trỏ về nguồn**: data, phỏng vấn, khảo sát, quy mô khoá có nguồn — không có nguồn thì ghi rõ *(tự ước tính)*. Hai hướng sát nhau → chọn hướng **bằng chứng mạnh hơn**.
- **Output:** `spec.md` §2 — bảng + lý do chọn + hướng bị loại (giữ lại, đừng xoá).
- **Giữ lại cho sau:** số lần / tháng của từng kiểu người dùng → dùng làm persona ở [4.2 Mô phỏng chi phí](#b4-2).
- **Ôn lại:** ngày 2, ngày 13.

<a id="b1-4"></a>
## 1.4 Canvas 7 dòng → nộp CP1 *(cả nhóm · 16:00–17:00 Thứ Sáu 27/11)*

- **Output:** `canvas.md` (mẫu trong repo nhóm):

  | # | Dòng |
  |---|---|
  | 1 | Track + lát cắt dự kiến |
  | 2 | Người dùng chính (một vai cụ thể) |
  | 3 | Pain một câu: ai — đang làm gì — vướng đâu — hậu quả |
  | 4 | Bằng chứng đầu (CP1: giả thuyết + nguồn sẽ kiểm · CP2: số đầu tiên + 1 trích dẫn) |
  | 5 | **Lát cắt một câu**: 1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả |
  | 6 | AI tự làm đến đâu + 1 dòng lý do (xem [2.2](#b2-2)) |
  | 7 | Phân công có tên |

- **Xong khi:** dòng 2 không phải "học viên nói chung" · dòng 5 đúng một câu.
- **Nộp CP1:** xem [README → Checkpoint](README.md#checkpoint). Tự soát: [03-rubric.md](03-rubric.md).
- Kẹt >30 phút chưa chọn được hướng? Hỏi: *"nhóm mình là người dùng thật của cái nào nhiều nhất?"* — chọn cái đó.

---

# Giai đoạn 2 · THIẾT KẾ *(17:00 → 19:30 Thứ Sáu 27/11 · CP2)*

<a id="b2-1"></a>
## 2.1 Câu hỏi thiết kế *(cả nhóm · 15 phút, ngay sau 20 phút tổng hợp pain)*

1. Người khác đã giải bài này thế nào — một điều đáng học, một điều đáng né, mình khác gì? *(mỗi người thử nhanh 1 sản phẩm gần giống, 10 phút)*
2. AI nên **tự làm đến đâu** — nếu sai thì ai chịu gì, sửa đắt hay rẻ?
3. Khi **sai hoặc không chắc**, sản phẩm nói gì, hiện gì, cho người dùng làm gì tiếp?
4. **"Tốt" nghĩa là gì** với người dùng, đo bằng gì, ngưỡng bao nhiêu?

- **Output:** `spec.md` §3 (giải pháp tương tự, 3–4 dòng).
- Lát cắt **phải dựa trên pain đã tổng hợp** ở [1.2](#b1-2), không dựa trên ý tưởng ban đầu.

<a id="b2-2"></a>
## 2.2 Kiến trúc & mức tự động *(cả nhóm · 30 phút)*

- **Câu hỏi:** Giải pháp gồm những phần nào, AI quyết định ở đâu, dựa trên dữ liệu gì, rủi ro chặn ở đâu, người duyệt ở đâu?
- **Làm — một sơ đồ** (vẽ tay chụp ảnh, Mermaid hay draw.io đều được) gồm:
  1. **Hình dạng** — chọn một, kèm 2 dòng lý do:

     | Hình dạng | Hợp khi |
     |---|---|
     | Workflow cố định (các bước định sẵn, AI làm 1–2 bước) | Việc lặp lại, các bước rõ — thường **rẻ hơn, dễ đo hơn** |
     | Một agent (AI tự chọn bước tiếp, gọi công cụ) | Đường đi thay đổi theo input |
     | Nhiều agent (mỗi agent một vai) | Các vai thật sự khác nhau (vd lớp học có nhiều vai AI, hướng lớp học kiểu mới ở track A) |

     Chọn hình dạng đơn giản nhất làm được lát cắt. Phải nói được vì sao **không** chọn cái phức tạp hơn.
  2. **AI dựa vào đâu:** dữ liệu / công cụ của bài toán mà AI dùng (tra đoạn bài, đọc lịch, đọc thông báo…). Mỗi công cụ: tên · input · output · có tác động ra ngoài không (gửi tin, sửa dữ liệu). Số công cụ do thiết kế quyết định.
  3. **Chỗ chặn rủi ro:** rủi ro lớn nhất của lát cắt (bịa nguồn, lộ đáp án, gửi nhầm…) bị chặn ở đâu, bằng gì.
  4. **Chỗ người duyệt:** việc gì AI **không** được tự làm.
- **Mức tự động — chọn theo "sai thì ai chịu gì":**

  | Mức | Khi nào đúng | Ví dụ trong khoá |
  |---|---|---|
  | **AI gợi ý, người quyết** | Sai thì đắt (kiến thức sai đến học viên, điểm số) | Quiz AI sinh, giảng viên duyệt từng câu |
  | **AI tự làm khi chắc, chuyển người khi không** | Đa số trường hợp lành, số ít hiểm | Trả lời khi có căn cứ trong tài liệu; không có → chuyển TA |
  | **AI tự làm** | Sai thì rẻ, người dùng tự thấy và sửa được | Sinh mốc thời gian cho video |

- **Nguyên tắc thiết kế — chọn ≥3, mỗi cái chỉ vào chỗ cụ thể trên sơ đồ:**
  - **G10 — Thu hẹp phạm vi khi không chắc** *(bắt buộc)*: không chắc → hỏi lại một câu, hoặc trả lời kèm giới hạn.
  - **G1 / G2 — Nói rõ làm được gì, làm tốt đến đâu:** người dùng biết khi nào nên tin, khi nào nên kiểm lại.
  - **G8 / G9 — Dễ bỏ qua, dễ sửa:** người dùng gạt hoặc sửa được output ngay.
  - **G11 — Giải thích vì sao:** "vì đoạn này của bài nói…" — gắn với việc làm tiếp.
- **Output:** `spec.md` §4 (sơ đồ + lý do + mức tự động + nguyên tắc).
- **Nhóm tự quyết:** hình dạng, công cụ, mức tự động.
- **Xong khi:** người ngoài nhóm nhìn sơ đồ kể lại được luồng chính · mỗi nguyên tắc chỉ được vào một chỗ.
- **Ôn lại:** ngày 3, ngày 5, ngày 8, ngày 11 · lab ngày 3, lab ngày 5, lab ngày 8.

> **Tham khảo — chọn workflow hay agent.** [Building effective agents](https://www.anthropic.com/research/building-effective-agents) (Anthropic): khi nào workflow cố định là đủ, khi nào mới cần agent, và các mẫu workflow hay gặp (nối chuỗi, phân luồng, chạy song song, điều phối, tự kiểm rồi sửa).

> **Tham khảo — HAX và PAIR.** Đủ 18 nguyên tắc HAX kèm câu tự kiểm và ví dụ trong khoá: [further-reading/hax-guidelines.md](further-reading/hax-guidelines.md). PAIR theo chương: [further-reading/pair-guidebook-digest.md](further-reading/pair-guidebook-digest.md) — *Mental Models* (đặt kỳ vọng thấp hơn khả năng một chút) · *Explainability + Trust* (tin đúng mức, hiện căn cứ để người dùng tự kiểm) · *Feedback + Control* (người dùng luôn bỏ qua AI được) · *Errors + Graceful Failure* (mỗi loại lỗi một đường lui). PAIR 1.3 gợi ý ba câu nên viết vào spec: *"AI luôn phải {…}"* · *"AI không được {…} kể cả khi người dùng vô tình yêu cầu"* · *"Nếu AI dự đoán yếu, người dùng không phiền {sửa nhỏ} miễn là {điều kiện}"*.

<a id="b2-3"></a>
## 2.3 Chỗ khó → nguồn câu thử *(cả nhóm · 20 phút)*

- **Câu hỏi:** Ở lát cắt này, AI dễ sai ở đâu nhất — và sai thì hậu quả gì?
- **Làm:** cụ thể hoá **4 lớp chỗ khó** cho lát cắt:
  1. **Nguồn sự thật** — chỗ nào AI bịa được? Không có căn cứ thì làm gì?
  2. **Mơ hồ / thiếu thông tin** — hỏi lại, đoán có báo, hay từ chối?
  3. **Ngoài phạm vi / thẩm quyền** — người dùng đòi gì mà sản phẩm không được làm?
  4. **Đặc thù lĩnh vực** — sai ở đâu thì người dùng mất gì đắt nhất trong lĩnh vực này? Ví dụ: track A, học viên học sai, mất điểm, lỡ hạn · track B, bỏ sót dấu hiệu nguy hiểm, gợi ý thuốc sai · track C, báo còn chỗ khi đã hết, sai giờ bay · track D, bồi thường vượt hạn mức, vi phạm dị ứng · track E, mất tiền, mở chặn giao dịch lừa đảo · track F, nhóm tự chỉ ra. Mục "An toàn" và "Chuẩn đạt nên có điều kiện cứng" trong file track là nơi bắt đầu.

  Chốt **≥6 kịch bản**, mỗi kịch bản một dòng: `tình huống | lớp | hành vi mong muốn (nói gì, hiện gì, cho làm gì tiếp)`. Thêm **2 kịch bản tấn công** nhắm vào chỗ chặn rủi ro ở [2.2](#b2-2) (vd người dùng cố bắt AI làm điều bị cấm).
- **Output:** `spec.md` §5. **Mỗi kịch bản thành ≥1 câu thử** ở [2.4](#b2-4).
- **Xong khi:** có ít nhất một kịch bản làm nhóm **sợ** khi demo. Chưa có = chưa đủ hiểm.
- **Ôn lại:** ngày 9, ngày 11.
- **Tham khảo:** bốn nguồn lỗi của PAIR chương 6 — [further-reading/pair-guidebook-digest.md](further-reading/pair-guidebook-digest.md) §6.2.

<a id="b2-4"></a>
## 2.4 Định nghĩa "tốt" và bộ câu thử *(một cặp · ~1 giờ · cặp kia review chéo · chốt trước CP2)*

- **Câu hỏi:** Thế nào là **đủ tốt với người dùng** — và đo bằng gì để người ngoài nhóm chấm ra cùng kết quả?
- **Input:** lát cắt ([2.1](#b2-1)) · kịch bản ([2.3](#b2-3)) · ghi chép / số đào được ([1.2](#b1-2)).
- **Làm — sáu bước:**
  1. **Nhìn output thật trước, viết tiêu chí sau.** Chạy tay 10–20 input (ChatGPT/Claude với prompt nháp cũng được), đọc từng output, ghi thô: dùng được / sửa được / không chấp nhận được. Tiêu chí tốt được **chưng cất từ lỗi đã thấy**.
  2. **Đặt tên cho lỗi:** bịa nguồn · lạc trình độ · trích sai đoạn · đoán khi thiếu thông tin · vượt thẩm quyền… Đối chiếu 4 lớp ở [2.3](#b2-3).
  3. **Viết `eval/metric_spec.yaml` — ≥3 metric**, mỗi metric: định nghĩa kiểm chứng được · cách chấm (code / LLM chấm / người chấm) · ngưỡng. "Trả lời hay" không đo được; "mọi khẳng định có mã đoạn nguồn đúng" đo được.
  4. **Người thứ hai chấm thử:** hai người chấm độc lập cùng 5 output theo spec → lệch ≥2/5 thì định nghĩa còn mơ hồ, viết lại.
  5. **Viết bộ câu thử** `eval/benchmark.csv` — cột `id, input, expected, pass_criterion, type, source`:
     - **CP2: ≥10 câu. CP3: 20–30 câu.** `type` ∈ `thuong` / `kho` / `tu_choi` · ≥5 `kho`, ≥2 `tu_choi` (gồm 2 câu tấn công ở [2.3](#b2-3)).
     - Cột `source` ghi câu lấy từ đâu, bắt đầu bằng một trong 4 mã: `nguoi_dung` (lời người dùng) · `data_that` (data thật) · `tu_viet` · `sinh_seed` (sinh có seed), chi tiết ghi sau dấu `:` — vd `nguoi_dung: P2`. **≥1/3 câu từ lời người dùng hoặc data thật.**
     - Phủ đều bằng **lưới input**: liệt kê 3–5 chiều mà đổi giá trị thì đáp án phải đổi (ai hỏi · loại câu · mức thiếu thông tin · sai thì đắt cỡ nào · hành vi mong đợi trả lời / hỏi lại / từ chối). Mỗi câu thử gắn một tổ hợp; ô trống = lỗ hổng. **Người thiết kế độ phủ, LLM chỉ viết biến thể câu chữ** — 50 câu LLM tự sinh thường chỉ bằng 3 câu thật.
  6. **Chốt chuẩn "đạt"** trong `spec.md` §7: *"Đạt khi ≥ __% câu qua, và [điều kiện cứng, vd 100% câu `tu_choi` qua]"*. **Chốt trước 19:30 Thứ Sáu 27/11, không sửa sau.**
- **Kèm `data/DATA_CARD.md`** (một trang): dùng dataset nào · từ đâu · xử lý những bước gì (lọc, làm sạch, ẩn danh, chia) · bao nhiêu dòng · phiên bản. Data giả lập: ghi cách sinh + seed + nhãn `synthetic`.
- **Lệnh:** `python run.py check` — kiểm đủ cột, đủ số câu `kho` / `tu_choi`.
- **Nhóm tự quyết:** metric nào quan trọng nhất **với người dùng** (từ pain, không từ AI) · ngưỡng.
- **Xong khi:** `run.py check` không lỗi · người chấm thử khớp ≥4/5 · ngưỡng đã commit trước 19:30 Thứ Sáu 27/11.
- **Ôn lại:** ngày 5, ngày 6, ngày 9 · lab ngày 5, lab ngày 6, lab ngày 9.
- **Tham khảo:** PAIR 2.3 "Evolve AI with evaluation" — các chiều chất lượng (đủ ý · đúng yêu cầu · có căn cứ · mạch lạc…): [further-reading/pair-guidebook-digest.md](further-reading/pair-guidebook-digest.md).

<a id="b2-5"></a>
## 2.5 Tự soát → nộp CP2 *(cả nhóm · 15 phút)*

- [ ] Canvas cập nhật: số bằng chứng đầu + lát cắt đã chốt + 1 dòng "đã đổi gì so với CP1"
- [ ] Đã bắt đầu tìm bằng chứng (đã hỏi / đã hẹn / đã gửi form / đã đào và có cách đếm)
- [ ] Sơ đồ kiến trúc trong `spec.md` §4
- [ ] `eval/benchmark.csv` ≥10 câu · `eval/metric_spec.yaml` · chuẩn "đạt" trong `spec.md` §7 · `data/DATA_CARD.md` bản đầu
- [ ] Bản chạy thử dạng khung: `python run.py` đi hết luồng với AI giả (xem [3.2](#b3-2))

Nộp CP2: [README → Checkpoint](README.md#checkpoint). **Trước khi rời lớp:** nên có 1 người lấy key và gọi thử được 1 câu ([3.3](#b3-3)) — sáng Thứ Bảy 28/11 không có lớp.

---

# Giai đoạn 3 · BUILD *(19:30 Thứ Sáu 27/11 → 10:00 Thứ Bảy 28/11 · CP3)*

<a id="b3-1"></a>
## 3.1 Câu hỏi định hướng

*"Demo 2 phút thì người dùng đưa gì vào, AI quyết định gì, ra cái gì?"* — build đúng đường đó trước, mọi thứ khác sau. Giao diện là phụ: một màn hình dòng lệnh làm trọn lát cắt tốt hơn giao diện đẹp chưa nối AI.

<a id="b3-2"></a>
## 3.2 Bản chạy thử làm trọn lát cắt *(cặp X · khung trước CP2 · AI thật trước CP3)*

- **Bản chạy thử phải:**

  | # | Yêu cầu | Kiểm thế nào |
  |---|---|---|
  | 1 | **Làm trọn lát cắt**: input của người dùng → AI ra quyết định trung tâm → kết quả người dùng dùng được | Demo 1 trường hợp thường + 1 trường hợp khó |
  | 2 | **Quyết định dựa trên dữ liệu / công cụ của bài toán**, không trả lời từ trí nhớ model | Khớp sơ đồ [2.2](#b2-2) · câu thử ngoài dữ liệu thì nói "không có" |
  | 3 | **Đúng hình dạng đã chọn** ở [2.2](#b2-2) | Code khớp sơ đồ |
  | 4 | **Chạy được bằng `run.py eval` và `run.py simulate`** | Hai lệnh chạy không lỗi |

- **Làm:**
  1. Viết phần của nhóm trong `codebase/`: nối model (`ai.py`), công cụ của bài toán (`tools.py`), luồng chính (`agent.py`). Khung trong [starter-repo/](starter-repo/README.md) đã tự ghi log token và lượt gọi — nhóm không phải làm riêng.
  2. **Trước CP2:** cho AI trả câu giả cố định để luồng đi hết; công cụ có thể trả dữ liệu giả. Ghi rõ phần nào giả trong `spec.md` §4.
  3. **Trước CP3:** thay bằng lời gọi model thật ([3.3](#b3-3)).
- **Output:** `codebase/` · README repo nhóm có lệnh chạy.
- **Nhóm tự quyết:** prompt, công cụ, luồng — đây là bài của nhóm, khung không có sẵn.
- **Ôn lại:** ngày 3, ngày 4, ngày 7 · lab ngày 3, lab ngày 4, lab ngày 7.
- **Được dùng lại code lab của chính mình** — ghi rõ trong `docs/ai-usage.md`.

<a id="b3-3"></a>
## 3.3 Nối model & an toàn *(cặp X · tối Thứ Sáu 27/11 — việc dễ kẹt nhất, nên xong trước khi ngủ)*

- **Làm:**
  1. Lấy API key của nhóm, làm theo [starter-repo/docs/connect-model.md](starter-repo/docs/connect-model.md). Key để trong `.env`, **không commit**.
  2. `python run.py` hỏi thử 1 câu → `python run.py eval --try` chạy 3 câu thử, thấy số token > 0 là nối được.
  3. Cài chỗ chặn rủi ro đã thiết kế ở [2.2](#b2-2).
- **An toàn:** gói miễn phí có thể dùng dữ liệu để huấn luyện. Data trong `data/` của bộ đề đưa vào được. Dữ liệu người thật nhóm tự thu thì chỉ đưa bản đã bỏ tên hoặc đoạn đã viết lại ([01-challenge-brief → Data](01-challenge-brief.md#data)).
- **Kẹt quá 20 phút → hỏi ngay** ([README → Kẹt thì hỏi ai](README.md#kẹt-thì-hỏi-ai)). Ghi lỗi và cách xử lý — dùng lại cho reflection.
- **Ôn lại:** ngày 1, ngày 11, ngày 14.

<a id="b3-4"></a>
## 3.4 Lượt 1 & tự soát → nộp CP3 *(cả nhóm cùng chạy · sáng Thứ Bảy 28/11 trước 10:00)*

- **Làm:**
  1. Bộ câu thử đủ 20–30 câu. **Câu thử chỉ được thêm, không được sửa đáp án cho khớp kết quả.**
  2. `python run.py eval` → `eval/run-1.csv` (có run ID, model, token từng câu).
  3. Chấm từng câu theo `metric_spec.yaml`, điền cột `pass` → `python run.py score eval/run-1.csv`.
  4. Quay **video 30 giây**: thao tác thật, AI trả kết quả thật. YouTube "Không công khai" hoặc Drive "Bất kỳ ai có đường liên kết"; mở thử bằng cửa sổ ẩn danh.
- **Tự soát CP3:**
  - [ ] Bằng chứng pain đủ ngưỡng ≥1 nguồn + ≥5 trích dẫn / ví dụ ([1.2](#b1-2)) · bảng impact ([1.3](#b1-3))
  - [ ] 20–30 câu thử, ≥5 `kho`, ≥2 `tu_choi`
  - [ ] Bản chạy thử gọi AI thật · video 30 giây
  - [ ] `eval/run-1.csv` + kết quả `score`
  - [ ] `spec.md` §0–§7 đã commit
- Nộp CP3: [README → Checkpoint](README.md#checkpoint). **Lượt 1 thấp là bình thường** — số thật được đủ điểm.

---

# Giai đoạn 4 · ĐO & TÍNH TIỀN *(10:00 → 14:30 Thứ Bảy 28/11 · CP4)*

<a id="b4-1"></a>
## 4.1 Đánh giá: lượt 1 → một cải tiến → lượt 2 *(cả nhóm đọc lỗi · cặp X sửa · ~1,5 giờ)*

- **Câu hỏi:** Sản phẩm trượt ở đâu nhiều nhất, và sửa cái nào thì đáng nhất?
- **Làm:**
  1. **Cả nhóm ngồi chung đọc các câu trượt** của lượt 1. Gom thành nhóm lỗi có tên (dùng tên ở [2.4](#b2-4) bước 2).
  2. Chọn **một nhóm lỗi đau nhất với người dùng** → một lần cải tiến (có thể gồm vài thay đổi cùng nhắm nhóm lỗi đó).
  3. `python run.py eval` lại **trên cùng bộ câu thử** → `eval/run-2.csv` → `score`. Sửa chỗ này vỡ chỗ kia là bình thường — luôn chạy **trọn bộ**.
  4. *(Tuỳ chọn)* thử hai cấu hình (hai prompt, hai model) rồi chọn bằng số.
- **Output:**
  - `eval/report.md`: % đạt lượt 1 và lượt 2 so với chuẩn "đạt" · **≥3 lỗi** (input · output · vì sao sai) · đã sửa gì · lỗi còn lại.
  - `eval/README.md` — **Hồ sơ đánh giá một trang:** dataset nào → xử lý gì → bộ câu thử dựng ra sao (bao nhiêu câu, từ nguồn nào) → metric và cách chấm → đã chạy gì (bảng run ID · model · cấu hình · kết quả) → lỗi chính. Trang slide "Đánh giá thế nào" lấy từ đây.
- **Xong khi:** người ngoài nhóm đọc `eval/README.md` hiểu được nhóm đo cái gì, bằng gì, ra số nào.
- **Không được:** sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output.
- **Ôn lại:** ngày 9, ngày 14 · lab ngày 9.
- **Muốn sâu hơn (không bắt buộc, không có điểm riêng; giám khảo dùng để phân hạng khi hai nhóm sát điểm):** tách phần giữ riêng (held-out) ~20% không nhìn khi sửa · LLM chấm có hiệu chuẩn với ≥20 câu chấm tay · chạy ≥3 lần mỗi câu.

<a id="b4-2"></a>
## 4.2 Mô phỏng chi phí khi dùng thật *(cặp Y · ~1 giờ)*

- **Câu hỏi:** Nếu đưa vào dùng thật ở quy mô thật của sản phẩm, mỗi tháng tốn bao nhiêu — và có đáng so với impact không? Quy mô thật: track A là khoá học (lớp L3 hơn 700 học viên, cả khoá hơn 1.000); track B–F là số người dùng của sản phẩm hoặc nhóm người dùng nhóm nhắm tới, lấy từ nguồn công khai có link, không chép số 700 của khoá.
- **Input:** số lần dùng của từng kiểu người dùng ([1.3](#b1-3)) · tỉ lệ đạt ([4.1](#b4-1)) · bảng giá model ([further-reading/model-prices.md](further-reading/model-prices.md)).
- **Làm:**
  1. **Persona** `cost/personas.yaml`: ≥3 kiểu người dùng (dùng ít · vừa · nhiều), tỉ lệ mỗi kiểu, số lần dùng / tháng — **số lấy từ data, phỏng vấn, khảo sát**; thiếu thì ghi rõ *(tự ước tính)*.
  2. **Chạy mô phỏng:** `python run.py simulate` — sinh ≥50 phiên theo persona (seed cố định), **chạy thật qua bản chạy thử**, đo token vào / ra, số lần gọi model, số lần gọi công cụ, thời gian. CP3 thử trước 10 phiên để kiểm khung.
  3. **Chi phí / task thành công** = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt (từ lượt 2). Không lấy tỉ lệ đạt 100%.
  4. **Phóng lên quy mô thật:** số người dùng thật (có nguồn, hoặc ghi rõ *(tự ước tính)*) × tần suất → chi phí / tháng, **3 kịch bản thấp · cơ sở · cao**, ≥2 mức model (rẻ và mạnh).
  5. **So với impact:** chi phí / người / tháng so với giá trị tiết kiệm / người / tháng ([1.3](#b1-3)) → một dòng kết luận: đáng làm không.
- **Output:** `cost/cost-estimate.md` (bảng 3 kịch bản + kết luận) · `cost/simulate-N.csv`.
- **Xong khi:** mọi con số trong bảng truy được về file chạy mô phỏng hoặc nguồn ghi rõ.
- **Ôn lại:** ngày 1, ngày 13, ngày 14 · lab ngày 13, lab ngày 14.
- **Muốn sâu hơn:** bảng độ nhạy (model rẻ hơn, cache, cắt ngữ cảnh, giới hạn bước) · chi phí ngoài model (hosting, giờ công người duyệt) · quy mô nào thì bài toán còn đáng làm.

<a id="b4-3"></a>
## 4.3 Người dùng thử *(bonus · 2–3 người ngoài nhóm · 10 phút / người)*

Đổi chéo với nhóm khác là nhanh nhất, **nếu** bạn nhóm kia đúng là người dùng của lát cắt: track A, cả khoá là người dùng; track D, E, học viên cũng là người mua online, người dùng ví; track B, C, F, phải đúng vai (người đi khám, người đi du lịch…). Vai chuyên môn như dược sĩ, lễ tân thì phải hẹn người làm nghề thật.

**Một phiên — 5 nhịp:**
1. **Làm quen (~1'):** "Tụi mình đánh giá sản phẩm, không đánh giá bạn. Cứ nói to suy nghĩ."
2. **Bối cảnh (~1'):** "Kể lần gần nhất bạn [việc của lát cắt], bạn đã làm gì?"
3. **Giao việc (~1'):** giao theo **kết quả** ("dùng cái này để…"), không chỉ nút. Người thử tự cầm chuột.
4. **Quan sát (~5'):** **im lặng** ghi: làm gì đầu tiên, chỗ do dự, chỗ hiểu sai. Kẹt chỉ dùng: "Bạn sẽ làm gì tiếp?" · "Bạn nghĩ nó nên chạy thế nào?". Không thuyết minh, không hỏi "bạn có thích không".
5. **Hỏi sau (~2'):** điều gì khó hiểu nhất? · kết quả này bạn có tin không, vì sao? · có dùng thật không? · *"Nếu mai không được dùng nữa, bạn thấy: rất tiếc / hơi tiếc / không sao?"*

- **Output:** `validation/log.md` — mỗi người một dòng: `người thử (vai) | việc giao | quan sát | trích nguyên văn | mức nghiêm trọng` + 4 dòng tổng hợp: chủ đề lặp nhiều nhất · sửa gì trước demo (→ changelog) · giữ gì và vì sao · để dành sau.
- Hành vi quan sát được nặng hơn lời nói; "mình sẽ dùng" là bằng chứng yếu nhất. Toàn lời khen = phiên chưa đạt, giao việc khó hơn.
- **Ôn lại:** ngày 5, ngày 13.

<a id="b4-4"></a>
## 4.4 Tự soát → nộp CP4

- [ ] Lượt 2 + `eval/report.md` + `eval/README.md` (Hồ sơ đánh giá)
- [ ] `cost/cost-estimate.md` 3 kịch bản + chi phí / task thành công
- [ ] `spec.md` đủ §0–§9 · bảng impact có nguồn
- [ ] Slide (PDF, PPTX, HTML…) trong repo hoặc link slide ở form CP4 ([5.1](#b5-1)) · video demo dự phòng
- [ ] Tự khai phần chưa xong — khai thật không bị trừ thêm
- [ ] *(Bonus)* `validation/log.md`

Nộp CP4: [README → Checkpoint](README.md#checkpoint).

---

# Giai đoạn 5 · DEMO & NỘP *(14:30 → 23:59 Thứ Bảy 28/11 · Demo Zone 14:30–16:00 · Demo Phòng 16:00–18:00 · hạn chót 23:59)*

<a id="b5-1"></a>
## 5.1 Slide — "không có bằng chứng thì không có slide"

Mỗi trang có ≥1 con số / trích dẫn có nguồn / kết quả đo. Định dạng nào cũng được (PDF, PPTX, HTML…): để file trong repo hoặc nộp link slide ở form CP4 (ai có link cũng xem được).

| # | Trang | Có gì | Lấy từ |
|---|---|---|---|
| 1 | Người dùng & pain | Ai · việc gì · chỗ đau + số và trích dẫn | [1.2](#b1-2) |
| 2 | Vì sao chọn bài này | Bảng impact rút gọn + hướng bị loại | [1.3](#b1-3) |
| 3 | Giải pháp | Lát cắt một câu · sơ đồ · AI tự làm đến đâu, vì sao | [2.2](#b2-2) |
| 4 | Demo live | 1 trường hợp thường + 1 trường hợp khó (lỗi được xử lý tốt là điểm cộng) | [3.2](#b3-2) |
| 5 | **Đánh giá thế nào** | Dataset · bộ câu thử · metric · lượt 1 → lượt 2 so với chuẩn "đạt" · lỗi chính | [4.1](#b4-1) |
| 6 | **Chi phí khi dùng thật** | Chi phí / task thành công · 3 kịch bản · so với impact | [4.2](#b4-2) |
| 7 | Kết luận | Go / iterate / stop — dẫn số ở trang 1, 5, 6 | — |
| 8 | Nếu có thêm 1 tuần | 2–3 việc, trỏ về lỗi còn lại / phản hồi người dùng | [4.1](#b4-1), [4.3](#b4-3) |

Mẫu: `slides/outline.md` trong repo nhóm. **Ôn lại:** ngày 10, ngày 13.

<a id="b5-2"></a>
## 5.2 Checklist cuối

- [ ] Repo đủ: `TEAMS.md` (đúng format) · `README.md` · `canvas.md` · `spec.md` · `evidence/` · `data/DATA_CARD.md` · `codebase/` · `eval/` · `cost/` · `demo-slides.pdf` · `reflection/` · *(bonus)* `validation/`
- [ ] Không có API key, không có dữ liệu cá nhân thật
- [ ] Video dự phòng mở được bằng cửa sổ ẩn danh
- [ ] Cả nhóm trả lời được: *Vì sao chọn hình dạng này?* · *Lỗi nguy hiểm nhất là gì?* · *Chi phí / task thành công tính thế nào?* · *Phần bạn làm là gì?*

<a id="b5-3"></a>
## 5.3 Demo & hạn chót

- **Demo Zone 14:30–16:00:** mọi nhóm demo trong zone của mình. **Demo Phòng 16:00–18:00:** các nhóm top của mỗi zone demo trước cả phòng. Mỗi người nói ≥1 phần. Giám khảo có thể đưa **1 câu thử lạ để chạy tại chỗ**, mở trace của một câu trượt, hoặc hỏi bất kỳ ai *"câu này vì sao trượt?"*. Mạng hỏng → chiếu video dự phòng.
- **Sau CP4 đến 23:59 Thứ Bảy 28/11:** sửa theo góp ý, mọi thay đổi ghi `spec.md` §10 (giờ · đổi gì · vì sao). Chạy thêm thì ghi thành lượt mới (`eval/run-3.csv`). Không sửa những gì [README → Luật chung](README.md#luật-chung) cấm.
- **Reflection:** mỗi người 1 file `reflection/<ten-khong-dau>.md`: vai trò và phần mình làm · AI hỗ trợ thế nào · một bài học từ một câu thử trượt của chính nhóm.

---

<a id="phu-luc"></a>
# Phụ lục · Bản đồ 15 ngày → hackathon

Mọi thứ hackathon đòi, nhóm đã làm trong lab của 15 ngày giai đoạn 1. Kẹt ở đâu, mở lại đúng ngày đó.

| Hạng mục | Bước | Ôn lại | Dùng lại từ lab của mình |
|---|---|---|---|
| Bằng chứng pain | [1.2](#b1-2) | ngày 2, ngày 6 | lab ngày 2: memo go/no-go, stakeholder map · lab ngày 6: gắn nhãn, đếm |
| Impact | [1.3](#b1-3) | ngày 2, ngày 13 | lab ngày 2: metric + ngưỡng · lab ngày 13: adoption metric |
| Kiến trúc & mức tự động | [2.2](#b2-2) | ngày 3, ngày 5, ngày 8, ngày 11 | lab ngày 3: tool contract · lab ngày 5: `autonomy_policy.yaml` · lab ngày 8: bốn hình dạng |
| Chỗ khó, chặn rủi ro | [2.3](#b2-3) | ngày 9, ngày 11 | lab ngày 11: trifecta lint, approval |
| Định nghĩa "tốt", bộ câu thử | [2.4](#b2-4) | ngày 5, ngày 6, ngày 9 | lab ngày 5: eval spec · lab ngày 6: sinh data có seed + data card · lab ngày 9: metric spec, harness một lệnh |
| Bản chạy thử | [3.2](#b3-2) | ngày 3, ngày 4, ngày 7 | lab ngày 3: tool / MCP · lab ngày 4: vòng lặp có giới hạn bước, trace · lab ngày 7: trích dẫn, "không biết" |
| Nối model | [3.3](#b3-3) | ngày 1, ngày 14 | lab ngày 1: gọi model, structured output |
| Đánh giá lượt 1 → 2 | [4.1](#b4-1) | ngày 9, ngày 14 | lab ngày 9: taxonomy lỗi · lab ngày 14: benchmark gate |
| Mô phỏng chi phí | [4.2](#b4-2) | ngày 1, ngày 13, ngày 14 | lab ngày 13: unit economics, độ nhạy · lab ngày 14: replay 1.000 ticket · lab ngày 1: cost / 1.000 item |
| Người dùng thử | [4.3](#b4-3) | ngày 5, ngày 13 | lab ngày 5: audit HAX |
| Kết luận, slide | [5.1](#b5-1) | ngày 10, ngày 12, ngày 13 | lab ngày 10: PoC exit memo · lab ngày 12: `AGENTS.md` |

<a id="hoi-nhanh"></a>
# Phụ lục · Hỏi nhanh

**Sáng Thứ Sáu 27/11 đi làm, không dự Zoom được?** Xem lại bản ghi nếu có, và làm đủ việc của buổi Zoom trước 16:00 Thứ Sáu 27/11. Nhóm phải có track và Canvas nháp trước khi vào lớp.

**Đến lớp Thứ Sáu muộn hoặc không đến được?** Đội trưởng vẫn nộp CP1, CP2 qua link nộp ([README → Checkpoint](README.md#checkpoint)).

**Bạn nhóm khác trong lớp có tính là "ngoài nhóm" không?** Có, nếu họ đúng là người dùng của lát cắt.

**Phỏng vấn 3 người, ghi "67%" được không?** Không. Với n = 3, viết "2/3 người" và liệt kê từng người.

**Chỉ đào `data/preclass/` có đủ làm bằng chứng không?** Đủ mức tối thiểu nếu đếm được, có x/N, % và cách đếm kiểm lại được. Nhưng data chỉ cho biết học viên **làm gì**, không cho biết **vì sao**. Kiểm lại bằng vài cuộc phỏng vấn hoặc một khảo sát ngắn thì bằng chứng mạnh hơn hẳn và được điểm cao hơn.

**Kết quả ngược giả thuyết thì sao?** Vẫn đủ điểm nếu số là thật. Ghi lại và đổi hướng: đó là bằng chứng tốt.

**Kẹt khi nối model?** Xem mục "Lỗi hay gặp" trong [starter-repo/docs/connect-model.md](starter-repo/docs/connect-model.md). Kẹt quá 20 phút thì hỏi ngay.

**Dùng gói miễn phí mà vẫn phải tính chi phí?** Có. Mô phỏng chi phí là cho **lúc đưa vào dùng thật**, tính theo giá gói trả phí.

**Không biết git?** Tạo repo trên web GitHub rồi tải file lên. Hướng dẫn ở [starter-repo/README.md](starter-repo/README.md).

**Không dùng Python được không?** Được, nhưng nhóm phải tự đo được kết quả bộ câu thử và số token cho mô phỏng chi phí. Dùng `starter-repo` là nhanh nhất.

---

**Đọc tiếp:** [03-rubric.md](03-rubric.md) — tự soát trước mỗi mốc · Khung repo: [starter-repo/](starter-repo/README.md) · Về đầu: [README](README.md)
