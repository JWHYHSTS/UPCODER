'''
Viết chương trình nhập vào 3 số nguyên là ngày tháng năm. Hãy xác định ngày tháng năm có hợp lệ hay không?
Lưu ý:
- Ngày phải tương ứng với tháng
- Tháng phải từ 1 đến 12
- Năm phải >= 1900
- Năm nhuận là năm chia hết cho 400 hoặc chia hết cho 4 nhưng không chia hết cho 100
Input: 3 số nguyên dương
Output: YES (hợp lệ), NO (không hợp lệ)

Vd:
Input: 28 9 2017
Output: YES
'''

n, t, m = map(int, input().split())

if m < 1900:
    print("NO")
else:
    if t < 1 or t > 12:
        print("NO")
    else:
        if t in [1,3,5,7,8,10,12]:
            if n > 31:
                print("NO")
            else:
                print("YES")
        elif t in [4, 6, 9, 11]:
            if n > 30:
                print("NO")
            else:
                print("YES")
        else:
            if m % 400 == 0 or (m % 4 == 0 and m % 100 != 0):
                if n > 29:
                    print("NO")
                else:
                    print("YES")
            else:
                if n > 28:
                    print("NO")
                else:
                    print("YES")