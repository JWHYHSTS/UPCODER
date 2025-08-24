'''
Nhập vào 2 số nguyên a,b (a,b>0). Xác định xem a và b có phải là 2 số nguyên tố cùng nhau hay không? (Hai số nguyên tố cùng nhau là 2 số có UCLN bằng 1. Kết quả là Yes nếu a và b là 2 số nguyên tố cùng nhau, ngược lại là No.
Input: 5 7
Output: Yes
'''
import math

a, b = map(int, input().split())
if math.gcd(a, b) == 1:
    print("Yes")
else:
    print("No")