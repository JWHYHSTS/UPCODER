'''
Input: cho ma trận NxN được nhập như sau:
- Dòng 1: gồm 1 số nguyên N
- Dòng 2: gồm N dòng, mỗi dòng gồm N số nguyên (cách nhau 1 khoảng trắng)

Output: xuất các phần tử đường chéo chính của ma trận NxN


hình đường chéo chính

ví dụ:
Ví dụ:

input
3
1 2 3
4 5 6
7 8 9

output
1 5 9

'''

n = int(input())
mang = []
for i in range(n):
    hang = list(map(int, input().split()))
    mang.append(hang)
for i in range(n):
    print(mang[i][i], end=' ')