//  Nhập vào các số tự nguyên, kết thúc nhập bằng cách nhập số 0 và chỉ tính tổng các số nguyên dương được nhập
#include <iostream>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn n, tong = 0;
    while (true){
        nhap >> n;
        if(n < 0){
            continue; // Bỏ qua số âm
        }
        else if(n == 0) break; // Kết thúc khi nhập 0
        tong += n; // Tổng các số nguyên dương
        xuat << n <<" ";
    }
    xuat << endl; // Xuất dòng mới sau khi in các số
    xuat << tong; 
    kt;
}