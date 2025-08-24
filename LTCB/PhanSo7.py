'''
Xây dựng cấu trúc PhanSo gồm 2 thành phần: tử và mẫu (là 2 số nguyên không âm <= 100)

Yêu cầu: Viết chương trình nhập vào 2 phân số và xuất ra kết quả của các phép tổng, hiệu, tích, thương 2 phân số đó. 

Lưu ý: 
Các kết quả là phân số đã được rút gọn. Xuất theo định dạng: tử / mẫu
Nếu phân số có tử bằng 0 thì chỉ xuất số 0
Nếu input có phân số nào có mẫu bằng 0 thì xuất kết quả ra -1 và không tính gì cả.
Input:
2 số nguyên cách nhau một khoảng trắng là tử và mẫu của PhânSố A.
2 số nguyên cách nhau một khoảng trắng là tử và mẫu của PhânSố B.
Output:
Phân số tổng của phân số A và phân số B.
Phân số hiệu của phân số A và phân số B.
Phân số tích của phân số A và phân số B.
Nếu Phân số B có giá trị khác 0 thì xuất phân số thương của A chia cho B. Ngược lại không tính phép tính này.
Ví dụ 1:

Input
1 2
1 0

Output
-1

Ví dụ 2:

Input
1 2
1 3

Output
5/6
1/6
1/6
3/2

'''

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def rut_gon(self):
        if self.tu == 0:
            self.mau = 1
            return
        g = gcd(abs(self.tu), abs(self.mau))
        self.tu //= g
        self.mau //= g

    def __str__(self):
        if self.tu == 0:
            return "0"
        return f"{self.tu}/{self.mau}"

    def cong(self, other):
        tu = self.tu * other.mau + other.tu * self.mau
        mau = self.mau * other.mau
        kq = PhanSo(tu, mau)
        kq.rut_gon()
        return kq

    def tru(self, other):
        tu = self.tu * other.mau - other.tu * self.mau
        mau = self.mau * other.mau
        kq = PhanSo(tu, mau)
        kq.rut_gon()
        return kq

    def nhan(self, other):
        tu = self.tu * other.tu
        mau = self.mau * other.mau
        kq = PhanSo(tu, mau)
        kq.rut_gon()
        return kq

    def chia(self, other):
        tu = self.tu * other.mau
        mau = self.mau * other.tu
        kq = PhanSo(tu, mau)
        kq.rut_gon()
        return kq

def check_input(tu, mau):
    return 0 <= tu <= 100 and 0 <= mau <= 100

def main():
    try:
        a_tu, a_mau = map(int, input().split())
        b_tu, b_mau = map(int, input().split())
    except:
        print(-1)
        return

    if not (check_input(a_tu, a_mau) and check_input(b_tu, b_mau)):
        print(-1)
        return

    if a_mau == 0 or b_mau == 0:
        print(-1)
        return

    A = PhanSo(a_tu, a_mau)
    B = PhanSo(b_tu, b_mau)

    print(A.cong(B))
    print(A.tru(B))
    print(A.nhan(B))
    if B.tu != 0:
        print(A.chia(B))

if __name__ == "__main__":
    main()