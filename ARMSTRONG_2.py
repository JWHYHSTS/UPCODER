'''
Armstrong Numbers 2

Một số nguyên dương có n chữ số được gọi là số Armstrong khi tổng các lũy thừa bậc n của các chữ số của nó bằng chính nó.

Ví dụ:

371 là số Armstrong vì: 3^3 + 7^3 + 1^3 = 371
8208 là số Armstrong vì: 8^4 + 2^4 + 8^4 = 8208


Hãy tìm tất cả các số Armstrong trong đoạn [A; B].



Input:

Gồm 2 số nguyên dương A, B cách nhau bởi 1 khoảng trắng (1 <= A <= B <= 10^7)

Output:

In ra tất cả các số Armstrong trong đoạn [A;B]. 

Xuất theo thứ tự từ nhỏ đến lớn, mỗi số cách nhau một khoảng trắng.

Nếu trong đoạn [A; B] không có số Armstrong nào thì xuất -1



Ví dụ:

Input	
30 40
Output
-1


Ví dụ:

Input	
300 400
Output
370 371


Ví dụ:

Input	
8000 9000
Output
8208

'''
def is_armstrong(num):
    digits = list(map(int, str(num)))
    n = len(digits)
    return num == sum(d ** n for d in digits)

A, B = map(int, input().split())
result = [str(i) for i in range(A, B + 1) if is_armstrong(i)]

if result:
    print(' '.join(result))
else:
    print(-1)