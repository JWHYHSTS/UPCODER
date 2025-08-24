'''
Ta định nghĩa trung bình cộng của ba số nguyên x1, x2, x3 là (x1 + x2 + x3)/3.

Cho ba số nguyên a, b và x. Hãy tìm số nguyên c sao cho trung bình cộng của ba số a, b, c đúng bằng x.

Input:

Gồm một dòng duy nhất chứa 3 số nguyên a, b và x.

Output:

Số nguyên c cần tìm.

Ví dụ:
Input
2 3 4
Output
7
'''
a, b, x = map(int, input().strip().split())
c = 3 * x - a - b
print(c)