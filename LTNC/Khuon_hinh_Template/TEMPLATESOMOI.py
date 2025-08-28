'''
Xây dựng 1 cấu trúc mảng có sử dụng khuôn hình, áp dụng cho bài sau:

Viết chương trình nhập vào 1 dãy số, yêu cầu xuất ra số lớn nhất, số lượng số lớn nhất có trong dãy và tổng của các dãy số đó ra màn hình.

Với các qui ước:

-     Kiểu N: là số nguyên ( <=1000)

-     Kiểu M: là SoMoi (được mô tả ở đây)

Dữ liệu đầu vào:

- Dòng đầu tiên: nhập vào loại kiểu của dãy số (kiểu N hoặc M)

- Các dòng còn lại, mỗi dòng chứa 1 số thuộc kiểu của dòng đầu tiên

Dữ liệu đầu ra:

-          Dòng 1: số lớn nhất (thuộc kiểu đã cho).

-          Dòng 2: Xuất số lượng số lớn nhất có trong dãy.

-          Dòng 2: tổng của dãy số.

Lưu ý:  

-          Số lượng phần tử của dãy <= 1000

 

Ví dụ 1:

Input:

N

1

4

3

4

Output:
4
2
12

Ví dụ 2:

Input:

M

12

23

Output:
[SoMoi] 23
1
[SoMoi]8

'''
from sys import stdin

class SoMoi:
    def __init__(self, raw: int):
        self.raw = int(raw)

    @property
    def digit_sum(self) -> int:
        return sum(int(d) for d in str(abs(self.raw)))

    # So sánh theo tổng chữ số
    def __lt__(self, other):
        if not isinstance(other, SoMoi):
            return NotImplemented
        return self.digit_sum < other.digit_sum

    def __eq__(self, other):
        if not isinstance(other, SoMoi):
            return NotImplemented
        return self.digit_sum == other.digit_sum

    def __str__(self):
        # Dạng in cho 1 phần tử
        return f"[SoMoi] {self.raw}"

def read_input():
    lines = [line.strip() for line in stdin.read().strip().splitlines() if line.strip() != ""]
    if not lines:
        return None, []
    typ = lines[0]
    nums = lines[1:]
    return typ, nums

def main():
    typ, nums = read_input()
    if typ is None:
        return
    if typ == 'N':
        arr = [int(x) for x in nums]
        if not arr:
            return
        max_val = max(arr)
        count_max = sum(1 for v in arr if v == max_val)
        total = sum(arr)
        print(max_val)
        print(count_max)
        print(total)
    elif typ == 'M':
        arr = [SoMoi(int(x)) for x in nums]
        if not arr:
            return
        # Tìm max theo digit_sum
        max_obj = max(arr, key=lambda o: o.digit_sum)
        max_sum = max_obj.digit_sum
        count_max = sum(1 for o in arr if o.digit_sum == max_sum)
        total_digit_sum = sum(o.digit_sum for o in arr)
        # In kết quả
        print(str(max_obj))
        print(count_max)
        # Tổng in theo quy ước ví dụ: không có khoảng trắng sau ]
        print(f"[SoMoi]{total_digit_sum}")
    else:
        # Kiểu không hợp lệ: không làm gì hoặc có thể in lỗi
        pass

if __name__ == "__main__":
    main()