'''
Một cặp số nguyên dương được gọi là số bạn bè nếu tổng các ước số của số này (không tính bản thân số đó) bằng chính số kia và ngược lại. Ví dụ 220 và 284 là cặp số bạn bè vì tổng các ước số của 220 là: 1+2+4+5+10+11+20+22+44+55+110=284 và tổng các ước số của 284 là 1+2+4+71+142=220. 1184 và 1210 cũng là hai số bạn bè. Hãy viết chương trình kiểm tra xem 2 số nhập vào có phải là số bạn bè hay không.

Dữ liệu nhập:

- Là hai số nguyên a, b cách nhau một khoảng trắng (1 ≤ a, b ≤ 105)

Dữ liệu xuất:

- In ra YES nếu a, b là hai số bạn bè. In ra NO nếu không phải.

Ví dụ
Input1
220 284
Output 1
YES
Input 2
12 20
Output 2
NO

'''

a, b = map(int, input().split())
def tong_uoc_so(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong
if tong_uoc_so(a) == b and tong_uoc_so(b) == a:
    print("YES")
else:
    print("NO")