'''
Nhập một số n và sau đó là n chuỗi họ tên. Xuất ra chữ ký của chuỗi họ tên đó bằng cách ghép các ký tự đầu của họ và chữ lót với tên của người đó.
Input: 
- Dòng 1:  một số nguyên dương n.
- N dòng tiếp theo là các chuỗi họ tên
Output:
- N dòng, mỗi dòng là chữ ký của từng họ tên.
Ví dụ:

Input
3
Nguyen Van Thanh Do
Le Thanh
Tran Quoc Vinh

Output
nvtDo
lThanh
tqVinh

'''
import sys

def read_names():
    it = iter(sys.stdin.read().splitlines())
    try:
        n_line = next(it).strip()
        while n_line == "":
            n_line = next(it).strip()
        n = int(n_line)
    except:
        return 0, []
    names = []
    for line in it:
        line = line.strip()
        if line:
            names.append(line)
            if len(names) == n:
                break
    return n, names

n, names = read_names()
for name in names:
    parts = name.strip().split()
    if not parts:
        print()
        continue
    initials = "".join(p[0].lower() for p in parts[:-1])
    last_part = parts[-1]
    print(initials + last_part)