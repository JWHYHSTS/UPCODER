'''
Armstrong Numbers 1



Một số nguyên dương có n chữ số được gọi là số Armstrong khi tổng các lũy thừa bậc n của các chữ số của nó bằng chính nó.

Ví dụ:
371 là số Armstrong vì: 3^3 + 7^3 + 1^3 = 371
8208 là số Armstrong vì: 8^4 + 2^4 + 8^4 = 8208
Hãy kiểm tra xem một số nguyên dương N nhập vào từ bàn phím có phải là số Armstrong hay không?
 
Input:
Gồm nhiều dòng, mỗi dòng là một số nguyên dương N (1 <= N <= 10.000.000)
Output:
Gồm nhiều dòng, mỗi dòng là câu trả lời cho từng số N ở trên. Nếu N là số Armstrong thì xuất “YES”. Ngược lại xuất “NO” (không xuất dấu ngoặc kép)
 
Ví dụ:
Input:
371
123
8208
 
Output:
YES
NO
YES

'''
import sys
def is_ams(n):
    s = str(n)
    p = len(s)
    return sum(int(digit) ** p for digit in s) == n

for line in sys.stdin:
    n = int(line.strip())
    print("YES" if is_ams(n) else "NO")