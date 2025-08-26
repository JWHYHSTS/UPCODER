'''
Cho 4 số nguyên không âm a, b, c, d. Hãy tìm số lớn thứ nhì trong 4 số này.

Input:
4 số a, b, c, d. Mỗi số cách nhau 1 khoảng trắng. Giá trị mỗi số không vượt quá 100.
Output:
Số lớn thứ nhì trong 4 số này. Nếu không tồn tại số lớn thứ nhì thì xuất -1.

Ví dụ 1:

Input

Output

2 5 3 1

3


Ví dụ 2:

Input

Output

4 4 1 2

2
'''
a, b, c, d = map(int, input().split())
max1 = max(a, b, c, d)

# Loại bỏ tất cả các số bằng max1
nums = [a, b, c, d]
nums2 = [x for x in nums if x != max1]

if not nums2:
    print(-1)
else:
    max2 = max(nums2)
    print(max2)
