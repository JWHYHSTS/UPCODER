'''
Viết chương trình tính tổng các số có dạng: 1+11+111+1111+...
Nhập vào n số cần tính tổng (n>=2), xuất ra kết quả tương ứng.
input: 5
output: 12345
'''
n = int(input().strip())
result = sum(int("1" * i) for i in range(1, n + 1))
print(result)