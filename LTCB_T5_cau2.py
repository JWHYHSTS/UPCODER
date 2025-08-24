'''
Nhập vào 2 số nguyên m, n.
Kiểm tra nếu:
m chia hết cho n thì xuất "M chia het cho N"
n chia hết cho m thì xuất "N chia het cho M"
m chia hết cho n và ngược lại thì xuất "1"
m không chia hết cho n và ngược lại thì xuất "-1"
ví dụ:
Input: 2 4
Output: 4 chia het cho 2
'''
m, n = map(int, input().split())

m_div_n = (n != 0 and m % n == 0)
n_div_m = (m != 0 and n % m == 0)

if m_div_n and n_div_m:
    print(1)
elif n_div_m:
    print(f"{n} chia het cho {m}")
elif m_div_n:
    print(f"{m} chia het cho {n}")
else:
    print(-1)