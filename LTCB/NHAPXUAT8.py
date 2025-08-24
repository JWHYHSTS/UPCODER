'''
Input: Nhập vào 3 số nguyên theo định dạng sau:
Dòng 1: 2 số nguyên a và b
Dòng 2: 2 số nguyên c và d
Dòng 3: 2 số nguyên e và f
Output: 
Xuất ra 1 số duy nhất là kết quả của biểu thức: (a+b+c)/(d+e+f)
(Lấy chính xác 1 chữ số thập phân)

Ví dụ:

Input	
1 2
3 4
5 6
Output
0.4
'''
a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
print(round((a + b + c) / (d + e + f), 1))