'''
Cho một biểu thức hậu tố với số hạng là các số nguyên dương và ba toán tử +, -, *. Hãy tính giá trị của biểu thức hậu tố.
Ví dụ: biểu thức hậu tố: 2 3 4 + * 5 - 2 2 * + có giá trị là 13.

Dữ liệu input:
- Gồm một dòng thể hiện biểu thức hậu tố, mỗi số hạng là một số nguyên dương trong phạm vi từ 1 đến 100. Giữa hai số hạng, hoặc giữa hai toán tử, hoặc giữa số hạng và toán tử, cách nhau một khoảng trắng. Chiều dài biểu thức không quá 100 ký tự. Dữ liệu đề bài cho đảm bảo biểu thức hậu tố là hợp lệ. Trong quá trình tính toán đảm bảo trị tuyệt đối các giá trị trung gian không vượt quá 109.

Dữ liệu output:
- Là giá trị của biểu thức hậu tố.

Ví dụ:
input
2 3 4 + * 5 - 2 2 * +

output
13

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
        self.data = [0]*capacity
        self.sz = 0
    def push(self, x):
        if self.full(): return
        self.data[self.sz] = x
        self.sz += 1
    def top(self):
        return self.data[self.sz-1]
    def pop(self):
        if self.empty(): return
        self.sz -= 1
        return self.data[self.sz]
    def empty(self):
        return self.sz == 0
    def full(self):
        return self.sz == self.cap

tokens = sys.stdin.read().strip().split()
if not tokens:
    sys.exit()
st = Stack(len(tokens))
ops = {"+", "-", "*"}
for tk in tokens:
    if tk in ops:
        b = st.pop()
        a = st.pop()
        if tk == '+': st.push(a + b)
        elif tk == '-': st.push(a - b)
        else: st.push(a * b)
    else:
        st.push(int(tk))
print(st.top())