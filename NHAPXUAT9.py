'''
Nhập vào 1 số nguyên, yêu cầu xuất ra chữ số hàng nghìn của số đó, nếu không có thì xuất ra -1.

Ví dụ:

Input

Output

4315

4

'''

n = int(input())
if n < 1000:
    print(-1)
else:
    print(n // 1000 % 10)
