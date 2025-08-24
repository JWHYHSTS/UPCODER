'''
Tính tiền quán Karaoke


Một quán Kara tính tiền khách hàng theo công thức sau: 
    + Mỗi giờ trong 3 giờ đầu tiên sẽ tính theo đơn giá mà cửa hàng nhập vào.
    + Mỗi giờ tiếp theo đơn giá sẽ giảm 30% so với đơn giá gốc.
    + Ngoài ra trong khung giờ 8h-17h được giảm 10% trên tổng số tiền.
    + Viết chức năng nhập vào đơn giá, nhập vào giờ bắt đầu, giờ kết thức. In ra số tiền phải trả.
    + Biết rằng quán kara mở quán lúc 8h và đóng lúc 24h.

Input: n(đơn giá), s(giờ bắt đầu), e(giờ kết thúc).

Output: Số tiền phải trả, nếu giờ hoặc số tiền không thỏa mãn xuất ra -1.

Giải thích testcase: 
Từ 10h - 22h, đơn giá 7000, từ 10h-22h sẽ phân ra hai chặng là từ 10h - 17h và 17h - 22h. 3 tiếng đầu là từ 10h - 13h tính giá bình thường là 3 * 7000, từ 13h - 17h tính giá giám cho mỗi đơn giá là 4 * 7000 * 70%. Lúc này khung giờ từ 10h - 17h sẽ được giảm giá 10% trên tổng số giờ này, tức (3*7000 + 4*7000 * 70%) * 90%. Tiếp tục là mốc 2 là từ 17h-22h thì sẽ tiếp tục tính đơn giá giảm 30% nhưng không giảm giá 10% trên tổng số tiền khoảng thời gian này, tức 5*7000*70% cho khoảng thời gian từ 17h-22h. Cuối cùng số tiền từ 10h-22h là tổng số tiền của hai chặng thời gian trên.

'''
import sys, math
data = sys.stdin.read().strip().split()
if len(data) != 3:
    print(-1); sys.exit()
try:
    rate = float(data[0]); s = float(data[1]); e = float(data[2])
except:
    print(-1); sys.exit()
if rate <= 0 or s < 8 or e > 24 or s >= e:
    print(-1); sys.exit()
dur = e - s
full = min(3.0, dur)
red = max(0.0, dur - 3.0)
t_full_end = s + full
def ov(a1,a2,b1,b2):
    x=max(a1,b1); y=min(a2,b2); return max(0.0, y-x)
b17_full = ov(s, t_full_end, 8.0, 17.0)
a17_full = full - b17_full
b17_red = ov(t_full_end, e, 8.0, 17.0)
a17_red = red - b17_red
cost_b17 = b17_full*rate + b17_red*rate*0.7
cost_a17 = a17_full*rate + a17_red*rate*0.7
total = cost_b17*0.9 + cost_a17
print(int(round(total)))