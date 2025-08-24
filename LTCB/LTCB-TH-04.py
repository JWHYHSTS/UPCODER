'''
Nhập  vào 1 số nguyên n>0. Tính tổng các chữ số của n.
input: 113
output: 5
'''
n = int(input().strip()) # strip() trong python dùng để loại bỏ các ký tự khoảng trắng ở đầu và cuối chuỗi.
print(sum(int(digit) for digit in str(n)))