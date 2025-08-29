'''
Xoá phần tử k 

Xoá tất cả phần tử có giá trị K trong danh sách liên kết đơn có n phần tử 

Input:
dòng 1: chứa số nguyên n (100>=n >= 1) và số nguyên K ( -1000<=k<=1000)
dòng 2: chứa n phần tử mỗi phần tử cách nhau 1 khoảng trắng (mỗi phần tử là số nguyên có giá trị tuyệt đối <= 1000)

Output:
dòng 1 : số phần tử của danh sách sau khi xoá
dòng 2: chứa n phần tử của danh sách sau khi xoá , mỗi phần tử cách nhau 1 khoảng trắng

lưu ý : PHẢI dùng danh sách liên kết để làm bài 

input:
6 2
1 2 3 6 2 8
output:
4
1 3 6 8

'''

import sys

class Node:
    __slots__=("val","next")
    def __init__(self,val):
        self.val=val
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

def delete_k(head,k):
    dummy=Node(0)
    dummy.next=head
    prev=dummy
    cur=head
    while cur:
        if cur.val==k:
            prev.next=cur.next
        else:
            prev=cur
        cur=cur.next
    return dummy.next

def to_list(head):
    out=[]
    while head:
        out.append(head.val)
        head=head.next
    return out

def main():
    data=sys.stdin.read().strip().split()
    if len(data)<2:
        return
    n=int(data[0]); k=int(data[1])
    nums=list(map(int,data[2:2+n]))
    head=build(nums)
    head=delete_k(head,k)
    res=to_list(head)
    print(len(res))
    print(" ".join(map(str,res)))

if __name__=="__main__":
    main()