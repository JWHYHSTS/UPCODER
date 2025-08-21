'''
Nhập vào điểm các môn học của một sinh viên (là các số nguyên từ 0 đến 10), yêu cầu xuất ra xếp loại của sinh viên đó.

Cách xếp loại dựa vào điểm trung bình (ĐTB) của sinh viên được xếp như sau.

- Nếu ĐTB <4 xếp loại F

- Nếu 4 <= ĐTB  <5.5 xếp loại D

- Nếu 5.5 <= ĐTB < 7.0 xếp loại C

- Nếu 7.0 <= ĐTB < 8.5 xếp loại B

- Nếu 8.5 <= ĐTB xếp loại A

Input:

Gồm nhiều dòng, mỗi dòng là 1 điểm kết thúc là số -1 

(lưu ý -1 chỉ là ký hiệu kết thúc, không tính vào điểm số của sinh viên)

Output:

Xuất ra xếp loại của sinh viên

Ví dụ:

Input:
10 
9 
5
-1
Output:
B
'''
diem = []
while True:
    x = int(input())
    if x == -1:
        break
    if 0 <= x <= 10:
        diem.append(x)
if diem:
    dtb = sum(diem) / len(diem)
    if dtb < 4:
        print("F")
    elif dtb < 5.5:
        print("D")
    elif dtb < 7.0:
        print("C")
    elif dtb < 8.5:
        print("B")
    else:
        print("A")

'''
Cách 2: Dùng Hàm Def

def xep_loai(diem_tb):
    if diem_tb < 4:
        return 'F'
    elif diem_tb < 5.5:
        return 'D'
    elif diem_tb < 7.0:
        return 'C'
    elif diem_tb < 8.5:
        return 'B'
    else:
        return 'A'

def main():
    diem = []
    while True:
        try:
            x = int(input())
            if x == -1:
                break
            if 0 <= x <= 10:
                diem.append(x)
        except:
            continue
    if diem:
        dtb = sum(diem) / len(diem)
        print(xep_loai(dtb))

if __name__ == "__main__":
    main()

'''