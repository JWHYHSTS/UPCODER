'''
Một phân số gồm tử  và mẫu (tử và mẫu là 2 số nguyên lớn hơn bằng 0 và bé hơn 100).
Yêu cầu viết chương trình nhập vào 2 phân số, yêu cầu xuất phân số tổng của 2 phân số đó (phân số tổng được rút gọn, sau đó xuất ra màn hình)

Nếu input có phân số nào có mẫu bằng 0 thì xuất kết quả ra -1

Dữ liệu đầu vào: gồm 2 dòng, mỗi dòng gồm 2 số nguyên cách nhau tối thiểu 1 khoảng trắng.

Dữ liệu đầu ra: gồm 1 dòng duy nhất chứa phân số tổng (sau khi rút gọn) của 2 phân số ban đầu, xuất theo dạng: tửsố/mẫusố

Ví dụ 1:

Input	
1 2
1 3
Output
5/6


Ví dụ 2:

Input	
1 2
1 0
Output
-1

'''
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def rut_gon(self):
        ucln = gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln

    def __add__(self, other):
        tu_moi = self.tu * other.mau + other.tu * self.mau
        mau_moi = self.mau * other.mau
        return PhanSo(tu_moi, mau_moi)

    def __str__(self):
        return f"{self.tu}/{self.mau}"
def main():
    try:
        tu1, mau1 = map(int, input().split())
        tu2, mau2 = map(int, input().split())
        if mau1 == 0 or mau2 == 0:
            print(-1)
            return
        ps1 = PhanSo(tu1, mau1)
        ps2 = PhanSo(tu2, mau2)
        tong = ps1 + ps2
        tong.rut_gon()
        print(tong)
    except:
        print(-1)
if __name__ == "__main__":
    main()
