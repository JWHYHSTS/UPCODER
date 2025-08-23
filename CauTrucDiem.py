'''
Xây dựng cấu trúc Diem gồm hoành độ và tung độ để biểu diễn 1 điểm trong mặt phẳng Oxy.
Viết chương trình nhập vào tọa độ 3 điểm A, B, C và thực hiện các yêu cầu sau:
Xuất tọa độ 3 điểm theo định dạng: (hoành độ, tung độ)
Tính độ dài các đoạn thẳng: AB, AC, BC.
Kiểm tra xem 3 điểm A, B, C có thẳng hàng không. 
Nếu thẳng hàng thì xuất kết quả -1
Nếu 3 điểm A, B, C không thẳng hàng thì tính Diện tích và Chu vi của tam giác ABC.
Input:
Dòng 1: 2 số nguyên cách nhau 1 khoảng trắng là tọa độ điểm A.
Dòng 2: 2 số nguyên cách nhau 1 khoảng trắng là tọa độ điểm B.
Dòng 3: 2 số nguyên cách nhau 1 khoảng trắng là tọa độ điểm C.
Giá trị tuyệt đối các số nguyên trong input không vượt quá 100.
Output:
Dòng 1: Xuất tọa độ 3 điểm theo thứ tự: tọa độ A, tọa độ B, tọa độ C. (xuất theo định dạng ở trên - xem ví dụ để biết cách xuất)
Dòng 2: Độ dài đoạn thẳng AB (kết quả lấy 3 chữ số thập phân).
Dòng 3: Độ dài đoạn thẳng AC (kết quả lấy 3 chữ số thập phân).
Dòng 4: Độ dài đoạn thẳng BC (kết quả lấy 3 chữ số thập phân).
Dòng 5: Nếu 3 điểm A, B, C thẳng hàng thì xuất -1. Ngược lại xuất Diện tích và Chu vi của tam giác ABC (kết quả lấy 3 chữ số thập phân).
Ví dụ 1:

Input
1 1
2 2
4 4

Output
(1,1) (2,2) (4,4)
1.414
4.243
2.828
-1


Ví dụ 2:

Input
0 0
3 0
1 2

Output
(0,0) (3,0) (1,2)
3.000
2.236
2.828
3.000 8.064

'''
import math

class Diem:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

def do_dai(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def thang_hang(a, b, c):
    # Kiểm tra bằng định thức: (x2 - x1)*(y3 - y1) == (x3 - x1)*(y2 - y1)
    return (b.x - a.x)*(c.y - a.y) == (c.x - a.x)*(b.y - a.y)

def dien_tich(a, b, c):
    # Công thức Heron
    ab = do_dai(a, b)
    ac = do_dai(a, c)
    bc = do_dai(b, c)
    p = (ab + ac + bc) / 2
    s = math.sqrt(p * (p - ab) * (p - ac) * (p - bc))
    return round(s, 3)

def chu_vi(a, b, c):
    return round(do_dai(a, b) + do_dai(a, c) + do_dai(b, c), 3)

# Nhập dữ liệu
a = Diem(*map(int, input().split()))
b = Diem(*map(int, input().split()))
c = Diem(*map(int, input().split()))

# Xuất tọa độ
print(a, b, c)

# Tính độ dài các đoạn thẳng
ab = do_dai(a, b)
ac = do_dai(a, c)
bc = do_dai(b, c)

print(f"{ab:.3f}")
print(f"{ac:.3f}")
print(f"{bc:.3f}")

# Kiểm tra thẳng hàng
if thang_hang(a, b, c):
    print("-1")
else:
    s = dien_tich(a, b, c)
    p = chu_vi(a, b, c)
    print(f"{s:.3f} {p:.3f}")