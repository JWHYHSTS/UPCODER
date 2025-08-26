'''
Cho số dòng và cột của 1 ma trận 2 chiều, cùng giá trị từng phần tử của ma trận đó.
Tính tổng các phần tử trong ma trận.
Input: 3 3 0 1 2 3 4 5 6 7 8 
Output: 36
(ghi chú: ma trận 2 chiều 3x3, giá trị từng phần tử là 0,1,2,3,4,5,6,7,8)

'''
nums = list(map(int, input().split()))
r, c = nums[0], nums[1]
values = nums[2:2 + r * c]
print(sum(values))