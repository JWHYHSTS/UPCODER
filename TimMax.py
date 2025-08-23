'''
Nhập vào 1 dãy số nguyên, yêu cầu tìm phần tử lớn nhất trong mảng

ví dụ:
input:
1 2 3 4 5

output:
5
'''
mang = list(map(int, input().split()))
print(max(mang))