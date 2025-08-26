'''
Bộ 3 số Pytago

Như ta đã biết, với 3 số nguyên dương cho trước (a < b < c), nếu 3 số đó là độ dài 3 cạnh của một tam giác vuông thì bộ 3 số này được gọi là bộ 3 số Pytago.



Yêu cầu: 
Cho trước số nguyên dương n (n<= 10^4). Hãy xuất ra màn hình tất cả các bộ 3 số Pytago mà cả 3 số đều <= n (mỗi bộ số 1 dòng và xuất theo thứ tự tăng dần). Nếu không có thì xuất -1

Ví dụ:
Input
5
Ouput
3 4 5
Input
13
Output
3 4 5
5 12 13
6 8 10

'''

n = int(input())
found = False
for a in range(1, n + 1):
    for b in range(a + 1, n + 1):
        c = (a**2 + b **2)**0.5
        if c == int(c) and c <= n:
            print(a,b,int(c))
            found = True
if not found:
    print(-1)
