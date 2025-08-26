'''
Yêu cầu 1:
Xây dựng cấu trúc SoMoi (Số Mới) biểu diễn một cấu trúc mới gồm 1 thành phần:
- Một số nguyên A (0<= A <= 1.000.000).
Yêu cầu xây dựng các hàm sau:

1. Quá tải nhập và xuất SoMoi (xem ví dụ để hiểu rõ hơn cách xuất 1 SoMoi)

2. Tính tổng các chữ số của SoMoi (tổng các chữ số của A).

3. Quá tải so sánh > hai SoMoi: dựa vào tổng các chữ số (tổng các chữ số SoMoi nào lớn hơn thì sẽ xác định số đó là số lớn hơn)

4. Quá tải cộng + với tham số là cộng 2 SoMoi, nội dung của hàm: tổng các chữ số của 2 SoMoi cộng lại với nhau , hàm trả về là 1 SoMoi.

Yêu cầu 2:
Sử dụng cấu trúc ở trên, giải bài tập với các yêu cầu sau:

Input:
Gồm 2 dòng, mỗi dòng chứa 1 nguyên đại diện cho 2 SoMoi.
Output:
-          Dòng 1: Xuất thông tin của SoMoi 1
-          Dòng 2: Xuất thông tin của SoMoi 2

-          Dòng 3: xuất chữ “true” (không có dấu “ ) nếu SoMoi 1 > SoMoi 2, ngược lại xuất “false” (không có dẫu “ )

-          Dòng 4: Xuất tổng SoMoi 1 và SoMoi 2                  


Ví dụ:
Input
21
34
Output
[SoMoi] 21
[SoMoi] 34
false
[SoMoi] 10
'''

class SoMoi:
    def __init__(self, A: int):
        self.A = A

    def sum_digits(self) -> int:
        return sum(int(ch) for ch in str(abs(self.A)))

    def __gt__(self, other):
        if not isinstance(other, SoMoi):
            return NotImplemented
        return self.sum_digits() > other.sum_digits()

    def __add__(self, other):
        if not isinstance(other, SoMoi):
            return NotImplemented
        # Kết quả là SoMoi chứa tổng các chữ số hai số
        return SoMoi(self.sum_digits() + other.sum_digits())

    def __str__(self):
        return f"[SoMoi] {self.A}"


def main():
        import sys
        data = sys.stdin.read().strip().split()
        if len(data) < 2:
            return
        a1 = int(data[0])
        a2 = int(data[1])
        s1 = SoMoi(a1)
        s2 = SoMoi(a2)
        print(s1)
        print(s2)
        print("true" if s1 > s2 else "false")
        print(s1 + s2)

if __name__ == "__main__":
    main()