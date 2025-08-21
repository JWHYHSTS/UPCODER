'''
UPCoder vừa cho ra mắt hệ thống tính điểm kinh nghiệm đi kèm các danh hiệu cho coder vào ngày 7/1/2017.

Theo cách tính mới, mỗi bài tập sẽ có các cấp độ: cơ bản, trung bình, nâng cao, khó; tương ứng với các số điểm 10, 20, 30, 40. Coder sẽ được cộng điểm kinh nghiệm tương ứng khi giải đúng 100% số test của bài đó.

Danh hiệu coder sẽ được đặt tùy theo kinh nghiệm mà coder đó đạt được. Cụ thể:



Cho trước số bài giải được của coder theo từng cấp độ. Hãy tính toán điểm kinh nghiệm và xem coder đó đang đạt danh hiệu nào.

Dữ liệu đầu vào: gồm 4 số nguyên dương (không lớn hơn 500) lần lượt là số bài giải được theo cấp độ cơ bản, trung bình, nâng cao, khó.

Dữ liệu đầu ra: gồm 2 dòng
- Dòng đầu tiên ghi lại điểm kinh nghiệm của coder.
- Dòng thứ hai ghi danh hiệu của coder đó (không dấu).

Ví dụ
input
20 10 2 1
output
500
Coder Tieu Hoc
'''

a, b, c, d = map(int, input().split())
expcoder = a * 10 + b * 20 + c * 30 + d * 40

print(expcoder)
if expcoder == 0:
    print("Coder So Sinh")
elif 1 <= expcoder <= 49:
    print("Coder Lop Mam")
elif 50 <= expcoder <= 99:
    print("Coder Lop Choi")
elif 100 <= expcoder <= 499:
    print("Coder Lop La")
elif 500 <= expcoder <= 999:
    print("Coder Tieu Hoc")
elif 1000 <= expcoder <= 1499:
    print("Coder THCS")
elif 1500 <= expcoder <= 1999:
    print("Coder TPHT")
elif 2000 <= expcoder <= 2499:
    print("Coder Trung Cap")
elif 2500 <= expcoder <= 3499:
    print("Coder Cao Dang")
elif 3500 <= expcoder <= 4199:
    print("Coder Dai Hoc")
elif 4200 <= expcoder <= 5499:
    print("Coder Thac Si")
elif 5500 <= expcoder <= 6999:
    print("Coder Tien Si")
else:
    print("Coder Giao Su")