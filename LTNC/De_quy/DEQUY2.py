'''
Liệt kê chuỗi hoán vị
Cho n chữ số 1, 2, 3, .., n (1 ≤ n ≤ 8), hãy liệt kê tất cả các hoán vị của n chữ số trên theo thứ tự từ điển.
Dữ liệu nhập:
- Là số nguyên n (1 ≤ n ≤ 8)
Dữ liệu xuất:
- Dòng thứ nhất là số nguyên m thể hiện số lượng hoán vị có được.
- Trong m dòng tiếp theo, mỗi dòng liệt kê một hoán vị theo thứ tự từ điển. Trong một hoán vị các chữ số đứng sát nhau (không dùng khoảng trắng để ngăn cách các chữ số)

Ví dụ
input
2
output
2
12
21

input
3
output
6
123
132
213
231
312
321

'''

import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()
n = int(data[0])

def factorial(x):
    if x < 2: return 1
    return x * factorial(x-1)

print(factorial(n))

path = []
used = [False]*(n+1)

def backtrack():
    if len(path) == n:
        print(''.join(map(str, path)))
        return
    for i in range(1, n+1):
        if not used[i]:
            used[i] = True
            path.append(i)
            backtrack()
            path.pop()
            used[i] = False

backtrack()