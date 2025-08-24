'''
Viết chương trình nhập giá trị ss là số giây từ bàn phím. Thông báo ra màn hình thời gian ss giây sau khi đổi thời gian tính bằng ngày, giờ, phút, giây.
Vd:
Input: 86401
Output: 1:0:0:1

'''
ss = int(input().strip())
day = ss // 86400
ss %= 86400
hour = ss // 3600
ss %= 3600
minute = ss // 60
second = ss % 60
print(f"{day}:{hour}:{minute}:{second}")