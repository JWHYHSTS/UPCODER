'''
Nhập vào một số gồm 4 chữ số. Tính và xuât ra màn hình tổng các chữ số
Input: 4321
Output: 10

'''
s = input()
print(sum(int(digit) for digit in s))