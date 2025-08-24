'''
Nhập vào 1 số nguyên, yêu cầu xuất ra chữ số ở vị trí i của số đó, nếu không có thì xuất ra -1
(Lưu ý thứ tự đếm từ trái sang phải - bắt đầu là vị trí thứ 0)

input:
- Dòng 1: Nhập vào vị trí thứ i cần xuất
- Dòng 2: Nhập vào số cần xử lý

output:
- Xuất ra chữ số thứ i, nếu không có xuất -1

ví dụ:
input:
1
1234

output  
2
'''
i = int(input())
n = int(input())
s = str(abs(n)) # Chuyển số nguyên thành chuỗi
if 0 <= i < len(s): # Điều kiện kiểm tra vị trí i, Lý do 0 <= i < len(s) để đảm bảo i nằm trong khoảng hợp lệ
    print(s[i])
else:
    print(-1)
    
# Cách 2: Sử dụng strip()
'''
i = int(input())
n = input().strip()

if i < 0 or i >= len(n):
    print(-1)
else:
    print(n[i])

'''
