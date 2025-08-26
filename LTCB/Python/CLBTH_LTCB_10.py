'''
Cho một số nguyên dương n, hãy chuyển n từ hệ thập phân sang hệ nhị phân.

Input:

Gồm một số nguyên dương n duy nhất (n ≤ 1018).

Output:

In ra số n dưới hệ nhị phân.

Ví dụ:
Input
5
Output
101
'''
n = int(input().strip())
print(bin(n)[2:])