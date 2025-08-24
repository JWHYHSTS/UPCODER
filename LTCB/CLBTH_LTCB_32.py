'''
Trên trục số Ox, cho N đoạn thẳng, mỗi đoạn thẳng được xác định bởi hai điểm đầu và cuối là hai số nguyên. Một điểm M được gọi là nằm trong đoạn thẳng AB nếu A ≤ M ≤ B.
Đếm xem có bao nhiêu điểm có toạ độ nguyên nằm trong đúng K đoạn thẳng.
Input:
Dòng đầu tiên chứa hai số nguyên N và K.
N dòng sau, mỗi dòng gồm hai số nguyên a, b mô tả hai điểm đầu và cuối của đoạn thẳng.
Output:
Một số nguyên duy nhất là số lượng điểm có toạ độ nguyên nằm trong đúng K đoạn thẳng.
Ví dụ 1:

Input
3 2
1 5
2 8
3 7
Output
3

Giải thích: Tọa độ của 3 điểm nằm trong đúng 2 đoạn thẳng là 2, 6, 7.
- Điểm có tọa độ 2 nằm trong 2 đoạn thẳng: đầu tiên và thứ hai.
- Điểm có tọa độ 6, 7 nằm trong 2 đoạn thẳng: thứ hai và thứ ba.
 
Ví dụ 2:

Input
3 1
1 5
2 8
3 7
Output
2

Giải thích: Tọa độ của 2 điểm nằm trong đúng 1 đoạn thẳng là 1, 8.
- Điểm có tọa độ 1 chỉ nằm trong đoạn thẳng đầu tiên.
- Điểm có tọa độ 8 chỉ nằm trong đoạn thẳng thứ 3.
 
Ví dụ 3:

Input
3 3
1 5
2 8
3 7
Output
3

Giải thích: Tọa độ của 3 điểm nằm trong cả 3 đoạn thẳng là 3, 4, 5.

'''

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    events = {}
    for _ in range(N):
        a = int(next(it)); b = int(next(it))
        if a > b:
            a, b = b, a
        events[a] = events.get(a, 0) + 1
        events[b+1] = events.get(b+1, 0) - 1  
    curr = 0
    prev = None
    ans = 0
    for pos in sorted(events):
        if prev is not None and curr == K:
            ans += pos - prev  
        curr += events[pos]
        prev = pos
    print(ans)

if __name__ == "__main__":
    main()