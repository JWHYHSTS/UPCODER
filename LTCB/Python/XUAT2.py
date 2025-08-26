'''
Yêu cầu xuất ra màn hình các dãy số như sau:

1
12
123
1234
12345
'''
for i in range(1, 6):
    print(''.join(str(j) for j in range(1, i + 1)))
    
'''
print(1)
print(12)
print(123)
print(1234)
print(12345)
'''