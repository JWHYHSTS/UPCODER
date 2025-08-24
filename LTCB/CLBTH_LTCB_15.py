'''

Nhập 1 số nguyên dương N. Nhập tiếp N số nguyên.

Ghi ra màn hình dãy số vừa nhập.

Ghi ra màn hình dãy số vừa nhập theo thứ tự ngược lại.

Input:

Dòng đầu tiên chứa số nguyên dương N.

Dòng tiếp theo chứa N số nguyên dương x.

Output:

Dòng đầu tiên chứa dãy số vừa nhập.

Dòng tiếp theo chứa dãy số vừa nhập theo thứ tự ngược lại.

Ví dụ:


Input
4
1 3 4 2
Output
1 3 4 2
2 4 3 1

'''
n = int(input())
arr = list(map(int, input().split()))
print(" ".join(map(str, arr)))
print(" ".join(map(str, arr[::-1])))

'''
n = int(input())
arr = list(map(int, input().split()))
print(" ".join(map(str, arr)))
b = arr[:]        # hoặc arr.copy()
b.reverse()       # đảo tại chỗ
print(" ".join(map(str, b)))
'''

# n = int(input())
# arr = list(map(int, input().split()))
# print(*arr)
# print(*reversed(arr))