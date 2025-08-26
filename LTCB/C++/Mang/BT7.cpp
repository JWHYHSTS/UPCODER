// Đếm số phần tử khác nhau trong mảng và số lần xuất hiện của chúng
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0
#define vl for
#define MAX 10000000
#define MIN -10000000

sn main(){
    sn n;
    nhap >> n;
    sn a[n];
    vl(sn i = 0; i < n; i++){
        nhap >> a[i];
    }

    sn dem = 0;
    sn khac[n]; // Mảng lưu các phần tử khác nhau
    sn idx = 0;

    for(sn i = 0; i < n; i++){
        sn checkgn = 1;
        for(sn j = 0; j < i; j++){
            if(a[i] == a[j]){
                checkgn = 0;
                break;
            }
        }
        if(checkgn == 1){
            dem++;
            // xuat << a[i] <<" "; // In ra các phần tử khác nhau
            khac[idx++] = a[i]; // Sử dụng mảng khac để lưu các phần tử khác nhau // Iidx++ dùng để tăng chỉ số của mảng khác (Nếu không dùng thì sẽ bị ghi đè lên phần tử trước đó)
            sn xh = 1;
            for(sn j = i + 1; j < n; j++){
                if(a[i] == a[j]) {
                    xh++;
                }
            }
            xuat << a[i] << " xuat hien " << xh << " lan\n";  
        }
    }
    // In các phần tử khác nhau trên 1 dòng
    xuat << "Cac phan tu khac nhau: ";
    for(sn i = 0; i < idx; i++){
        xuat << khac[i] << " ";
    }
    xuat << endl;
    xuat << dem;
    kt;
}