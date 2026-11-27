  // Tạo Google Form khảo sát. Dán vào https://script.google.com rồi bấm Run (hàm taoForm).
  // Câu hỏi phải khớp questions.md.
  function taoForm() {
    var form = FormApp.create('Khảo sát 2 phút: những lúc mất thời gian khi làm lab');
    form.setDescription(
      'Gần như chỉ cần tích, khoảng 2 phút. Không hỏi tên, email, mã học viên. ' +
      'Câu trả lời được dùng ẩn danh cho bài hackathon của một nhóm AI20K (kho bài công khai). ' +
      'Hãy trả lời theo chuyện đã xảy ra với chính bạn. Thành viên nhóm TheLiems không điền.'
    );
    form.setCollectEmail(false);
  
    function chonMot(tieuDe, luaChon, coKhac) {
      var item = form.addMultipleChoiceItem();
      item.setTitle(tieuDe).setChoiceValues(luaChon).setRequired(true);
      if (coKhac) item.showOtherOption(true);
    }
  
    function chonNhieu(tieuDe, luaChon) {
      var item = form.addCheckboxItem();
      item.setTitle(tieuDe).setChoiceValues(luaChon).setRequired(true);
      item.showOtherOption(true);
    }
  
    var danhSachA = [
      'Lỗi cài đặt, cấu hình máy',
      'Lỗi Docker hoặc deploy',
      'Chưa hiểu kiến thức, khái niệm',
      'Không chắc đề yêu cầu gì ở bước đang làm',
      'Sót một yêu cầu của đề, sau mới biết',
      'Không chắc kết quả đã đạt yêu cầu chưa',
      'Không gặp chuyện nào'
    ];
  
    chonMot('1. Bạn là', [
      'Học viên L3 AI20K khoá 5',
      'Học viên khoá hoặc lớp khác',
      'Lab coach / TA / giảng viên'
    ], true);
  
    chonMot('2. Lần gần nhất bạn làm một bài lab chia nhiều bước (checkpoint) là khi nào?', [
      'Trong 7 ngày qua',
      '8–30 ngày trước',
      'Hơn 1 tháng trước',
      'Chưa từng'
    ]);
  
    chonNhieu('3. Trong 1 tháng qua khi làm lab, bạn đã gặp chuyện nào?', danhSachA);
  
    chonMot('4. Trong các chuyện đó, chuyện nào làm bạn mất nhiều thời gian nhất?', danhSachA, true);
  
    chonMot('5. Lần gần nhất gặp chuyện ở câu 4, bạn mất khoảng bao lâu?', [
      'Dưới 15 phút',
      '15 đến dưới 30 phút',
      '30 đến dưới 60 phút',
      'Từ 60 phút trở lên',
      'Không gặp'
    ]);
  
    chonMot('6. Trong 1 tháng qua, mấy lần bạn phải sửa, chạy lại hoặc nộp lại vì sót hay hiểu nhầm yêu cầu?', [
      '0 lần',
      '1 lần',
      '2–3 lần',
      'Từ 4 lần'
    ]);
  
    chonMot('7. Lần gần nhất sót hoặc không chắc một yêu cầu, yêu cầu đó nằm ở đâu?', [
      'Ngay mục của bước đang làm',
      'Mục khác trong đề (quy định chung, nộp bài…)',
      'File khác',
      'Ngoài đề (Discord, lời giảng)',
      'Không nhớ',
      'Chưa gặp'
    ]);
  
    chonNhieu('8. Lần gần nhất gặp chuyện ở câu 4, bạn đã làm gì?', [
      'Đọc lại đề',
      'Hỏi ChatGPT hoặc AI khác',
      'Hỏi bạn',
      'Hỏi lab coach / TA',
      'Chạy test hoặc script chấm',
      'Đọc log, tài liệu',
      'Bỏ qua',
      'Không gặp'
    ]);
  
    chonMot('9. Lần đó kết thúc thế nào?', [
      'Xong đúng hạn',
      'Xong nhưng trễ',
      'Nộp thiếu',
      'Bỏ phần đó',
      'Không gặp'
    ]);
  
    form.addParagraphTextItem()
      .setTitle('10. (Không bắt buộc) Kể 1 câu về lần đó')
      .setHelpText('Đừng ghi tên người hay tên nhóm. Câu này có thể được trích, không kèm tên.')
      .setRequired(false);
  
    // Form nhận quà tách riêng, để email không bao giờ nằm chung với câu trả lời khảo sát.
    var qua = FormApp.create('Nhận quà: bốc thăm 1 slot ge');
    qua.setDescription(
      'Không bắt buộc. Để lại email nếu muốn tham gia bốc thăm ngẫu nhiên 1 slot ge. ' +
      'Email không gắn với câu trả lời khảo sát, chỉ dùng để liên hệ người trúng, xoá sau khi trao.'
    );
    qua.setCollectEmail(false);
    qua.addTextItem()
      .setTitle('Email của bạn')
      .setValidation(FormApp.createTextValidation().requireTextIsEmail().build())
      .setRequired(true);
  
    form.setConfirmationMessage(
      'Cảm ơn bạn! Muốn bốc thăm 1 slot ge thì để email ở đây (không bắt buộc): ' + qua.getPublishedUrl()
    );
  
    Logger.log('Link sửa form khảo sát: ' + form.getEditUrl());
    Logger.log('Link gửi người trả lời: ' + form.getPublishedUrl());
    Logger.log('Link sửa form nhận quà: ' + qua.getEditUrl());
  }
