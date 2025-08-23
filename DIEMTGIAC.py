'''
Yêu cầu 1:  Xây dựng cấu trúc ĐIỂM gồm tung độ và hoành độ (số nguyên)

-      Viết hàm nhập,xuất điểm (xem ví dụ đê hiểu rõ cách xuất hơn)

-      Viết hàm tính khoảng cách giữa 2 điểm

-      Viết hàm kiểm tra 2 điểm có trùng nhau không?

Yêu cầu 2: Xây dựng cấu trúc TAMGIAC gồm 3 điểm (PHẢI dựa vào cấu trúc ĐIỂM ở trên)

-      Viết quá tải hàm nhập,xuất (không cần kiểm tra điều kiện của tam giác, giả sử với 3 điểm bất kỳ đều là tam giác) (xem ví dụ đê hiểu rõ cách xuất hơn)

-      Viết hàm tính chu vi tam giác

-      Viết hàm so sánh chu vi của 2 tam giac.

-      Viết hàm kiểm tra 2 TAM GIÁC có trùng nhau hay không?

Yêu cầu 3: nhập dữ liệu tọa độ của 2 tam giác theo cấu trúc

-      Dòng 1: 3 điểm của tam giác 1

-      Dòng 2: 3 điểm của tam giác 2
Xuất kết quả theo cấu trúc sau:

-      Dòng 1: xuất các tọa độ của tam giác 1

-      Dòng 2: xuất các tọa độ của tam giác 2

-      Dòng 1: ghi TRUE, nếu tam giác 1 có chu vi < chu vi của tam giác 2, ngược lại ghi FALSE

-      Dòng 2: ghi TRUE, nếu 2 tam giác trùng nhau, ngược lại ghi FALSE


Ví dụ:

Input:
1 2 3 4 5 6
7 8 9 0 1 2

 

Output:
(1,2)(3,4)(5,6)
(7,8)(9,0)(1,2)
TRUE
FALSE.

'''
import math

class Diem:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def nhap(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def khoang_cach(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def trung(self, other):
        return self.x == other.x and self.y == other.y

class TamGiac:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return f"{self.A}{self.B}{self.C}"

    def chu_vi(self):
        return self.A.khoang_cach(self.B) + self.B.khoang_cach(self.C) + self.C.khoang_cach(self.A)

    def nho_hon(self, other):
        return self.chu_vi() < other.chu_vi()

    def trung(self, other):
        self_points = {(self.A.x, self.A.y), (self.B.x, self.B.y), (self.C.x, self.C.y)}
        other_points = {(other.A.x, other.A.y), (other.B.x, other.B.y), (other.C.x, other.C.y)}
        return self_points == other_points

data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))

A1 = Diem(data1[0], data1[1])
B1 = Diem(data1[2], data1[3])
C1 = Diem(data1[4], data1[5])
tg1 = TamGiac(A1, B1, C1)

A2 = Diem(data2[0], data2[1])
B2 = Diem(data2[2], data2[3])
C2 = Diem(data2[4], data2[5])
tg2 = TamGiac(A2, B2, C2)

print(tg1)
print(tg2)
print("TRUE" if tg1.nho_hon(tg2) else "FALSE")
print("TRUE" if tg1.trung(tg2) else "FALSE")