'''
Viết chương trình nhập vào số nguyên dương n, in ra giá trị của tổng sau
1 + 2/3 + 2/3 * 4/5 + 2/3 * 4/5 * 6/7 + ... + 2/3 * 4/5 * ... * 2(n + 1)/ (2n + 3)
Ví dụ:  

input
3
output
3.06
Lưu ý: kết quả lấy 2 chữ số thập phân
'''
n = int(input())
tong = 0
t = 1
for i in range(1, n + 1):
    t *= (2 * (i + 1)) / (2 * i + 3)
    tong += t
tong = (2 * (tong + 1) / 3) + 1
print(f"{tong:.2f}")