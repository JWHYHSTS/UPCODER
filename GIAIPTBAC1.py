""" Bài này trên upcoder Lỗi nhập giá trị trên & ko cùng hàng
Giải phương trình Ax + B = 0. Với A, B là hai hệ sô kiểu số nguyên được nhập vào từ bàn phím

- Nếu phương trình vô nghiệm xuất kết quả: VN
- Nếu phương trình VSN xuất ra : VSN
- Nếu phương có nghiệm, xuất ra nghiệm (Lưu ý: kết quả xuất ra là số thực (lấy 2 chữ số thập phân)

Ví dụ:

Input	
2
-4
Output
2.00

Input	
2
3
Output
-1.50
"""

A = int(input())
B = int(input())

if A == 0:
	if B == 0:
		print("VSN")
	else:
		print("VN")
else:
	x = -B / A
	print(f"{x:.2f}")

