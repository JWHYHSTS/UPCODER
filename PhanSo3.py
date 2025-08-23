'''
xây dựng 1 cấu trúc Phân Số (gồm tử và mẫu là số nguyên) với yêu cầu, xây dựng các hàm sau:
- Nhập, xuất phân số
- Hàm rút gọn.

Viết chương trình nhập vào dãy phân số, yêu cầu tính tổng của các phân số trên (sau khi tối giản)

input:
Gồm nhiều dòng, mỗi dòng gồm 2 số nguyên là tử và mẫu của 1 phân số

output: phân số tổng sau khi rút gọn

Ví dụ:

input
1 2
2 4
output
1/1 

'''

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

class PhanSo:
    def __init__(self, tu = 0, mau = 1):
        self.tu = tu
        self.mau = mau
        self.rut_gon()
    
    def rut_gon(self):
        ucln = gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln
        if self.mau < 0:
            self.tu = -self.tu
            self.mau = -self.mau
    
    def __lt__(self, other):
        return self.tu * other.mau < self.mau * other.tu
    
    def __str__(self):
        return f"{self.tu}/{self.mau}"
    
    def __add__(self, other):
        tu_moi = self.tu * other.mau + other.tu * self.mau
        mau_moi = self.mau * other.mau
        return PhanSo(tu_moi, mau_moi)
            
def nhap():
    # tu, mau = map(int, input().split())
    # return PhanSo(tu, mau)
    try:
        tu, mau = map(int, input().split())
        return PhanSo(tu, mau)
    except ValueError:
        print("Input không hợp lệ. Vui lòng nhập lại.")
        return nhap()

def main():
    # N = int(input())
    # phan_so_list = [nhap() for _ in range(N)]
    # phan_so_min = min(phan_so_list)
    # print(phan_so_min)
    import sys
    tong = None
    for line in sys.stdin:
        if not line.strip():
            continue
        tu, mau = map(int, line.strip().split())
        ps = PhanSo(tu, mau)
        if tong is None:
            tong = ps
        else:
            tong = tong + ps
    if tong:
        print(tong)
if __name__ == "__main__":
    main()
