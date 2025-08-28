'''
Điểm trong không gian và mặt phẳng 

Xây dựng cấu trúc điểm trong mặt phẳng Oxy 
Viết quá tải toán tử nhập ( >> ) , xuất ( << ) (xuất theo dạng (x, y) ) 
viết quá tải toán tử trừ ( - ) để tính khoảng cách giữa 2 điểm 
viết quá tải toán tử so sánh nhỏ hơn ( < ) để so sánh toạ độ của 2 điểm (theo thứ tự hoành độ rồi tới tung độ)

Xây dựng cấu trúc điểm trong không gian Oxyz
Viết quá tải toán tử nhập ( >> ) , xuất ( << ) (xuất theo dạng (x, y, z) )
viết quá tải toán tử trừ ( - ) để tính khoảng cách giữa 2 điểm 
viết quá tải toán tử so sánh nhỏ hơn ( < ) để so sánh toạ độ của 2 điểm (theo thứ tự ưu tiên hoành độ, tung độ, cao độ)  
Xây dựng cấu trúc mảng lưu trữ cấu trúc điểm ở trên sử dụng template
Viết quá tải toán tử nhập ( >> ) , xuất ( << )
viết hàm tìm khoảng cách lớn nhất giữa 2 điểm trong mảng (tìm trong mảng 2 điểm sao cho khoảng cách giữa 2 điềm đó là lớn nhất )
viết hàm sắp xếp mảng tăng dần
viết hàm sắp xếp mảng giảm dần
Dữ liệu nhập:
chuỗi "Oxy" và "Oxyz" và toạ độ điểm, nếu là Oxy thì nhập điểm trong mp Oxy , nếu là Oxyz thì nhập điểm trong không gian Oxyz

Dữ liệu xuất:
dòng 1: xuất ra mảng toạ độ trong hệ toạ độ Oxy theo thứ tự tăng dần, mỗi phần tử cách nhau 1 khoảng trắng
dòng 2:  xuất ra mảng toạ độ trong hệ toạ độ Oxyz theo thứ tự giảm dần, mỗi phần tử cách nhau 1 khoảng trắng 
dòng 3: xuất ra khoảng cách lớn nhất giữa 2 điểm trong mảng toạ độ Oxy, làm tròn đến 3 chữ số thập phân
dòng 4:  xuất ra khoảng cách lớn nhất giữa 2 điểm trong mảng toạ độ Oxyz, làm tròn đến 3 chữ số thập phân

lưu ý: sử dụng roundf(n * 1000) / 1000 ; để làm tròn n tới 3 chữ số thập phân 

Input:
Oxy 1 2
Oxyz 1 2 3
Oxy 5 2
Oxyz 4 5 6
Oxy 7 8

Output:
(1,2) (5,2) (7,8) 
(4,5,6) (1,2,3) 
8.485
5.196
'''

