'''
Cho 1 mảng các số nguyên. Hãy in ra mảng đó theo thứ tự đảo ngược.

Input:
- Dòng 1: số nguyên N
- Dòng 2: N số nguyên, mỗi số cách nhau 1 khoảng trắng.
Output:
- Mảng xuất theo thứ tự đảo ngược. Lưu ý: nếu mảng không có phần tử thì xuất chữ "NULL"

Ví dụ:
Input: 
5
1 2 3 4 5
Output: 
5 4 3 2 1

'''
n = int(input())
if n == 0:
    print("NULL", end="")   
else:
    nums = []
    while len(nums) < n:      
        nums.extend(map(int, input().split()))
    nums = nums[:n]
    nums.reverse()
    print(" ".join(map(str, nums)), end="") 
