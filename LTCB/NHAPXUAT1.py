'''
Input:
Nhập vào 1 số nguyên dương có 3 chữ số
Output:
Dòng 1: xuất số hàng đơn vị
Dòng 2: xuất số hàng trăm
Dòng 3: xuất số hàng chục

Ví dụ:

Input	
123
Output
3
1
2
Lưu ý: dòng cuối cùng không có xuất xuống hàng
'''

a = int(input())
print(a % 10)
print(a // 100)
print((a // 10) % 10, end="")

'''
Cách 2:
a = input()
print(a[-1])   # hàng đơn vị
print(a[0])    # hàng trăm
print(a[1])    # hàng chục

*** Còn nếu trên 3 số: 
numbers = input().split()
for a in numbers:
    print(a[-1])
    print(a[0])
    print(a[1], end="")

'''