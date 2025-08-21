'''
Nhập vào 1 dãy số, yêu cầu tính tổng các chữ số của dãy đó.

ví dụ:
input:
1
12
23
output:
1
3
5
'''
while True:
    try:
        a = int(input())
        sum_ = 0
        while a != 0:
            sum_ += a % 10
            a //= 10
        print(sum_)
    except EOFError:
        break
    
# while True:
#     try:
#         s = input()
#         if s == "":
#             continue
#         tong = sum(int(ch) for ch in s)
#         print(tong)
#     except EOFError:
#         break