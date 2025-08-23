'''
input:
Dong 1: nhap vao 1 mang

output:
Dong 1: xuất mảng vừa nhập

vi du:
input:
4 5 6

output
4 5 6
'''

mang = list(map(int, input().split()))
print(*mang)
