#include <iostream>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout 
#define kt return 0

sn main(){
    char c;
    sn dem[256] = {0};
    while(nhap >> c){
        if(c >= 'a' && c <= 'z'){
            dem[c - 'a']++; // Tăng số lần xuất hiện của ký tự c trong mảng dem
        }
    }
    for(sn i = 0; i < 26; i++){
        if(dem[i] > 0){
            xuat << (char)(i + 'a') << ":" << dem[i] << endl; // In ký tự và số lần xuất hiện của nó
        }
    }
    kt;
}