'''
Yêu cầu 1:

Xây dựng cấu trúc HCN biểu diễn hình chữ nhật gồm các thông tin gồm chiều dài a và chiều rộng b (a, b là 2 số thực lớn hơn bằng 0 và bé hơn 1000).
Yêu cầu xây dựng các hàm sau:

1. Quá tải nhập và xuất HCN (xem ví dụ để hiểu rõ hơn cách xuất 1 HCN)

2. Tính chu vi HCN.

3. Quá tải so sánh < hai HCN dựa vào chu vi (chu vi của HCN nhỏ hơn thì sẽ xác định là HCN đó bé hơn)

4. Quá tải cộng + với tham số là cộng 1 HCN và 1 số thực, nội dung của hàm: lấy chu vi HCN cộng với số thực, hàm trả về là 1 số thực.






Yêu cầu 2:
Sử dụng cấu trúc ở trên, giải bài tập với các yêu cầu sau:

Input:
Gồm 2 dòng, mỗi dòng chứa 2 số thực đại diện cho chiều dài và chiều rộng của 2 HCN.
Output:
-          Dòng 1: Xuất thông tin của HCN 1
-          Dòng 2: Xuất thông tin của HCN 2

-          Dòng 3: xuất chữ “true” (không có dấu “ ) nếu HCN 1 < HCN 2, ngược lại xuất “false” (không có dẫu “ )                   

Ví dụ:



Input
2 1
3 4
Output
[HCN] 2,1
[HCN] 3,4
true

Lưu ý: mỗi yêu cầu thiếu sẽ bị trừ 1 điểm

'''

class HCN:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def perimeter(self) -> float:
        return 2 * (self.a + self.b)

    def __lt__(self, other):
        if not isinstance(other, HCN):
            return NotImplemented
        return self.perimeter() < other.perimeter()

    def __add__(self, val):
        if isinstance(val, (int, float)):
            return self.perimeter() + val
        return NotImplemented

    def __radd__(self, val):
        return self.__add__(val)

    def __str__(self):
        def fmt(x):
            if x == int(x):
                return str(int(x))
            s = f"{x}"
            if "." in s:
                s = s.rstrip('0').rstrip('.')
            return s
        return f"[HCN] {fmt(self.a)},{fmt(self.b)}"


def main():
    import sys
    data = sys.stdin.read().strip().split()
    if len(data) < 4:
        return
    a1, b1, a2, b2 = map(float, data[:4])
    h1 = HCN(a1, b1)
    h2 = HCN(a2, b2)
    print(h1)
    print(h2)
    print("true" if h1 < h2 else "false")


if __name__ == "__main__":
    main()