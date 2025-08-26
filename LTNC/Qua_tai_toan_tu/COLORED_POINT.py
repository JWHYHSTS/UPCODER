'''
Trong mặt phẳng tọa độ Oxy, xây dựng cấu trúc mô tả các đối tượng COLORED_POINT, là các đối tượng điểm có màu, bao gồm: hoành độ x và tung độ y (kiểu integer) và mã màu (kiểu chuỗi, tối đa 6 kí tự). Viết chương trình thực hiện các yêu cầu sau:

1.    Nhập danh sách điểm. Dùng kĩ thuật nạp chồng toán tử nhập >>

2.    Xuất danh sách điểm theo định dạng (x,y,#). Dùng kĩ thuật nạp chồng toán tử xuất <<

3.    Đếm số lượng điểm có mã màu là “5DC3A8”

4.    Đổi các điểm có hoành độ lớn hơn tung độ sang màu “1F00F3”

 

Yêu cầu:

-       Sử dụng kĩ thuật cấp phát động để tạo mảng

-       Sử dụng con trỏ để quản lý mảng

 

Input:

-       Dòng đầu tiên là số nguyên N cho biết số lượng điểm trong danh sách

-       N dòng tiếp theo, mỗi dòng chứa 3 giá trị, bao gồm: 2 số nguyên và 1 chuỗi (không có khoảng trắng) cho biết hoành độ, tung độ và mã màu của điểm. Mỗi giá trị cách nhau 1 khoảng trắng.

Output:

-       Dòng đầu tiên là danh sách các điểm theo đúng định dạng
(x,y,#), mỗi điểm cách nhau 1 khoảng trắng. Lưu ý, loại bỏ khoảng trắng cuối cùng trong chuỗi xuất.

-       Dòng thứ hai là số nguyên cho biết số lượng điểm có mã màu “5DC3A8”

-       Dòng thứ ba là danh sách các điểm sau khi đã đổi màu các điểm có hoành độ lớn hơn tung độ. Mỗi điểm xuất theo đúng định dạng
(x,y,#)

 

Vd:

Input:         
5
3 2 5DC3A8
-2 5 2AF700
0 6 3D0FD6
4 7 5DC3A8
5 -5 5DC3A8

Output:

(3,2,#5DC3A8) (-2,5,#2AF700) (0,6, #3D0FD6) (4,7,#5DC3A8) (5,-5,#5DC3A8)
3
(3,2,#1F00F3) (-2,5,#2AF700) (0,6,#3D0FD6) (4,7,#5DC3A8) (5,-5,#1F00F3)
                  
'''
import sys
from dataclasses import dataclass

TARGET_COLOR = "5DC3A8"
NEW_COLOR = "1F00F3"

@dataclass
class ColoredPoint:
    x: int
    y: int
    color: str

    def __str__(self):
        return f"({self.x},{self.y},#{self.color})"

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    pts = []
    idx = 1
    for _ in range(n):
        x = int(data[idx]); y = int(data[idx+1]); c = data[idx+2]; idx += 3
        pts.append(ColoredPoint(x, y, c))

    # Dòng 1: danh sách ban đầu
    print(" ".join(str(p) for p in pts))

    # Dòng 2: số điểm có mã TARGET_COLOR
    count_target = sum(1 for p in pts if p.color == TARGET_COLOR)
    print(count_target)

    # Dòng 3: sau khi đổi màu với điều kiện x > y
    for p in pts:
        if p.x > p.y:
            p.color = NEW_COLOR
    print(" ".join(str(p) for p in pts))

if __name__ == "__main__":
    main()