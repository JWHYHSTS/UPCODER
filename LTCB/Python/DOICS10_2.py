'''
Yêu cầu xây dựng 1 lớp Ngăn xếp, sau đó áp dụng vào giải bài tập sau:
Nhập vào 1 số nguyên ở hệ 10, yêu cầu xuất ra 1 số ở hệ 2

Ví dụ:

Input
10
Output
1010

'''
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
def dec_to_bin(n):
    if n == 0:
        return "0"
    s = Stack()
    while  n > 0:
        s.push(n % 2)
        n //= 2
    bin_str = ""
    while not s.is_empty():
        bin_str += str(s.pop())
    return bin_str
n = int(input())
print(dec_to_bin(n))