### Giao diện của chương trình quản lý bóng đá Worldcup 2022
1. Tổng quan
    Chương trình quản lý bóng đá Worldcup 2022 giúp người dùng có thể lựa chọn những gợi ý câu hỏi và nhận được câu trả lời từ những dữ liệu đã được xử lý trong database.
    Giúp người dùng hiểu và nắm thông tin trước khi 1 trận đấu bắt đầu, ví dụ như:
    Note: Dữ liệu sử dụng cho bảng G, các bảng khác hoặc khu vực khác sẽ cập nhật sau
    *** Trước trận đấu ***
    > Tổng quan
        - Bảng thi đấu vào vòng loại Worldcup 2022 (A -> H)
        - Kết quả
        - Lượt thi đấu thứ x
            - Trận giữa 2 đội tuyển nào, thuộc bảng nào
            - Ngày, giờ bắt đầu trận đấu
            - Địa điểm sân thi đấu
            - Truyền hình trực tiếp ở kênh nào

    > Đội bóng
        - Đội hình thi đấu, huấn luận viên
        - Số trận thắng, thua, hòa, bàn thắng, bàn thua, hiệu số, điểm
        - Cơ hội vào vòng trong sau khi thi đấu x trận (Đưa ra thông số chứng minh)

    > Cầu thủ
        - Thông số cầu thủ (Tên(*), tuổi, số áo (*), vị trí, số thẻ bị phạt, số bàn thắng)


    *** Sau trận đấu ***
    > Đội bóng
        - Tỉ lệ thắng thua
                + Dựa vào điểm số đội bóng đã đạt được trước khi trận đấu bắt đầu (*)
                + Tỉ lệ cầm bóng (ball possesion)
                + Số lần dứt điểm trúng đích (Shot on target)
                + Tỉ lệ chuyền banh chính xác (Pass arcuracy))
                + Số lần phạt góc
                + Số lần ngăn cản
        - Số trận thắng, thua, hòa, bàn thắng, bàn thua, hiệu số, điểm
    > Cầu thủ
        - Số thẻ bị phạt
        - Số bàn thắng
