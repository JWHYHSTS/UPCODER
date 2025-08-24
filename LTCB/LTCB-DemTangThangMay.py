'''
Bạn T giấu tên đi thang máy ở trường Đại học Khoa học tự nhiên, được biết rằng trường có 11 lầu (từ tầng 1 đến tầng 11). Khi đứng chờ thang máy, bạn T đứng tính xem thang máy sẽ đi bao nhiêu tầng nữa để đến được tầng mà bạn đang đứng, nhưng do bạn T chạy deadline nhiều quá nên không còn khả năng tính nhẩm nữa @@ Vậy nên các bạn hãy lập trình ra một chương trình giúp bạn T làm việc này nhé ^^
Input: 
-Dòng đầu tiên là nhập số tầng bạn T đang đứng
-Dòng thứ hai là nhập số tầng hiện tại của thang máy
-Dòng thứ ba là nhập chiều đi của thang máy, nếu thang máy đang đi lên thì hãy nhập -1, còn nếu thang máy đang đi xuống thì nhập -2.
Output:
-Số tầng thang máy sẽ đi qua để đến được tầng của bạn T
Lưu ý rằng để đổi chiều đi của thang máy thì thang phải đi đến tầng trên cùng hoặc dưới cùng nhé!
Ví dụ
-Bạn T đang đứng ở tầng 5
-Thang máy đang ở tầng 10 và đi lên
Input:
5
10
-1
Output:
7
Giải thích ví dụ trên (Tầng 10 ->tầng 11->tầng 10->tầng 9->tầng8->tầng 7->tầng 6->tầng 5).
Tổng cộng thang máy đi qua 7 tầng nữa để đến được tầng bạn T.
À mà trường mình không có tầng 12 đâu nhe nên nhập sai thì xuất ra 0 ha.
Chúc bạn thành công nhé !

'''

def solve():
    try:
        target = int(input().strip())
        current = int(input().strip())
        direction = int(input().strip())
    except:
        print(0); return
    if not (1 <= target <= 11 and 1 <= current <= 11 and direction in (-1, -2)):
        print(0); return
    if target == current:
        print(0); return
    if direction == -1:  # going up
        if target > current:
            print(target - current)
        else:
            print((11 - current) + (11 - target))
    else:  # direction == -2 (going down)
        if target < current:
            print(current - target)
        else:
            print((current - 1) + (target - 1))
solve()