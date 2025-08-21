'''
Viết chương trình in ra màn hình tam giác sao cân với chiều cao h nhập vào từ bàn phím.

Ví dụ 1:

Input	Output
3
__*__
_***_
*****

Ví dụ 2:

Input	Output
5
____*____
___***___
__*****__
_*******_
*********

Ví dụ 3:

Input	Output
6
_____*_____
____***____
___*****___
__*******__
_*********_
***********

Lưu ý: 
Xuất chính xác từng ký tự. Không xuất dư hoặc thiếu khoảng trắng, không xuất dư endl dòng cuối cùng.
Các ký tự gạch nối màu đen (_) ở phía trên đại diện cho khoảng trắng mà các bạn phải xuất ra màn hình. Phải có các khoảng trắng này thì mới được tính là tam giác cân.
'''
h = int(input())
for i in range(h):
    spaces = ' ' * (h - i - 1)
    stars = '*' * (2 * i + 1)
    line = spaces + stars + spaces
    if i != h - 1:
        print(line)
    else:
        print(line, end="")