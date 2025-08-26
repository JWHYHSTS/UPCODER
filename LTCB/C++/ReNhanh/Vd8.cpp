#include <iostream>
using namespace std;
#define nt int
#define nhap cin
#define xuat cout
#define kt return 0
#define va &&
#define hoac ||

int main(){
    nt n,m;
    nhap >> n >> m;
    if(n == 1 hoac n == 3 hoac n == 5 hoac n == 7 hoac n == 8 hoac n == 10 hoac n == 12 ){
        cout << 31;
    } else if( n == 4 hoac n == 6 hoac n == 9 hoac n == 11 ){
        cout << 30;
    } else if( n == 2){
        if(m % 400 hoac (m%4 == 0 va m%100 != 0)){
            cout << 29;
        }else {
            cout<< 28; 
        }
    }
    else {
        cout << "ERROR"; 
    }
    kt; 
}