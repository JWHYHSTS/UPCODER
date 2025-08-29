'''
Số có dạng z = a + bi, gọi là số phức. Trong đó a gọi là phần thực (real), còn b gọi là phần ảo (image).

|z| = sqrt(a2 + b2), gọi là mô-đun của số phức z

Cho hai số phức z1 = a + bi, z2 = c + di

Cộng, trừ số phức: z1 + z2 = (a+c) + (b+d)i

Trừ số phức: z1 - z2 = (a-c) + (b-d)i
Xây dựng cấu trúc mô tả một dãy N (0 <= N <= 10,000) số phức với các thao tác sau:

a)     Tính tổng N số phức

b)    Tính hiệu N số phức

c)     Tính mô-đun N số phức

d)    Xuất N số phức theo định dạng: z = a + bi (với a là phần thực và b là phần ảo)

 

Yêu cầu: sử dụng kĩ thuật cấp phát động và con trỏ để quản lý dãy số. Bài làm không đúng yêu cầu sẽ không được tính điểm.

 

Input:

-       N dòng, mỗi dòng là 1 cặp a và b mô tả thông tin phần thực và phần ảo của 1 số phức.

Output:

-       Dòng 1: xuất N số phức theo định dạng {a+bi}, mỗi số phức cách nhau 1 khoảng trắng;

-       Dòng 2: giá trị mô-đun của N số phức, lấy tối đa 2 số lẻ ở phần thập phân, mỗi giá trị cách nhau 1 khoảng trắng;

-       Dòng 3: xuất tổng N số phức


Ví dụ 1:
Input	
1 2
3 4
Output
{1+2i} {3+4i} 
2.24 5.00 
{4+6i}

Ví dụ 2:
Input	
0 -2
3 4
1 1
1 -1
-2 0
Output
{-2i} {3+4i} {1+i} {1-i} {-2} 
2.00 5.00 1.41 1.41 2.00 
{3+2i}
'''

import math

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def modulus(self):
        return round(math.sqrt(self.real**2 + self.imag**2), 2)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        r, i = self.real, self.imag
        if r == 0 and i == 0:
            return "{0}"
        elif r == 0:
            return f"{{{i}i}}"
        elif i == 0:
            return f"{{{r}}}"
        elif i > 0:
            return f"{{{r}+{i}i}}"
        else:
            return f"{{{r}{i}i}}"

try:
    complex_list = []
    while True:
        line = input()
        if not line.strip():
            break
        a, b = map(int, line.strip().split())
        complex_list.append(Complex(a, b))
except EOFError:
    pass

ptr = complex_list[:]

print(' '.join(str(z) for z in ptr))
print(' '.join(f"{z.modulus():.2f}" for z in ptr))

total = Complex(0, 0)
for z in ptr:
    total += z
print(str(total))