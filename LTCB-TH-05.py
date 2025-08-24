'''
Nhập vào n số nguyên và giá trị các số tương ứng. Tính tổng các số chẳn và tích các số lẻ.
Lưu ý: số 0 là số không chẵn không lẻ nên không tính vào kết quả.
input: 5 12 8 7 3 0
output: 20 21
'''
data = list(map(int, input().split()))
n = data[0]
arr = data[1:1+n]

sum_even = 0
prod_odd = 1
has_odd = False

for x in arr:
    if x == 0:
        continue
    if x % 2 == 0:
        sum_even += x
    else:
        prod_odd *= x
        has_odd = True

if not has_odd:
    prod_odd = 0  

print(sum_even, prod_odd)