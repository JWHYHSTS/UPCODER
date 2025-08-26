'''
Cho một dãy gồm n số nguyên dương A1, A2, …, An. Một cặp số được gọi là cặp tương đồng với x, nếu cặp số này có tổng bằng số x cho trước nào đó.
Hãy đếm xem trong dãy số A có bao nhiêu cặp số (Ai, Aj) tương đồng với x (có nghĩa là Ai + Aj = x) với i < j.
Input:
Dòng đầu tiên chứa số n và x.
Dòng thứ 2 gồm n số nguyên dương A1, A2, …, An.
Output:
Ghi ra một số nguyên là cặp đôi tương đồng của dãy số.
Ví dụ:

Input
7 6
1 2 4 3 4 5 3
Output
4

'''
n, x = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == x:
            count += 1
print(count)