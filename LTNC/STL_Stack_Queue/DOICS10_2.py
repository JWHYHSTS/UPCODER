'''
Yêu cầu xây dựng 1 lớp Ngăn xếp, sau đó áp dụng vào giải bài tập sau:
Nhập vào 1 số nguyên ở hệ 10, yêu cầu xuất ra 1 số ở hệ 2

Ví dụ:

Input
10
Output
1010

'''

import sys

class Stack:
    def __init__(self):
        self.a=[]
    def push(self,x):
        self.a.append(x)
    def pop(self):
        return self.a.pop()
    def empty(self):
        return not self.a
    def top(self):
        return self.a[-1]

data=sys.stdin.read().strip().split()
if not data: sys.exit()
n=int(data[0])
if n==0:
    print(0)
    sys.exit()
st=Stack()
while n>0:
    st.push(str(n%2))
    n//=2
res=[]
while not st.empty():
    res.append(st.pop())
print("".join(res))