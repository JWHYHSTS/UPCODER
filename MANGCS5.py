'''
Nhập vào 1 mảng, yêu cầu tính tổng các số chính phương ra màn hình

ví dụ
4 5 6 7 9

output:
13

'''
def scp(n):
    if n < 0:
        return False
    x = int(n ** 0.5)
    return x * x == n
mang = list(map(int, input().split()))
tong = sum(x for x in mang if scp(x))
print(tong)