'''
Cho hai số nguyên dương a, n. Tính a^n.   

Input:

Gồm một dòng chứa hai số nguyên dương a và n.

Dữ liệu đảm bảo an luôn luôn nhỏ hơn 1019.

Output:

Giá trị an.

Ví dụ:
Input
2 3
Output
8
'''
a, b = map(int, input().strip().split())
print(a ** b)