'''
Viết chương trình nhập vào 2 số nguyên, sau đó hoán đổi giá trị của chúng cho nhau

Input: 
2 số nguyên a và b, mỗi số cách nhau 1 khoảng trắng
Output: 
2 số nguyên a và b đã hoán đổi giá trị, mỗi số cách nhau 1 khoảng trắng

Ví dụ:

Input	
2 3
Output
3 2

'''

a, b = map(int, input().split())
def swap(a, b):
    return b, a
a, b = swap(a, b)
print(a, b)
