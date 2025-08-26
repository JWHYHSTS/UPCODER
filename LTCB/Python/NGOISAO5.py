'''
Viết chương trình in ra màn hình tam giác sao ngược với chiều cao h nhập vào từ bàn phím.

Ví dụ:
Input:
3

Output:
*****
 *** 
  *  

Input:
5

Output:
*********
 ******* 
  *****  
   ***   
    *    

Input:
6

Output:
***********
 ********* 
  *******  
   *****   
    ***    
     *     
Lưu ý: 
Xuất chính xác từng ký tự. Không xuất dư hoặc thiếu khoảng trắng, không xuất dư endl dòng cuối cùng.
'''
h = int(input())
for i in range(h):
    spaces = ' ' * i
    stars = '*' * (2 * (h - i) - 1)
    line = spaces + stars + spaces
    if i != h - 1:
        print(line)
    else:
        print(line, end="")