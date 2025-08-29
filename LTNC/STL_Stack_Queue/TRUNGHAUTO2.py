'''
Nhập vào 1 biêu thức trung tố, yêu cầu xuất biểu thức theo dạng hậu tố.

Input:

+ Nhập biểu thức trung tố

(lưu ý:

+ Các số hạng, phép toán cách nhau 1 khoảng trắng

+ mỗi số hạng <= 106)

Ouput:

  + Biểu thức trung tố (số hạng và phép toán cách nhau 1 khoảng trắng)



Ví dụ:

Input	
3 + 4 * 2 / ( 1 – 5 )
Output
3 4 2 * 1 5 - / +

'''

import sys

class Stack:
    def __init__(self):
        self.a=[]
    def push(self,x): self.a.append(x)
    def pop(self): return self.a.pop()
    def top(self): return self.a[-1]
    def empty(self): return not self.a

line = sys.stdin.read().strip()
if not line:
    sys.exit()

line = line.replace('–','-')
tokens = line.split()

prec = {'+':1,'-':1,'*':2,'/':2,'^':3}
right_assoc = {'^'}
st = Stack()
out = []

for tk in tokens:
    if tk.isdigit():               
        out.append(tk)
    elif tk == '(':
        st.push(tk)
    elif tk == ')':
        while not st.empty() and st.top()!='(':
            out.append(st.pop())
        if not st.empty() and st.top()=='(':
            st.pop()
    else:  
        while (not st.empty() and st.top()!='(' and
               (prec[st.top()]>prec[tk] or
                (prec[st.top()]==prec[tk] and tk not in right_assoc))):
            out.append(st.pop())
        st.push(tk)

while not st.empty():
    out.append(st.pop())

print(' '.join(out))