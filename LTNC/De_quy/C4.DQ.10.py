'''
Đệ quy là 1 phần không thể thiếu khi học lập trình cũng như các môn toán. Vì vậy ta cùng luyện tập lập trình nó với yêu cầu đơn giản sau đây. 
Hãy viết chương trình sử dụng hàm đệ quy tính luỹ thừa có sau: T(n,x) = xn 
với x <= 50, n <=10.
Ví dụ:

Input
5 3
Output
243


'''
import sys
data=sys.stdin.read().strip().split()
if not data: sys.exit()
n=int(data[0]); x=int(data[1])

def calc(k, x):
    if k==0: return 1
    return calc(k-1, x)*x

print(calc(n,x))