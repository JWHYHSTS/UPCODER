'''
Cho đầu vào là một biểu thức dạng trung tố, bao gồm:
- Các toán tử: +, -, *, /, ^
- Các tham số là kí tự từ 'a'->'z'
- Các dấu ngoặc đơn thể hiện thứ tự thực hiện phép tính

Viết chương trình chuyển biểu thức đầu vào thành biểu thức dạng hậu tố

Ví dụ:
Input: (a+(b+c))              (chú ý: đầu vào không ghi a+b+c)
Output: abc++

'''

import sys

class Stack:
    def __init__(self): self.a=[]
    def push(self,x): self.a.append(x)
    def pop(self): return self.a.pop()
    def top(self): return self.a[-1]
    def empty(self): return not self.a

prec = {'+':1,'-':1,'*':2,'/':2,'^':3}

s = sys.stdin.read()
if not s: sys.exit()
expr = ''.join(c for c in s.strip() if not c.isspace())

st = Stack()
out = []

for c in expr:
    if 'a' <= c <= 'z':
        out.append(c)
    elif c == '(':
        st.push(c)
    elif c == ')':
        while not st.empty() and st.top()!='(':
            out.append(st.pop())
        if not st.empty() and st.top()=='(':
            st.pop()
    else:  # operator
        while (not st.empty() and st.top()!='(' and
               (prec[st.top()] > prec[c] or
                (prec[st.top()] == prec[c] and c != '^'))):
            out.append(st.pop())
        st.push(c)

while not st.empty():
    out.append(st.pop())

print(''.join(out)) 