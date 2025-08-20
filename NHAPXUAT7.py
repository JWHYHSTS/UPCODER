'''
Input
Nhập vào 1 số thực
Ouput:
Xuất số ở intput ra lấy chính xác 3 chữ số thập phân
Ví dụ:

Input	
1.0123
Output
1.012
Hướng dẫn: 
Sử dụng lệnh printf của C, ví dụ muốn xuất 2 chữ số thập phân của biến x, với x là biến số thực thì sử dụng như sau:
printf("%.2f",x);
'''

a = float(input())
print("%.3f" % a)