'''
Nhập các tọa độ x ,y trên trục tọa độ OXY. Nhiệm vụ của bạn là đếm xem có bao nhiêu đường thẳng song song với trục Oy. Như ảnh dưới thì ta có 1 đường thẳng vì 2 điểm kia nối lại là // với trục oy


 Lưu ý : Chỉ có 1 điểm thì không phải là đường thẳng , nếu 1 đường thẳng nằm trong đường thẳng dài hơn thì chỉ tính 1 đường thẳng 

Điều kiện nhập: ko trùng lại tọa độ đã nhập , các số đều là số nguyên 


Input:
Dòng 1 : Nhập số nguyên dương n
Dòng 2 : Nhập tọa độ xi
Dòng 3 : Nhập tọa độ yi

Output: Xuất ra có bao nhiêu đường thẳng // với trục Oy

Input example:
5 
1 3 4 5 2
3 9 2 7 8
Output example: 
0

'''

import sys

tokens = list(map(int, sys.stdin.read().split()))
if not tokens:
    sys.exit()
n = tokens[0]
if len(tokens) < 1 + 2 * n:
    sys.exit()
xs = tokens[1:1+n]
ys = tokens[1+n:1+2*n]

freq = {}
for x in xs:
    freq[x] = freq.get(x, 0) + 1

count = sum(1 for v in freq.values() if v >= 2)
print(count)