'''
Viết chương trình in ra tam giác vuông cân đặc
ví dụ
input: 4
output: 
*
**
***
****
'''
n = int(input())
for i in range(1, n + 1):
    print("*" * i)