'''
Viết chương trình chuyển đổi 1 số nguyên n (n>0) từ hệ thập phân sang  hệ nhị phân. VD
input: 35
Output: 100011
'''
n = int(input().strip())
print(bin(n)[2:])