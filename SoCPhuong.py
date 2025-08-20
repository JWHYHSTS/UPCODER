'''
Nhập vào 1 số.

Kiểm tra số đó có phải là số chính phương không?
Xuất: yes, nếu đó là số chính phương, ngược lại xuất no

ví dụ:
input: 4

output: yes
'''

n = int(input())
def scp(n):
    if n < 0:
        return False
    x = int(n ** 0.5)
    return x * x == n
if(scp(n)):
    print("yes")
else:
    print("no")
    
# Cách 2:
n = int(input())
if n < 0:
    print("no")
else:
    x = int(n ** 0.5)
    if x * x == n:
        print("yes")
    else:
        print("no")