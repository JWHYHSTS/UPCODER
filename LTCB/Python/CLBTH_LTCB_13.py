'''
Cho một dãy A gồm n số nguyên a1, a2, a3,…, an và hai số nguyên v, T. Hãy tìm cách thêm số T vào vị trí v trong dãy A (các số ban đầu vẫn giữ nguyên thứ tự).

Input:

Dòng thứ nhất gồm ba số nguyên n, v, T.

Dòng tiếp theo gồm n số nguyên a1, a2, a3,…, an.

Output:

In ra dãy n + 1 số (các số cách nhau một khoảng trắng) sau khi thêm số T vào vị trí v.

Ví dụ:
Input
5 2 9
8 6 2 10 5
Output
8 9 6 2 10 5

'''
n, v, T = map(int, input().split())
arr = list(map(int, input().split()))
if v < 1: v = 1
if v > n + 1: v = n + 1
res = arr[:v-1] + [T] + arr[v-1:]
print(" ".join(map(str, res)))