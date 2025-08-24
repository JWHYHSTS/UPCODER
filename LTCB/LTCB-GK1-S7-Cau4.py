'''
Câu 4: (2d)

Input gồm nhiều dòng, mỗi dòng chứa 1 ký tự 'A' -> 'Z' hoặc 'a' -> 'z', kết thúc là ký tự '0'.

Output: gồm 1 ký tự duy nhất, là ký tự có mã ASCII lớn nhất trong input (không tính ký tự '0')

Lưu ý: Chỉ sử dụng những kiến thức đã được học trên lớp (không được sử dụng kiến thức khác, ví dụ mảng). 
Ví dụ:
Input
A
B
0
Output
B
'''

max_ch = None
while True:
    try:
        ch = input().strip()
    except EOFError:
        break
    if ch == '0':
        break
    if len(ch) == 0:
        continue
    if max_ch is None or ch > max_ch:
        max_ch = ch

if max_ch is not None:
    print(max_ch)