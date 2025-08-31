#include <bits/stdc++.h>
using namespace std;

int r1=3,y1=2,g1=5; // light 1
int r2=2,y2=4,g2=3; // light 2;
int cycle1 = r1+y1+g1; //10
int cycle2 = r2+y2+g2; //9

bool green1(int t){
    int x = t % cycle1;
    return x >= r1 + y1 && x < cycle1; // [5,10)
}
bool green2(int t){
    int x = t % cycle2;
    return x >= r2 + y2 && x < r2 + y2 + g2; // [6,9)
}

int search_rec(int t){
    if(green1(t) && green2(t)) return t;
    return search_rec(t+1);
}

int main(){
    cout << search_rec(0); // 6
    return 0;
}