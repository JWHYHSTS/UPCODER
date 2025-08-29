'''
(yêu cầu dùng vector để làm bài này)

Nhập:

Dòng 1: vào số n
Dòng 2: nhập vào n số nguyên
Dòng 3: nhập vị trí cần xóa hoặc đoạn cần xóa [a,b), hoặc nếu là -1 thì xóa hết dãy

Xuất:
mảng sau khi xóa, nếu dãy rỗng xuất ra chữ "empty"

ví dụ 1:
input:
4
1 2 3 4
2

output:
1 2 4

ví dụ 2:
input:
4
1 2 3 4
1 3

output:
1 4
'''

n = int(input())
vec = list(map(int, input().split()))
pos = input().strip().split()

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