'''

Trong mùa đông này, Tỷ được giao nhiệm vụ thống kê và báo cáo nhiệt độ của các ngày trong tuần. Việc thống kê thì đã quá dễ dàng vì Tỷ có thể Google và hàng chục triệu kết quả sẽ hiện ra trước mắt. Nhưng còn việc viết báo cáo, vì Tỷ mãi chơi và lười nghĩ nên Tỷ quyết định nhờ các bạn thực hiện công việc hộ Tỷ.

Một bản báo cáo nhiệt độ cần có các thông tin như sau:

- Nhiệt độ của các ngày lạnh hơn 10ºC.

- Nhiệt độ của ngày lạnh nhất và nóng nhất.

Vậy đó, mặc dù biết cổ xúy cho việc lười biếng là không tốt, các bạn hãy giúp Tỷ lần này nhé!

Input:

Gồm bảy số thực, lần lượt là nhiệt độ các ngày trong tuần.

Output:

Dòng thứ nhất in ra nhiệt độ của các ngày lạnh hơn 10ºC. Nếu có nhiều ngày thỏa mãn thì in theo thứ tự ngày trong tuần.

Dòng thứ hai in ra nhiệt độ của ngày lạnh nhất.

Dòng thứ ba in ra nhiệt độ của ngày nóng nhất.

Ví dụ:
Input
12.8 15.3 20.1 15.9 9.0 8.9 12.6 
Output
9 8.9
8.9
20.1


'''

import sys

nums = []
for tok in sys.stdin.read().strip().split():
    try:
        nums.append(float(tok))
    except:
        pass
if len(nums) != 7:
    sys.exit()

def fmt(v: float) -> str:
    return str(int(v)) if v.is_integer() else str(v)

cold = [fmt(v) for v in nums if v < 10]
print(" ".join(cold))
mn = min(nums)
mx = max(nums)
print(fmt(mn))
print(fmt(mx))