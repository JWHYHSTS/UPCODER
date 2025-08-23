'''
Nhập vào một mảng 2 chiều => xuất ma trận zic zac
input:
- dòng 1: nhập chiều nxm
- dòng 2: n dòng tiếp theo, mỗi dòng m số nguyên
output:
xuất ma trận ziczac

ví dụ:
3 3
7 8 9
1 2 3
6 5 4


output:
1 2 3
6 5 4
7 8 9

'''
n, m = map(int, input().split())
mang = []
for _ in range(n):
    mang.extend(map(int, input().split()))
mang.sort()
matran = []
for i in range(n):
    row = mang[i*m:(i+1)*m]
    if i % 2 == 1:
        row = row[::-1]
    print(*row)