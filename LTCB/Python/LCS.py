'''
Để quảng bá cho kì thi Olympic Tin Học Sinh Viên Toàn Quốc & Kỳ Thi Lập Trình Viên Quốc Tế (gọi tắt là OLP&ACM/ICPC), ban tổ chức phát động cuộc thi ảnh "Khoảnh khắc OLP&ACM/ICPC".

Các đội tuyển sẽ đăng ảnh của đội mình vào fanpage của cuộc thi. Dựa vào số lượt tương tác (like, comment, share), ban tổ chức sẽ chọn ra ba bức ảnh có điểm cao nhất để trao quà.

Cách tính điểm như sau: mỗi lượt like được 1 điểm, comment được 2 điểm và share được 3 điểm.

Ban tổ chức đã nhờ người thống kê số lượt tương tác của từng đội, việc còn lại của bạn là tính điểm và xác định 3 đội được trao quà.

Dữ liệu đầu vào: gồm nhiều đội tuyển, dữ liệu mỗi đội tuyển bao gồm 4 dòng:
- Tên đội (không có khoảng trắng)
- Số lượt like
- Số lượt comment
- Số lượt share
Dữ liệu đầu vào kết thúc khi tên đội là "000"

Dữ liệu đầu ra: gồm 3 dòng ghi tên lần lượt 3 đội được trao quà theo thứ tự điểm cao đến thấp (dữ liệu vào đảm bảo không có 2 đội nào bằng điểm)


Ví dụ:
Input:
UP_Balloons
456
215
34
UP_Unlimited
654
45
21
UP_Explorer
452
142
15
UP_Ashe
356
654
78
000

Output:
UP_Ashe
UP_Balloons
UP_Unlimited

'''

def main():
    teams = []
    while True:
        name = input().strip()
        if name == "000":
            break
        like = int(input())
        comment = int(input())
        share = int(input())
        score = like * 1 + comment * 2 + share * 3
        teams.append((score, name))
    teams.sort(reverse = True)
    for i in range(3):
        print(teams[i][1])
if __name__ == "__main__":
    main()