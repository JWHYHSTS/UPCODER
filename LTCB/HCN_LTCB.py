'''
Viết chương trình nhập vào hai cạnh của một hình chữ nhật, tính và xuất ra chu vi và diện tích của nó, mỗi kết quả trên một dòng, không có xuống dòng sau diện tích.
Nếu người dùng lỡ nhập số âm thì lấy trị tuyệt đối để tính.
Input: cạnh 1, cạnh 2 cách nhau bằng khoảng trắng.
Output: chu vi
        diện tích

1
2
3
INPUT | OUTPUT
2 3   | 10
      | 6
'''
import sys

data = sys.stdin.read().strip().split()
if len(data) < 2:
    sys.exit(0)

a, b = map(float, data[:2])
a = abs(a)
b = abs(b)

chu_vi = 2 * (a + b)
dien_tich = a * b

def fmt(x): # hàm fmt dùng để định dạng đầu ra
    return str(int(x)) if x.is_integer() else str(x)

print(fmt(chu_vi))
print(fmt(dien_tich), end="")