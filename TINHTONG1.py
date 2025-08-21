'''
Input: 
1 số nguyên n
ouput: 
kết quả của phép toán: 1+1/23+1/33+...+1/n3 
(kết quả lấy 3 chữ số thập phân)

ví dụ:
input:
3

output:
1.162

'''
n = int(input())
kq = 0
for i in range(1, n + 1):
    kq += 1 / (i ** 3)
print(f"{kq:.3f}")