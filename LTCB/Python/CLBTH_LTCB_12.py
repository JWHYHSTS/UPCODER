'''
Cho ba số a, b, c. Hãy kiểm tra xem ba số có thể tạo thành một cấp số nhân hay không.

Input:

Gồm một dòng chứa ba số nguyên dương a, b, c.

Output:

In ra YES nếu ba số tạo được một cấp số nhân, ngược lại in ra NO.

Ví dụ:
Input
1 9 3
Output
YES
'''
a, b, c = map(int, input().strip().split())
if b * b == a * c:
    print("YES")
else:
    print("NO")