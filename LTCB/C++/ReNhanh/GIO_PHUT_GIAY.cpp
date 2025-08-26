#include <iostream>
using namespace std;

#define nt int 
#define nhap cin
#define xuat cout
#define va &&
#define hoac ||
#define kt return 0

nt main(){
    int gio, phut, giay;
    nhap >> gio >> phut >> giay;
    if((gio < 0 hoac gio > 23) hoac (phut < 0 hoac phut > 59) hoac (giay < 0 hoac giay > 59)){
        cout <<"NO";
    }else {
        cout <<"YES"<<endl;
        giay++;
        if(giay == 60){
            giay = 0;
            phut++;
        }
        if(phut == 60){
            phut = 0;
            gio++;
        }
        if(gio == 24){
            gio = 0;
        }
        cout <<gio<<":"<<phut<<":"<<giay;
    }
    kt;
}