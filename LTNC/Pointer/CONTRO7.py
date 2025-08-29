'''
cho danh sách liên kết đơn các số nguyên có nhiều hơn 2 giá trị và các giá trị trong danh sách khác nhau từng đôi một. hãy tìm trong danh sách các cặp giá trị (a, b) sao cho khoảng cách giữa a và b là nhỏ nhất  và xuất ra số lượng các cặp giá trị đó



dữ liệu vào từ file văn bản "CONTRO.inp":

·         dòng 1: chứa số phần tử của danh sách 

·         dòng 2: chứa các phần tử của danh sách , mỗi phần tử cách nhau 1 khoảng trắng 

dữ liệu ra file văn bản "CONTRO.out":

·         dòng 1: số lượng các cặp giá trị thoả đề và khoảng cách của cặp giá trị đó

·         dòng 2 : danh sách các cặp giá trị xuất theo dạng (a, b) với a < b , mỗi cặp cách nhau 1 khoảng trắng 

lưu ý : 

·         1. dùng DSLK để làm bài 

·         2. Chỉ số được đánh từ 1



Ví dụ:

Input	
5 
1 2 3 10 -5
Output
2 1
(1, 2) (2, 3)

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def read_input(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        values = list(map(int, f.readline().split()))
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

def find_min_distance_pairs(head):
    nodes = []
    current = head
    while current:
        nodes.append(current.value)
        current = current.next
    min_dist = float('inf')
    pairs = []
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            dist = abs(nodes[i] - nodes[j])
            if dist < min_dist:
                min_dist = dist
                pairs = [(min(nodes[i], nodes[j]), max(nodes[i], nodes[j]))]
            elif dist == min_dist:
                pairs.append((min(nodes[i], nodes[j]), max(nodes[i], nodes[j])))
    return pairs, min_dist

def write_output(filename, pairs, min_dist):
    with open(filename, 'w') as f:
        f.write(f"{len(pairs)} {min_dist}\n")
        f.write(' '.join(f"({a}, {b})" for a, b in pairs))

head = read_input("CONTRO.inp")
pairs, min_dist = find_min_distance_pairs(head)
write_output("CONTRO.out", pairs, min_dist)