'''
Bài toán Josephus là một trong những bài toán rất nổi tiếng, ra đời từ rất sớm, khoảng năm 370 sau công nguyên bởi Aurelius Ambrosius, là một Tiến sĩ Hội thánh sống vào khoảng năm 340 đến 397 sau công nguyên. Ông cũng được xem là vị thánh bảo trợ của thành phố Milan, nước Ý.

Bài toán đưa ra bởiAmbrôsiô như sau: Titus Flavius Vespasianus là một vị tướng lãnh đạo quân đội tài năng, người về sau đã trở thành hoàng đế La Mã (từ năm 69 đến năm 79), đã cùng với quân đội dưới sự chỉ huy của ông ta dập tắt cuộc nổi loạn của người Do Thái chống lại đế quốc La Mã. Trong cuộc vây hãm Yodfat, Vespasian đã bắt được Flavius Josephus, một nhà lãnh đạo kháng chiến của người Do Thái. Sau khi bắt được các tù nhân Do Thái, người La Mã quyết định xử tử tù nhân bằng cách cho toàn bộ xếp thành vòng tròn và bắt đầu đếm từ một, cứ người nào đến 3 là bị giết cho đến khi chỉ còn lại 1 người. Trước yêu cầu khắc nghiệt như trên, Josephus đã nhanh chóng tìm ra vị trí để mình và người bạn thân không bị giết. Hỏi rằng ông đã chọn vị trí nào cho ông?

Bài toán cần giải:
Cho N người đứng thành vòng tròn và số M (ở đây cho dễ ta sẽ giả sử M < N). Bắt đầu từ người số 1, anh ta sẽ đếm 1, người bên trái anh ta đếm 2, ... cho tới người đếm M sẽ tự động bước ra khỏi vòng tròn đó và người bên trái anh ta tiếp tục đếm lại 1 ... Cứ thế cho tới khi vòng không còn người nào. Xuất thứ tự người ra khỏi vòng tròn.
Ví dụ: với N = 9, M=7 thì thứ tự sẽ là: 7  5  4  6  9  3  8  1 2

'''
from collections import deque
import sys

def josephus_order(n: int, m: int):
    dq = deque(range(1, n + 1))
    order = []
    while dq:
        dq.rotate(-(m - 1))   
        order.append(dq.popleft())
    return order

def main():
    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        print("Need N and M")
        return
    n, m = map(int, data[:2])
    if n <= 0 or m <= 0:
        print("Invalid")
        return
    order = josephus_order(n, m)
    print(" ".join(map(str, order)))

if __name__ == "__main__":
    main()