'''
cho danh sách liên kết đơn các số nguyên có nhiều hơn 3 giá trị và các giá trị trong danh sách khác nhau từng đôi một .Hãy xác định xem trong danh sách có bộ 3 giá trị ( a, b, c ) nào thoả điều kiện a = b + c (với a, b, c là 3 giá trị khác nhau trong danh sách ) hay không , nếu có xuất ra "YES" ngược lại xuất ra "NO"

 

dữ liệu input: 

·         dòng 1 : số phần tử của danh sách sách liên kết đơn 

·         dòng 2 : các phần tử của danh sách , mỗi phần tử cách nhau 1 khoảng trắng 

 

dữ liệu output:

·         dòng 1 : xuất ra "YES" hoặc "NO"

Ví dụ:

Input	
6
1 2 3 4 5 6
Output
YES

lưu ý: dùng danh sách liên kết để làm bài
'''

import sys

class Node:
    __slots__=("val","next")
    def __init__(self,v):
        self.val=v
        self.next=None

def build(values):
    head=None
    tail=None
    for v in values:
        n=Node(v)
        if head is None:
            head=tail=n
        else:
            tail.next=n
            tail=n
    return head

def exists_sum_triplet(head):
    vals=[]
    cur=head
    while cur:
        vals.append(cur.val)
        cur=cur.next
    s=set(vals)
    for a in vals:
        for b in vals:
            if b==a: 
                continue
            c=a-b
            if c!=b and c!=a and c in s:
                return True
    return False

def main():
    data=sys.stdin.read().strip().split()
    if not data:
        return
    n=int(data[0])
    nums=list(map(int,data[1:1+n]))
    if len(nums)!=n:
        return
    head=build(nums)
    print("YES" if exists_sum_triplet(head) else "NO")

if __name__=="__main__":
    main()