'''
Input:
- Dòng 1: Nhập vào N là số lượng phần tử của mảng
- Dòng 2: N số nguyên (mỗi số cách 1 khoảng trắng)

Ouput:
- Dòng 1: xuất các số âm của dãy
- Dòng 2: xuất các số dương của dãy

Ví dụ:
input
4
1 -2 3 -4
output
-2 -4
1 3

'''
n = int(input())
mang = list(map(int, input().split()))
print(*[x for x in mang if x < 0])
print(*[x for x in mang if x > 0])