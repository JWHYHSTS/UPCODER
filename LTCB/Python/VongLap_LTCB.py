'''
Giả sử bạn có n số trong mảng , nhiệm vụ của bạn là cần tìm các cặp số có tổng bẳng x ,thứ tự duyệt sẽ bắt đầu từ trái sang phải , nếu như không có cặp số nào tạo ra tổng bằng x thì in ra "thì ra đến cả số còn không có cặp giống chủ tus" , còn nếu như có 1 cặp thì in ra như mẫu bên dưới

input : dòng đầu tiên sẽ nhập số n và x
Dòng thứ 2 nhập n số

output:Nếu như có cặp thì in ra như output mẫu phía dưới , còn ko có cặp nào thì in ra "thì ra đến cả số còn không có cặp giống chủ tus".

example
input 
7 7
1 4 3 2 5 8 6

output
(1,6)
(4,3)
(2,5)

'''

n_x = input().split()
n, x = int(n_x[0]), int(n_x[1])
arr = list(map(int, input().split()))

pairs = []
for i in range(n):
    need = x - arr[i]
    # tìm một phần tử phía sau
    for j in range(i + 1, n):
        if arr[j] == need:
            pairs.append((arr[i], arr[j]))
            break  # chỉ lấy cặp với phần tử xuất hiện sớm nhất

if not pairs:
    print("thì ra đến cả số còn không có cặp giống chủ tus")
else:
    for a, b in pairs:
        print(f"({a},{b})")