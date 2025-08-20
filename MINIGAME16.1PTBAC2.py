'''
Cho phương trình bậc hai: Ax2 + Bx + C = 0

Yêu cầu: Xác định xem phương trình trên có bao nhiêu nghiệm và xuất các nghiệm đó theo thứ tự tăng dần.

Input:
3 số nguyên A, B, C (-105 <= A, B, C <= 105). Lưu ý: Các hệ số có thể bằng 0
Output:
Dòng đầu tiên:
Nếu phương trình có vô số nghiệm thì xuất -1
Nếu phương trình vô nghiệm thì xuất 0
Ngược lại: Xuất số nghiệm của phương trình. Các dòng tiếp theo xuất các nghiệm của phương trình theo thứ tự tăng dần.
Lưu ý: Xuất "chính xác" nghiệm của phương trình với 10 chữ số thập phân sau dấu phẩy.
Bài này hệ thống có "cờ" chấm theo định dạng chính xác của output. Thiếu một số "0" cũng là sai kết quả.

Ví dụ:
Input
1 -5 6
Output
2
2.0000000000
3.0000000000

Input
0 -2 0
Output
1
0.0000000000
'''
a, b, c = map(int, input().split())

def format_num(x):
    return "{0:.10f}".format(0.0 if abs(x) < 1e-12 else x)

if a == 0:
    if b == 0:
        print(-1 if c == 0 else 0)
    else:
        x = -c / b
        print(1)
        print(format_num(x))
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print(0)
    elif abs(delta) < 1e-12:
        x = -b / (2 * a)
        print(1)
        print(format_num(x))
    else:
        sqrt_delta = delta ** 0.5
        x1 = (-b + sqrt_delta) / (2 * a)
        x2 = (-b - sqrt_delta) / (2 * a)
        x1, x2 = sorted([x1, x2])
        print(2)
        print(format_num(x1))
        print(format_num(x2))
