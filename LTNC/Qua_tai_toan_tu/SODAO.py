'''
Yêu cầu 1:
Xây dựng cấu trúc SoDao (Số Đảo) biểu diễn một cấu trúc mới gồm 1 thành phần:
-  Một số tự nhiên có 3 chữ số.
Yêu cầu xây dựng các hàm sau:

1. Quá tải nhập và xuất SoDao (xem ví dụ để hiểu rõ hơn cách xuất 1 SoDao)

2. Viết hàm trả về số đảo ngược của SoDao (bằng cách trả về số ngược ).

3. Quá tải so sánh > hai SoDao: giá trị đảo ngược (giá trị đảo ngược của SoDao nào lớn hơn thì sẽ xác định số đó là số lớn hơn)

4. Quá tải cộng + với tham số là 1 SoDao và 1 số nguyên, nội dung hàm là lấy giá trị đảo ngược của SoDao cộng với số nguyên đó, kết trả về của hàm là 1 số nguyên.

Yêu cầu 2:
Sử dụng cấu trúc ở trên, giải bài tập với các yêu cầu sau:

Input:
Gồm 2 dòng, mỗi dòng chứa 1 số tự nhiên có 3 chữ số đại diện cho số SoDao (Dữ liệu đầu vào đảm bảo mỗi dòng chứa 1 số tự nhiên có 3 chữ số).
Output:
-   Dòng 1: Xuất thông tin của SoDao 1
-   Dòng 2: Xuất thông tin của SoDao 2

-   Dòng 3: xuất chữ “YES” (không có dấu “ ) nếu SoDao 1 > SoDao 2, ngược lại xuất “NO” (không có dấu “ )

-   Dòng 4: Xuất tổng SoDao 1 và SoDao 2

(Sử dụng toán tử + được mô tả ở trên, HD: lấy SoDao 1 cộng với số 0, sau đó lấy kết quả cộng với SoDao 2)                    


Ví dụ:
Input
127
456
Output
[SoDao] 127
[SoDao] 456
YES
1375

Lưu ý: mỗi yêu cầu bị thiếu sẽ bị trừ 1 điểm
'''

class SoDao:
    def __init__(self, n: int):
        self.n = n  

    def reverse_value(self) -> int:
        a = self.n // 100
        b = (self.n // 10) % 10
        c = self.n % 10
        return c * 100 + b * 10 + a

    def __gt__(self, other):
        if not isinstance(other, SoDao):
            return NotImplemented
        return self.reverse_value() > other.reverse_value()

    def __add__(self, val):
        if isinstance(val, int):
            return self.reverse_value() + val
        return NotImplemented

    def __radd__(self, val):
        if isinstance(val, int):
            return val + self.reverse_value()
        return NotImplemented

    def __str__(self):
        return f"[SoDao] {self.n}"


def main():
    import sys
    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        return
    n1 = int(data[0])
    n2 = int(data[1])
    s1 = SoDao(n1)
    s2 = SoDao(n2)
    print(s1)
    print(s2)
    print("YES" if s1 > s2 else "NO")
    total = (s1 + 0) + s2  
    print(total)

if __name__ == "__main__":
    main()