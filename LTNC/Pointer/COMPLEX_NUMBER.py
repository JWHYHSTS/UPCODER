'''
Số có dạng z = a + bi, trong đó a, b là số thực, i2 = -1, gọi là số phức. Trong đó a gọi là phần thực (real), còn b gọi là phần ảo (image).

, gọi là mô-đun của số phức z

Cho hai số phức z1 = a + bi, z2 = c + di

Cộng, trừ số phức:

 

 

Xây dựng cấu trúc mô tả một dãy N (0 <= N <= 10,000) số phức với các thao tác sau:

a)     Tính tổng N số phức

b)    Tính hiệu N số phức

c)     Tính mô-đun N số phức

d)    Xuất N số phức theo định dạng: z = a + bi (với a là phần thực và b là phần ảo)

 

Yêu cầu: sử dụng kĩ thuật cấp phát động và con trỏ để quản lý dãy số. Bài làm không đúng yêu cầu sẽ không được tính điểm.

 

Input:

-       N dòng, mỗi dòng là 1 cặp a và b mô tả thông tin phần thực và phần ảo của 1 số phức.

Output:

-       Dòng 1: xuất N số phức theo định dạng {a+bi}, mỗi số phức cách nhau 1 khoảng trắng;

-       Dòng 2: giá trị mô-đun của N số phức, lấy tối đa 2 số lẻ ở phần thập phân, mỗi giá trị cách nhau 1 khoảng trắng;

Dòng 3: xuất tổng N số phức

Ví dụ:

Input	
3 4
-2 5
11 -14
Output
{3+4i} {-2+5i} {11-14i}
5.00 5.39 17.80
{12-5i}

'''

import sys
import math

class SoPhuc:
    __slots__ = ("thuc", "ao")
    def __init__(self, thuc: int, ao: int):
        self.thuc = thuc
        self.ao = ao
    def modun(self) -> float:
        return math.sqrt(self.thuc * self.thuc + self.ao * self.ao)
    def __str__(self):
        a, b = self.thuc, self.ao
        inner = ""
        if a != 0:
            inner += str(a)
        if b != 0:
            if b > 0 and a != 0:
                inner += "+"
            if b < 0:
                inner += "-"
            if abs(b) != 1:
                inner += str(abs(b))
            inner += "i"
        return "{" + inner + "}"

def read_all_complex() -> list:
    data = sys.stdin.read().strip().split()
    res = []
    for i in range(0, len(data), 2):
        thuc = int(data[i])
        ao = int(data[i+1])
        res.append(SoPhuc(thuc, ao))
    return res

def tong(ds: list) -> SoPhuc:
    s_thuc = 0
    s_ao = 0
    for sp in ds:
        s_thuc += sp.thuc
        s_ao += sp.ao
    return SoPhuc(s_thuc, s_ao)

def main():
    ds = read_all_complex()
    if not ds:
        return  
    # Dòng 1
    print(" ".join(str(sp) for sp in ds))
    # Dòng 2
    print(" ".join(f"{sp.modun():.2f}" for sp in ds))
    # Dòng 3: tổng
    print(str(tong(ds)))

if __name__ == "__main__":
    main()