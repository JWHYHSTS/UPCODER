'''
Nhập vào 1 số nguyên, yêu cầu xuất ra chữ số hàng trăm của số đó, nếu không có thì xuất ra -1


ví dụ:
input:
1234

output
2
'''
n = int(input())
if n < 100:
    print(-1)
else:
    x = (n // 100) % 10
    print(x)