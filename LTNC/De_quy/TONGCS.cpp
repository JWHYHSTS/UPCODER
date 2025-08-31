#include <iostream>
using namespace std;

long long sum_digits(long long n){
    if(n < 10) return n;
    return n%10 + sum_digits(n/10);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n;
    if(!(cin >> n)) return 0;
    cout << sum_digits(n);
    return 0;
}