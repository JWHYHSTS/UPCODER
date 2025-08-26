'''
Cho hai số nguyên dương x và y lần lượt là chỉ số một tháng và một năm. Hãy cho biết số ngày của tháng trong năm đó.

Input:

Gồm hai dòng, dòng thứ nhất gồm số nguyên dương x và dòng thứ hai gồm số nguyên dương y (x ≤ 12, y ≤ 3000).

Output:

In ra số ngày của tháng x trong năm y.

Ví dụ:
Input
1
2020
Output
31

Ví dụ:
Input
2
2024
Output
29
'''
import sys

tokens = sys.stdin.read().split()
if len(tokens) < 2:
    sys.exit()  

x = int(tokens[0])
y = int(tokens[1])

if x == 2:
    leap = (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)
    print(29 if leap else 28)
elif x in (1,3,5,7,8,10,12):
    print(31)
else:
    print(30)