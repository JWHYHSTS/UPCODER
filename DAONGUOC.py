'''
Nhập vào 1 số gồm 3 chữ số, yêu cầu xuất số đó theo thứ tự ngược lại

ví dụ
input 
123

output
321
'''
a = int(input())
print(str(a)[::-1])

'''Cách 2:
a = int(input())
def dao_n(a):
    return int(str(a)[::-1])
print(dao_n(a))
'''