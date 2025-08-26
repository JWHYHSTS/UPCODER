#include <iostream>
#include <bits/stdc++.h>
using namespace std;

#define nt int
#define nhap cin
#define xuat cout
#define ktu char
#define kt return 0

void c1(){
    nt a,b;
    nhap >> a >> b;
    ktu pt; 
    nhap >> pt; 
    switch (pt){
        case '+': xuat << a <<"+"<<b<<"="<<a+b; break; 
        case '-': xuat << a <<"-"<<b<<"="<<a-b; break;
        case '*': xuat <<a <<"*" <<b<<"="<<a*b; break; 
        case '%': xuat <<a <<"%" <<b<<"="<<a%b; break;    
    }
}

void c2(){
    nt a,b;
    nhap >> a >> b;
    ktu pt; 
    nhap >> pt;
    if(pt == '+'){
        xuat << a << "+" << b << "=" << a + b;
    } else if(pt == '-'){
       xuat << a <<"-" << b <<"=" << a - b;
    } else if(pt  == '*'){
        xuat << a << "*" << b << "=" << a * b;
    } else if(pt == '%'){
        xuat << a << "%" << b << "=" << a % b;
    } else {
        xuat << "ERROR";
    }
}
nt main(){
    c2();
    kt; 
}