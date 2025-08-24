'''
Khoa Công nghệ Thông tin - trường Đại học Sư phạm TP. Hồ Chí Minh cần in một số tài liệu để phục vụ giảng dạy và nghiên cứu, chúng có thể là luận văn/báo cáo nghiên cứu khoa học hoặc là giáo trình giảng dạy. Biết rằng mỗi loại tài liệu sẽ có những quy định khác nhau:
Nếu là luận văn hoặc báo cáo khoa học thì phải in 1 mặt.
Nếu là giáo trình, thì có thể in trên cả 2 mặt để tiết kiệm chi phí.
Tất cả các loại tài liệu đều phải in trên giấy A4.
Yêu cầu hãy tính số lượng giấy tối thiểu cần dùng để in hết tài liệu đó.

Input: 
Gồm 3 số nguyên không âm: T, P và C. Trong đó T là loại tài liệu (1 nếu là luận văn/báo cáo khoa học, 2 nếu là giáo trình), P là số trang của tài liệu và C là số bản cần in (1 ≤ T ≤ 2, 1 ≤ P, C, ≤ 109).

Output: 
số tờ giấy A4 tối thiểu cần dùng.
Ví dụ:

Input	Output
2 250 19
2375
'''
t, p, c = map(int, input().split())
if t == 1:
    print(p * c)
else:
    tong = ((p + 1) // 2) * c
    print(tong)