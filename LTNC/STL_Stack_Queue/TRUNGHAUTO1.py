'''


Nhập vào 1 biêu thức trung tố, yêu cầu xuất biểu thức theo dạng hậu tố.

(Các số dạng chỉ là số có 1 chữ số)

Ví dụ:
input
3+4*2/(1-5)

output
3 4 2 * 1 5 - / +

Yêu cầu của đề (mỗi yêu cầu bị thiếu hoặc sai sẽ bị trừ 1 điểm):
+ sử dụng cấu trúc Stack  
+ Xây  dựng các thao tác: init, push, top, pop, empty, full
+ Lưu ý: ghi chính xác tên cấu trúc và hàm theo yêu cầu
+ Không sử dụng cấu trúc Stack mà sử dụng stack có sẵn trong std sẽ không tính điểm


'''

import sys

class Stack:
    def __init__(self, capacity):  
        self.cap = capacity
        self.data = [''] * capacity
        self.sz = 0
    def push(self, x):
        if self.full(): return
        self.data[self.sz] = x
        self.sz += 1
    def top(self):
        return self.data[self.sz-1]
    def pop(self):
        if self.empty(): return None
        self.sz -= 1
        return self.data[self.sz]
    def empty(self):
        return self.sz == 0
    def full(self):
        return self.sz == self.cap

expr = sys.stdin.read()
if not expr:
    sys.exit()
expr = ''.join(c for c in expr.strip() if not c.isspace())

prec = {'+':1,'-':1,'*':2,'/':2,'^':3}
right_assoc = {'^'}

st = Stack(len(expr)+5)
out = []

for c in expr:
    if c.isdigit():  
        out.append(c)
    elif c == '(':
        st.push(c)
    elif c == ')':
        while not st.empty() and st.top() != '(':
            out.append(st.pop())
        if not st.empty() and st.top() == '(':
            st.pop()
    else:  
        while (not st.empty() and st.top() != '(' and
               (prec[st.top()] > prec[c] or
                (prec[st.top()] == prec[c] and c not in right_assoc))):
            out.append(st.pop())
        st.push(c)

while not st.empty():
    out.append(st.pop())

print(' '.join(out))