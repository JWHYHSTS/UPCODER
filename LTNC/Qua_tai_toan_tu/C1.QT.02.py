'''
Xây dựng cấu trúc SoPhuc để biểu diễn Số Phức trong toán học. Số phức là biểu thức có dạng: a + bi, với i2 = -1. Trong đó: a là phần thực, b là phần ảo.
Các phép toán cơ bản trong số phức được tính như sau:
(a + bi) + (c + di) = (a + c) + (b + d)i
(a + bi) - (c + di) = (a - c) + (b - d)i
(a + bi) * (c + di) = (ac - bd) + (ad + bc)i

Viết các quá tải toán tử sau:
Quá tải toán tử >> (nhập số phức với phần thực và phần ảo)
Quá tải toán tử << (xuất số phức theo định dạng: a + b*i). Lưu ý khi xuất số phức có phần ảo < 0 thì không xuất dấu + phía trước.
Quá tải phép toán + 2 số phức. Kết quả trả về là số phức.
Quá tải phép toán - 2 số phức. Kết quả trả về là số phức.
Quá tải phép toán * 2 số phức. Kết quả trả về là số phức.
Quá tải phép so sánh nhỏ hơn ( < ) để so sánh 2 số phức. Để so sánh 2 số phức ta so sánh từng thành phần tương ứng với nhau.
So sánh theo thứ tự từ điển. Ví dụ: 2 + 3i < 3 - i ; 2 + 3i < 2 + 4i.

Input:
Dòng 1: Nhập số nguyên dương N
N dòng tiếp theo, mỗi dòng là 2 số nguyên cách nhau 1 khoảng trắng biểu diễn các số phức.
Output:
Dòng 1: Xuất số phức lớn nhất trong các số phức nhập vào.
Dòng 2: Xuất tổng của các số phức.
Dòng 3: Xuất tích của các số phức.
Dòng 4: Xuất hiệu của số phức lớn nhất và số phức nhỏ nhất trong các số phức đã cho.

Ví dụ:

Input
4
2 -2
1 0
2 -1
3 2
Output
3+2*i
8-1*i
18-14*i
2+2*i
'''

class SoPhuc:
    __slots__ = ("a", "b")
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
    def __add__(self, other):
        return SoPhuc(self.a + other.a, self.b + other.b)
    def __sub__(self, other):
        return SoPhuc(self.a - other.a, self.b - other.b)
    def __mul__(self, other):
        # (a+bi)(c+di) = (ac - bd) + (ad + bc)i
        return SoPhuc(self.a * other.a - self.b * other.b,
                      self.a * other.b + self.b * other.a)
    def __lt__(self, other):
        if self.a != other.a:
            return self.a < other.a
        return self.b < other.b
    def __str__(self):
        if self.b >= 0:
            return f"{self.a}+{self.b}*i"
        return f"{self.a}{self.b}*i"  # b already has '-'

def main():
        import sys
        data = sys.stdin.read().strip().split()
        if not data: 
            return
        n = int(data[0])
        nums = []
        idx = 1
        for _ in range(n):
            a = int(data[idx]); b = int(data[idx+1]); idx += 2
            nums.append(SoPhuc(a, b))
        # Largest (max) and smallest (min) by lexicographic order
        mn = nums[0]
        mx = nums[0]
        total = SoPhuc(0, 0)
        prod = nums[0]
        for i, sp in enumerate(nums):
            if sp < mn: mn = sp
            if mx < sp: mx = sp
            total = total + sp
            if i > 0:
                prod = prod * sp
        diff = mx - mn
        print(mx)
        print(total)
        print(prod)
        print(diff)

if __name__ == "__main__":
    main()