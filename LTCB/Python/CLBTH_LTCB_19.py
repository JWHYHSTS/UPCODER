'''
Sau khi làm việc nhà một cách chăm chỉ, bạn và em của bạn được mẹ mua tặng một hộp bánh gồm n chiếc bánh. Vì muốn công bằng cho cả hai anh em, hãy kiểm tra xem bạn có thể chia số bánh trong hộp thành hai phần bằng nhau hay không.

Input:

Một số nguyên n (1 ≤ n ≤ 100) – số bánh có trong hộp.

Output:

Hãy in ra “Co the” nếu có thể chia, ngược lại bạn hãy in ra “Khong the”.

Ví dụ:
Input
10
Output
Co the


'''
n = int(input().strip())

if n % 2 == 0:
    print("Co the")
else:
    print("Khong the")