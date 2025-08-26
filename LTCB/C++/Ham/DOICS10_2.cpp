#include <iostream>
#include <stack>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout
#define kt return 0

sn main(){
    sn n;
    nhap >> n;
    if(n == 0){
        xuat << "0";
        return 0;
    }
    stack<sn>s;
    while(n>0){
        s.push(n%2);
        n /= 2;
    }
    while(!s.empty()){
        xuat<< s.top();
        s.pop();
    }
    kt;
}