'''
Xây dựng khuôn hình cấu trúc mảng 1 chiều đặt tên là M1C.

yêu cầu viết hàm nhập, xuất mảng, tổng các phần tử trong mảng.

Các tên hàm và kiểu trả về của các hàm mà đề yêu cầu: void nhap, void xuat, int tong

input:
- Nhập vào 1 dãy số nguyên.

output:
- Xuất tổng các phần tử ra màn hình

Ví dụ:

Input
1 2 3
Output
6


Yêu cầu đề:
Viết đúng tên hàm, tên cấu trúc
'''

import sys

class M1C:
    def __init__(self):
        self.a = []

    def nhap(self):
        data = sys.stdin.read().strip().split()
        if not data:
            self.a = []
            return
        try:
            self.a = [int(x) for x in data]
        except:
            # ignore non-integer tokens
            self.a = [int(x) for x in data if x.lstrip("-").isdigit()]

    def xuat(self):
        if not self.a:
            print()
        else:
            print(" ".join(str(x) for x in self.a))

    def tong(self) -> int:
        return sum(self.a)

if __name__ == "__main__":
    m = M1C()
    m.nhap()
    print(m.tong())