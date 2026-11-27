# Rubric — 100 điểm = 15 điểm nộp + 85 điểm chấm bài + 5 bonus

> [README](README.md) → [01-challenge-brief](01-challenge-brief.md) → [tracks/](tracks/README.md) → [02-guide](02-guide.md) → **[03-rubric]**

**Giám khảo và lab coach chấm theo file này. Nhóm dùng nó để tự soát trước mỗi mốc.** Cách làm từng phần nằm ở [02-guide.md](02-guide.md). Giờ và mốc nằm ở [README → Checkpoint](README.md#checkpoint).

**Nguyên tắc chấm**

1. **Mỗi tiêu chí trỏ về một file trong repo nhóm**, nên chấm và phúc khảo đều đối chiếu được.
2. **Chấm quyết định và bằng chứng**, không chấm độ hoành tráng của sản phẩm.
3. **Kết quả thấp mà trung thực vẫn được đủ điểm**, kể cả khi dưới chuẩn "đạt", kể cả khi ngược giả thuyết.
4. **Số bị sửa hoặc giấu → khối đó 0 điểm** ([Trừ điểm](#tru-diem)).

| Phần | Điểm | Chấm khi nào |
|---|---|---|
| [0 · Điều kiện cứng](#phan-0) | — | CP4, 14:30 Thứ Bảy 28/11. Thiếu thì không xét giải |
| [1 · Điểm nộp 4 checkpoint](#phan-1) | 15 | Mỗi checkpoint |
| [2 · Điểm chấm bài](#phan-2) | 85 | Trên repo nhóm + phần demo |
| [Bonus · Người dùng thử](#bonus) | +5 | Trên repo nhóm. Tổng tối đa vẫn 100 |

---

<a id="phan-0"></a>
## Phần 0 — Điều kiện cứng

Kiểm tại CP4, 14:30 Thứ Bảy 28/11. Thiếu 1 trong 4 điều kiện → **không xét giải**. Nhóm vẫn được chấm điểm lab bình thường (Phần 1 + Phần 2).

| # | Điều kiện | Kiểm thế nào |
|---|---|---|
| 1 | **Bản chạy thử gọi AI thật** ở quyết định trung tâm của lát cắt | Chạy theo README repo nhóm hoặc demo trực tiếp. Bản trả câu giả cố định không tính. Mạng hỏng lúc demo thì video dự phòng (thao tác thật, AI trả kết quả thật) được tính thay |
| 2 | **Bằng chứng pain ≥1 nguồn đạt ngưỡng** | Ngưỡng ở [R1](#r1) · `evidence/` |
| 3 | **Bộ câu thử ≥20 câu + kết quả có % đạt** | `eval/benchmark.csv` · `eval/run-N.csv` đã chấm · `eval/report.md` |
| 4 | **Slide** | Định dạng nào cũng được (PDF, PPTX, HTML…): file trong repo hoặc link slide nộp ở form CP4, có tại CP4 |

---

<a id="phan-1"></a>
## Phần 1 — 15 điểm nộp: 4 checkpoint

| CP1 · 17:00 Thứ Sáu 27/11 | CP2 · 19:30 Thứ Sáu 27/11 | CP3 · 10:00 Thứ Bảy 28/11 | CP4 · 14:30 Thứ Bảy 28/11 |
|:---:|:---:|:---:|:---:|
| 3 | 4 | 4 | 4 |

- **Đúng hạn và đủ phần → đủ điểm mốc. Muộn hoặc thiếu → 0 điểm mốc đó.**
- **"Đủ phần"** là đủ những gì [README → Checkpoint](README.md#checkpoint) liệt kê cho mốc đó. Lab coach kiểm theo danh sách tự soát trong guide: [1.4](02-guide.md#b1-4) · [2.5](02-guide.md#b2-5) · [3.4](02-guide.md#b3-4) · [4.4](02-guide.md#b4-4) (ô bonus không tính).
- **Hạn chót 23:59 Thứ Bảy 28/11:** không có điểm nộp. Kiểm theo [guide 5.3](02-guide.md#b5-3): changelog cho mọi thay đổi sau 14:30 · reflection đủ người · không sửa những gì [README → Luật chung](README.md#luật-chung) cấm.
- **Bản dùng để chấm:**
  - Điểm lab (Phần 2) chấm trên **commit cuối trước 23:59 Thứ Bảy 28/11**.
  - Giải xét trên **bản CP4 + phần demo**.

---

<a id="phan-2"></a>
## Phần 2 — 85 điểm chấm bài

| Khối | Điểm | Chấm trên file nào | Làm theo |
|---|---|---|---|
| [R1 · Bằng chứng pain](#r1) | **14** | `evidence/` · `spec.md` §1 | [1.2](02-guide.md#b1-2) |
| [R2 · Impact có số](#r2) | **11** | `spec.md` §1–§2 | [1.3](02-guide.md#b1-3) |
| [R3 · Giải pháp AI: thiết kế + bản chạy thử](#r3) | **16** | `spec.md` §4 · `codebase/` · README repo nhóm | [2.2](02-guide.md#b2-2), [3.2](02-guide.md#b3-2) |
| [R4 · Định nghĩa "tốt": bộ câu thử + metric](#r4) | **14** | `eval/benchmark.csv` · `eval/metric_spec.yaml` · `spec.md` §7 · `data/DATA_CARD.md` | [2.3](02-guide.md#b2-3), [2.4](02-guide.md#b2-4) |
| [R5 · Báo cáo đánh giá](#r5) | **8** | `eval/report.md` · `eval/README.md` | [4.1](02-guide.md#b4-1) |
| [R6 · Mô phỏng chi phí khi dùng thật](#r6) | **12** | `cost/personas.yaml` · `cost/simulate-N.csv` · `cost/cost-estimate.md` | [4.2](02-guide.md#b4-2) |
| [R7 · Slide & demo](#r7) | **10** | slide (file trong repo hoặc link ở form CP4) · demo | [5.1](02-guide.md#b5-1), [5.3](02-guide.md#b5-3) |
| **Tổng** | **85** | | |
| [*Bonus* · Người dùng thử](#bonus) | +5 | `validation/log.md` | [4.3](02-guide.md#b4-3) |

<a id="r1"></a>
### R1 · Bằng chứng pain — 14

| Tiêu chí | Điểm |
|---|---|
| **Đạt ngưỡng ≥1 nguồn, cách làm kiểm lại được, ra số.** *Đào data:* x/N và %, cách chọn mẫu và cách đếm ghi trước, script / công thức có trong repo. *Phỏng vấn:* ≥3 người ngoài nhóm, đúng người dùng, hỏi chuyện đã xảy ra trong 1 tháng qua, mỗi người 1 file ghi chép, ghi "x/n người" (n nhỏ không ghi %). *Khảo sát:* ≥20 người ngoài nhóm, đúng người dùng, hỏi hành vi đã xảy ra, giữ log từng câu trả lời | 8 |
| **≥5 trích dẫn hoặc ví dụ nguyên văn**, có nguồn, bỏ tên | 3 |
| **Có nguồn thứ hai kiểm lại nguồn thứ nhất** (ví dụ đào data rồi phỏng vấn / khảo sát), khớp nhau, hoặc chỗ lệch được giải thích | 3 |

- Không đạt ngưỡng nguồn nào → **R1 tối đa 5** và không xét giải ([Phần 0](#phan-0)).
- **Không tính là bằng chứng:** người trong nhóm · dữ liệu giả lập (do BTC hoặc nhóm tự viết) · trò chuyện với nhân vật AI.

<a id="r2"></a>
### R2 · Impact có số — 11

| Tiêu chí | Điểm |
|---|---|
| **Pain cụ thể và bảng ≥3 hướng:** ai, ở đâu, vướng gì, hậu quả gì (không có chữ AI) · số trong bảng lấy từ bằng chứng ở R1 · hướng bị loại giữ lại, có lý do | 5 |
| **Công thức impact / tháng** của hướng chọn ra một con số (số người × lần / tháng × tốn bao nhiêu mỗi lần) · mỗi thừa số trỏ về nguồn, hoặc ghi rõ *(tự ước tính)* | 6 |

<a id="r3"></a>
### R3 · Giải pháp AI: thiết kế + bản chạy thử — 16

| Tiêu chí | Điểm |
|---|---|
| **Thiết kế giải pháp AI** (`spec.md` §4): lát cắt một câu + ≥3 điều không làm · sơ đồ có hình dạng (workflow cố định / 1 agent / nhiều agent) + lý do, nói được vì sao không chọn cái phức tạp hơn · AI quyết định dựa trên dữ liệu và công cụ nào (mỗi công cụ: tên · input · output · có tác động ra ngoài không) · mức tự động, chỗ người duyệt, chỗ chặn rủi ro lớn nhất · ≥3 nguyên tắc thiết kế (bắt buộc G10), mỗi cái chỉ vào một chỗ cụ thể | 8 |
| **Bản chạy thử làm trọn lát cắt:** gọi AI thật ở quyết định trung tâm · code khớp sơ đồ · câu ngoài dữ liệu thì trả lời "không có" · chỗ chặn rủi ro đã cài · README repo nhóm có lệnh chạy, người ngoài chạy được · phần còn giả ghi rõ, không giả làm thật | 8 |

- Số công cụ, kiểu công cụ **không có điểm riêng**. Chấm ở chỗ khớp với thiết kế và với bài toán.
- Chọn nhiều agent: lý do phải nói vì sao **từng vai** cần có và khác nhau ở đâu.
- Hai câu thử tấn công nhắm vào chỗ chặn rủi ro: chấm ở [R4](#r4).

<a id="r4"></a>
### R4 · Định nghĩa "tốt": bộ câu thử + metric — 14

| Tiêu chí | Điểm |
|---|---|
| **Bộ câu thử 20–30 câu** đủ cột `id, input, expected, pass_criterion, type, source` · `pass_criterion` kiểm được (không phải "trả lời hay") · ≥5 `kho` · ≥2 `tu_choi` gồm 2 câu tấn công · **≥1/3 câu có `source` từ lời người dùng hoặc data thật** | 6 |
| **Metric và chuẩn "đạt":** `eval/metric_spec.yaml` ≥3 metric (định nghĩa kiểm chứng được · cách chấm · ngưỡng) · người thứ hai chấm thử 5 output khớp ≥4/5, ghi trong `eval/README.md` · chuẩn "đạt" bằng số trong `spec.md` §7, commit trước 19:30 Thứ Sáu 27/11, không sửa sau | 5 |
| **Data card + chạy một lệnh:** `data/DATA_CARD.md` (dataset nào, từ đâu, xử lý gì, bao nhiêu dòng, data giả lập ghi cách sinh + seed) · `python run.py eval` ra `eval/run-N.csv` có run ID, model, token từng câu | 3 |

- **Track A, hướng lớp học kiểu mới:** chuẩn "đạt" phải có **≥1 chỉ số về học** (trả lời đúng sau khi học, giải thích lại được, thời gian tới lời giải). Thiếu thì trừ 2 điểm ở tiêu chí thứ hai.

<a id="r5"></a>
### R5 · Báo cáo đánh giá — 8

| Tiêu chí | Điểm |
|---|---|
| **Lượt 1 và lỗi:** kết quả từng câu + % đạt so với chuẩn "đạt" · ≥3 lỗi, mỗi lỗi có input · output · vì sao sai, gom thành nhóm có tên | 4 |
| **Cải tiến và lượt 2:** một lần cải tiến nhắm nhóm lỗi đau nhất với người dùng + lượt 2 trên cùng bộ câu thử, báo % lượt 1 → lượt 2 · `eval/README.md` là hồ sơ đánh giá một trang (dataset → bộ câu thử → metric → bảng các lượt chạy → lỗi chính) | 4 |

- Lượt 2 thấp hơn lượt 1 vẫn đủ điểm nếu ghi thật. Không bắt phân tích lỗi từ trace.
- R5 chấm lượt 1 → lượt 2. Lượt chạy sau CP4 chỉ ghi nhận trong changelog, không dùng để chấm R5.

<a id="r6"></a>
### R6 · Mô phỏng chi phí khi dùng thật — 12

| Tiêu chí | Điểm |
|---|---|
| **Persona và mô phỏng:** ≥3 kiểu người dùng trong `cost/personas.yaml`, số lần dùng / tháng có nguồn hoặc ghi rõ *(tự ước tính)* · `python run.py simulate` ≥50 phiên, seed cố định, chạy thật qua bản chạy thử, token đọc từ log | 6 |
| **Chi phí khi dùng thật:** chi phí / task thành công dùng tỉ lệ đạt thật của lượt 2 (cùng model) · 3 kịch bản thấp · cơ sở · cao · ≥2 mức model, giá có link + ngày xem · một dòng so chi phí / người / tháng với impact / người / tháng | 6 |

- Lúc build dùng gói miễn phí vẫn phải tính theo giá gói trả phí: mô phỏng là cho lúc dùng thật.
- **Phần "muốn sâu hơn"** ở guide [4.1](02-guide.md#b4-1) và [4.2](02-guide.md#b4-2) (phần giữ riêng, LLM chấm có hiệu chuẩn, chạy ≥3 lần mỗi câu, bảng độ nhạy, chi phí ngoài model): không có điểm riêng. Giám khảo dùng để phân hạng khi hai nhóm sát điểm.

<a id="r7"></a>
### R7 · Slide & demo — 10

| Tiêu chí | Điểm |
|---|---|
| **Slide** (PDF, PPTX, HTML… hoặc link) theo khung 8 trang ở [guide 5.1](02-guide.md#b5-1): kể rõ câu chuyện Pain → Impact → Giải pháp AI → Đánh giá → Chi phí, mỗi trang có ≥1 con số / trích dẫn có nguồn / kết quả đo | 4 |
| **Demo trực tiếp:** 1 trường hợp thường + 1 trường hợp khó · chạy được câu thử lạ giám khảo đưa tại chỗ · mạng hỏng thì chiếu video dự phòng | 3 |
| **Ai được hỏi cũng trả lời được:** vì sao chọn hình dạng này · lỗi nguy hiểm nhất là gì · chi phí / task thành công tính thế nào · phần mình làm là gì | 3 |

<a id="bonus"></a>
### Bonus · Người dùng thử — +5 *(không bắt buộc, tổng tối đa vẫn 100)*

| Tiêu chí | Điểm |
|---|---|
| `validation/log.md`: ≥2 người ngoài nhóm đã dùng thử theo 5 nhịp ở [guide 4.3](02-guide.md#b4-3), mỗi người đủ cột (vai · việc giao · quan sát · trích nguyên văn · mức nghiêm trọng) · rút ra ≥1 thay đổi (ghi changelog `spec.md` §10), hoặc giữ nguyên có lý do | 5 |

Người dùng thử là sau khi build, **không thay được** bằng chứng pain ở R1.

---

<a id="tru-diem"></a>
## Trừ điểm

- Repo có **API key** hoặc **dữ liệu cá nhân thật** → **−10**, gỡ ngay. Thông tin thành viên trong `TEAMS.md` là bắt buộc, không tính vào lỗi này.
- **Số bị sửa hoặc giấu** → khối liên quan **0 điểm**. Ví dụ:
  - đổi chuẩn "đạt" sau CP2
  - bỏ câu thử trượt khỏi bộ
  - sửa `expected` cho khớp output
  - sửa kết quả của lượt đã chạy
  - số trong slide không truy được về file
- Thành viên không giải thích được phần có tên mình → phần đó **0 điểm** ([README → Luật chung](README.md#luật-chung) mục 1).

## Reflection cá nhân

Mỗi người 1 file `reflection/<ten-khong-dau>.md`, nội dung theo [guide 5.3](02-guide.md#b5-3). Reflection không có điểm riêng, dùng để đối chiếu phần việc của từng người. Thiếu reflection, hoặc bị hỏi lúc demo mà không giải thích được phần có tên mình → phần đó 0 điểm.

## Thể thức và giải

Rubric này cho **điểm lab**. Giải chỉ xét nhóm qua [Phần 0](#phan-0). Thể thức và giải: công bố sau.

---

**Đọc tiếp:** quay lại [02-guide.md](02-guide.md) để làm tiếp bước đang dở · Về đầu: [README](README.md)
