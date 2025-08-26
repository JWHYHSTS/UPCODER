'''
Tìm “vị trí số hoàn thiện cuối cùng” trong mảng một chiều các sốnguyen (vitrihoanthiencuoi). 
Nếu mảng không có số hoàn thiện thì trả về giá trị - 1.
Số hoàn thiện là một số nguyên dương mà tổng các ước nguyên dương thực sự của nó bằng chính nó
Input: 
 Dòng đầu số n
 Dòng hai là mảng

'''

n = int(input().strip())
arr = list(map(int, input().split()))
def is_perfect(x: int) -> bool:
    if x < 2: return False
    s = 1
    i = 2
    while i * i <= x:
        if x % i == 0:
            s += i
            if i * i != x:
                s += x // i
        i += 1
    return s == x
last = -1
for i, v in enumerate(arr[:n]):
    if is_perfect(v):
        last = i
print(last)