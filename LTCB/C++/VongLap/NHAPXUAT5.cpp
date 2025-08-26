#include <iostream>
using namespace std;

#define sn int
#define chuoi string
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn n;
    chuoi s; 
    nhap >> n >> s;
    bool ktra = false;
    //if (n >= 0 && n < s.length()){
    //    xuat << s[n];
    //} else xuat << "-1";
    for(sn j = 0; j < s.length(); j++){
        if(j == n){
            xuat << s[j];
            ktra = true;
            break;
        }
    }
    if(!ktra) xuat << "-1";
    kt;
}