'''
input:
- Nhập vào 1 số nguyên n

output:
- Nếu n là chẵn xuất "chan" ngược lại xuất "le"

ví dụ
input:
3

output:
le
'''
n = int(input())
if n % 2 == 0:
    print("chan")
else:
    print("le")