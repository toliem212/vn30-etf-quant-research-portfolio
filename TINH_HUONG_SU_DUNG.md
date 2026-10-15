# Khi tín hiệu bán không đồng nghĩa với bán được

**Một tình huống từ sổ mô phỏng ETF VN30: chiến lược B4, ngày 01/10/2026**

Một mô hình đầu tư có thể xác định rất rõ tỷ trọng ETF cần nắm giữ. Nhưng danh mục còn phải đối mặt với khối lượng khớp lệnh, lô giao dịch, tiền chờ thanh toán và biến động giá. Trường hợp dưới đây cho thấy khoảng cách giữa **quyết định theo tín hiệu** và **kết quả thực hiện trong mô phỏng**.

## Tín hiệu dẫn đến quyết định gì?

B4 sử dụng trạng thái VN30 so với SMA200 để điều chỉnh tỷ trọng ETF mục tiêu giữa 30% và 90%. Tại phiên **01/10/2026**, tỷ trọng mục tiêu được xác định là **30%**. Sổ mô phỏng ghi nhận một lệnh bán ETF để đưa danh mục về gần mức này.

| Nội dung | Sổ mô phỏng ghi nhận |
|:--|--:|
| Tỷ trọng ETF mục tiêu | 30% |
| Khối lượng đề nghị bán | **37.700 CCQ** |
| Khối lượng thực hiện giả định | **25.600 CCQ** |
| Phần không thực hiện | **12.100 CCQ** |
| Giới hạn khối lượng | 5% ADV20, làm tròn theo lô 100 CCQ |
| Tỷ trọng ETF tại ngày 13/10/2026 | **43,62%** |

Theo giả định thanh khoản của nghiên cứu, **không phải toàn bộ 37.700 CCQ đều được thực hiện**. Phần chưa thực hiện giữ cho trạng thái danh mục khác với ý định phân bổ ban đầu.

Con số **43,62%** phản ánh tài khoản tại **13/10**, sau các phiên giao dịch tiếp theo; nó không phải tỷ trọng ngay sau lệnh ngày 01/10. Ngoài giới hạn khớp lệnh, giá thị trường và dòng tiền cũng có thể làm tỷ trọng thay đổi.

Đó là lý do nghiên cứu không dừng ở câu hỏi *“Tín hiệu mua hay bán?”* mà tiếp tục đến *“Tài khoản còn bao nhiêu ETF, bao nhiêu tiền và đang lệch mục tiêu ra sao?”*

[**Mở Dashboard để đối chiếu lệnh và trạng thái tài khoản B4**](https://vn30-etf-quant-platform.onrender.com/)

Tại trang **Tổng quan nghiên cứu**, nút **“Kiểm tra lệnh và tài khoản B4”** dẫn đến sổ mô phỏng ở mục **Theo dõi giao dịch mô phỏng**. Có thể xem khối lượng đề nghị, khối lượng thực hiện giả định và trạng thái tài khoản theo từng phiên.

## Một chính sách đầu tư cần được đánh giá trong cả danh mục

Bài toán nghiên cứu bắt đầu với **1 tỷ đồng**, cùng **59 khoản góp thêm 20 triệu đồng**, trên giai đoạn **01/10/2021–30/09/2026**. Các chính sách B1–B4/A3 được kiểm tra trên cùng giả định vốn và giao dịch; S1 được xem xét riêng vì dữ liệu thành phần VN30 còn giới hạn xác minh đúng thời điểm.

Trong mẫu lịch sử, B1 có **XIRR 10,06%/năm** và **MDD −42,27%**. B4 có **XIRR 7,94%/năm**, **MDD −20,39%**; A3 có **XIRR 8,75%/năm**, **MDD −18,91%**. Mức sụt giảm thấp hơn đi cùng tỷ trọng ETF bình quân thấp hơn, nên chưa thể quy toàn bộ khác biệt cho chất lượng tín hiệu.

Nghiên cứu vì vậy đặt hiệu quả đầu tư cạnh rủi ro, mức tiếp xúc thị trường, chi phí và khả năng thực hiện lệnh. Không có một chính sách phù hợp cho mọi mức chịu lỗ.

## Alpha dương đã đủ thuyết phục chưa?

Chưa. A3 có Alpha ước lượng **+3,4028%/năm**, với **p = 0,2393**; S1 có Alpha ước lượng **+2,5347%/năm**, với **p = 0,3347**, theo CAPM với sai số chuẩn HAC. Khoảng tin cậy 95% của hai ước lượng đều chứa 0.

Điều đó có nghĩa là nghiên cứu **chưa tìm được bằng chứng thống kê ở mức ý nghĩa 5%** để khẳng định Alpha khác 0. Hơn nữa, S1 vẫn thiếu xác minh đầy đủ dữ liệu giá cổ phiếu thành phần tại đúng ngày tín hiệu.

## Ý nghĩa của tình huống

Trọng tâm của sản phẩm là nối các phần việc thường bị tách rời: **tín hiệu → tỷ trọng mục tiêu → nhu cầu giao dịch → giới hạn thực hiện → trạng thái danh mục → đánh giá rủi ro**. Nhờ có sổ mô phỏng và phương pháp đi kèm, một kết quả có thể được truy nguyên thay vì chỉ quan sát trên biểu đồ.

Các giao dịch tháng 10/2026 là **mô phỏng lại trên lịch sử đã quan sát**, không phải quyết định tiến cứu được ghi nhận trước khi thị trường diễn biến. Nghiên cứu chưa có bằng chứng ngoài mẫu độc lập đủ mạnh, chưa xác minh khớp lệnh thực tế và chưa đủ cơ sở triển khai vốn thật.

*Nguồn: Báo cáo nghiên cứu sáu chiến lược tháng 10/2026 (mục V, VII, VIII và Phụ lục A), sổ lệnh và sổ tài khoản B4 trong bộ dữ liệu nghiên cứu lưu riêng.*
