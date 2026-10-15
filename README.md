# VN30 ETF | Nghiên cứu và mô phỏng đầu tư định lượng

**Công trình nghiên cứu cá nhân** phục vụ giới thiệu năng lực nghiên cứu định lượng và phát triển sản phẩm đầu tư; không phải sản phẩm được TVS nghiệm thu hay khuyến nghị đầu tư.

**[Mở ứng dụng trực tuyến — VN30 ETF Quant Platform](https://vn30-etf-quant-platform.onrender.com/)** · [Tình huống sử dụng](TINH_HUONG_SU_DUNG.md) · [Ví dụ mã Python](examples/accounting_example.py)

Ứng dụng dùng cho nghiên cứu và mô phỏng, không kết nối đặt lệnh tiền thật. Dịch vụ miễn phí trên Render có thể mất thời gian khởi động sau thời gian không truy cập.

## Bài toán và sản phẩm

Với **1 tỷ đồng ban đầu**, sau đó góp **20 triệu đồng mỗi tháng trong 59 tháng**, nhà đầu tư nên giải ngân, duy trì ETF hay điều chỉnh tỷ trọng thế nào? Một công cụ hữu ích không chỉ đưa tín hiệu mua/bán mà còn phải theo dõi **tiền mặt, số chứng chỉ quỹ, thanh khoản, chi phí, NAV và mức sụt giảm** sau mỗi quyết định.

Ứng dụng Streamlit gồm **7 mục**, hỗ trợ so sánh chính sách đầu tư, truy nguyên tín hiệu, mô phỏng một quyết định phân bổ, kiểm tra khả năng thực hiện lệnh, phân tích rủi ro và theo dõi tài khoản giả định. Giai đoạn mô phỏng chính: **01/10/2021–30/09/2026**, 1.245 phiên; tổng vốn góp **2,18 tỷ đồng**.

## Ai sử dụng và giải quyết việc gì?

Sản phẩm hướng tới **chuyên viên nghiên cứu định lượng, phân tích đầu tư và theo dõi rủi ro danh mục**. Thay vì dừng ở tín hiệu SMA200 hay một bảng lợi suất, người dùng có thể kiểm tra ba công việc liên tiếp:

| Công việc | Thao tác trong Dashboard | Điều nhận được |
|:--|:--|:--|
| Chọn chính sách phù hợp mức chịu lỗ | Lọc chiến lược bằng MDD và so XIRR/NAV trên **Tổng quan** | Các phương án lịch sử còn phù hợp ngưỡng tự chọn, kèm đánh đổi lợi suất–rủi ro |
| Biến tín hiệu thành danh mục | Xem kỳ tín hiệu; nhập tiền, số CCQ và vốn góp tại **Chiến lược / Danh mục** | Tỷ trọng mục tiêu, lượng mua/bán giả định, chi phí và phần chưa thực hiện |
| Kiểm tra vì sao không đạt mục tiêu | Mở **Theo dõi giao dịch mô phỏng**, chọn B4 và phiên 01/10/2026 | Sổ lệnh, trần 5% ADV20, CCQ khớp một phần và tiền chờ thanh toán |

**Ví dụ trực tiếp:** B4 dự kiến bán 37.700 CCQ, nhưng chỉ thực hiện giả định 25.600 CCQ và còn 12.100 CCQ không thực hiện. Đến 13/10/2026, danh mục còn 43,62% ETF so với mục tiêu đặt ngày 01/10 là 30%. Hai thời điểm khác nhau; khoảng cách còn chịu tác động của thị trường và những phiên tiếp theo. [Xem ứng dụng](https://vn30-etf-quant-platform.onrender.com/) → **Tổng quan** → **Kiểm tra lệnh và tài khoản B4**.

**Giá trị có thể kiểm tra:** gom tín hiệu, quy tắc phân bổ, dữ liệu lệnh và trạng thái tài khoản vào một chuỗi có thể truy nguyên, thay vì chỉ đọc các bảng kết quả rời. So với bảng tính hoặc công cụ Backtest riêng lẻ, đây là *phạm vi công việc được tích hợp*, không phải bằng chứng đã tiết kiệm thời gian, giảm chi phí hay dự báo tốt hơn. Nhu cầu sử dụng định kỳ và khả năng thương mại hóa chưa được khảo sát.

## Cơ sở lựa chọn ETF E1VFVN30

Mẫu nghiên cứu chỉ sử dụng **một ETF làm tài sản giao dịch** để so sánh các chính sách phân bổ trên cùng cơ sở. E1VFVN30 được chọn dựa trên thời gian hoạt động dài, tính liên tục của chuỗi giá và thanh khoản khảo sát, chứ không mặc định là ETF có lợi suất hoặc tổng chi phí tối ưu.

| ETF theo dõi VN30 | Giao dịch từ | Phí quản lý (%/năm) | Trung vị khớp lệnh (tỷ đồng/phiên) |
|:--|:--:|--:|--:|
| **E1VFVN30 – DCVFMVN30** | 06/10/2014 | 0,65 | **14,351** |
| FUESSV30 – SSIAM VN30 | 18/08/2020 | 0,55 | 0,444 |
| FUEMAV30 – MAFM VN30 | 08/12/2020 | 0,60 | 0,239 |
| FUEKIV30 – KIM Growth VN30 | 07/01/2022 | 0,55 | 0,060 |

*Dữ liệu theo Bảng 1 của báo cáo nghiên cứu ngày 15/10/2026. Giá trị trung vị khảo sát trên cùng 182 phiên 05/01–30/09/2026, **không phải thông tin có sẵn tại đầu mẫu năm 2021**. Đối chiếu một phiên 17/09/2021 ghi nhận giá trị khớp lệnh xấp xỉ 22,08 tỷ đồng (E1VFVN30), 2,07 tỷ đồng (FUEMAV30) và 0,70 tỷ đồng (FUESSV30); không đủ chứng minh ETF tối ưu. FUEKIV30 chưa giao dịch ở đầu mẫu.*

**Giới hạn chuẩn so sánh:** Theo hồ sơ quỹ được dẫn trong báo cáo, E1VFVN30 tham chiếu VN30 Total Return Index; mô hình tín hiệu và CAPM dùng VN30 Price Index. Chưa có phép thử tương đương giữa các ETF về lợi suất đầu tư thực hiện được, sai lệch bám chỉ số và toàn bộ chi phí. Đây là lý do lựa chọn *quỹ để nghiên cứu*, không phải khuyến nghị chọn quỹ tốt nhất.

## Sáu phương án nghiên cứu

| Mã | Chính sách phân bổ | Vai trò |
|:--|:--|:--|
| **B1** | Tích lũy ETF định kỳ | Đầu tư sớm, bổ sung vốn hằng tháng |
| **B2** | Giải ngân vốn ban đầu thành 6 đợt | Đối chứng rủi ro chọn thời điểm mua |
| **B3** | ETF/tiền mặt mục tiêu 60/40 | Đối chứng tỷ trọng cố định |
| **B4** | VN30 so với SMA200, mục tiêu ETF 30% hoặc 90% | Phân bổ theo xu hướng |
| **A3** | SMA200 kết hợp Momentum120, mục tiêu 30/60/90% | Nghiên cứu bổ sung động lượng |
| **S1** | SMA200 kết hợp Breadth60, mục tiêu 30/60/90% | Giả thuyết độ rộng thị trường đang nghiên cứu |

**B1–B4/A3** thuộc bộ kết quả chính đã đối soát. **S1** có mô phỏng riêng nhưng giá cổ phiếu điều chỉnh chưa được xác minh đầy đủ theo thông tin có sẵn đúng ngày tín hiệu. Không gộp S1 vào nhóm kết quả đã xác nhận.

## Kết quả lịch sử sau chi phí

| Chiến lược | NAV cuối kỳ (tỷ đồng) | TWR (%) | XIRR (%/năm) | MDD (%) |
|:--|--:|--:|--:|--:|
| B1 | 3,1266 | 40,06 | 10,06 | −42,27 |
| **B2** | **3,0709** | **34,51** | **9,55** | **−42,00** |
| B3 | 2,7588 | 26,16 | 6,53 | −26,81 |
| B4 | 2,9013 | 35,74 | 7,94 | −20,39 |
| A3 | 2,9856 | 41,40 | 8,75 | −18,91 |
| S1* | 2,8603 | 34,60 | 7,54 | −17,62 |

*Nguồn: bảng kết quả R01 của năm chiến lược chính và sổ nghiên cứu S1, Phụ lục A của báo cáo sáu chiến lược ngày 15/10/2026. S1 là kết quả thăm dò, khác trạng thái xác minh dữ liệu so với R01. NAV gồm vốn đã góp và biến động tài sản; TWR loại ảnh hưởng cơ học của vốn góp, XIRR xét thời điểm góp vốn, MDD là sụt giảm đỉnh–đáy.*

**Những gì số liệu thực sự cho thấy:** B1 có NAV/XIRR lớn nhất trong giai đoạn khảo sát nhưng chịu MDD khoảng 42%. B4 và A3 giảm sụt giảm danh mục so với B1 đồng thời duy trì tỷ trọng ETF bình quân thấp hơn. Alpha ước lượng của các chiến lược đều **chưa đạt ý nghĩa thống kê 5%** theo CAPM/HAC. Kết quả quá khứ chưa đủ xác nhận lợi thế dự báo hoặc mức sinh lời tương lai.

## Từ tín hiệu đến một quyết định có thể kiểm tra

**Tình huống B4 ngày 01/10/2026:** Tỷ trọng ETF mục tiêu là 30%. Hệ thống đề nghị bán **37.700 CCQ**, thực hiện giả định **25.600 CCQ** theo trần 5% ADV20 và ghi nhận **12.100 CCQ không thực hiện**. Đến 13/10/2026, tỷ trọng ETF thực tế vẫn là **43,62%**. Đây là ví dụ vì sao *tín hiệu đúng quy tắc chưa bảo đảm danh mục đạt tỷ trọng mong muốn*.

[Xem tình huống sử dụng và cách kiểm chứng](TINH_HUONG_SU_DUNG.md).

## Trải nghiệm trực tiếp trên ứng dụng

1. **Chọn chính sách và mức chịu lỗ:** tại *Tổng quan*, thay đổi ngưỡng MDD, xem XIRR/NAV và lọc phương án; lựa chọn dựa trên đánh đổi lịch sử, không dự báo lợi nhuận.
2. **Từ tín hiệu đến khối lượng lệnh:** tại *Chiến lược* và *Tín hiệu*, chọn B4/A3, kiểm tra mốc xác nhận SMA200/Momentum120, tỷ trọng mục tiêu và khối lượng thực hiện giả định; dùng *Danh mục* để xem tỷ trọng thực tế cùng tiền còn lại.
3. **Kiểm tra rủi ro và kết quả:** tại *Hiệu quả và rủi ro*, xem Alpha và khoảng tin cậy, so sánh mức sụt giảm, thanh khoản và kịch bản sức chịu đựng; tại *Theo dõi giao dịch mô phỏng*, truy nguyên một phiên tháng 10 và nghĩa vụ thanh toán.

**Quyết định sử dụng vốn thật tại thời điểm công bố: chưa chấp thuận.** Nghiên cứu còn thiếu kiểm định ngoài mẫu/tiến cứu độc lập, bằng chứng khớp lệnh thực tế và đối chứng benchmark tương đương; S1 chưa xác minh đầy đủ dữ liệu đúng thời điểm. Không dùng riêng Sharpe, MDD hoặc Alpha dương làm ngưỡng phê duyệt đầu tư.

## Các màn hình ứng dụng

| Tổng quan nghiên cứu | Tín hiệu đầu tư | Hiệu quả và rủi ro |
|:--:|:--:|:--:|
| ![Tổng quan](assets/tong-quan.png) | ![Tín hiệu](assets/tin-hieu.png) | ![Rủi ro](assets/rui-ro.png) |

*Ảnh chụp từ phiên Streamlit ngày 15/10/2026 (09:19–09:21), trước lượt biên tập giao diện cuối. Chúng là tư liệu ghi nhận giao diện thực tế, không phải ảnh kiểm thử của bản phát hành trực tuyến.*

## Phương pháp và giới hạn

Tài sản giao dịch mô phỏng là **E1VFVN30** và tiền mặt; chỉ số giá **VN30** được dùng cho tín hiệu. Giả định nghiên cứu gồm phí **0,15%/chiều**, trượt giá **0,05%/chiều**, thuế bán **0,10%**, lô **100 CCQ**, giới hạn **5% ADV20** và tiền mặt không hưởng lãi. Lệnh giả định đặt từ phiên hợp lệ sau khi xác nhận tín hiệu. Những giả định này chưa phản ánh đầy đủ độ sâu sổ lệnh hoặc xác suất khớp ngoài thực tế.

Chuỗi **9 phiên 01–13/10/2026** là **mô phỏng lại trên lịch sử đã quan sát**, không phải Paper Trading tiến cứu độc lập. Ứng dụng đã có địa chỉ trực tuyến; việc máy chủ khởi động thành công chưa thay thế nghiệm thu đầy đủ các hành trình người dùng. Không có bằng chứng giao dịch tiền thật hoặc Paper Trading tiến cứu độc lập được xác nhận.

## Mã ví dụ được phép công khai

`examples/` có đoạn Python **minh họa độc lập** việc kiểm tra NAV và giới hạn khối lượng lệnh, không trích xuất bộ máy Backtest hoặc Paper Trading thực tế. Chạy từ thư mục repository:

```bash
python -m unittest discover -s examples -p 'test_*.py'
```

Kho Public được xuất bản riêng biệt, **không chứa mã nguồn sản xuất, dữ liệu nguyên gốc, tài liệu làm việc và lịch sử Git của Private**. Chưa áp dụng giấy phép mã nguồn mở. Có thể xem hoặc sao chép mã đã công khai theo khả năng kỹ thuật của GitHub; phạm vi bảo vệ thực tế đến từ việc không xuất bản những phần cốt lõi.
