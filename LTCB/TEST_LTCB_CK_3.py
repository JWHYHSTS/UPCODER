'''
Cho n điểm trong mặt phẳng tọa độ Oxy (n không quá 300). Mỗi điểm có tọa độ nguyên (x, y). Hãy đếm xem có bao nhiêu điểm trong số đó nằm trên trục hoành (Ox) hoặc trục tung (Oy).
Ví dụ:

Input
5
0 3
1 0
0 1
2 2
-3 0
Output
4

'''
n = int(input())
count = 0
for _ in range(n):
    x, y = map(int, input().strip().split())
    if x == 0 or y == 0:
        count += 1
print(count)