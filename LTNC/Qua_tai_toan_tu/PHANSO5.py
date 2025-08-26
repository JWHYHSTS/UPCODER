'''
Xây dựng cấu trúc Phân Số với 2 thành phần là tử và mẫu (là 2 số nguyên <=100), yêu cầu xây dựng các toán tử sau:
- Toán tử nhập >>
- Toán tử xuất<<
- 2 toán tử ++ và -- với ý nghĩa là tăng và giảm tử số 1 đơn vị.

Yêu cầu áp dụng cấu trúc trên và 2 toán tử trên để giải bài sau:
Input:
- Dòng 1: Nhập vào 1 Phân Số gồm 2 số nguyên, mỗi cách nhau 1 khoảng trắng.
- Dòng 2: Nhập toán tử ++ hoặc --

Output:
- Dòng 1: Xuất Phân Số ban đầu.
- Dòng 2: Thực hiện phép toán trong input, sau đó xuất phân số sau khi thực hiện toán phép

ví dụ:
input
1 2
++
output
1/2
2/2

'''
import sys

class PhanSo:
    def __init__(self, tu: int, mau: int):
        self.tu = tu
        self.mau = mau
    def inc(self):
        self.tu += 1
    def dec(self):
        self.tu -= 1
    def __str__(self):
        return f"{self.tu}/{self.mau}"

def main():
    data = sys.stdin.read().strip().split()
    if len(data) < 3:  # tu mau op
        return
    tu, mau = int(data[0]), int(data[1])
    op = data[2]
    ps = PhanSo(tu, mau)
    print(ps)
    if op == "++":
        ps.inc()
    elif op == "--":
        ps.dec()
    print(ps)

if __name__ == "__main__":
    main()