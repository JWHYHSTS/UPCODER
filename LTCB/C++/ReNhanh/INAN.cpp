    #include <iostream>
    #include <cmath>
    using namespace std;

    #define nt int
    #define ll long long
    #define nhap cin
    #define xuat cout
    #define va &&
    #define kt return 0 

    nt main(){
        ll t,c,p;
        nhap >> t >> c >> p;
        if( t == 1 ) xuat << c*p;
        else xuat << ((c+1)/2)*p;
        kt; 
    }