'''
Sau khi quên làm bài tập về nhà của mình, bạn đã được cô giáo ra yêu cầu chép phạt N lần câu “Có chí thì nên”. Tuy nhiên, bạn đã nghĩa ra cách lập trình để không phải chép quá nhiều lần câu chép phạt đó.

Hãy in ra N lần câu chép phạt trên và đánh số cho từng câu theo định dạng “#: Co chi thi nen”. Trong đó, kí tự “#” thể hiện số thứ tự của câu.

Input:

Một dòng duy nhất chứa số nguyên dương N.

Output:

In ra N câu chép phạt theo yêu cầu nêu trên.

Ví dụ:


Input
3
Output
1: Co chi thi nen
2: Co chi thi nen
3: Co chi thi nen
'''
n = int(input().strip())

for i in range(1, n + 1):
    print(f"{i}: Co chi thi nen")