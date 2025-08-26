'''
Cho bốn số thực A, B, C, D. Hỏi tích của bốn số đó là số dương, số âm hay số 0.

Input:
Gồm bốn dòng, mỗi dòng gồm một số thực lần lượt là bốn số A, B, C, D. (-1018 ≤ A, B, C, D ≤ 1018).
Output:
Một số nguyên duy nhất là:
1 nếu tích bốn số là số dương.
-1 nếu tích bốn số là số âm.
0 nếu tích bốn số là số 0.

Ví dụ:

Input
20.21
-1.2
-2.3
1.0
Output
1

Ví dụ:

Input
5.0
-8.9
0.0
123.456
Output
0

'''
import sys

vals = []
for _ in range(4):
    line = sys.stdin.readline()
    if not line:
        break
    vals.append(float(line.strip()))

if len(vals) != 4:
    sys.exit()

if any(v == 0 for v in vals):
    print(0)
else:
    neg = sum(1 for v in vals if v < 0)
    print(1 if neg % 2 == 0 else -1)