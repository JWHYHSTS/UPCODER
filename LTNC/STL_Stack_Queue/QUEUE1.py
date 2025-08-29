'''
Xuất nội dung của queue sau mỗi thao tác trong dãy.
Một chữ cái tượng trưng cho thao tác thêm chữ cái đó vào trong queue, dấu * tượng trưng cho thao tác lấy nội dung một phần tử trong queue in lên màn hình (nếu không có thì không in).
Cho biết kết quả xuất ra màn hình sau khi hoàn tất chuỗi input.

Ví dụ:

Input
AB*
Output
A
'''

import sys
from collections import deque
s=sys.stdin.read().strip()
q=deque()
out=[]
for c in s:
    if c=='*':
        if q: out.append(q.popleft())
    elif c:
        q.append(c)
print("".join(out))