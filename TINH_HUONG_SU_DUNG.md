# Tình huống sử dụng | Từ dữ liệu đến quyết định phân bổ ETF

## 1. Chọn chính sách theo khả năng chịu rủi ro

Bài toán sử dụng 1 tỷ đồng ban đầu, góp 20 triệu đồng/tháng từ tháng thứ hai và không sử dụng đòn bẩy. Sáu chính sách được so sánh trên cùng thời kỳ 01/10/2021–30/09/2026, gồm năm kết quả chính B1–B4/A3 và nhánh thăm dò S1.

Trong mẫu, B1 có XIRR **10,06%/năm** nhưng MDD **−42,27%**. B4 có XIRR **7,94%/năm**, MDD **−20,39%**; A3 có XIRR **8,75%/năm**, MDD **−18,91%**. Các số liệu trình bày sự đánh đổi giữa hiệu quả, mức giữ ETF và rủi ro lịch sử, **không phải tiêu chuẩn tự động khuyến nghị**.

## 2. Truy nguyên một giao dịch mô phỏng

Trường hợp B4 tại phiên **01/10/2026**:

| Thành phần | Giá trị được ghi nhận |
|---|---:|
| Tỷ trọng ETF mục tiêu | 30% |
| Khối lượng dự kiến bán | 37.700 CCQ |
| Khối lượng thực hiện giả định | 25.600 CCQ |
| Phần bị hủy | 12.100 CCQ |
| Giới hạn giao dịch | 5% ADV20, làm tròn lô 100 CCQ |
| Tỷ trọng ETF thực tế ngày 13/10/2026 | 43,62% |

Dữ liệu nguồn lưu trong nhật ký mô phỏng lịch sử thuộc dự án Private. Giới hạn thanh khoản khiến quy mô lệnh thực hiện khác nhu cầu phân bổ. Tỷ trọng 43,62% là tại ngày 13/10, không phải ngay sau lệnh ngày 01/10; biến động giá, dòng tiền và các phiên sau cũng tác động. Quy trình nghiên cứu truy vết được *tín hiệu → mục tiêu → nhu cầu lệnh → giới hạn → trạng thái tài khoản*, thay vì chỉ đưa ra điểm mua/bán.

Để tự kiểm tra, mở [Dashboard trực tuyến](https://vn30-etf-quant-platform.onrender.com/) → **Tổng quan** → **Kiểm tra lệnh và tài khoản B4**; so số liệu tại **Theo dõi giao dịch mô phỏng**.

Đây là **sổ mô phỏng lại diễn biến đã xảy ra**, không phải quyết định được ghi nhận trước phiên 01/10/2026. Bộ mã Public không cung cấp chức năng đặt lệnh, tính tín hiệu hoặc khôi phục sổ tài khoản này.

## 3. Kiểm tra giá trị bổ sung của tín hiệu

A3 ước lượng Alpha **+3,4028%/năm**, giá trị **p = 0,2393**; S1 ước lượng Alpha **+2,5347%/năm**, **p = 0,3347** theo CAPM/HAC. Các khoảng tin cậy 95% đều chứa 0 nên chưa có bằng chứng thống kê ở mức 5% để khẳng định Alpha khác 0. Việc S1 giảm sụt giảm còn gắn với tỷ trọng ETF bình quân thấp hơn B4 và khác biệt trạng thái một số lệnh.

## 4. Phạm vi sản phẩm

Ứng dụng hỗ trợ nghiên cứu và mô phỏng phân bổ, đối soát kết quả, giải thích quyết định và quản trị rủi ro lịch sử. Dữ liệu thành phần phục vụ S1 chưa được xác minh hoàn toàn tại đúng thời điểm tín hiệu; chưa có kết quả kiểm định ngoài mẫu/tiến cứu độc lập đủ mạnh và chưa có cơ sở triển khai giao dịch vốn thật.

**Nguồn:** Báo cáo nghiên cứu sáu chiến lược tháng 10/2026 (mục V, VII, VIII và Phụ lục A), cùng sổ mô phỏng B4 của bộ dữ liệu nghiên cứu gốc được lưu riêng trong Private Master. Con số ở đây được chọn lọc để minh họa quy trình, không phải sổ lệnh đầy đủ hay mã nguồn công khai.
