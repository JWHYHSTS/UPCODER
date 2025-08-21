'''
Input:
Nhập vào 1 số gồm 4 chữ số
Output:
Tính tổng chữ số nhỏ nhất và chữ số lớn nhất của số trong input
Ví dụ:

Input	
1234
Output
5

'''
n = int(input())
# hang_nghin = n // 1000
# hang_tram = (n // 100) % 10
# hang_chuc = (n // 10) % 10
# hang_don_vi = n % 10
# max_digit = max(hang_nghin, hang_tram, hang_chuc, hang_don_vi)
# min_digit = min(hang_nghin, hang_tram, hang_chuc, hang_don_vi)
# print(max_digit + min_digit)

# cách 2:
digits = [int(d) for d in str(n)]
print(max(digits) + min(digits))
