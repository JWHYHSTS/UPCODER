'''
Viết một hàm chuyển đổi cơ số từ hệ 10 sang hệ 2, 8 và 16 theo prototype sau:

void chuyenCoSo(long soHe10, int heCoSoMoi);

nếu tham số heCoSoMoi có giá trị là 0 thì chuyển sang cơ số 2, nếu là 1 thì chuyển sang hệ 8 còn nếu là 2 thì chuyển sang hệ 16.
Mặc định tham số heCoSoMoi có giá trị là 0.

ví dụ:
chuyenCoSo(10)   => kết quả sẽ là: 1010
chuyenCoSo(10,0)   => kết quả sẽ là: 1010
chuyenCoSo(10,1)   => kết quả sẽ là: 12
chuyenCoSo(10,2)   => kết quả sẽ là: A

Yêu cầu viết chương trình nhập vào 1 số nguyên n (0 < n <= 2000) là hệ cần đổi (theo qui ước của tham số là 0,1,2)
Xuất ra  số đã được đổi sang hệ tương ứng

Ví dụ:

Input	
10 0
10 1
Output
1010
12


Yêu cầu phải dùng stack để làm bài này - nếu không dùng stack sẽ bị 0 điểm bài này
'''

import sys

class Stack:
    def __init__(self, capacity=1000):
        self.a = [None]*capacity
        self.cap = capacity
        self.sz = 0
    def push(self, x):
        if self.full():  # simple auto-grow
            self.a.append(x)
            self.cap += 1
            self.sz += 1
        else:
            self.a[self.sz] = x
            self.sz += 1
    def pop(self):
        if self.empty(): return None
        self.sz -= 1
        return self.a[self.sz]
    def top(self):
        return None if self.empty() else self.a[self.sz-1]
    def empty(self):
        return self.sz == 0
    def full(self):
        return self.sz == self.cap

def chuyenCoSo(soHe10, heCoSoMoi=0):
    base_map = {0:2, 1:8, 2:16}
    base = base_map.get(heCoSoMoi, 2)
    if soHe10 == 0:
        return "0"
    digits = "0123456789ABCDEF"
    st = Stack()
    n = soHe10
    while n > 0:
        st.push(digits[n % base])
        n //= base
    res = []
    while not st.empty():
        res.append(st.pop())
    return "".join(res)

lines = [ln.strip() for ln in sys.stdin.read().strip().splitlines() if ln.strip()]
out = []
for line in lines:
    parts = line.split()
    if not parts: continue
    if len(parts) == 1:
        val = int(parts[0])
        out.append(chuyenCoSo(val))
    else:
        val = int(parts[0])
        base_code = int(parts[1])
        out.append(chuyenCoSo(val, base_code))
print("\n".join(out))