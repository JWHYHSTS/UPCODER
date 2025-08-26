/*
Cau 4:
Viết chương trình thực hiện các yêu cầu sau:
1. Xây dựng cấu trúc dữ liệu để lưu trữ các Phân số (PS), bao gồm tử số
và mẫu số (kiểu số nguyên)
2. Viết hàm nhập danh sách các PS và hàm xuất ra theo thứ tự ngược lại
3. Viết hàm in ra PS có tử số nhỏ nhất và PS có mẫu số lớn nhất
4. Viết hàm xuất số lượng PS có tử số là số nguyên tố
5. Viết hàm xuất số lượng PS có tử số và mẫu số là nguyên tố cùng nhau
(Hướng dẫn: 2 số a và b được gọi nguyên tố cùng nhau khi và chỉ chỉ khi
ước chung lớn nhất của a và b bằng 1)
Input:
Chứa 1 số nguyên n.
n dòng tiếp theo, mỗi dòng là 1 cặp số nguyên cho biết tử số và mẫu sốOutput:
Dòng 1: danh sách các PS theo thứ tự ngược lại so với thứ tự nhập. Mỗi PS
được in ra theo định dạng {tử số}/{mẫu số}, mỗi PS cách nhau 1 khoảng
trắng
Dòng 2: PS có tử số nhỏ nhất và PS có mẫu số lớn nhất
Dòng 3: số lượng PS có tử số là số nguyên tố
Dòng 4: số lượng PS có tử số và mẫu số là nguyên tố cùng nhau
Ví dụ:
Input
4
1 2
4 3
5 6
7 8
Output
7/8 5/6 4/3 1/2
1/2 7/8
2
4

*/

#include <bits/stdc++.h>
using namespace std;

struct PS{
    int tu, mau;

    void nhap() {
        cin >> tu >> mau;
    }

    void xuat() const {
        cout << tu << "/" << mau;
    }

    bool isPrime() const {
        if (tu < 2) return false;
        for (int i = 2; i <= sqrt(tu); i++) {
            if (tu % i == 0) return false;
        }
        return true;
    }

    bool isCoprime() const {  
        return __gcd(abs(tu), abs(mau)) == 1;
    }
};

int main(){
    int n;
    cin >> n;
    vector<PS> psList(n);

    for (int i = 0; i < n; i++) {
        psList[i].nhap();
    }

    // 1. Xuất danh sách PS theo thứ tự ngược lại
    for (int i = n - 1; i >= 0; i--) {
        psList[i].xuat();
        if (i > 0) cout << " ";
    }
    cout << endl;

    // 2. Tìm PS có tử số nhỏ nhất và PS có mẫu số lớn nhất
    PS minTu = psList[0], maxMau = psList[0];
    for (const auto& ps : psList) {
        if (ps.tu < minTu.tu) minTu = ps;
        if (ps.mau > maxMau.mau) maxMau = ps;
    }
    minTu.xuat();
    cout << " ";
    maxMau.xuat();
    cout << endl;

    // 3. Số lượng PS có tử số là số nguyên tố
    int countPrime = 0;
    for (const auto& ps : psList) {
        if (ps.isPrime()) countPrime++;
    }
    cout << countPrime << endl;

    // 4. Số lượng PS có tử số và mẫu số là nguyên tố cùng nhau
    int countCoprime = 0;
    for (const auto& ps : psList) { 
        if (ps.isCoprime()) countCoprime++;
    }
    cout << countCoprime << endl;

    return 0;
}

/* Cách 2: không dùng vector

#include <bits/stdc++.h>
using namespace std;

struct PS{
    int tu, mau;

    void nhap() {
        cin >> tu >> mau;
    }

    void xuat() const {
        cout << tu << "/" << mau;
    }

    bool isPrime() const {
        if (tu < 2) return false;
        for (int i = 2; i <= sqrt(tu); i++) {
            if (tu % i == 0) return false;
        }
        return true;
    }

    bool isCoprime() const {  
        return __gcd(abs(tu), abs(mau)) == 1;
    }
};

int main(){
    int n;
    cin >> n;
    PS psList[100];

    for (int i = 0; i < n; i++) {
        psList[i].nhap();
    }

    // 1. Xuất danh sách PS theo thứ tự ngược lại
    for (int i = n - 1; i >= 0; i--) {
        psList[i].xuat();
        if (i > 0) cout << " ";
    }
    cout << endl;

    // 2. Tìm PS có tử số nhỏ nhất và PS có mẫu số lớn nhất
    PS minTu = psList[0], maxMau = psList[0];
    for (int i = 1; i < n; i++) { 
        if (psList[i].tu < minTu.tu) minTu = psList[i];
        if (psList[i].mau > maxMau.mau) maxMau = psList[i];
    }
    minTu.xuat();
    cout << " ";
    maxMau.xuat();
    cout << endl;

    // 3. Số lượng PS có tử số là số nguyên tố
    int countPrime = 0;
    for (int i = 0; i < n; i++) { 
        if (psList[i].isPrime()) countPrime++;
    }
    cout << countPrime << endl;

    // 4. Số lượng PS có tử số và mẫu số là nguyên tố cùng nhau
    int countCoprime = 0;
    for (int i = 0; i < n; i++) {  
        if (psList[i].isCoprime()) countCoprime++;
    }
    cout << countCoprime << endl;

    return 0;
}
*/