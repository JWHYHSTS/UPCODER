'''
Nhập vào 1 số.

Kiểm tra số đó có phải là số nguyên tố không?
Xuất: true, nếu đó là số nguyên tố, ngược lại xuất false

Ví dụ:

Input	
4
Output
false
'''

n = int(input())
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
if(snt(n)):
    print("true")
else:
    print("false")