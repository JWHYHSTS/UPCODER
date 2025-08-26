#include <iostream>
#include <stack>
using namespace std;

#define sn int
#define ll long long
#define nhap cin
#define xuat cout
#define kt return 0

void chuyencs(ll sohe10, sn hecosomoi = 0 ){
    stack<char> st;
    sn heso;
    if(hecosomoi == 0) heso = 2;
    else if(hecosomoi == 1) heso = 8;
    else heso = 16;
    if(sohe10 == 0) {
        xuat << "0";
        return;
    }
    while(sohe10 > 0){
        sn du = sohe10 % heso;
        if(du < 10) st.push('0'+du);
        else st.push('A' + du - 10);
        sohe10 /= heso;
    }
    while(!st.empty()){
        xuat << st.top();
        st.pop();
    }
}

sn main(){
    ll n;
    sn he;
    nhap >> n >> he;
    chuyencs(n, he);
    kt;
}