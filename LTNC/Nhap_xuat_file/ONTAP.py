'''
ÔN TẬP CẤU TRÚC, QUÁ TẢI TOÁN TỬ, TEMPLATE

Yêu cầu 1:

Xây dựng cấu trúc PhanSo biểu diễn phân số gồm 2 thành phần a, b trong đó a, b là số không âm.

+ Viết quá tải toán tử nhập và xuất ( >> ; << ) cho cấu trúc trên.

Lưu ý:

Dữ liệu nhập vào ở dạng chuỗi như sau: “1/2” thì ta sẽ được phân số với các thành phần tương ứng: a = 1 và b = 2.
Khi xuất có kiểm tra tính hợp lí. Ví dụ: xuất phân số “2/1”, “1/1”, hoặc “0/3”  đều SAI.

+ Viết quá tải toán tử so sánh ==, <, > để so sánh 2 phân số.

+ Viết quá tải toán tử + để cộng hai phân số. Kết quả trả về là một phân số tối giản.



Yêu cầu 2: Có sử dụng template.

Xây dựng cấu trúc Mảng 1 chiều thực hiện các yêu cầu sau:

+ Viết quả tải nhập (>>), xuất (<<) cho cấu trúc.


+ Viết hàm tongPhanTu tính tổng các phần tử của mảng.

+ Viết hàm phanTuMax tìm phần tử lớn nhất trong mảng.

+ Viết hàm sapXep để sắp xếp mảng 1 chiều. Tham số truyền vào theo tùy chọn ‘<’ là sắp xếp tăng dần, ‘>’ là sắp xếp giảm dần.

Lưu ý: Sử dụng giá trị mặc định là sắp xếp tăng dần.


Ví dụ:

sapXep(m1)      => sắp xếp m1 tăng dần.
sapXep(m1,’<’) => sắp xếp m1 tăng dần.
sapXep(m1,’>’) => sắp xếp m1 giảm dần.

 

Dữ liệu vào:

Dòng 1: 1 ký tự in hoa ( I hoặc F ). Nếu ‘I’ thì  là kiểu số nguyên, ‘F’ là phân số.
Dòng 2: 1 số nguyên dương n là số phần tử của mảng thứ 1.
Dòng 3: n số (số nguyên hoặc phân số tùy vào tùy chọn ở dòng 1), mỗi số cách nhau một khoảng trắng, là các phần tử của mảng thứ 1.
Dòng 4: 1 số nguyên dương n là số phần tử của mảng thứ 2.
Dòng 5: n số (số nguyên hoặc phân số tùy vào tùy chọn ở dòng 1), mỗi số cách nhau một khoảng trắng, là các phần tử của mảng thứ 2.



Dữ liệu xuất:

Dòng 1: xuất mảng 1 vừa nhập
Dòng 2: xuất phần tử lớn nhất của mảng 1 theo mẫu: MAX 1 = X trong đó X là phần tử lớn nhất.
Dòng 3: xuất tổng các phần tử của mảng 1 theo mẫu: SUM 1 = X trong đó X là kết quả tìm được.
Dòng 4:
Nếu là mảng số nguyên thì xuất các phần tử của mảng 1 theo mẫu: tăng dần các phần tử chẵn, tăng dần các phần tử lẻ.
Ví dụ: m1 = {4, 5, 2, 3, 1} thì xuất ra: 2 4 1 3 5

Nếu là mảng phân số thì xuất các phần tử của mảng 1 sau khi đã sắp xếp tăng dần.
Ví dụ: m1 = { 1/2, 1/3, 2/4, 1/5, 4/6 } thì xuất ra: 1/5 1/3 1/2 1/2 2/3

Dòng 5: xuất mảng 2.
Dòng 6: xuất phần tử lớn nhất của mảng 2 theo mẫu: MAX 2 = X trong đó X là phần tử lớn nhất.
Dòng 7: xuất tổng các phần tử của màng 2 theo mẫu: SUM 2 = X trong đó X là kết quả tìm được.
Dòng 8:
Nếu là mảng số nguyên thì xuất các phần tử của mảng 2 theo mẫu: giảm dần các phần tử lẻ, giảm dần các phần tử chẵn.
Ví dụ: m2 = {5, 1, 6, 4, 2, 3} thì xuất ra: 5 3 1 6 4 2


Nếu là mảng phân số thì xuất các phần tử của mảng 2 sau khi đã sắp xếp giảm dần.
Ví dụ: m2 = { 2/3, 1/4, 4/5, 3/6, 2/7, 1/8 } thì xuất ra: 4/5 2/3 1/2 2/7 1/4 1/8

Dòng 9: xuất mảng tổng của mảng 1 và mảng 2 ban đầu.



Ví dụ:

Input
I
5
4 5 2 3 1
6
5 1 6 4 2 3
Output
4 5 2 3 1
MAX 1 = 5
SUM 1 = 15
2 4 1 3 5 
5 1 6 4 2 3
MAX 2 = 6
SUM 2 = 21
5 3 1 6 4 2 
9 6 8 7 3 3
 
Input
F
5
1/2 1/3 2/4 1/5 4/6
6
2/3 1/4 4/5 3/6 2/7 1/8
Output
1/2 1/3 1/2 1/5 2/3
MAX 1 = 2/3
SUM 1 = 11/5
1/5 1/3 1/2 1/2 2/3
2/3 1/4 4/5 1/2 2/7 1/8
MAX 2 = 4/5
SUM 2 = 2207/840
4/5 2/3 1/2 2/7 1/4 1/8
7/6 7/12 13/10 7/10 20/21 1/8

'''

from math import gcd

class PhanSo:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.rut_gon()

    @classmethod
    def from_string(cls, s):
        a, b = map(int, s.strip().split('/'))
        return cls(a, b)

    def rut_gon(self):
        g = gcd(self.a, self.b)
        self.a //= g
        self.b //= g

    def __str__(self):
        if self.b == 1 or self.a == 0 or self.a == self.b:
            return "SAI"
        return f"{self.a}/{self.b}"

    def __add__(self, other):
        tu = self.a * other.b + other.a * self.b
        mau = self.b * other.b
        return PhanSo(tu, mau)

    def __eq__(self, other):
        return self.a * other.b == self.b * other.a

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

    def __gt__(self, other):
        return self.a * other.b > self.b * other.a

class Mang:
    def __init__(self, elements):
        self.ds = elements

    def __str__(self):
        return ' '.join(str(x) for x in self.ds)

    def tong_phan_tu(self):
        total = self.ds[0]
        for x in self.ds[1:]:
            total = total + x
        return total

    def phan_tu_max(self):
        return max(self.ds)

    def sap_xep(self, kieu='<'):
        reverse = kieu == '>'
        self.ds.sort(reverse=reverse)

def sap_xep_int_tang_le_chan(arr):
    chan = sorted([x for x in arr if x % 2 == 0])
    le = sorted([x for x in arr if x % 2 != 0])
    return chan + le

def sap_xep_int_giam_le_chan(arr):
    le = sorted([x for x in arr if x % 2 != 0], reverse=True)
    chan = sorted([x for x in arr if x % 2 == 0], reverse=True)
    return le + chan

def main():
    loai = input().strip()
    n1 = int(input())
    raw1 = input().split()
    n2 = int(input())
    raw2 = input().split()

    if loai == 'I':
        m1 = Mang(list(map(int, raw1)))
        m2 = Mang(list(map(int, raw2)))

        print(m1)
        print(f"MAX 1 = {m1.phan_tu_max()}")
        print(f"SUM 1 = {m1.tong_phan_tu()}")
        print(' '.join(map(str, sap_xep_int_tang_le_chan(m1.ds))))

        print(m2)
        print(f"MAX 2 = {m2.phan_tu_max()}")
        print(f"SUM 2 = {m2.tong_phan_tu()}")
        print(' '.join(map(str, sap_xep_int_giam_le_chan(m2.ds))))

        tong = Mang([m1.ds[i] + m2.ds[i] for i in range(min(len(m1.ds), len(m2.ds)))])
        print(tong)

    elif loai == 'F':
        m1 = Mang([PhanSo.from_string(s) for s in raw1])
        m2 = Mang([PhanSo.from_string(s) for s in raw2])

        print(m1)
        print(f"MAX 1 = {m1.phan_tu_max()}")
        print(f"SUM 1 = {m1.tong_phan_tu()}")
        m1.sap_xep('<')
        print(m1)

        print(m2)
        print(f"MAX 2 = {m2.phan_tu_max()}")
        print(f"SUM 2 = {m2.tong_phan_tu()}")
        m2.sap_xep('>')
        print(m2)

        tong = Mang([m1.ds[i] + m2.ds[i] for i in range(min(len(m1.ds), len(m2.ds)))])
        print(tong)

main()
