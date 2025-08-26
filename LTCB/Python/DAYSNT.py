'''
Dãy nguyên tố 

Cho 1 dãy các số nguyên ,Hãy tìm số nguyên tố lớn nhất nhỏ hơn hoặc bằng K

Input
dòng 1: số nguyên K
dòng 2 : dãy số nguyên 

output:
dòng 2 : số nguyên tố lớn nhất mà không lớn hơn K, nếu không có in ra -1

ví dụ:
input:
9
5 4 7 11 10 13

output:
7

'''
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

k = int(input())
mang = list(map(int, input().split()))
max_snt = -1
for i in mang:
    if snt(i) and i <= k:
        max_snt = max(max_snt, i)
print(max_snt)