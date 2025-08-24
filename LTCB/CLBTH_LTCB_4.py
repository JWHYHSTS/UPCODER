'''
Biết rằng giá tiền điện được tính như sau:

- từ KW thứ 1 đến 50 giá 1678 đồng/KW.

- từ KW thứ 51 đến 100 giá 1734 đồng/KW.

- từ KW thứ 101 đến 200 giá 2014 đồng/KW.

- từ KW thứ 201 đến 300 giá 2536 đồng/KW.

- từ KW thứ 301 đến 400 giá 2834 đồng/KW.

- từ KW thứ 401 trở đi giá 2937 đồng/KW.

Cho một số nguyên x là số KW điện tiêu thụ của một hộ gia đình. Tính số tiền điện mà hộ gia đình đó phải trả.
Input:
Gồm một số nguyên dương x duy nhất.
Output:
Số tiền phải trả theo đơn vị đồng.
Ví dụ:
Input
10
Output
16780
'''

n = int(input().strip())
if n <= 50:
    print(n * 1678)
elif n <= 100:
    print(50 * 1678 + (n - 50) * 1734)
elif n <= 200:
    print(50 * 1678 + 50 * 1734 + (n - 100) * 2014)
elif n <= 300:
    print(50 * 1678 + 50 * 1734 + 100 * 2014 + (n - 200) * 2536)
elif n <= 400:
    print(50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + (n - 300) * 2834)
else:
    print(50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + 100 * 2834 + (n - 400) * 2937)