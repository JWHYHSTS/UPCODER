'''
Có a chiếc kẹo và b em bé. Hãy viết chương trình nhập 2 số nguyên dương a, b và kiểm tra a chiếc kẹo có chia đều được cho b em bé hay không. Giá trị a, b không vượt quá 1018. Hãy thông báo ra “Co” hoặc “Khong”.
Input:
Gồm hai số nguyên lần lượt là a và b.
Output:
In ra “Co” nếu a kẹo có thể chia đều cho b bé, ngược lại in ra “Khong”.
Ví dụ:
Input
12 4
Output
Co

'''
a, b = map(int, input().strip().split())
if a % b == 0:
    print("Co")
else:
    print("Khong")