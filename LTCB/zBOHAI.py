'''
Viết chương trình nhập vào 2 số nguyên dương N,M;  trong đó N có số chữ số lớn hơn một. Yêu cầu kiểm tra tích các chữ số của N có bằng tổng các ước của M hay không? Nếu có xuất YES ngược lại xuất NO

Dữ liệu nhập:

- Là hai số nguyên N, M cách nhau một khoảng trắng (1 ≤ N, M ≤ 105)

Dữ liệu xuất:

- In ra YES nếu N, M là thỏa điều kiện trên. In ra NO nếu không phải.

Ví dụ
Input
23 6
Output
NO
'''

a, b = map(int, input().split())

tich = 1
for digit in str(a):
    tich *= int(digit)

tong = 0
for i in range(1, b + 1):
    if b % i == 0:
        tong += i

if tich == tong:
    print("YES")
else:
    print("NO")