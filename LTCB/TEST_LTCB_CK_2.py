'''
Cho mảng số nguyên a không quá 300 phần tử. Mỗi phần tử của mảng là một số nguyên có giá trị nằm trong đoạn từ [-100, 100]. Hãy in ra các phần tử không trùng lặp, theo đúng thứ tự xuất hiện lần đầu trong mảng.
Ví dụ: 

Input
4 3 8 3 3 1 4 2
Output
4 3 8 1 2

'''
arr = list(map(int, input().strip().split()))
lap = set()
for i in arr:
    if i not in lap:
        print(i, end=' ')
        lap.add(i)