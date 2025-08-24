'''
Input:
- Gồm nhiều ký tự (mỗi ký tự cách nhau 1 khoảng trắng) 
(chỉ tính các ký tự từ 'a' đến 'z', không tính khoảng trắng)

Output:
- Xuất số lượng các ký tự ra màn hình (xuất theo thứ tự từ nhỏ đến lớn - xem ví dụ để hiểu rõ hơn)

Ví dụ:

input
b a n a n a

output
a:3
b:1
n:2
Giải thích: 
ký tự 'a' xuất hiện 3 lần 
ký tự 'b' xuất hiện 1 lần 
ký tự 'n' xuất hiện 2 lần

'''
s = input().split()
mang = {}
for c in s:
    if 'a' <= c <= 'z':
        mang[c] = mang.get(c, 0) + 1
for k in sorted(mang):
    print(f"{k}:{mang[k]}")