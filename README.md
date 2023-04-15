Báo cáo đồ án 1 lần 1 (từ 02/04/2023 đến 15/04/2023) 
Họ và tên: Vũ Văn Nghĩa 
MSSV: 20206206205 
NỘI DUNG BÁO CÁO: 
1.      Em đang tìm hiểu kiến thức cơ bản React và JavaScript 
2.      Xây dựng giao diện font - end (html, css, js). Em chưa làm xong tất cả các chức năng. 
•	Mã nguồn: https://github.com/vvn20206205/Frontend_DoAn1 
•	Demo: https://vvn20206205.github.io/Frontend_DoAn1 
3.       Công nghệ em dự định tìm hiểu để xây dựng làm website: 
•	Back - end: Express JS và mySQL 
•	Font - end: React JS  
4.       Mô tả nghiệp vụ:  
- Một cửa hàng bán tranh cần xây dựng quản lí tranh. Sản phẩm tranh gồm (id, tiêu đề, giá, kích thước, mô tả, đường dẫn file ảnh, id thể loại, id tác giả) 
===> SQL: authors (id, name, date_of_birth, gender, phone_number, email, address, image) 
===> SQL: categories (id, name) 
===> SQL: products (id, title, price, size, description, image, category_id, artist_id) 
- Ban đầu khi truy cập vào website sẽ có đăng nhập nhiều vai trò:  
- Đối với tất cả các vai trò đều có trang chung: Trang chủ (Home), Hồ sơ (Profile), Thông báo (Notification), Cài đặt (Settings), Đăng xuất (Logout).  
•	Home - có nghiệp vụ riêng của từng vai trò (mô tả bên dưới).  
•	Profile - có hồ sơ người dùng như (vai trò, id, mật khẩu, tên, ngày sinh, giới tính, số điện thoại, email, địa chỉ, ảnh avatar) 
===> SQL: user (role, id, password, name, date_of_birth, gender, phone_number, email, address, image) 
•	Notification - có id, thời gian, tiêu đề, nội dung của thông báo 
===> SQL: notification (id, time, title, content) 
•	Settings - thay đổi thông tin của tài khoản như mật khẩu, tên, ngày sinh, giới tính, số điện thoại, email, địa chỉ, ảnh avatar 
•	Logout - trở về trang đăng nhập nhiều vai trò  
 * Nghiệp vụ riêng của từng vai trò:  
- Đối với khách hàng:  
•	Tất cả sản phẩm - All products - hiển thị tất cả các sản phẩm 
•	Phân loại theo thể loại - All categories - hiển thị tất cả các thể loại sản phẩm 
•	Các tác giả - All authors - hiển thị tất cả các tác giả 
•	Tìm kiếm tranh - Search product - tìm kiếm các sản phẩm liên quan đến từ khóa 
•	Sản phẩm yêu thích - Favorite product - chức năng sản phẩm yêu thích của khách hàng 
===> SQL: favorite (customer_id, product_id) 
- Chức năng chấm công: (nhân viên nào cũng có) = > Tạo 1 chức năng đếm theo ngày để tính lương.  
===> SQL: bảng chấm công 
- Đối với tư vấn sản phẩm: có chức năng xem sản phẩm như khách hàng.  
- Đối với thu ngân: Tạo hóa đơn (thời gian, các sản phẩm, id nhân viên, id khách, tổng tiền... )  
- Đối với Nhập kho: Thông tin nhập kho (thời gian, các sản phẩm, id nhân viên, id khách, tổng tiền... ) 
===> SQL: bảng hóa đơn ( thời gian, các sản phẩm, id nhân viên, id khách, tổng tiền... ) có loại là "Nhập" hoặc "Bán" 
- Đối với Kế toán:  
•	Trả lương cho nhân viên 
•	Xuất báo cáo excel hoặc csv, word hoặc pdf. 
- Đối với Chăm sóc khách hàng: nhắn tin hoặc gọi điện tư vấn khách hàng 
===> SQL: bảng Chat messsss 
- Đối với Admin UI:  
•	Có dashboard tổng quan thống kê trực qaun về các bảng SQL (sản phẩm,nhân viên,khách hàng,...) 
•	Thêm sửa xóa sản phẩm,người dùng 
•	Xuất báo cáo tổng quan về quản lí

 
5.      Dự định kế hoạch 2 tuần tiếp theo: 
•	Do em đang tìm hiểu cả Back - end (Express JS , mySQL) và Font - end (React JS ) nên em dự định xây dựng ứng dụng CRUD đơn giản: ví dụ Todo App 
•	Tiếp tục làm giao diện Font - end của chương trình 
•	Thiết kế UML Diagrams (Use Case Diagrams,Activity Diagrams,Sequence Diagrams,Class Diagrams) 

