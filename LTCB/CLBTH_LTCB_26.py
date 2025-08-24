'''
Cho mảng 1 chiều gồm n phần tử số nguyên. Hãy tính tổng các phần tử trong đoạn từ l đến r.

Input:
Dòng đầu tiên lần lượt là 3 số nguyên n l r.
Dòng tiếp theo chứa n số nguyên a0, a1, a2,… an-1.
Output:
Đáp án của bài toán.
Ví dụ:
Input
5 1 3
1 2 3 4 5 
Output
9

'''
n, l, r = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
print(sum(a[l:r+1]))