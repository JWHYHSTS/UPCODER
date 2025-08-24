'''
Viết chương trình in ra màn hình ngôi sao (với chiều cao h nhập từ bàn phím)

ví dụ:

input:

3

output

*
**
***

'''
h = int(input())
for i in range(1, h + 1):
    print("*" * i)