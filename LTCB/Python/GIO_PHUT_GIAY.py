'''
Viết chương trình nhập vào giờ, phút, giây. Kiểm tra giờ, phút, giây đó có hợp lệ hay không, nếu hợp lệ hãy cho biết giờ sau đó 1 giây là bao nhiêu?
Dữ liệu vào: 3 số nguyên lần lượt là giờ, phút, giây.
Dữ liệu ra: 
- Dòng đầu xuất "YES" nếu hợp lệ, ngược lại xuất "NO" nếu không hợp lệ.
- Dòng thứ hai xuất giờ sau đó 1 giây nếu hợp lệ.

Ví dụ:

Input	
3 
59 
60
Output
NO

Input	
1 
59 
59
Output
YES
2:0:0
'''
g = int(input())
p = int(input())
s = int(input())
if 0 <= g < 24 and 0 <= p < 60 and 0 <= s < 60:
    print("YES")
    s += 1
    if s == 60:
        s = 0
        p += 1
        if p == 60:
            p = 0
            g += 1
            if g == 24:
                g = 0
    print(f"{g}:{p}:{s}")
else:
    print("NO")
