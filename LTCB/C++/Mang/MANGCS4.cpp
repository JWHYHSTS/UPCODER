#include <iostream>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn n,m;
    nhap >> n >> m;
    sn a[100][100];
    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < m; j++){
            nhap >> a[i][j];
        }
    }
    for(sn i = 0; i < n - 1; i++){
        for(sn j = i + 1; j < n; j++){ // sn j = i + 1; // Bắt đầu so sánh từ phần tử tiếp theo của i
            if(a[i][0] > a[j][0]){
                for(sn k = 0; k < m; k++){
                    sn temp = a[i][k];
                    a[i][k] = a[j][k];
                    a[j][k] = temp;
                }
            }
        }
    }
    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < m; j++){
            xuat << a[i][j] <<" ";
        }
        xuat << endl;
    }
    kt;
}