'''
Công ty cấp nước Nam Định lắp đặt cho mỗi hộ gia đình trong tỉnh 1 công tơ và quy định bảng giá tính tiền nước theo chỉ số công tơ cho từng tháng sau:
16 số đầu thì tính 7.000đ/số
Từ số 17 đến số 50 thì tính 8.500đ/số
Từ số 51 trở lên thì tính 100.000đ/số
Yêu cầu: Em hãy lập trình tính số tiền nước của 1 hộ gia đình phải trả theo bảng giá trên
Ví dụ:

Input
20
Output
146000
'''
n = int(input())
if n <= 16:
    total = n * 7000
elif n <= 50:
    total = 16 * 7000 + (n - 16) * 8500
else:
    total = 16 * 7000 + (50 - 16) * 8500 + (n - 50) * 100000

print(total)