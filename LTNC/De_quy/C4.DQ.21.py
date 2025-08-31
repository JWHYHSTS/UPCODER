'''
Bài toán: Đèn giao thông giao nhau

Giả sử bạn đang đứng trước một ngã tư có hai đèn giao thông giao nhau. Mỗi đèn có một chu kỳ hoạt động riêng, bao gồm đèn đỏ, vàng và xanh. Khi một đèn chuyển từ màu này sang màu khác, thời gian chờ đợi bắt đầu tính từ lúc đèn chuyển sang màu đỏ.

Mỗi đèn có các chu kỳ sau:

Đèn 1: Đỏ (3 giây) -> Vàng (2 giây) -> Xanh (5 giây)
Đèn 2: Đỏ (2 giây) -> Vàng (4 giây) -> Xanh (3 giây)
Nhiệm vụ của bạn là tính tổng thời gian chờ đợi khi băng qua đường từ điểm xuất phát của bạn.

'''
def wait_time():
    # Cycle definitions
    r1,y1,g1 = 3,2,5
    r2,y2,g2 = 2,4,3
    cycle1 = r1 + y1 + g1  # 10
    cycle2 = r2 + y2 + g2  # 9

    def is_green1(t):
        x = t % cycle1
        return r1 + y1 <= x < cycle1   # [5,10)
    def is_green2(t):
        x = t % cycle2
        return r2 + y2 <= x < r2 + y2 + g2  # [6,9)

    # recursive search
    def search(t):
        if is_green1(t) and is_green2(t):
            return t
        return search(t+1)
    return search(0)

if __name__ == "__main__":
    print(wait_time())  # prints 6