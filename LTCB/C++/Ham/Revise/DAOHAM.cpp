/*
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
*/
#include <iostream>
#include <cmath>
using namespace std;

struct DonThuc
{
    double a;
    int n;
};

struct DaThuc
{
    int size;
    DonThuc arr[100];

    void nhapDaThuc()
    {
        cin >> size;
        for (int i = 0; i < size; i++)
            cin >> arr[i].a;
        for (int i = 0; i < size; i++)
            cin >> arr[i].n;
        return;
    }

    void xuatDaThuc()
    {
        bool check = false;
        for (int i = 0; i < size; i++)
        {
            if (arr[i].a != 0)
            {
                if (i == 0 && arr[i].a < 0)
                    cout << "-";

                if (check && arr[i].a < 0)
                    cout << " - ";
                else if (check && arr[i].a > 0)
                    cout << " + ";

                if (abs(arr[i].a) != 1 || (abs(arr[i].a) == 1 && arr[i].n == 0))
                {
                    cout << abs(arr[i].a);
                    check = true;
                }

                if (arr[i].n != 0)
                {
                    cout << "x";
                    if (arr[i].n > 1)
                        cout << "^" << arr[i].n;
                }
            }
        }
        return;
    }

    double giaTri(int x)
    {
        double res = 0;
        for (int i = 0; i < size; i++)
            res += arr[i].a * pow(x, arr[i].n);
        return res;
    }

    void xuatDaoHam()
    {
        DaThuc res;
        res.size = this->size;
        for (int i = 0; i < this->size; i++)
        {
            if (this->arr[i].n > 0)
                res.arr[i].a = this->arr[i].a * this->arr[i].n,
                res.arr[i].n = this->arr[i].n - 1;
            else
                res.arr[i].a = 0,
                res.arr[i].n = 0;
        }
        res.xuatDaThuc();
        return;
    }
};

int main()
{
    double x;
    DaThuc daThuc;
    daThuc.nhapDaThuc();
    daThuc.xuatDaThuc();
    cout << endl;

    cin >> x;
    cout << daThuc.giaTri(x) << endl;
    daThuc.xuatDaoHam();
    cout << endl;
    return 0;
}