'''
Cho một bảng A kích thước n hàng, m cột gồm các số nguyên dương. Hãy đưa ra tổng lớn nhất của một hàng và một cột.

Input:

Dòng đầu tiên chứa hai số n, m.

n dòng tiếp theo, mỗi dòng chứa m số mô tả bảng A.

Các số được nhập vào là các số nguyên dương không vượt quá 1000.

Output:

Dòng thứ nhất in ra tổng lớn nhất của một hàng bảng A.

Dòng thứ hai in ra tổng lớn nhất của một cột bảng A.

Ví dụ:
Input
2 3
2 4 5
9 9 2
Output
20
13

'''
n, m = map(int, input().strip().split())
A = [list(map(int, input().strip().split())) for _ in range(n)]
max_row_sum = max(sum(row) for row in A)
max_col_sum = max(sum(A[i][j] for i in range(n)) for j in range(m))
print(max_row_sum)
print(max_col_sum)