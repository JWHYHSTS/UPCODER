'''
Viết chương trình in ra màn hình tam giác sao rỗng (nghĩa là chỉ in đường viền cạnh của tam giác) với chiều cao h nhập vào từ bàn phím.

Ví dụ:
Input:
3

Output:
  *  
 * * 
*****

Input:
5

Output:
    *    
   * *   
  *   *  
 *     * 
*********

Input:
6

Output:
     *     
    * *    
   *   *   
  *     *  
 *       * 
***********
Lưu ý: 

Xuất chính xác từng ký tự. Không xuất dư hoặc thiếu khoảng trắng, không xuất dư endl dòng cuối cùng.
'''

h = int(input())
for i in range(h):
    line = ""
    for j in range(2 * h - 1):
        if i == h - 1:
            line += "*"
        else:
            if j == h - i - 1 or j == h + i - 1:
                line += "*"
            else:
                line += " "
    print(line, end="" if i == h - 1 else "\n")