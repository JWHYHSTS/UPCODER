'''
Hàng ngày vào mỗi buổi sáng sớm, Tèo thường rủ Tý ra công viên chạy bộ. Vào một ngày nọ, Tèo thấy vui nên muốn chơi một trò chơi nhỏ với Tý. Tèo chọn 3 gốc cây trong công viên, 3 gốc cây này tạo thành một hình tam giác như hình vẽ:


(Khoảng cách giữa các cây với nhau là tùy ý).

Tèo sẽ bắt đầu chạy từ A đến B, rồi từ B đến C, rồi lại quay về A. Cứ chạy tiếp như vậy. Mỗi giây Tèo chạy được 1 mét. Tèo đố Tý rằng sau t giây kể từ lúc bắt đầu chạy, Tèo đang ở vị trí nào? (Câu trả lời chỉ là ở A, B, C hoặc trên quãng đường AB, BC, CA)
Bạn hãy giúp Tý trả lời câu hỏi này nhé!

Input:
Dòng 1: 3 số nguyên dương là khoảng cách giữa 3 gốc cây (mét). Lần lượt theo thứ tự là AB, BC, CA (mỗi số cách nhau một khoảng trắng).
Dòng 2: số nguyên dương t - thời gian Tèo sẽ chạy.
Output:
Vị trí của Tèo sau t giây (tại A, B, C, hoặc là trên đường AB, BC, CA)

Ví dụ:
Input:
15 10 20
32
Output:
CA
Input:
15 10 20
25
Output:
C
'''
a, b, c = map(int, input().split())
t = int(input())
total = a + b + c
res = t % total

if res == 0 or res == total:
    print("A")
elif res == a:
    print("B")
elif res == a + b:
    print("C")
elif 0 < res < a:
    print("AB")
elif a < res < a + b:
    print("BC")
elif a + b < res < total:
    print("CA")