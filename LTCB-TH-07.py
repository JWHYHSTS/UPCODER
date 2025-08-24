'''
Từ năm sinh, tính ra can chi cho năm sinh đó. Ta có 10 can và 12 chi như sau:
10 can: Canh, Tân, Nhâm, Quý, Giáp, Ất, Bính, Đinh, Mậu, Kỷ

12 chi (12 con giáp): Tý, Sửu, Dần, Mẹo, Thìn, Tỵ, Ngọ, Mùi, Thân, Dậu, Tuất, Hợi

Ta tính được can chi theo năm sinh nhờ số dư của phép chia lấy năm sinh chia cho 10 và 12, cụ thể



Input: 1984

Output: Giap Ty
'''

year = int(input().strip())

stems = ["Giap","At","Binh","Dinh","Mau","Ky","Canh","Tan","Nham","Quy"]
branches = ["Ty","Suu","Dan","Meo","Thin","Ty","Ngo","Mui","Than","Dau","Tuat","Hoi"]

can = stems[(year + 6) % 10]
chi = branches[(year + 8) % 12]

print(can, chi)