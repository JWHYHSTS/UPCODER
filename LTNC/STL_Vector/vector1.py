'''
Nhập vào một dãy số dùng vector.
yêu cầu dùng iterator để xuất ra màn hình
- Dòng 1 xuất theo chiều thuận (từ begin() đến end() )
- Dòng 2 xuất theo chiều ngược (từ rbegin() đến rend() )

Ví dụ:

Input
1 2 3
Output
1 2 3
3 2 1
'''
nums = list(map(int, input().split()))

for it in iter(nums):
    print(it, end=' ')
print()

for rit in reversed(nums):
    print(rit, end=' ')
print()