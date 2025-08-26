'''
Xây dựng cấu trúc BACNHAT biểu diễn một đa thức bậc 1 có dạng ax+b, trong đó a,b là số nguyên



Yêu cầu 1:

a) Xây dựng cấu trúc trên.

b) Viết hàm nhập và xuất cho cấu trúc trên (nhập hệ số a,b)

c) Viết hàm tính giá trị của BACNHAT với giá trị x cụ thể

ví dụ: với F(x) =  2x + 3 và x = 2;

               F(2) =   2*2 + 3 =  4 +3 =7

d) Hãy cài đặt hàm  cộng 2 BACNHAT bằng cách cộng từng hệ số với nhau, kết quả trả về 1 BACNHAT.

ví dụ:  

F1(x) = 2x + 3

F2(x) = 5x + 6

=> Tong(x) = 7x + 9

e) hãy cài đặt hàm so sánh bằng, so sánh 2 BACNHAT bằng xét tổng 2 hệ số a+b

ví dụ:

F1(x) = 2x + 3

F2(x) = 5x + 6

F1 không bằng F2, vì 2 + 3 != 5+6

 

Yêu cầu 2:

Viết chương trình nhập vào theo cấu trúc sau

- Dòng 1 là 2 hệ số của 1 BACNHAT F1
- Dòng 2 là 2 hệ số của 1 BACNHAT F2
- Dòng 3 là 1 số nguyên x0



Xuất kết quả theo cấu trúc sau:
- Dòng 1: xuất F1 (dạng đầy đủ ax+b)
- Dòng 2: xuất F2 (dạng đầy đủ ax+b)
- Dòng 3: xuất tổng F1 và F2 (xem cách xuất ở ví dụ bên dưới)
- Dòng 4: giá trị F1(x0)
- Dòng 5: giá trị F2(x0)
- Dòng 6: xuất TRUE nếu 2 BACNHAT bằng nhau, ngược lại xuất FALSE



Ví dụ:

Input
2 3
5 6
2

Output
2x+3
5x+6
2x+3+5x+6=7x+9
7
16
FALSE

'''

from dataclasses import dataclass
import sys

@dataclass
class BacNhat:
    a: int
    b: int

    def eval(self, x: int) -> int:
        return self.a * x + self.b

    def __add__(self, other):
        return BacNhat(self.a + other.a, self.b + other.b)

    def __eq__(self, other):
        return (self.a + self.b) == (other.a + other.b)

    def __str__(self):
        # format ax+b with correct sign for b
        if self.b >= 0:
            return f"{self.a}x+{self.b}"
        else:
            return f"{self.a}x{self.b}"  # b already has '-'

def main():
    data = sys.stdin.read().strip().split()
    if len(data) < 5:
        return
    a1, b1, a2, b2, x0 = map(int, data[:5])
    f1 = BacNhat(a1, b1)
    f2 = BacNhat(a2, b2)
    s = f1 + f2
    print(f1)
    print(f2)
    print(f"{f1}+{f2}={s}")
    print(f1.eval(x0))
    print(f2.eval(x0))
    print("TRUE" if f1 == f2 else "FALSE")

if __name__ == "__main__":
    main()