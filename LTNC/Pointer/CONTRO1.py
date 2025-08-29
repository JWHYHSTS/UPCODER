'''
Tìm Min-Max  

cho danh sách liên kết đơn n phần tử (số nguyên) tìm giá trị lớn nhất và nhỏ nhất trong danh sách và in ra vị trí của các giá trị lớn nhất, giá trị nhỏ nhất trong danh sách đó 
dư liệu được cho như sau:
dòng đầu tiên là n (số phần tử của danh sách)
n dòng tiếp theo là giá trị của phần tử thứ i trong danh sách 
dữ liệu ra xuất ra:
dòng đầu tiên xuất ra giá trị lớn nhất 
dòng tiếp theo xuất ra vị trí của các phần tử lớn nhất trong danh sách mỗi phần tử cách nhau 1 khoảng trắng
dòng tiếp theo xuất ra giá trị nhỏ nhất 
dòng tiếp theo xuất ra vị trí của các phần tử nhỏ nhất trong danh sách, mỗi phần tử cách nhau 1 khoảng trắng
lưu ý: dùng con trỏ để làm bài  

ví dụ:
input :
7
-1 2 6 3 6 -1 2
output :
6
3 5
-1
1 6

Lưu ý danh sách được đánh số từ 1
'''
import sys

class Node:
    __slots__ = ("val", "next")
    def __init__(self, val):
        self.val = val
        self.next = None

def build_linked_list(values):
    head = None
    tail = None
    for v in values:
        node = Node(v)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    nums = list(map(int, data[1:1 + n]))
    if len(nums) != n:
        # thiếu dữ liệu
        return
    head = build_linked_list(nums)

    # Lần 1: tìm min, max
    cur = head
    pos = 1
    min_val = max_val = cur.val
    while cur:
        if cur.val < min_val:
            min_val = cur.val
        if cur.val > max_val:
            max_val = cur.val
        cur = cur.next
        pos += 1

    # Lần 2: thu thập vị trí
    cur = head
    pos = 1
    max_pos = []
    min_pos = []
    while cur:
        if cur.val == max_val:
            max_pos.append(pos)
        if cur.val == min_val:
            min_pos.append(pos)
        cur = cur.next
        pos += 1

    print(max_val)
    print(" ".join(map(str, max_pos)))
    print(min_val)
    print(" ".join(map(str, min_pos)))

if __name__ == "__main__":
    main()
