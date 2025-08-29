'''
(YÊU CẦU SỬ DỤNG STACK ĐỂ LÀM BÀI NÀY)

Xâu ngoặc đúng

Gọi xâu chỉ chứa các kí tự ngoặc tròn (, ), ngoặc vuông [, ] và ngoặc nhọn {, } là xâu ngoặc. Xâu ngoặc đúng được định nghĩa như sau:
- Xâu rỗng được coi là xâu ngoặc đúng
- Nếu a là xâu ngoặc đúng thì (a), {a}, [a] cũng là xâu ngoặc đúng
- Nếu a và b là các xâu ngoặc đúng thì ab cũng là xâu ngoặc đúng

Viết chương trình xác định xâu đầu vào có phải xâu ngoặc đúng hay không?

input:

Chứa một xâu cần xác định

output:

Nếu xâu ngoặc đúng thì xuất  “yes” ngược lại xuất ra “no”
Ví dụ:

Input
[()]
Output
yes

'''

import sys

s = sys.stdin.readline().strip()
st = []
pairs = {')': '(', ']': '[', '}': '{'}
valid_chars = set("()[]{}")

for c in s:
    if c not in valid_chars:
        print("no")
        sys.exit()
    if c in "([{":
        st.append(c)
    else:
        if not st or st[-1] != pairs[c]:
            print("no")
            sys.exit()
        st.pop()

print("yes" if not st else "no")