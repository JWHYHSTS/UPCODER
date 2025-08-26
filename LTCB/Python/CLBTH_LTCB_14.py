'''
Cho hai điểm A(xA, yA) và B(xB, yB) trên mặt phẳng tọa độ Oxy. Hãy tính khoảng cách giữa hai điểm A và B.

Input:

Gồm một dòng chứa 4 số thực xA, yA, xB, yB.

Output:

In ra khoảng cách giữa hai điểm A(xA, yA) và B(xB, yB). Kết quả lấy chính xác 3 chữ số sau dấu thập phân.

Ví dụ:


Input
1 1 4 5
Output
5.000

'''
xa, ya, xb, yb = map(float, input().strip().split())
distance = ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5
print(f"{distance:.3f}")