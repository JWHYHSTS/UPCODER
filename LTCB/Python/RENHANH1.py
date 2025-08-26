'''
Input:
Một số nguyên dương n (n<=10^4)
Ouput: Nếu n chia hết cho 3, xuất "n chia het cho 3", ngược lại nếu n chia cho 3 dư 1 xuất "n chia 3 du 1" ngược lại nếu n chia 3 dư 2 xuất "n chia 3 du 2"
(Lưu ý: 
Không xuất dấu "
Thay n bằng giá trị input
Ví dụ:

Input	Output
9
5
9 chia het cho 3
5 chia 3 du 2

'''
n = int(input())
if n % 3 == 0:
    print(f"{n} chia het cho 3")
elif n % 3 == 1:
    print(f"{n} chia 3 du 1")
else:
    print(f"{n} chia 3 du 2")
