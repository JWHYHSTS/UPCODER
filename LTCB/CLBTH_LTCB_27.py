'''
Nhập vào từ bàn phím một xâu ký tự S, in ra màn hình số lượng kí tự chỉ xuất hiện đúng 1 lần trong xâu S.
Input:
Một chuỗi S chỉ chứa các ký tự chữ cái và có không quá 255 kí tự.
Output:
Kết quả của bài toán.
Ví dụ:
Input
abbacdmedc
Output
2
Giải thích: Trong xâu kí tự được nhập từ bàn phím có 2 kí tự là m và e chỉ xuất hiện đúng 1 lần.
'''
s = input().strip()
count = 0
for char in set(s):
    if s.count(char) == 1:
        count += 1
print(count)