'''
Viết chương trình sử dụng hàm đệ quy đổi một số n từ hệ thập phân sang hệ nhị phân.
Input: Số nguyên dương n (n<=10^9)
Output: Giá trị số n ở hệ nhị phân. Ví dụ:

Input

Output

123

1111011



'''
import sys
data=sys.stdin.read().strip().split()
if not data: sys.exit()
n=int(data[0])

def bin_repr(x):
    if x == 0:
        return "0"
    return bin_repr(x//2) + str(x%2)

s = bin_repr(n)
# remove leading zeros (can appear due to base case returning "0")
s = s.lstrip('0') or '0'
print(s)