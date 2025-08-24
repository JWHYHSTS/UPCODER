'''
Câu 5: (1đ)

Viết chương trình tính tiền khách hàng cho một quán Karaoke với dữ liệu nhập vào là giờ bắt đầu, giờ kết thúc và in ra số tiền khách phải trả, biết rằng 8 ≤ giờ bắt đầu ≤ giờ kết thúc ≤ 24 và:

·      Mỗi giờ trong 3 giờ đầu tiên tính 30,000đ/giờ

·      Mỗi giờ tiếp theo có đơn giá giảm 30% so với đơn giá trong 3 giờ đầu tiên

Input:

Nhập 2 số nguyên giobatdau và gioketthuc cách nhau khoảng trắng.

Output:

In ra màn hình số tiền phải trả

Ví dụ:
Input
10 12
10 14
Output
60000
111000
'''
start, end = map(int, input().split())

rate_first = 30000
rate_later = 21000  # 30000 * 70%

hours = end - start
if hours <= 0:
    print(0)
else:
    first = min(hours, 3)
    later = max(0, hours - 3)
    total = first * rate_first + later * rate_later
    print(total)
