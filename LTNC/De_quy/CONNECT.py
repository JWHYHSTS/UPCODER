'''
Cho n số nguyên dương a1,a2,…,ai,…an (a[i] <=109). Từ các số nguyên này người ta tạo ra một số nguyên mới bằng cách kết nối tất cả các số đã cho viết liên tiếp nhau. Ví dụ, với n = 4 và các số 12, 34, 567, 890 ta có thể tạo ra các  số mới như sau: 1234567890, 3456789012, 8905673412, …. Dễ thấy rằng có 4! = 24 cách tạo mới như vậy. Trong trường hợp này, số lớn nhất có thể tạo thành là 8905673412.

Yêu cầu: cho n các số a1,a2,…,ai,…,an. Hãy xác định số lớn nhất có thể kết nối được theo quy tắc trên.

Hãy in ra một cách nối các số đó lại với nhau sau cho đạt được số lớn nhất.
Dữ liệu vào: cho trong file văn bản CONNECT.INP gồm n+1 dòng
          - Dòng đầu là số N. (0 < N <= 100)
          - Trong các dòng còn lại, dòng thứ  i + 1 ghi số ai
Dữ liệu ra: Ghi vào file văn bản CONNECT.OUT số lớn nhất được kết nối thành từ các số ban đầu

ví dụ:

CONNECT.INP   
4
12
34
567
890   

CONNECT.OUT
8905673412

'''

import sys, functools

def cmp(a,b):
    return (a+b > b+a) - (a+b < b+a)

def main():
    try:
        fin = open("CONNECT.INP","r")
    except:
        return
    data = fin.read().strip().split()
    fin.close()
    if not data: 
        return
    n = int(data[0])
    nums = data[1:1+n]
    nums = [x.strip() for x in nums]
    nums.sort(key=functools.cmp_to_key(cmp))
    with open("CONNECT.OUT","w") as f:
        f.write("".join(nums))

if __name__ == "__main__":
    main()