# Đề bài — sản phẩm AI cho người dùng thật: 6 track, một khung chung

> [README](README.md) → **[01-challenge-brief]** → [tracks/](tracks/README.md) → [02-guide](02-guide.md) → [03-rubric](03-rubric.md)

**Bối cảnh.** AI đã đi vào những việc rất đời thường: học trên một nền tảng online, đặt lịch khám, mua thuốc, đặt vé, mua sắm, gọi đồ ăn, chuyển tiền. Ở mỗi chỗ đều có việc lặp lại, chỗ nghẽn, chỗ sai thì đắt. Hackathon có 6 track:
- **Track A · EdTech** lấy bối cảnh chính khoá AI20K khoá 5 (hơn 1.000 học viên L23 và L34): học trên LMS và trang pre-class, hỏi đáp trên Discord, sản xuất bài giảng bằng AI, xếp lịch và chia việc cho giảng viên, lab coach. BTC cấp data cho track này.
- **Track B–E** lấy bối cảnh 4 lĩnh vực ngoài khoá học: y tế, du lịch, thương mại điện tử, tài chính. Nhóm tự tìm data.
- **Track F · Làn khác:** lĩnh vực bất kỳ, miễn có insight từ người dùng thật.

**Nhóm là một product team làm AI.** Nhóm phải làm đủ ba việc:
1. Chọn một track và tìm một pain có bằng chứng.
2. Thiết kế giải pháp AI cho **một lát cắt**, cả về sản phẩm (ai dùng, dùng lúc nào, kết quả là gì) lẫn công nghệ (AI quyết định gì, dựa trên dữ liệu và công cụ nào, workflow hay agent, chặn rủi ro thế nào).
3. Chứng minh bằng số: giải pháp **đúng được bao nhiêu** trên bộ câu thử, và **tốn bao nhiêu mỗi tháng** khi đưa vào dùng thật.

---

## Chọn 1 track, rồi tìm bài toán của nhóm trong track

| Track | Bối cảnh | Định hướng ý tưởng | File |
|---|---|---|---|
| **A** · EdTech | Việc học và dạy ở chính khoá AI20K: LMS và trang pre-class có trợ giảng AI, Discord rất đông, bài giảng online làm bằng AI, lớp học AI trên pre-class, lịch học và phòng chốt sát ngày | Tutor có căn cứ · trợ lý Discord · kiểm và duyệt bài giảng AI · lớp học kiểu mới · vận hành đào tạo · khách hàng ảo tập phỏng vấn, giám khảo ảo, hỗ trợ lab… | [track-a](tracks/track-a-edtech.md) |
| **B** · Y tế | Người bệnh không biết đi khoa nào; người uống nhiều thuốc không ai kiểm tra tương tác; nhà thuốc trả lời chat lúc tối muộn | Gợi ý chuyên khoa trước khi đặt khám · kiểm tra tương tác thuốc · tư vấn ở nhà thuốc qua chat, biết lúc nào chuyển dược sĩ | [track-b](tracks/track-b-healthcare.md) |
| **C** · Du lịch | Lịch trình nhiều điểm, giờ mở cửa khác nhau; lễ tân tra tay yêu cầu đổi phòng; chuyến bay bị huỷ sát giờ | Xếp lịch trình một ngày · đề xuất đổi / nâng hạng phòng để lễ tân duyệt · hỗ trợ khách khi chuyến bay bị huỷ | [track-c](tracks/track-c-travel.md) |
| **D** · Thương mại điện tử | Đơn giao đồ ăn thiếu món, sai món, trễ; đặt đơn nhóm có người ăn chay, dị ứng; trả hàng trên sàn phải công bằng cho cả hai bên | Xử lý khiếu nại trong hạn mức · đặt đơn nhóm có ràng buộc · trả hàng / hoàn tiền trung lập | [track-d](tracks/track-d-ecommerce.md) |
| **E** · Tài chính | Sao kê khó đọc; chỉ biết vượt ngân sách khi đã hết tiền; giao dịch nghi lừa đảo bị tạm chặn | Giải thích chi tiêu · cảnh báo sắp vượt ngân sách · hỗ trợ khi giao dịch bị chặn | [track-e](tracks/track-e-finance.md) |
| **F** · Làn khác | Lĩnh vực bất kỳ mà A–E chưa chạm tới | Bất kỳ, miễn có **insight từ người dùng thật** và gặp được người dùng trong hai ngày | [track-f](tracks/track-f-other-lane.md) |

- **Định hướng ý tưởng chỉ là điểm xuất phát, không phải danh sách đóng.** Nhóm được đi theo hướng khác, miễn là vẫn nằm trong bối cảnh của track và có pain có bằng chứng. Bài toán không thuộc track nào trong A–E thì chọn track F.
- Dù đi theo hướng gợi ý hay hướng riêng, nhóm vẫn **tự cắt lát cắt của mình** từ pain đã chứng minh.
- Mỗi file track viết theo cùng một khung để dễ so sánh: bối cảnh · người dùng · data · định hướng ý tưởng · công cụ gợi ý · persona chi phí · bẫy · an toàn. Cách chọn track trong 20 phút: [tracks/README.md](tracks/README.md).
- **Mọi track chấm chung một rubric** ([03-rubric.md](03-rubric.md)). Đi theo hướng riêng không bị chấm khác.

<a id="data"></a>
## Data

- **Track A (EdTech): BTC cấp data** trong `data/` để đào bằng chứng và hình dung bối cảnh:
  - [data/preclass/](data/preclass/README.md): nhật ký hành vi thật của khoá trên trang pre-class, từ 05/11 đến 25/11/2026. Đã ẩn danh, mọi mã đã thay mới.
  - [data/training-ops/](data/training-ops/README.md): bộ **giả lập** dựng lại cách khoá vận hành lịch học, xếp phòng, phân công giảng viên và lab coach. Dùng để hình dung và chạy thử, **không phải bằng chứng pain**.
- **Track B–F: BTC không cấp data. Nhóm tự tìm.**
  - Để đào bằng chứng: **review công khai** (Google Play, App Store, Google Maps…), bài hỏi đáp công khai, số liệu công khai có nguồn. Cách lấy và đếm review: [guide bước 1.2](02-guide.md#b1-2).
  - Để chạy thử: trang chính sách / FAQ công khai của sản phẩm, hoặc tự dựng dữ liệu giả có seed.
- **Data để chạy thử** (bài mẫu có mã đoạn, thông báo mẫu, danh sách thuốc, đơn hàng, giao dịch…) **nhóm tự dựng** ở mọi track. Ghi nguồn và cách dựng trong `data/DATA_CARD.md` ([guide 2.4](02-guide.md#b2-4)). Data tự dựng **không phải bằng chứng pain**.
- **Người dùng thật:** ở track A, cả lớp là người dùng. Ở track D, E, học viên cũng là người mua online, người dùng ví. Track B, C, F: xem mục "Gặp người dùng ở đâu" trong file track.

**Luật dùng dữ liệu**
1. **Người được phỏng vấn / khảo sát:** ghi P1, P2… kèm vai, không ghi họ tên, số điện thoại, email, mã học viên. Không ghi âm khi chưa được đồng ý.
2. **data/preclass/:** không cố đoán ai là ai, không xếp hạng học viên. Repo nhóm chỉ chứa số đã tổng hợp và vài dòng ví dụ, không chép lại nguyên file.
3. **Discord và bài công khai:** người trong đó là bạn cùng khoá. Trích tối đa 2 câu, bỏ tên, không đoán "tin này của ai".
4. **Tài liệu khoá** (slide, transcript, đề lab): repo nhóm là công khai, nên **không commit nguyên tài liệu**, chỉ trích đoạn ngắn.
5. **Review công khai:** không chép tên người viết review, trích tối đa 2 câu mỗi review, ghi link và ngày xem.
6. **Không dùng dữ liệu thật của người thật** ở mọi track: bệnh án, đơn thuốc, sao kê, giao dịch, đơn hàng, tin nhắn của ai đó. Cần thì tự dựng dữ liệu giả.
7. **Công cụ AI gói miễn phí** có thể dùng dữ liệu gửi lên để huấn luyện.
   - Data trong `data/` của bộ đề **được đưa vào thoải mái**: đã ẩn danh hoặc là giả lập.
   - Dữ liệu người thật nhóm tự thu (phỏng vấn, khảo sát, Discord) chỉ đưa bản đã bỏ tên hoặc đoạn đã viết lại.

## Lát cắt = MỘT CÂU

> **một người dùng · một công việc · một quyết định AI · một kết quả**

Ví dụ để hình dung độ lớn: *Một học viên · dán lỗi khi làm lab · AI quyết định gợi ý bước tiếp theo mà không đưa lời giải · học viên tự sửa được.*

- Lát cắt **phải đi ra từ pain đã chứng minh**, không đi ra từ ý tưởng ban đầu.
- Demo được trong 2 phút, làm trọn trong khoảng 10 giờ. Bối cảnh càng lớn thì lát cắt càng phải nhỏ.
- Viết ở Canvas dòng 5 ([guide 1.4](02-guide.md#b1-4)) và `spec.md` §4.

## Ràng buộc chung

1. **Phạm vi theo track.** Track A: việc học và dạy ở chính khoá AI20K. Track B–E: đúng lĩnh vực của track. Track F: lĩnh vực bất kỳ, có insight từ người dùng thật. Ở mọi track, người dùng phải là người nhóm **gặp được trong hai ngày**.
2. **Bản chạy thử chạy riêng, không sửa và không kết nối vào hệ thống thật** (trang pre-class, LMS, Discord của khoá, hay app của bất kỳ hãng nào).
   - Đó là bản mô phỏng tính năng (dòng lệnh, web nhỏ, bot thử, notebook) trên dữ liệu giả lập, tự viết hoặc đã ẩn danh. Không bắt buộc đưa lên mạng.
   - Bắt buộc: gọi AI thật ở quyết định trung tâm, và quyết định dựa trên dữ liệu / công cụ của bài toán ([guide 3.2](02-guide.md#b3-2)).
3. **Tự xác định 4 lớp chỗ khó** cho lát cắt, rồi biến thành câu thử ([guide 2.3](02-guide.md#b2-3)): nguồn sự thật · mơ hồ, thiếu thông tin · ngoài phạm vi, thẩm quyền · đặc thù lĩnh vực (sai thì ai mất gì).
4. **Mô tả hệ thống đang có phải có nguồn** (ảnh chụp tài khoản của mình đã che thông tin, trang chính thức). Không kiểm được thì ghi "chưa kiểm".

<a id="7-hang-muc"></a>
## Bài của nhóm là một câu chuyện — 7 hạng mục bắt buộc

**Pain → Impact → Giải pháp AI**, chống lưng bằng **Đánh giá** và **Mô phỏng chi phí**. Thiếu một mắt xích thì câu chuyện không đứng được.

| # | Hạng mục | Trả lời câu hỏi | Mức tối thiểu | Làm ở | Nằm ở file |
|---|---|---|---|---|---|
| 1 | **Bằng chứng pain** | Ai đau, đau thế nào, bao nhiêu người? | ≥1 nguồn đạt ngưỡng: **đào data** (x/N và %, cách đếm kiểm lại được) · **phỏng vấn** ≥3 người · **khảo sát** ≥20 người (ngoài nhóm, đúng người dùng) · ≥5 trích dẫn / ví dụ nguyên văn. Mạnh nhất: đào data rồi kiểm lại bằng phỏng vấn hoặc khảo sát | [1.2](02-guide.md#b1-2) | `evidence/` |
| 2 | **Impact có số** | Mỗi tháng mất bao nhiêu, vì sao chọn bài này? | Số người × số lần / tháng × tốn bao nhiêu mỗi lần, mỗi số có nguồn | [1.3](02-guide.md#b1-3) | `spec.md` |
| 3 | **Thiết kế giải pháp AI** | AI quyết định gì, dựa trên dữ liệu và công cụ nào, chặn rủi ro ở đâu, người duyệt ở đâu? | 1 sơ đồ: hình dạng (workflow / 1 agent / nhiều agent) + lý do · dữ liệu và công cụ AI dùng · chỗ chặn rủi ro · chỗ người duyệt | [2.2](02-guide.md#b2-2) | `spec.md` |
| 4 | **Bản chạy thử làm trọn lát cắt** | Người dùng đưa gì vào, AI quyết định gì, ra cái gì dùng được? | Gọi AI thật · quyết định dựa trên dữ liệu / công cụ của bài toán · chạy được bằng `run.py eval` và `run.py simulate` | [3.2](02-guide.md#b3-2) | `codebase/` |
| 5 | **Định nghĩa "tốt" + bộ câu thử** | Thế nào là đủ tốt với người dùng, và giải pháp đúng được bao nhiêu? | Data card · 20–30 câu thử · metric spec ≥3 metric · chuẩn "đạt" chốt ở CP2 · lượt 1 → lượt 2 | [2.4](02-guide.md#b2-4), [4.1](02-guide.md#b4-1) | `data/`, `eval/` |
| 6 | **Mô phỏng chi phí khi dùng thật** | Dùng thật ở quy mô thật của sản phẩm thì tốn bao nhiêu mỗi tháng, có đáng so với impact? | ≥50 phiên giả lập chạy qua bản chạy thử → chi phí / task thành công → 3 kịch bản ở quy mô thật | [4.2](02-guide.md#b4-2) | `cost/` |
| 7 | **Slide + demo + video dự phòng** | Kết luận go / iterate / stop dựa trên số nào? | Slide (PDF, PPTX, HTML… hoặc link) có trang "Đánh giá thế nào" và "Chi phí khi dùng thật" | [5.1](02-guide.md#b5-1) | thư mục gốc repo |
| + | *Bonus:* người dùng thử | Người dùng thật dùng được không, đổi gì sau khi thử? | 2–3 người ngoài nhóm dùng thử, có log | [4.3](02-guide.md#b4-3) | `validation/` |

**Thiếu hạng mục 1, 4, 5 (bộ câu thử + % đạt) hoặc slide → không xét giải** (vẫn được chấm điểm lab). Cách chấm: [03-rubric.md](03-rubric.md).

## 5 câu tự kiểm bài toán — trước CP1 (17:00 Thứ Sáu 27/11) và trước khi chốt lát cắt ở CP2 (19:30)

| # | Tiêu chí | Đạt khi |
|---|---|---|
| 1 | Pain cụ thể | Ai, đang làm gì, vướng ở đâu, hậu quả gì. "Mọi người thấy bất tiện" là chưa đạt |
| 2 | Có đường ra bằng chứng | Biết sẽ lấy bằng chứng từ nguồn nào (đào data · phỏng vấn ≥3 · khảo sát ≥20) và gặp được người dùng trong hai ngày. Ngưỡng: [guide 1.2](02-guide.md#b1-2) |
| 3 | Mô tả vấn đề không có chữ AI | Bỏ AI đi, việc đó vẫn tồn tại. Có ≥3 hướng để so trong bảng impact |
| 4 | Lát cắt đủ nhỏ | Đúng một câu theo mẫu trên, demo được trong 2 phút |
| 5 | Đo được và tính được tiền | Viết được "thế nào là tốt" thành câu thử có đáp án kiểm được, và biết người dùng dùng bao nhiêu lần / tháng để mô phỏng chi phí |

---

**Đọc tiếp:** chọn track ở [tracks/README.md](tracks/README.md) → đọc kỹ file track của nhóm → làm theo [02-guide.md bước 1.0](02-guide.md#b1-0).
