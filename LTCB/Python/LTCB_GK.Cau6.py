'''
Mr An vừa bán căn nhà 4 mặt tiền ở trung tâm quận 1 để mở điểm
truy cập Internet thật hoành tráng để kiếm lời. Tất cả vốn Mr. An bỏ ra là a $, Vy
Tô là cấp dưới của An, đã tính toán được cứ mỗi tháng Mr.An sẽ lời được 10% trên 
tổng số vốn và số tiền lời của những tháng trước. 
Nhập vào số nguyên dương a, Mr.An yêu cầu Vy Tô phải thống kê và in ra xem sau tổng cộng bao nhiêu tháng An sẽ lấy lại được số vốn đã bỏ ra.
Input: vốn
Output: số tháng hoàn vốn

'''

a = int(input().strip())
months = 0
total = a  
while total - a < a:  
    total *= 1.1      
    months += 1
print(months)