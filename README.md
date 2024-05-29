## Final Project môn Thực hành phát triển hệ thống trí tuệ nhân tạo
| Thành viên      | MSV      | Phân công công việc                                                                                                          |
|-----------------|----------|------------------------------------------------------------------------------------------------------------------------------|
| Đỗ Quang Dũng   | 22022561 |Thiết kế hệ thống đề xuất với content-based và collaborative filtering, crawl data, hỗ trợ thiết kế database                  |
| Lê Trung Hiếu   |          |                                                                                                                              |
| Trần An Thắng   | 22022525 |Backend về Sản phẩm và Thanh toán : Thêm vào giỏ hàng, Đặt hàng, Thanh toán                                                   |
| Phạm Văn Trường | 22022564         | Thiết kế hệ thống backend (Sản phẩm, Người dùng, Admin panel, ...), tạo Dockerfile                                                                                                                             |  
  
Link youtube demo dự án: https://youtu.be/NWRkG0gCdUw

## Mô tả dự án
Trong bối cảnh hiện đại, nhu cầu mua sắm trực tuyến ngày càng tăng cao, đặc biệt là với các sản phẩm thể thao như quần áo, giày dép, dụng cụ và phụ kiện. Tuy nhiên, người tiêu dùng thường gặp phải các vấn đề như khó khăn trong việc tìm kiếm sản phẩm phù hợp, thiếu thông tin chi tiết về sản phẩm và quy trình mua sắm phức tạp.
Website bán hàng đồ thể thao của chúng tôi được xây dựng nhằm giải quyết những thách thức này, cung cấp một nền tảng mua sắm tiện lợi, đáng tin cậy, với dịch vụ hỗ trợ khách hàng chuyên nghiệp, giúp người tiêu dùng dễ dàng tiếp cận và mua sắm các sản phẩm thể thao chất lượng.

## Các chức năng chính
- Thêm/chỉnh sửa/xoá sản phẩm
- Đề xuất sản phẩm với content-based và collaborative filtering
- Phân trang, phân loại sản phẩm
- Hiển thị danh sách sản phẩm kèm theo hình ảnh, mô tả, giá cả
- Giỏ hàng
- Thanh toán bằng thẻ tín dụng
- Tài khoản cá nhân

## Cài đặt
  1. Không sử dụng Docker:
  - Clone repo
  - Cài đặt các thư viện cần thiết bằng lệnh: `pip install -r require. txt`
  - Chạy file main.py
  - Truy cập địa chỉ `http://127.0.0.1:5000/`
  2. Sử dụng Docker:
  - Clone repo
  - Command: docker build -t &lt;name of docker image> .
  - Run docker container
 
  ## Công nghệ sử dụng
  - HTML, CSS, JS, Flask Python, SQLite, Docker
