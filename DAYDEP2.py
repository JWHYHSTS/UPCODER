'''
Nhập vào một dãy số, yêu cầu xuất độ “đẹp” của dãy số đó.

Độ “đẹp” của dãy được xác định như sau:

-          Nếu tổng của dãy có 2 chữ số tận cùng là 00, xuất ra màn hình là “DEP”

-          Nếu tổng của dãy có 2 chữ số tận cùng là 55, xuất ra màn hình là “TRUNGBINH”

-          Còn nếu không rơi vào 2 trường hợp trên, xuất ra là “XAU”

Dữ liệu nhập:

Gồm nhiều dòng, mỗi dòng là 1 số kết thúc là số 0 

(lưu ý 0 chỉ là ký hiệu kết thúc, không tính vào dãy số)

Dữ liệu xuất:

Xuất ra độ “đẹp” của dãy số.

Ví dụ:

Input:
10
9 
5
0
output:
XAU

'''
tong = 0
while True:
    s = input()
    if not s:
        continue
    try:
        x = int(s)
    except ValueError:
        continue
    if x == 0:
        break
    tong += x
if tong % 100 == 0:
    print("DEP")
elif tong % 100 == 55:
    print("TRUNGBINH")
else:
    print("XAU")