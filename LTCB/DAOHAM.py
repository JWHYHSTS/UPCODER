'''
Cho đa thức P(x) = a1xn1 + a2xn2 + a3xn3 + … + akxnk
với a1, a2, …, ak là giá trị số thực bất kỳ; n1, n2, …, nk là giá trị số nguyên bất kỳ
Xây dựng chương trình làm việc với danh sách các đa thức với các thao tác:
1. Nhập đa thức
2. Xuất đa thức
3. Tính đa thức khi biết giá trị x
4. Tính đạo hàm của đa thức

Dữ liệu đầu vào:
- Dòng đầu tiên chứa số nguyên k cho biết số lượng đơn thức trong đa thức
- Dòng thứ hai chứa k số thực không âm lần lượt là các giá trị từ a1 đến ak
- Dòng thứ ba chứa k số nguyên không âm lần lượt là các giá trị từ n1 đến nk
- Dòng thứ ba chứa giá trị của số thực x
Dữ liệu đầu ra:
- Dòng đầu tiên là đa thức vừa nhập được in ra theo cú pháp a1x^n1 + a2x^n2 + a3x^n3 + ... + akx^nk. Mỗi đơn thức và toán tử cách nhau 1 khoảng trắng.
- Dòng thứ hai là giá trị đa thức tương ứng với giá trị số thực x nhập vào
- Dòng thứ ba là đa thức đạo hàm của đa thức ban đầu. Mỗi đơn thức và toán tử cách nhau 1 khoảng trắng.

*Lưu ý: nếu đơn thức akx^nk có:
+ ak = 0 thì không cần xuất
+ ak = 1 thì xuất dưới dạng x^nk
+ nk = 0 thì xuất dưới dạng ak
+ nk = 1 thì xuất dưới dạng akx

Vd:
input:
5
5 4 3 2 1
0 1 2 3 4
2
output:
5 + 4x + 3x^2 + 2x^3 + x^4
57
4 + 6x + 6x^2 + 4x^3

'''
def format_term(a, n):
    if a == 0:
        return ""
    if n == 0:
        return f"{int(a) if a == int(a) else a}"
    if a == 1:
        if n == 1:
            return "x"
        else:
            return f"x^{n}"
    else:
        if n == 1:
            return f"{int(a) if a == int(a) else a}x"
        else:
            return f"{int(a) if a == int(a) else a}x^{n}"

def print_poly(a_list, n_list):
    terms = []
    for a, n in zip(a_list, n_list):
        t = format_term(a, n)
        if t != "":
            terms.append(t)
    return " + ".join(terms) if terms else "0"

def eval_poly(a_list, n_list, x):
    return sum(a * (x ** n) for a, n in zip(a_list, n_list))

def derivative(a_list, n_list):
    da = []
    dn = []
    for a, n in zip(a_list, n_list):
        if n == 0:
            continue
        da.append(a * n)
        dn.append(n - 1)
    return da, dn

# Input
k = int(input())
a_list = list(map(float, input().split()))
n_list = list(map(int, input().split()))
x = float(input())

# Output
print(print_poly(a_list, n_list))
print(int(eval_poly(a_list, n_list, x)) if eval_poly(a_list, n_list, x) == int(eval_poly(a_list, n_list, x)) else eval_poly(a_list, n_list, x))
da, dn = derivative(a_list, n_list)
print(print_poly(da, dn))