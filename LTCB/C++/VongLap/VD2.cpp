#include <iostream>
using namespace std;

#define nt int
#define nhap cin
#define xuat cout
#define kt return 0

nt main(){
    int n;
    nhap >> n;
    for(int i = 1; i <= n; i++){
        if(n % i == 0){
            xuat << i <<" ";
        }
    }
    kt;
}