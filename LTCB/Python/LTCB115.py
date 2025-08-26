'''
Viết hàm tính điểm trung bình giữa 3 cột điểm toán và 3 cột điểm văn của một học sinh. 
Người dùng nhập lần lượt theo thứ tự điểm toán rồi tới điểm văn.
Trả kết quả về 2 chữ số thập phân. 
Nếu giá trị nhập vào không hợp lệ trả về kết quả -1 (điểm âm hoặc điểm lớn hơn 10)
VD :
Input : 8 9 8 6 7 10       Output : 8.00
Input 13 4 6 2 3 4         Output : -1

'''

import sys

parts = sys.stdin.read().strip().split()
if len(parts) != 6:
    print(-1)
    sys.exit()

try:
    scores = [float(x) for x in parts]
except:
    print(-1)
    sys.exit()

if any(s < 0 or s > 10 for s in scores):
    print(-1)
else:
    avg = sum(scores) / 6
    print(f"{avg:.2f}")