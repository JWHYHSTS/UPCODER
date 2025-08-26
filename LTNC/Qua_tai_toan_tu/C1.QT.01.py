'''
Xây dựng cấu trúc PhanSo để biểu diễn Phân số trong toán học. Phân số gồm 2 thành phần là tử và mẫu là các số nguyên.

Viết các quá tải toán tử: >> (nhập Phân số), << (xuất Phân số). Xuất phân số theo định dạng: tử/mẫu.
Lưu ý: Phân số phải được rút gọn sao cho mẫu phải luôn dương trước khi tính toán.

Ví dụ: 
Phân số p1 có tử = 2, mẫu = 3 thì xuất: 2/3
Phân số p2 có tử = 3, mẫu = -2 thì xuất: -3/2. Xuất 3/-2 là sai.
Phân số p3 có tử = 4, mẫu = -6 thì xuất: -3/2. Xuất -4/6 hoặc 4/-6 đều sai.

Xây dựng cấu trúc SoPhuc để biểu diễn Số Phức trong toán học. Số phức là biểu thức có dạng: a + bi, với i2 = -1. Trong đó: a là phần thực, b là phần ảo.
Các phép toán cơ bản trong số phức được tính như sau:
(a + bi) + (c + di) = (a + c) + (b + d)i
(a + bi) - (c + di) = (a - c) + (b - d)i
(a + bi) * (c + di) = (ac - bd) + (ad + bc)i

Viết các quá tải toán tử sau:
Quá tải toán tử >> (nhập số phức với phần thực và phần ảo)
Quá tải toán tử << (xuất số phức). Lưu ý khi xuất số phức phải tuân thủ định dạng sau:
Nếu a khác 0 và b khác 0 thì xuất số phức theo định dạng: a  + bi. Nếu |b| = 1 thì không xuất số 1, nếu b < 0 thì không xuất dấu + phía trước b.
Nếu b = 0 thì chỉ xuất phần thực.
Nếu a = 0 thì chỉ xuất phần ảo như định dạng ở trên.
Quá tải phép toán + của số phức để:
Cộng số phức với số phức.
Cộng số phức với một số nguyên (cộng số nguyên đó vào phần thực của số phức).
Cộng số phức với phân số (cộng tử của phân số vào phần thực của số phức, cộng mẫu của phân số vào phần ảo của số phức).
Input:
Dòng 1: Nhập 2 thành phần của số phức x.
Dòng 2: Nhập 1 ký tự trong 3 ký tự sau: ('i', 'z', 'p'). Trong đó 'i' đại diện cho số nguyên, 'z' đại diện cho số phức, 'p' đại diện cho phân số.
Dòng 3: Nhập thông tin của số y (kiểu dữ liệu của số y phụ thuộc vào ký tự nhập vào ở dòng 2).
Output:
Dòng 1: Xuất ra số phức x theo định dạng.
Dòng 2: Xuất ra số y. Nếu y là phân số thì phải rút gọn phân số trước khi xuất.
Dòng 3: Xuất kết quả của phép cộng x + y.
Ví dụ 1:

Input
2 -2
z
1 0
Output
2-2i
1
3-2i


Ví dụ 2:

Input
3 -1
p
2 -1
Output
3-i
-2/1
1
'''

from math import gcd
import sys

class PhanSo:
    def __init__(self, tu: int, mau: int):
        if mau == 0:
            raise ValueError("Mau khong the 0")
        self.tu = tu
        self.mau = mau
        self._rut_gon()
    def _rut_gon(self):
        if self.mau < 0:
            self.tu = -self.tu
            self.mau = -self.mau
        g = gcd(abs(self.tu), self.mau)
        if g:
            self.tu //= g
            self.mau //= g
    def __str__(self):
        return f"{self.tu}/{self.mau}"

class SoPhuc:
    def __init__(self, thuc: int, ao: int):
        self.thuc = thuc
        self.ao = ao
    def __add__(self, other):
        if isinstance(other, SoPhuc):
            return SoPhuc(self.thuc + other.thuc, self.ao + other.ao)
        if isinstance(other, int):
            return SoPhuc(self.thuc + other, self.ao)
        if isinstance(other, PhanSo):
            return SoPhuc(self.thuc + other.tu, self.ao + other.mau)
        return NotImplemented
    __radd__ = __add__
    def __str__(self):
        a, b = self.thuc, self.ao
        if b == 0:
            return str(a)
        if a == 0:
            # only imaginary
            if b == 1: return "i"
            if b == -1: return "-i"
            return f"{b}i"
        # both parts non-zero
        sign = "+" if b > 0 else "-"
        absb = abs(b)
        if absb == 1:
            return f"{a}{sign}i"
        return f"{a}{sign}{absb}i"

def main():
    data = sys.stdin.read().strip().split()
    if len(data) < 4:
        return
    a, b = int(data[0]), int(data[1])
    t = data[2]
    x = SoPhuc(a, b)
    if t == 'i':
        y = int(data[3])
    elif t == 'z':
        if len(data) < 5: return
        y = SoPhuc(int(data[3]), int(data[4]))
    elif t == 'p':
        if len(data) < 5: return
        y = PhanSo(int(data[3]), int(data[4]))
    else:
        return
    print(x)
    print(y)
    print(x + y)

if __name__ == "__main__":
    main()