'''
Cho A quả bóng đỏ và B quả bóng xanh vào trong một túi đen. Hãy tìm số quả bóng tối thiểu nhất cần lấy khỏi túi để chắc chắn lấy được ít nhất một quả đỏ.
Input:
Một dòng duy nhất chứa hai số nguyên A và B.
Output:
In ra kết quả bài toán.
Ví dụ:
Input
2 3
Output
4
'''
a, b = map(int, input().strip().split())
if a == 0:
    print(0)
else:
    print(b + 1)