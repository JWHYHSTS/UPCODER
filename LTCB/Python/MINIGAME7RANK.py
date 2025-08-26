'''
Các giải đấu thể thao quốc tế luôn dành một phần thưởng lớn cho các đoàn có thứ hạng cao. Có hai cách để xếp hạng các đoàn:

Cách 1: 
Đoàn nào có tổng số huy chương lớn hơn thì xếp trên
Cách 2: 
Đoàn nào có nhiều huy chương vàng hơn thì xếp trên, nếu bằng nhau thì xét đến huy chương bạc, nếu bằng sẽ xét đến huy chương đồng.

Việt Nam và Thái Lan là hai cường quốc thể thao ở Đông Nam Á. Cho biết số lượng các huy chương của hai đoàn này cùng cách xếp hạng của ban tổ chức, hãy cho biết đội nào xếp trên.

Dữ liệu đầu vào: 
Dòng đầu tiên chứa 6 số nguyên không âm (không vượt quá 200) ghi lại số huy chương vàng, bạc, đồng của Việt Nam và số huy chương vàng, bạc, đồng của Thái Lan
Dòng tiếp theo chứa một số nguyên duy nhất 1 hoặc 2 ghi lại cách xếp hạng của ban tổ chức.

Dữ liệu đầu ra:
Nếu Việt Nam xếp trên thì xuất ra "VN".
Nếu Thái Lan xếp trên thì xuất ra "TL".
Nếu không phân định được thì xuất ra "TIE".

Ví dụ
input
20 15 30 12 24 35
1
output
TL

Ví dụ
input
20 15 30 12 24 35
2
output
VN
'''
a, b, c, d, e, f = map(int, input().split())
rank = int(input())

if rank == 1:
    if a + b + c > d + e + f:
        print("VN")
    elif a + b + c < d + e + f:
        print("TL")
    else:
        print("TIE")
else:
    if a > d:
        print("VN")
    elif a < d:
        print("TL")
    else:
        if b > e:
            print("VN")
        elif b < e:
            print("TL")
        else:
            if c > f:
                print("VN")
            elif c < f:
                print("TL")
            else:
                print("TIE")