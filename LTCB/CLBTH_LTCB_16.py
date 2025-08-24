'''
Cho số nguyên dương k, hãy liệt kê tất cả các số nguyên tố từ 1 đến k.

Input:

Gồm một số nguyên dương k duy nhất. (1 < k < 105).

Output:

Gồm nhiều dòng, mỗi dòng lần lượt chứa một số nguyên tố trong đoạn [1, k]. Các số được in theo thứ tự từ bé đến lớn.

Ví dụ:
Input
3
Output
2
3
'''
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input())
for i in range(1, n + 1):
    if snt(i):
        print(i)