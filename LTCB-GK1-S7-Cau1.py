'''
Câu 1: (2đ)

Nhập vào 3 số nguyên a, b, c. Kiểm tra xem 3 số đó có lập thành 3 cạnh của tam giác không, nếu có hãy tính chu vi của tam giác. Biết: 

· a, b, c tạo tam giác  a>0 và b>0 và c>0 và a+b>c và a+c>b và b+c>a.

· chu vi = a + b + c

Input: 
3 số nguyên, mỗi số các nhau 1 khoảng trắng (a,b,c >0)
Ouput: 
Chu vi của tam giác hoặc NO (nếu đó không phải là tam giác)

Ví dụ:
Input
3 5 6
-3 5 6
1 2 3
Output
14
NO
NO
'''
import sys
nums = list(map(int, sys.stdin.read().strip().split()))
for i in range(0, len(nums), 3):
    if i + 2 >= len(nums):
        break
    a,b,c = nums[i], nums[i+1], nums[i+2]
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        print(a + b + c)
    else:
        print("NO")
