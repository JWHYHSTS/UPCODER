'''
Nhập:

Dòng 1: nhập vị trí cần xóa
Dòng 2: nhập vào 1 dãy số

Xuất:
mảng sau khi xóa

ví dụ:
input:
2
1 2 3 4

output:
1 2 4

'''
a = int(input())
mang = list(map(int, input().split()))
mang.pop(a) # Hàm pop() dùng để xóa phần tử tại vị trí a
print(*mang)