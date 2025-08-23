'''
Viết một hàm chuyển đổi cơ số từ hệ 10 sang hệ 2, 8 và 16 theo prototype sau:

void chuyenCoSo(long soHe10, int heCoSoMoi);

nếu tham số heCoSoMoi có giá trị là 0 thì chuyển sang cơ số 2, nếu là 1 thì chuyển sang hệ 8 còn nếu là 2 thì chuyển sang hệ 16.
Mặc định tham số heCoSoMoi có giá trị là 0.

ví dụ:
chuyenCoSo(10)   => kết quả sẽ là: 1010
chuyenCoSo(10,0)   => kết quả sẽ là: 1010
chuyenCoSo(10,1)   => kết quả sẽ là: 12
chuyenCoSo(10,2)   => kết quả sẽ là: A

Yêu cầu viết chương trình nhập vào 1 số nguyên n (0 < n <= 2000) là hệ cần đổi (theo qui ước của tham số là 0,1,2)
Xuất ra  số đã được đổi sang hệ tương ứng

Ví dụ:

Input	
10 0
Output
1010
Input
10 1
Output
12

Yêu cầu phải dùng stack để làm bài này - nếu không dùng stack sẽ bị 0 điểm bài này

'''
def chuyenCoSo(soHe10, heCoSoMoi=0):
    if heCoSoMoi == 0:
        base = 2
    elif heCoSoMoi == 1:
        base = 8
    elif heCoSoMoi == 2:
        base = 16
    else: 
        return False
    if soHe10 == 0:
        print(0)
        return 
    stack = []
    n = soHe10
    while n > 0:
        du = n % base
        stack.append(du)
        n //= base
    result = ""
    while stack:
        x = stack.pop()
        if x >= 10:
            result += chr(x - 10 + ord('A'))
        else:
            result += str(x)
    print(result)
if __name__ == "__main__":
    arr = input().split()
    n = int(arr[0])
    if len(arr) == 2:
        he = int(arr[1])
        chuyenCoSo(n, he)
    else:
        chuyenCoSo(n)