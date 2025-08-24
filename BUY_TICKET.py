'''
Có n người xếp hàng để mua vé. Người đứng đầu hàng có chỉ số 0, người kế tiếp là 1, …, cho tới người cuối cùng có chỉ số n − 1.
Người thứ i cần mua t[i] tấm vé.
Quy tắc mua vé:
Mỗi lần mua chỉ được mua 1 vé và tốn đúng 1 giây. 
Sau khi mua, nếu vẫn còn vé cần mua thì người đó sẽ đi ra cuối hàng ngay lập tức để chờ lượt tiếp theo. 
Khi một người đã mua đủ số vé mình cần thì sẽ rời khỏi hàng.
Yêu cầu: Tính tổng thời gian để người ở vị trí k mua xong toàn bộ vé.
Input
Dòng đầu tiên là số nguyên dương n là số người trong xếp hàng. 
Dòng thứ hai là n số nguyên dương, trong đó t[i] là số vé người thứ i cần mua. 
Dòng thứ ba là một số nguyên k.
Output
Một số nguyên duy nhất là tổng thời gian để người thứ k mua xong vé.
Ràng buộc
1 ≤ n ≤ 100.
0 ≤ k < n.
Ví dụ
Input
4
1 3 2 4
3
Output
10
'''
import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    tickets = list(map(int, data[1:1 + n]))
    k = int(data[1 + n])
    tk = tickets[k]
    total = 0
    for i, v in enumerate(tickets):
        if i <= k:
            total += min(v, tk)
        else:
            total += min(v, tk - 1)
    print(total)

if __name__ == "__main__":
    solve()