/*
Cho số nguyên dương n. Hãy đưa ra số lượng chữ số của n và tổng các chữ số trong biểu diễn thập phân của n.

Input:

Gồm một số nguyên dương duy nhất.

Output:

Gồm hai dòng, dòng thứ nhất chứa số chữ số và dòng thứ hai chứa tổng chữ số của n.

Ví dụ:


Input
66
Output
2
12

*/
#include <iostream>
using namespace std;
int TongChuSo(int n){
    int tong = 0;
    int dem = 0;
    while(n > 0){
        tong += n % 10;
        n /= 10;
        dem++;
    }
    cout << dem << endl;
    return tong;
}
int main(){
    int n;
    cin >> n;
    cout << TongChuSo(n) << endl;
}