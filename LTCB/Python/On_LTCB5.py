'''
Cho một số nguyên dương gồm N phần tử (2<=n<=50). Hãy đoán xem trong đây có bao nhiêu phần tử không nhỏ hơn phần tử đứng trước nó( tính cả phần tử đầu tiên)
Input:
Dòng 1: Số nguyên dương N(2<=N<=50)
Dòng 2: Số nguyên dương,mỗi số cách nhau một khoảng trắng.Mỗi số không vượt quá 100
Output:
Số duy nhất là số lượng các phần tử trong dãy không nhỏ hơn số đứng trước nó

Ví dụ:

Input
7
3 5 6 8 4 2 9
Output
5
'''

import sys
data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)
    
n = int(data[0])
arr = list(map(int, data[1:1+n]))
arr = arr[:n]
cnt = 0
for i, v in enumerate(arr):
    if i == 0 or v >= arr[i-1]:
        cnt += 1
print(cnt, end="")