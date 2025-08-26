'''
Hình Học 

xây dựng cấu trúc DIEM (điểm) để lưu trữ điểm trong toạ độ Oxy 
Viết quá tải toán tử nhập ( >> ) , xuất ( << ) điểm (xuất toạ độ điểm theo dạng (x, y))
viết quá tải toán tử so sánh bằng ( == ) để kiểm tra 2 điểm có trùng nhau không 
viết quá tải toán tử trừ ( - ) để tính khoảng cách giữa 2 điểm 
Xây dựng cấu trúc HCN (hình chữ nhật) để lưu trữ toạ độ điểm của 4 đỉnh của hình chữ nhật
Viết quá tải toán tử nhập ( >> ) , xuất ( << ) hình chữ nhật
viết hàm tính diện tích HCN 
Viết quá toán tử cộng ( + ) để tính tổng diện tích của 2 HCN
Viết quá tải so sánh nhỏ hơn ( < ), lớn hơn ( > ) để so sánh diện tích giữa 2 HCN
Xây dựng cấu trúc TGV (tam giác vuông) để lưu trữ toạ độ điểm của 3 đỉnh của tam giác vuông
Viết quá tải toán tử nhập ( >> ), xuất ( << ) tam giác vuông 
viết hàm tính diện tích tam giác vuông 
Viết quá toán tử cộng ( + ) để tính tổng diện tích của 2 TGV
Viết quá tải so sánh nhỏ hơn ( < ), lớn hơn ( > ) để so sánh diện tích giữa 2 TGV
Xây dựng cấu trúc HT (hình tròn) để lưu trữ toạ độ điểm của tâm và bán kính hình tròn
Viết quá tải toán tử nhập ( >> ) , xuất ( << ) hình tròn (xuất theo dạng (x, y, r) ,với x,y là toạ độ tâm và r là bán kính) 
viết hàm tính diện tích hình tròn
Viết quá toán tử cộng ( + ) để tính tổng diện tích của 2 HT
Viết quá tải so sánh nhỏ hơn ( < ), lớn hơn ( > ) để so sánh diện tích giữa 2 HT

dữ liệu nhập từ file "HINH.inp": toạ độ điểm của HCN và TGV đảm bảo theo chiều kim đồng hồ theo đùng thứ tự các đỉnh
dòng 1 : toạ độ 4 đỉnh hình chữ nhật 1 
dòng 2 : toạ độ 4 đỉnh hình chữ nhật 2 
dòng 3 : toạ độ 3 đỉnh tam giác vuông 1
dòng 4 : toạ độ 3 đỉnh tam giác vuông 2
dòng 5 : toạ độ tâm và bán kính hình tròn 1 
dòng 6 : toạ độ tâm và bán kính hình tròn 2

dữ liệu xuất ra file "HINH.out":
dòng 1: xuất ra toạ độ HCN 1 và 2 ,mỗi phần tử cách nhau 1 khoảng trắng
dòng 2: xuất ra toạ độ TGV 1 và 2 ,mỗi phần tử cách nhau 1 khoảng trắng
dòng 3: xuất ra toạ độ HT 1 và 2 ,mỗi phần tử cách nhau 1 khoảng trắng
dòng 4 : xuất tổng diện tích của 2 HCN
dòng 5 : xuất tổng diện tích của 2 TGV
dòng 6 : xuất tổng diện tích của 2 HT
dòng 7: Nếu HCN 1 có diện tích nhỏ hơn HCN 2 thì xuất ra "1 < 2", Nếu HCN 1 có diện tích bằng HCN 2 thì xuất ra "1 = 2", Nếu HCN 1 có diện tích lớn hơn HCN 2 thì xuất ra "1 > 2",
dòng 8: Nếu TGV 1 có diện tích nhỏ hơn TGV 2 thì xuất ra "1 < 2", Nếu TGV 1 có diện tích bằng TGV 2 thì xuất ra "1 = 2", Nếu TGV 1 có diện tích lớn hơn TGV 2 thì xuất ra "1 > 2",
dòng 9: Nếu HT 1 có diện tích nhỏ hơn HT 2 thì xuất ra "1 < 2", Nếu HT 1 có diện tích bằng HT 2 thì xuất ra "1 = 2", Nếu HT 1 có diện tích lớn hơn HT 2 thì xuất ra "1 > 2"
Các diện tích lấy 2 chữ số phần thập phân.
Ví dụ:

HINH.inp
1 1 1 5 3 5 3 1
1 -1 1 -4 3 -4 3 -1
0 0 0 4 2 0
0 0 -2 0 0 4
0 0 2
0 0 3

HINH.out
(1, 1) (1, 5) (3, 5) (3, 1) (1, -1) (1, -4) (3, -4) (3, -1)
(0, 0) (0, 4) (2, 0) (0, 0) (-2, 0) (0, 4)
(0, 0, 2) (0, 0, 3)
14.00
8.00
40.84
1 > 2
1 = 2
1 < 2

'''
import math

class DIEM:
    __slots__ = ("x", "y")
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)
    @classmethod
    def from_pair(cls, x, y):
        return cls(x, y)
    def __sub__(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)
    def __eq__(self, other):
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)
    def __str__(self):
        if self.x.is_integer() and self.y.is_integer():
            return f"({int(self.x)}, {int(self.y)})"
        return f"({self.x}, {self.y})"

class HCN:
    def __init__(self, points):
        self.points = points  # list[DIEM] length 4 in order
    @classmethod
    def from_flat(cls, nums):
        pts = [DIEM(nums[i], nums[i+1]) for i in range(0, 8, 2)]
        return cls(pts)
    def area(self):
        # Shoelace
        s = 0.0
        for i in range(4):
            x1,y1 = self.points[i].x, self.points[i].y
            x2,y2 = self.points[(i+1)%4].x, self.points[(i+1)%4].y
            s += x1*y2 - x2*y1
        return abs(s)/2.0
    def __add__(self, other):
        return self.area() + other.area()
    def __lt__(self, other):
        return self.area() < other.area() - 1e-9
    def __eq__(self, other):
        return math.isclose(self.area(), other.area(), rel_tol=1e-9, abs_tol=1e-9)
    def __gt__(self, other):
        return self.area() > other.area() + 1e-9
    def __str__(self):
        return " ".join(str(p) for p in self.points)

class TGV:
    def __init__(self, points):
        self.points = points  # list[DIEM] length 3
    @classmethod
    def from_flat(cls, nums):
        pts = [DIEM(nums[i], nums[i+1]) for i in range(0, 6, 2)]
        return cls(pts)
    def area(self):
        x1,y1 = self.points[0].x, self.points[0].y
        x2,y2 = self.points[1].x, self.points[1].y
        x3,y3 = self.points[2].x, self.points[2].y
        return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))/2.0
    def __add__(self, other):
        return self.area() + other.area()
    def __lt__(self, other):
        return self.area() < other.area() - 1e-9
    def __eq__(self, other):
        return math.isclose(self.area(), other.area(), rel_tol=1e-9, abs_tol=1e-9)
    def __gt__(self, other):
        return self.area() > other.area() + 1e-9
    def __str__(self):
        return " ".join(str(p) for p in self.points)

class HT:
    def __init__(self, center, r):
        self.center = center
        self.r = float(r)
    @classmethod
    def from_flat(cls, nums):
        return cls(DIEM(nums[0], nums[1]), nums[2])
    def area(self):
        return math.pi * self.r * self.r
    def __add__(self, other):
        return self.area() + other.area()
    def __lt__(self, other):
        return self.area() < other.area() - 1e-9
    def __eq__(self, other):
        return math.isclose(self.area(), other.area(), rel_tol=1e-9, abs_tol=1e-9)
    def __gt__(self, other):
        return self.area() > other.area() + 1e-9
    def __str__(self):
        cx, cy = self.center.x, self.center.y
        if cx.is_integer() and cy.is_integer() and float(self.r).is_integer():
            return f"({int(cx)}, {int(cy)}, {int(self.r)})"
        return f"({cx}, {cy}, {self.r})"

def cmp_str(a1, a2):
    if a1 < a2:
        return "1 < 2"
    if a1 == a2:
        return "1 = 2"
    return "1 > 2"

def format_area(val):
    return f"{val:.2f}"

def read_input(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    nums = [list(map(float, line.split())) for line in lines]
    rect1 = HCN.from_flat(nums[0])
    rect2 = HCN.from_flat(nums[1])
    tri1  = TGV.from_flat(nums[2])
    tri2  = TGV.from_flat(nums[3])
    cir1  = HT.from_flat(nums[4])
    cir2  = HT.from_flat(nums[5])
    return rect1, rect2, tri1, tri2, cir1, cir2

def write_output(path, rect1, rect2, tri1, tri2, cir1, cir2):
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"{rect1} {rect2}\n")
        f.write(f"{tri1} {tri2}\n")
        f.write(f"{cir1} {cir2}\n")
        f.write(format_area((rect1 + rect2)) + "\n")
        f.write(format_area((tri1 + tri2)) + "\n")
        f.write(format_area((cir1 + cir2)) + "\n")
        f.write(cmp_str(rect1, rect2) + "\n")
        f.write(cmp_str(tri1, tri2) + "\n")
        f.write(cmp_str(cir1, cir2) + "\n")

def main():
    rect1, rect2, tri1, tri2, cir1, cir2 = read_input("HINH.inp")
    write_output("HINH.out", rect1, rect2, tri1, tri2, cir1, cir2)

if __name__ == "__main__":
    main()