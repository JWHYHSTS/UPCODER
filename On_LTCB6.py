'''
Xây dựng một cấu trúc Diem biểu diễn một điểm trong tọa độ Oxy
Xây dựng một cấu trúc DuongTron biểu diễn một đường tròn.Gồm các thông tin:
Điểm: là một Điểm có tọa độ là số nguyên
Bán kính: là số nguyên không âm
Cho một danh sách n đường tròn xác định xem có bao nhiêu đường tròn cắt nhau 
Input:
Dòng 1: Số nguyên dương N - số lượng đường tròn (N<=50)
N dòng tiếp theo mỗi dòng là 3 số nguyên x,y,r cách nhau một khoảng trắng.Trong đó x,y là tọa độ tâm đường tròn, r là bán kính đường tròn
Output:
Số duy nhất là số các cặp đường tròn cắt nhau
Ví dụ:

Input
3
1 0 2
6 2 2
3 4 1
Output
0

Gợi ý: Hai đường tròn giao nhau khi |R1-R2|<i1i2<|R1+R2| ( với i1i2 là khoảng cách tâm hai đường tròn, R1 là bán kính đường tròn 1,R2 là bán kính đường tròn 2 
'''

import sys
from dataclasses import dataclass

@dataclass
class Diem:
    x: int
    y: int

@dataclass
class DuongTron:
    tam: Diem
    r: int

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)

n = int(data[0])
circles = []
idx = 1
for _ in range(n):
    if idx + 2 >= len(data):
        break
    x = int(data[idx]); y = int(data[idx+1]); r = int(data[idx+2])
    idx += 3
    circles.append(DuongTron(Diem(x, y), r))

cnt = 0
for i in range(len(circles)):
    c1 = circles[i]
    for j in range(i+1, len(circles)):
        c2 = circles[j]
        dx = c1.tam.x - c2.tam.x
        dy = c1.tam.y - c2.tam.y
        d2 = dx*dx + dy*dy  
        rsum = c1.r + c2.r
        rdiff = abs(c1.r - c2.r)
        if rdiff*rdiff < d2 < rsum*rsum:
            cnt += 1

print(cnt, end="")