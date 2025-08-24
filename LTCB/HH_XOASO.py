'''(HUS3_D)
Bạn được cho một số nguyên không âm. Giả sử bạn phải lựa chọn xóa một chữ số và để lại những chữ số còn lại , không thay đổi thứ tự, thì bạn có thể tạo thành số nào lớn nhất?

Input:  Số nguyên không âm N duy nhất (N < 1018 ).
vd : 1001
Output: Số lớn nhất có thể tạo ra khi xóa đi đúng 1 chữ số trong N.
vd : 101
'''
n = int(input())
max_num = -1
for i in range(len(str(n))):
    new_num = int(str(n)[:i] + str(n)[i+1:])
    max_num = max(max_num, new_num)
print(max_num)