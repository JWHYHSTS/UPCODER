'''

Anagram là thuật ngữ để chỉ hai chuỗi có số ký tự và các ký tự giống nhau, nhưng thứ tự của các ký tự trong chuỗi có thể khác nhau.

Ví dụ: hai chuỗi listen và sliten là anagram.

Hãy viết chương trình để kiểm tra hai chuỗi có phải là Anagram với nhau hay không?

 

Lưu ý: có thể dùng chuỗi dạng C-string hoặc String class để thực hiện.

 

Input:

-       Dòng 1: chuỗi thứ nhất

-       Dòng 2: chuỗi thứ hai

Output:

-       YES nếu hai chuỗi là Anagram

-       NO nếu hai chuỗi không phải là Anagram


Ví dụ 1:
Input	
listen
stilen
Output
YES

Ví dụ 2:
Input	
upcoder hcmup
upcoder.hcmup
Output
NO


'''

s1 = input().strip()
s2 = input().strip()

if sorted(s1) == sorted(s2):
    print("YES")
else:
    print("NO")