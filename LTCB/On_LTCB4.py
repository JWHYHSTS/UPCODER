'''
Viết chương trình bằng cách nén các ký tự giống nhau liên tiếp.Nếu ký tự đứng độc lập thì ghi số 1 trước ký tự đó
Input:
Chuỗi cần nén là các ký tự 'a....z' và 'A..Z'.Không có khoảng trắng và ký tự số.Độ dài không vượt quá 100 ký tự
Output:
Chuỗi sau khi nén
Ví dụ:

Input
abbXXYYY
Output
1a2b2X3Y
'''
import sys
s = sys.stdin.read().strip()
if not s:
    sys.exit(0)

res = []
prev = s[0]
cnt = 1
for ch in s[1:]:
    if ch == prev:
        cnt += 1
    else:
        res.append(f"{cnt}{prev}")
        prev = ch
        cnt = 1
res.append(f"{cnt}{prev}")
print("".join(res), end="")