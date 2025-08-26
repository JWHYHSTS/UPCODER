#include <iostream>
using namespace std;
#define nt int
#define nhap cin
#define xuat cout
#define kt return 0
#define va && 

int main(){
    nt n;
    nhap >> n;
    if( n % 3 == 0 va n % 5 == 0){
        cout << 1;
    } else{
        cout << 0; 
    }
    kt;
}