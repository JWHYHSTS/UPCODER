'''
Cho dãy số nguyên tố được sắp theo thứ tự tăng dần. Gọi m là số nguyên tố nhỏ nhất trong dãy và M là số nguyên tố lớn nhất trong dãy. 
Hãy xác định trong đoạn từ m đến M còn thiếu những số nguyên tố nào và tự động điền những số còn thiếu để tạo thành một mảng các giá trị số nguyên tố liên tục từ m đến M
Yêu cầu:
Sử dụng biến con trỏ để quản lý mảng
Sử dụng vùng nhớ động để cấp phát mảng
Input: hai số nguyên tố m và M, với m < M
Output: mảng các số nguyên tố liên tục từ m đến M, mỗi số cách nhau 1 khoảng trắng

Ví dụ: 
Input: 2 11
Output: 2 3 5 7 11

Input: 13 17
Output: 13 17

'''

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

m, M = map(int, input().split())
prime_list = []

for num in range(m, M + 1):
    if is_prime(num):
        prime_list.append(num)

ptr = prime_list[:]

print(' '.join(map(str, ptr)))