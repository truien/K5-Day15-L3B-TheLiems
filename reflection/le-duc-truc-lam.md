# Reflection — [Họ tên]

> Làm ở guide bước 5.3. Mỗi người một file: chép file này thành `reflection/<ten-khong-dau>.md` (viết thường, không dấu). Hạn: **23:59 Thứ Bảy 28/11**. Mỗi câu 3–6 dòng.

1. Vai trò + phần mình làm (trỏ tới file / commit):

Mình chịu trách nhiệm việc tra soát các yêu cầu đề bài, hoàn thành phần giải về quy trình không AI của vấn đề trong phần 0 `spec.md` (commit `da13cec`), và vẽ sơ đồ workflow minh hoạ cho cách model vận hành trong `spec.md` (commit `76f273f`). Mình cũng đã nghiên cứu các giải pháp học tập AI hiện tại (cụ thể là chế độ học tập trên ChatGPT), giải thích nhưng ưu nhược điểm của công cụ và điểm khác của model nhóm với công cụ này (commit `da13cec`). Ngoài ra, mình cũng hỗ trợ đội trưởng trong việc tính toán chi phí cho model.  
2. AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):

Mình đã sử dụng Codex để hỗ trợ mình trong việc tóm tắt nhiệm vụ và gợi ý vạch ra sơ đồ workflow cho model. Mình đã thêm một vài các trường hợp mà model có thể báo Không Rõ hoặc Từ Chối vào sơ đồ sau khi trao đổi với các thành viên khác.
3. Một câu thử trượt của nhóm và mình học được gì từ nó:

Trong lượt chạy đầu tiên (`run-1.csv`), câu `B04` là câu trượt duy nhất. Trong câu này, model đã trả lời thiếu yêu cầu LAB3-0.4 trong số các yêu cầu CP1. Nguyên nhân theo mình có thể do trong input nhắc Docker, container, file môi trường, còn LAB3-0.4 chỉ nhắc đến việc "Số liệu lấy từ file chạy thật trong outputs", nghe không liên quan đến docker nên bị model bỏ qua mặc dù input nêu rõ "CP1 cần ĐỦ mục nào?".

Bài học rút ra là nên có những ràng buộc nhất định cho model thông qua system config (ví dụ như luôn phải hiện đầy đủ các yêu cầu bài) để người dùng không phải ràng buộc qua prompt, vốn có thể bị bỏ qua hoặc hiểu sai nếu có những ràng buộc khác chồng chéo.
