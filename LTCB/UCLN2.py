'''
Cho hai số nguyên không âm a và b, hãy tìm ước số chung lớn nhất của a và b.



Dữ liệu nhập:

Gồm 2 số a và b cách nhau một khoảng trắng (0 ≤ a, b ≤ 10^18)

Dữ liệu xuất:

Số nguyên dương duy nhất là ước số chung lớn nhất của a và b.


Ví dụ:

Input
6 9
Output
3

Input
1 10
Output
1
'''
a, b = map(int, input().split())
while b != 0:
    a, b = b, a % b
print(a)
