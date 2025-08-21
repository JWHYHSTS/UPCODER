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
A, B, C = map(int, input().split())

if A == 0:
    if B == 0:
        if C == 0:
            print(-1)
        else:
            print(0)
    else:
        x = -C / B
        print(1)
        print(f"{x:.10f}")
else:
    delta = B * B - 4 * A * C
    if delta < 0:
        print(0)
    elif delta == 0:
        x = -B / (2 * A)
        print(1)
        print(f"{x:.10f}")
    else:
        sqrt_delta = delta ** 0.5
        x1 = (-B - sqrt_delta) / (2 * A)
        x2 = (-B + sqrt_delta) / (2 * A)
        x1, x2 = sorted([x1, x2])
        print(2)
        print(f"{x1:.10f}")
        print(f"{x2:.10f}")