'''
xây dựng 1 cấu trúc Phân Số (gồm tử và mẫu là số nguyên) với yêu cầu, xây dựng các hàm sau:
- Nhập, xuất phân số
- Hàm rút gọn.

Viết chương trình nhập vào nhiều phân số, yêu cầu tìm phân số nhỏ nhất trong các phân số trên (sau khi tối giản)

input:
- Gồm nhiều dòng, mỗi dòng gồm 2 số nguyên là tử và mẫu của 1 phân số

output: phân số nhỏ nhất (sau khi rút gọn)

Ví dụ:

input
1 2
2 4
output
1/2

'''

from math import gcd
import sys

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
        self.rut_gon()

    def rut_gon(self):
        if self.mau < 0:
            self.tu = -self.tu
            self.mau = -self.mau
        ucln = gcd(abs(self.tu), abs(self.mau))
        self.tu //= ucln
        self.mau //= ucln

    def __lt__(self, other):
        return self.tu * other.mau < other.tu * self.mau

    def __str__(self):
        return f"{self.tu}/{self.mau}"

def nhap_phan_so():
    try:
        while True:
            line = input()
            if not line.strip():
                break
            tu, mau = map(int, line.strip().split())
            yield PhanSo(tu, mau)
    except EOFError:
        return

def main():
    phan_sos = list(nhap_phan_so())
    if not phan_sos:
        return
    min_ps = min(phan_sos)
    print(min_ps)

if __name__ == "__main__":
    main()