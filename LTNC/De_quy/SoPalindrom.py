'''Mã:
SoPalindrom
Tên:
Số Palindrom
Dạng thi:
oi
Thang điểm:
10 điểm
Giới hạn thời gian:
1 giây
Giới hạn bộ nhớ:
64 MB
Được tạo bởi:
admin

Một số nguyên gọi là palindrom nếu nó đọc từ trái sang cũng bằng đọc từ phải sang. Ví dụ 121 là số palindrom.

Yêu cầu:

-         Hãy xây dựng hàm kiểm tra một số có phải là palindrom hay không?

-         Viết chương trình sử dụng hàm đã viết để in ra các số palindrom.



Dữ liệu vào trong gồm n + 1 dòng:

-         dòng đầu ghi số n ( 0 < n < 1000 )

-         n dòng còn lại mỗi dòng ghi một số nguyên dương m (0< m <106)

Kết quả in ra màn hình các số Palindrom



Ví dụ: 

4

102
121
250
9889

Kết quả xuất ra màn hình các số Palindrom là:  
121   9889

'''

def is_pal(x):
    s=str(x)
    return s==s[::-1]

import sys
data=sys.stdin.read().strip().split()
if not data: exit()
n=int(data[0])
nums=list(map(int,data[1:1+n]))
res=[str(x) for x in nums if is_pal(x)]
print(' '.join(res))