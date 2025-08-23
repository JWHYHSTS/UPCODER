'''
Nhập:
Dòng 1: nhập vị trí cần thêm và giá trị thêm (có giá trị <=100)
Dòng 2: nhập vào 1 dãy số (dãy số có tối đa 100 phần tử)

Xuất: 
Mảng sau khi thêm

Lưu ý: mảng được đánh chỉ số bắt đầu từ 0

ví dụ
input:
2 5
1 2 3 4
output:
1 2 5 3 4

'''
a, b = map(int, input().split())
mang = list(map(int, input().split()))
mang.insert(a, b)
print(*mang) # Dấu * trong print(*mang) giúp in từng phần tử của mảng ra màn hình, nhờ đó các phần tử được in cách nhau bằng dấu cách thay vì dấu phẩy và ngoặc vuông.