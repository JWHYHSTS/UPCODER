'''
(yêu cầu dùng vector để làm bài này)

Nhập:
Dòng 1: nhập vị trí cần xóa hoặc đoạn cần xóa [a,b), hoặc nếu là -1 thì xóa hết dãy
Dòng 2: nhập vào 1 dãy số

Xuất:
mảng sau khi xóa, nếu dãy rỗng xuất ra chữ "empty"
Ví dụ 1:

Input
2
1 2 3 4
Output
1 2 4



Ví dụ 2:

Input
1 3
1 2 3 4
Output
1 4
'''

pos = input().strip().split()

vec = list(map(int, input().split()))

if pos == ['-1']:
    vec.clear()
elif len(pos) == 1:
    idx = int(pos[0])
    if 0 <= idx < len(vec):
        vec.pop(idx)
elif len(pos) == 2:
    a, b = map(int, pos)
    del vec[a:b]

if not vec:
    print("empty")
else:
    print(' '.join(map(str, vec)))