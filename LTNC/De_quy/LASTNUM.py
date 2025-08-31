'''
Một LASTNUM được xác định là tổng các chữ số của số đó, sau đó lại tiếp tục tính tổng các chữ số của số mới tạo ra cho đến khi chỉ còn 1 chữ số duy nhất.

Nhờ bạn hãy giúp tìm ra số cuối cùng đó nhé!

Yêu cầu: Cho số N, bạn hãy tìm LASTNUM của số đó.
Dữ liệu nhập:

  Gồm 1 số nguyên N duy nhất (1 ≤ N ≤ 101000000).

Dữ liệu xuất:

  Gồm 1 số nguyên duy nhất là LASTNUM tìm được.

Ví dụ
input
79
output
7
Các số được tạo ra lần lượt là 79 ➔ 16 ➔  7



Lưu ý: Bài này sự dụng nhập xuất chuẩn (từ bàn phím).

'''

import sys

s = sys.stdin.read().strip()
if not s:
    sys.exit()
s = s.lstrip('0')
if not s:
    print(0)
else:
    r = sum(ord(c)-48 for c in s) % 9
    print(9 if r == 0 else r)