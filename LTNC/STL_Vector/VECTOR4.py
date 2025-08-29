'''
Bạn cần thực hiện một loạt truy vấn trên một vector các số nguyên. Mỗi truy vấn thuộc một trong ba loại sau: 

1 x y: Chèn số nguyên y vào vị trí x trong vector (chỉ số bắt đầu từ 0). Nếu x lớn hơn độ dài hiện tại của vector, hãy chèn y vào cuối vector.
2 x: Xoá tất cả các phần tử trong vector có giá trị đúng bằng x (nếu có). 
3 x: In ra giá trị của phần tử tại vị trí x trong vector. Nếu x là chỉ số không hợp lệ (lớn hơn hoặc bằng độ dài vector), hãy in ra "ERROR".
Input
Dòng đầu tiên chứa số nguyên N, Q lần lượt là số lượng phần tử ban đầu của vector và số lượng truy vấn.
Dòng thứ hai chứa N số nguyên: các phần tử ban đầu của vector. 
Trong Q dòng kế tiếp, mỗi dòng mô tả một truy vấn theo định dạng sau: “1 x y”, “2 x” hoặc “3 x”.
Output

Với mỗi truy vấn loại 3, in ra một dòng duy nhất chứa: Giá trị tại vị trí x nếu vị trí hợp lệ. Ngược lại, in "ERROR".
Constraints
1 ≤ N, Q ≤ 1000 
0 ≤ x, y ≤ 1000
Examples
Input
3 3
1 5 7
1 2 6
3 0
2 5
Output
1



Input
4 4
5 2 1 1
2 1
1 3 5
3 6
3 2
Output
ERROR
5

'''

import sys
data=sys.stdin.read().strip().split()
if not data: sys.exit()
N=int(data[0]);Q=int(data[1])
a=list(map(int,data[2:2+N]))
idx=2+N
out=[]
for _ in range(Q):
    t=int(data[idx]);idx+=1
    if t==1:
        x=int(data[idx]);y=int(data[idx+1]);idx+=2
        if x>len(a):
            a.append(y)
        else:
            a.insert(x,y)
    elif t==2:
        x=int(data[idx]);idx+=1
        a=[v for v in a if v!=x]
    else:
        x=int(data[idx]);idx+=1
        if 0<=x<len(a):
            out.append(str(a[x]))
        else:
            out.append("ERROR")
sys.stdout.write("\n".join(out))