'''
Cho một mảng các số nguyên, hãy kiểm tra mảng có tính đối xứng hay không?
Yêu cầu:
Sử dụng biến con trỏ để quản lý mảng
Sử dụng vùng nhớ động để cấp phát mảng
Input:
- Dòng đầu tiên: số nguyên cho biết số lượng phần tử mảng
- Dòng thứ hai: danh sách các số nguyên là giá trị của từng phần tử mảng, mỗi phần tử cách nhau khoảng trắng.
Output:
- Nếu mảng có tính đối xứng, in ra dòng chữ: "mang doi xung"
- Nếu mảng không có tính đối xứng, in ra dòng chữ: "mang khong doi xung" và các cặp phần tử làm cho mảng không đối xứng.

Ví dụ:
Input:
5
1 2 3 2 1
Output:
mang doi xung

Input:
5
1 2 3 4 5
Output:
mang khong doi xung
1 5
2 4

'''
n = int(input())
arr = list(map(int, input().split()))
ptr = arr[:]

is_symmetric = True
mismatch_pairs = []

for i in range(n // 2):
    if ptr[i] != ptr[n - 1 - i]:
        is_symmetric = False
        mismatch_pairs.append((ptr[i], ptr[n - 1 - i]))

if is_symmetric:
    print("mang doi xung")
else:
    print("mang khong doi xung")
    for a, b in mismatch_pairs:
        print(f"{a} {b}")