// Tìm hàng, cột có nhiều số nguyên tố nhất
#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin 
#define xuat cout 
#define kt return 0
#define Max 10000000
#define Min -10000000

sn snt(sn n){
    if(n < 2) return 0;
    for(sn i = 2; i <= sqrt(n); i++){
        if(n % i == 0) return 0;
    }
    return 1;
}

sn main(){
    sn n, m;
    nhap >> n >> m;
    sn a[100][100];
    for(sn i = 0; i < n ; i++){
        for(sn j = 0; j < m; j++){
            nhap >> a[i][j];
        }
    }
    // Tìm hàng có nhiều số nguyên tố nhất
    sn kq = 0, hang = -1; // Khởi tạo hang = -1 để kiểm tra nếu không có hàng nào có số nguyên tố
    for(sn i = 0; i < n; i++){
        sn dem = 0;
        for(sn j = 0; j < m; j++){
            if(snt(a[i][j])){
                dem++;
            }
        }
        if(dem > kq){
            kq = dem;
            hang = i; // Lưu số hàng (bắt đầu từ 0)
        }
    }
    if(kq == 0) xuat << "Ko co so nguyen to";
    else xuat << "Hang " << hang << " co nhieu so nguyen to nhat: " << kq << endl;
    // Tìm cột có nhiều số nguyên tố nhất (nếu có nhiều cột có cùng số nguyên tố thì chọn cột có số thứ tự lớn hơn)
    sn kq1 = 0, cot = -1; // Khởi tạo cot = -1 để kiểm tra nếu không có cột nào có số nguyên tố
    for(sn j = 0; j < m; j++){
        sn dem1 = 0;
        for(sn i = 0; i < n; i++){
            if(snt(a[i][j])){
                dem1++;
            }
        }
        if(dem1 >= kq1){ // Dùng >= để ưa tiên cột có số thứ tự lớn hơn nếu có cùng số nguyên tố
            kq1 = dem1;
            cot = j; // Lưu số cột (bắt đầu từ 1)
        }
    }
    if(kq1 == 0) xuat << "Ko co so nguyen to";
    else xuat << "Cot " << cot << " co nhieu snt nhat: " << kq1 << endl;
    kt;
}