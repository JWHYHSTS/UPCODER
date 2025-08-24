'''
Nhap vào 2 sô nguyên a,b. Xuất sô lớn nhât

ví dụ:
input 
2 3

output
3
'''
a, b = map(int, input().split())
if a > b:
    print(a)
else:
    print(b)