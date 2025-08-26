'''
Đọc một dãy số không cho trước số lượng phần tử, sau đó hãy xác định số lượng phần tử của dãy, tính tổng và sắp xếp từ bé đến lớn.
Nếu số lượng phần tử chưa tới 3 thì xuất ra "NO" (không có ngoặc kép)
Ví dụ:
Input:
5 4 3 2 1

Output:
5
15
1 2 3 4 5

'''

mang = list(map(int, input().split()))
if len(mang) < 3:
    print("NO")
else:
    print(len(mang))
    print(sum(mang))
    print(*sorted(mang)) # Sorted trong python dùng để sắp xếp mảng theo thứ tự tăng dần, còn reversed=True sẽ sắp xếp theo thứ tự giảm dần
    print(*reversed(mang))