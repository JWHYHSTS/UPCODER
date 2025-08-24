'''
Hiện nay có một loại virus đang hoành hành với một tốc độ tăng trưởng rất nhanh. Sau mỗi ngày số virus sẽ tăng lên gấp đôi. Ví dụ, trong tế bào có chứa 1 con virus, thì sau ngày thứ nhất nó tăng lên thành 2 con, sau ngày thứ hai nó tăng lên thành 4 con,…
Cho biết có n con virus đang kí sinh trong các tế bào, sau ít nhất bao nhiêu ngày thì số lượng con virus vượt quá 1 tỉ?
Input:
Gồm một số nguyên dương n duy nhất.
Output:
Số ngày ít nhất để số virus vượt quá 1 tỉ.
Ví dụ:
Input
1000
Output
20
'''
n = int(input().strip())
days = 0
while n <= 1_000_000_000:
    n *= 2
    days += 1
print(days)