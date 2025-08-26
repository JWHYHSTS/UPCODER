#include <iostream>
using namespace std;

#define sn int
#define nhap cin 
#define xuat cout
#define kt return 0

sn main(){
    sn n, m;
    nhap >> n >> m;
    sn a[100][100];
    sn gtri = 1;
    for(sn i = 0; i < n; i++){
        if(i % 2 == 0){ // Dòng chẵn (0, 2, 4, ...) đi từ trái sang phải
            for(sn j = 0; j < m; j++){ // Dòng chẵn đi từ trái sang phải
                a[i][j] = gtri++;
            }
        }
        else{
            for(sn j = m - 1; j >= 0; j--){ // Dòng lẻ (1, 3, 5, ...) đi từ phải sang trái
                // Dòng lẻ đi từ phải sang trái
                a[i][j] = gtri++;
            }
        }
    }
    for(sn i = 0; i < n; i++){
        for(sn j = 0; j < m; j++){
            xuat << a[i][j] << " ";
        }
        xuat << endl;
    }
    kt;
}