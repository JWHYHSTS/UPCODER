'''
Giả sử một chiếc ô tô chuyển động thẳng, có vận tốc ban đầu v0 (m/s), gia tốc a (m/s2) và thời gian chuyển động t (s). 

Viết chương trình C++ để tìm vận tốc cuối cùng của ô tô và in kết quả ra màn hình.

input: 1 2 3

output: 7
'''
import sys

data = sys.stdin.read().strip().split()
if len(data) < 3:
    sys.exit(0)
v0, a, t = map(int, data[:3])
print(v0 + a * t, end="")