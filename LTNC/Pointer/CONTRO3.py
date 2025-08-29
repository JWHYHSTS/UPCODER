'''
Thêm phần tử vào vị trí K

cho danh sách liên kết đơn gồm n phần tử ,hãy thêm phần tử a vào vị trí k trong danh sách 

Input:
dòng 1: chứa 3 số nguyên n , a và k (100> n, k >=1, -1000 <= a <= 1000)
dòng 2: chứa n phần tử của danh sách ,mỗi phần tử cách nhau 1 khoảng trắng (mỗi phần tử là số nguyên có giá trị tuyệt đối <= 1000)

Output:
dòng 1: chứa số phần tử của danh sách sau khi thêm 
dòng 2: chứa các phần tử của danh sách sau khi thêm ,mỗi phần tử cách nhau 1 khoảng trắng 

lưu ý: 
1 . Phải dùng danh sách liên kết để làm bài
2. Chỉ số được đánh từ 1

Ví dụ:
input:
5 8 3
1 2 3 4 5

output:
6
1 2 8 3 4 5
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

def insert_at(head, a, k):
    new_node=Node(a)
    if k<=1 or head is None:
        new_node.next=head
        return new_node
    cur=head
    pos=1
    while cur and pos<k-1:
        cur=cur.next
        pos+=1
    if cur is None:
        return head
    new_node.next=cur.next
    cur.next=new_node
    return head

def to_list(head):
    out=[]
    while head:
        out.append(head.val)
        head=head.next
    return out

def main():
    data=sys.stdin.read().strip().split()
    if len(data)<3:
        return
    n=int(data[0]); a=int(data[1]); k=int(data[2])
    vals=list(map(int,data[3:3+n]))
    head=build(vals)
    head=insert_at(head,a,k)
    res=to_list(head)
    print(len(res))
    print(" ".join(map(str,res)))

if __name__=="__main__":
    main()