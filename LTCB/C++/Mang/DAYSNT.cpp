#include <iostream>
#include <cmath>
using namespace std;

#define sn int
#define nhap cin 
#define xuat cout 
#define kt return 0

sn snt(sn n){
    if(n < 2) return 0;
    for(sn i = 2; i <= sqrt(n); i++){
        if(n%i == 0) return 0;
    }
    return 1;
}

sn main(){
    sn k;
    nhap >> k;
    sn a[100];
    sn n = 0;
    sn x;
    while(nhap >> x){
        a[n] = x;
        n++;
    }
    sn max_snt = -1;
    for(sn i = 0; i < n; i++){
        if(a[i] <= k && snt(a[i])){
            if(max_snt == -1 || a[i] > max_snt){ // Điều kiện này bỏ cũng đc nhưng nếu bỏ thì max_snt sẽ là giá trị đầu tiên tìm thấy, không phải giá trị lớn nhất
                // Nếu max_snt = -1 thì chưa có số nguyên tố nào thỏa mãn điều kiện
                // Nếu a[i] > max_snt thì cập nhật max_snt
                max_snt = a[i];
            }
        }
    }
/*
i = 0: a[0] = 5, 5 ≤ 9 ✓, snt(5) ✓ → max_snt = 5
i = 1: a[1] = 4, 4 ≤ 9 ✓, snt(4) ✗ → bỏ qua
i = 2: a[2] = 7, 7 ≤ 9 ✓, snt(7) ✓, 7 > 5 → max_snt = 7
i = 3: a[3] = 11, 11 ≤ 9 ✗ → bỏ qua
i = 4: a[4] = 10, 10 ≤ 9 ✗ → bỏ qua
i = 5: a[5] = 13, 13 ≤ 9 ✗ → bỏ qua
*/
    xuat << max_snt;
    kt;
}