'''
Nhập vào một dãy ký tự, các ký tự gồm có chữ thường ('a' - 'z'), chữ hoa ('A' - 'Z') và chữ số ('0' - '9'). In ra các chữ số chẵn có trong dãy.
Ví dụ:

Input

Output

a B 3 D 8 2 m 1 Z 0

8 2 0

'''

s = input()
for i in s:
    if i.isdigit() and int(i) % 2 == 0:
        print(i, end=' ')