'''
Cho số nguyên dương n. Hãy đưa ra số lượng chữ số của n và tổng các chữ số trong biểu diễn thập phân của n.

Input:

Gồm một số nguyên dương duy nhất.

Output:

Gồm hai dòng, dòng thứ nhất chứa số chữ số và dòng thứ hai chứa tổng chữ số của n.

Ví dụ:
Input
66
Output
2
12
'''
n = int(input().strip())
count = 0
total = 0
while n > 0:
    digit = n % 10
    total += digit
    count += 1
    n //= 10
print(count)
print(total)