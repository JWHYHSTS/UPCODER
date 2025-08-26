'''
Viết chương trình tính tiền khách hàng cho một quán Karaoke với dữ liệu nhập vào

là giờ bắt đầu, giờ kết thúc và in ra số tiền khách phải trả, biết rằng 8 ≤ giờ bắt đầu

≤ giờ kết thúc ≤ 24 và:

·        Mỗi giờ trong 3 giờ đầu tiên tính 30,000đ/giờ

·        Mỗi giờ tiếp theo có đơn giá giảm 30% so với đơn giá trong 3 giờ đầu tiên.

Ví dụ:


Input
8 10
9 9.5
14 24
Output
60000
15000
237000
'''
import sys

RATE_FIRST = 30000
RATE_LATER = int(RATE_FIRST * 0.7)  # 21000

tokens = sys.stdin.read().strip().split()
for i in range(0, len(tokens), 2):
    if i + 1 >= len(tokens):
        break
    start = float(tokens[i])
    end = float(tokens[i + 1])
    hours = end - start
    if hours <= 0:
        print(0)
        continue
    first = min(hours, 3.0)
    later = max(0.0, hours - 3.0)
    total = first * RATE_FIRST + later * RATE_LATER
    print(int(total))