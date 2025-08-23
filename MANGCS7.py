'''
input:
Dong 1: nhap số nguyên dương n>0
Dòng 2: nhập n số nguyên

output:
Dong 1: xuất mảng vừa nhập
Ví dụ:

Input
3
2 3 1

Output
2 3 1
'''
n = int(input())
mang = list(map(int, input().split()))
print(*mang)
