'''
Xuất nội dung của stack sau mỗi thao tác trong dãy.
Một chữ cái tượng trưng cho thao tác thêm chữ cái đó vào trong stack, dấu * tượng trưng cho thao tác lấy nội dung một phần tử trong stack in lên màn hình (nếu không có thì không in).
Cho biết kết quả xuất ra màn hình sau khi hoàn tất chuỗi input.

Ví dụ:

Input	
AB*
Output
B

'''

import sys
s=sys.stdin.read().strip()
st=[]
out=[]
for c in s:
    if c=='*':
        if st: out.append(st.pop())
    elif c:
        st.append(c)
print("".join(out))