'''
Tìm số tự nhiên có 3 chữ số, biết chữ số hàng chục thua hàng đơn vị 3 đơn vị và hàng đơn vị hơn hàng trăm 6 đơn vị. Nếu xen chữ số 0 vào giữa hàng đơn vị và hàng chục thì được số mới lớn hơn số đã cho 2250 đơn vị.

Input	Output

Số tìm được theo yêu cầu đề.
'''
for a in range(100, 1000):
    don_vi = a % 10
    chuc = (a // 10) % 10
    tram = a // 100
    if chuc == don_vi - 3 and don_vi == tram + 6:
        b = don_vi + 0*10 + chuc*100 + tram*1000  
        if b - a == 2250:
            print(a)