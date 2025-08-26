'''
Nhập vào các điểm tọa độ OXY.Bạn hãy đếm xem có bao nhiêu đường thẳng song song với trục OX và OY ( 2 điểm bất kỳ nối lại sẽ tạo 1 đường thẳng )
Lưu ý : 1 điểm thì không phải là 1 đường thẳng , nếu 1 đường thẳng nằm trong đường thẳng khác thì sẽ tính đường thẳng dài nhất 

Điều kiện nhập : Không nhập lại tọa độ đã nhập trước đó , tất cả là số nguyên
Input:
Dòng 1 : Nhập vào n
Dòng 2 : Nhập vào xi
Dòng 3 : Nhập vào yi
Output: Theo yêu cầu đề bài

'''
import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
if len(data) < 1 + 2 * n:
    sys.exit()

xs = data[1:1+n]
ys = data[1+n:1+2*n]

count_ox = 0
freq_y = {}
for y in ys:
    freq_y[y] = freq_y.get(y, 0) + 1
for v in freq_y.values():
    if v >= 2:
        count_ox += 1

count_oy = 0
freq_x = {}
for x in xs:
    freq_x[x] = freq_x.get(x, 0) + 1
for v in freq_x.values():
    if v >= 2:
        count_oy += 1

print(count_ox, count_oy)