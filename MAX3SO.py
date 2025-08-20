'''
Nhập vào 3 sô nguyên a,b,c. Tìm sô lớn nhât và sô nhỏ nhất trong 3 sô đó.

Ví dụ:
input
1 2 3

outpt:
3 1

'''
a,b,c = map(int, input().split())
# Cách 1: dùng Hàm
# max_num = max(a,b,c)
# min_num = min(a,b,c)
# print(max_num, min_num)

# Cách 2: Dùng Câu Lệnh Điều Kiện
if a >= b and a >= c:
    max_n = a
elif b >= a and b >= c:
    max_n = b
else:
    max_n = c

if a <= b and a <= c:
    min_n = a
elif b <= a and b <= c:
    min_n = b
else:
    min_n = c

print(max_n, min_n)