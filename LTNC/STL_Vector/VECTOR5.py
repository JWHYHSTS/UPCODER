'''
Cho một vector các số nguyên, hãy đếm số phần tử và xuất các phần tử có giá trị lớn hơn giá trị trung bình của vector đó.

Input:

Dòng đầu tiên: số nguyên n (1 ≤ n ≤ 100) là số phần tử trong vector.

Dòng thứ hai: n số nguyên, mỗi số có giá trị từ -109 đến 109.

Output:

In ra số lượng phần tử và các phần tử có giá trị lớn hơn trung bình của vector  .

      Nếu không có phần tử nào thì in ra -1 

      Yêu cầu : sử dụng vector 

Ví dụ 1: 

Input
5
1 2 3 4 5
Output
2
4 5



Ví dụ 2:

Input
10
2 2 2 2 2 2 2 2 2 2
Output
0
-1

'''
import sys
data=list(map(int,sys.stdin.read().strip().split()))
if not data: sys.exit()
n=data[0]
arr=data[1:1+n]
avg=sum(arr)/n
greater=[x for x in arr if x>avg]
print(len(greater))
if greater:
    print(" ".join(map(str,greater)))
else:
    print(-1)