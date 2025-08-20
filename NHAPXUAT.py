'''
Viết chương trình nhập vào 2 số nguyên a,b, yêu cầu xuất ra tổng 2 số nguyên đó theo định dạng
a+b = tổng.

ví dụ:
input:
2 3

output
2+3=5
'''
a, b = map(int, input().split())
print(str(a) + "+" + str(b) + "=" + str(a + b))
# cách 2: print(f"{a}+{b}={a+b}")

''' Cách 3:
values = list(map(int, input().split()))

total = 0
for i in values:
    total += i

print(str(values[0]) + "+" + str(values[1]) + "=" + str(total))
'''