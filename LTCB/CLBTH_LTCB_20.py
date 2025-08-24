'''
Một kỳ thi Tin học có ba thí sinh tham dự (có vẻ kỳ thi này khá kín tiếng). Ban tổ chức kỳ thi có ba giải thưởng trị giá là t1, t2, t3 (chỉ số của các trị giá này không theo thứ tự xếp giải). Thí sinh được xếp hạng cao hơn sẽ nhận được giải thưởng có giá trị cao hơn.

Bạn hãy cho biết người đạt giải nhất và người đạt giải ba nhận được giải thưởng có trị giá là bao nhiêu?

Input:

Một dòng chứa ba số nguyên dương t1, t2, t3 là trị giá của các giải thưởng.

Output:

Dòng đầu tiên ghi giải thưởng cho người được giải nhất.

Dòng thứ hai ghi giải thưởng cho người được giải ba.

Ví dụ:
Input
2 1 3
Output
3
1
'''
arr = list(map(int, input().strip().split()))
arr.sort()
print(arr[2])
print(arr[0])