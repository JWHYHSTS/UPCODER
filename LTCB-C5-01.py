'''
Cho số phần tử và giá trị từng phần tử trong mảng 1 chiều (số phần tử nhỏ hơn 100)
Tính tổng các phần tử trong mảng
Input: 5 0 1 2 3 4
Output: 10
(Ghi chú: 5 phần tử, giá trị từng phần tử là 0, 1, 2, 3, 4)

'''
data = list(map(int, input().split()))
n = data[0]
arr = data[1:1+n]
print(sum(arr))