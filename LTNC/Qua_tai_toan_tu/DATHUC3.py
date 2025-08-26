'''
Xây dựng cấu trúc BacHai biểu diễn một đa thức bậc 2 có dạng ax^2+bx+c, trong đó a,b,c là số nguyên dương biểu diễn 3 hệ số của đa thức bậc 2.

Yêu cầu 1:

a) Xây dựng cấu trúc trên.

b) Viết quả tải toán tử nhập và xuất cho cấu trúc trên (nhập hệ số a,b,c)

c) Viết hàm tinhGiaTri của BacHai với giá trị x cụ thể.

Ví dụ: với F(x) =  3x^2 + 2x + 3 và x = 2 thì:

                F(2) =  3*2^2 + 2*2 + 3 = 3*4 + 4 + 3 = 19

d) Hãy cài đặt hàm quá tải toán tử cộng 2 BacHai bằng cách cộng từng hệ số tương ứng với nhau, kết quả trả về là một đa thức BacHai.

Ví dụ:

F1(x) = 3x^2 + 2x + 3

F2(x) = 2x^2 + 5x + 6

=> Tong(x) = 5x^2 + 7x + 9  (xuất hệ số bình thường. Không yêu cầu xử lý các trường hợp hệ số đặc biệt)

e) Hãy cài đặt quá tải toán tử so sánh bằng, so sánh 2 BacHai bằng cách so sánh từng hệ số. Hai đa thức BacHai bằng nhau nếu tất cả các hệ số bằng nhau.

Ví dụ:

F1(x) = 3x^2 + 2x - 4

F2(x) = 3x^2 + 5x + 6

F1 không bằng F2, vì 2 != 5

f) Hãy bổ sung thêm cấu trúc BacNhat để biểu diễn đa thức bậc 1 có dạng: ax + b (hệ số a, b cũng là các số nguyên dương).



g) Hãy cài đặt các quá tải toán tử cần thiết cho BacNhat như: >> (nhập), << (xuất).



h) Cài đặt quá tải toán tử nhân 2 BacNhat, kết quả trả về là một đa thức BacHai.



Ví dụ:

     F3(x) = 2x + 3

     F4(x) = 5x + 4

     => F3(x) * F4(x) = (2x+3)*(5x+4) = 10x^2 + 23x + 12.



i) Quá tải hàm tinhGiaTri của BacNhat để tính giá trị của đa thức bậc nhất với giá trị x cụ thể.



Ví dụ:

    F3(x) = 2x + 3 và x = 2 thì:

    F3(2) = 2*2 + 3 = 4 + 3 = 7



Yêu cầu 2:

Viết chương trình nhập vào theo cấu trúc sau:

- Dòng 1 là 3 hệ số của đa thức BacHai F1

- Dòng 2 là 3 hệ số của đa thức BacHai F2

- Dòng 3 là 2 hệ số của đa thức BacNhat F3
- Dòng 4 là 2 hệ số của đa thức BacNhat F4
- Dòng 5 là 1 số nguyên x0

Xuất kết quả theo cấu trúc sau:

- Dòng 1: xuất F1 (dạng đầy đủ ax^2 + bx + c) - không cần xử lý các hệ số đặc biệt
- Dòng 2: giá trị F1(x0)

- Dòng 3: xuất F2 (dạng đầy đủ ax^2 + bx + c) - không cần xử lý các hệ số đặc biệt

- Dòng 4: giá trị F2(x0)
- Dòng 5: xuất đa thức F5 là tổng F1 và F2 (chỉ xuất F5)

- Dòng 6: giá trị F5(x0)

- Dòng 7: xuất đa thức F6 là tích của F3 và F4 

                      xem cách xuất ở bên dưới theo mẫu: (F3)*(F4)=F6

- Dòng 8: giá trị F6(x0)
- Dòng 9: xuất TRUE1 nếu đa thức F1 và F6 bằng nhau.

            xuất TRUE2 nếu đa thức F2 và F6 bằng nhau. 

            xuất TRUE3 nếu cả 3 đa thức F1, F2 và F6 đều bằng nhau. 

            Ngược lại xuất FALSE.



Ví dụ:

Input
3 2 3
2 5 6
2 3
5 4
2
Output
3x^2+2x+3
19
2x^2+5x+6
24
5x^2+7x+9
43
(2x+3)*(5x+4)=10x^2+23x+12
98
FALSE

'''

class BacHai:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c
    def tinhGiaTri(self, x: int) -> int:
        return self.a * x * x + self.b * x + self.c
    def __add__(self, other):
        return BacHai(self.a + other.a, self.b + other.b, self.c + other.c)
    def __eq__(self, other):
        if not isinstance(other, BacHai):
            return NotImplemented
        return self.a == other.a and self.b == other.b and self.c == other.c
    def __str__(self):
        return f"{self.a}x^2+{self.b}x+{self.c}"

class BacNhat:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
    def tinhGiaTri(self, x: int) -> int:
        return self.a * x + self.b
    def __mul__(self, other):
        # (a1x + b1)(a2x + b2) = (a1a2)x^2 + (a1b2 + a2b1)x + b1b2
        return BacHai(self.a * other.a,
                      self.a * other.b + other.a * self.b,
                      self.b * other.b)
    def __str__(self):
        return f"{self.a}x+{self.b}"

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if len(data) < 11:
        return
    a1,b1,c1 = map(int, data[0:3])
    a2,b2,c2 = map(int, data[3:6])
    a3,b3 = map(int, data[6:8])
    a4,b4 = map(int, data[8:10])
    x0 = int(data[10])
    F1 = BacHai(a1,b1,c1)
    F2 = BacHai(a2,b2,c2)
    F3 = BacNhat(a3,b3)
    F4 = BacNhat(a4,b4)
    F5 = F1 + F2
    F6 = F3 * F4
    print(F1)
    print(F1.tinhGiaTri(x0))
    print(F2)
    print(F2.tinhGiaTri(x0))
    print(F5)
    print(F5.tinhGiaTri(x0))
    print(f"({F3})*({F4})={F6}")
    print(F6.tinhGiaTri(x0))
    if F1 == F6 and F2 == F6:
        print("TRUE3")
    elif F1 == F6:
        print("TRUE1")
    elif F2 == F6:
        print("TRUE2")
    else:
        print("FALSE")

if __name__ == "__main__":
    main()