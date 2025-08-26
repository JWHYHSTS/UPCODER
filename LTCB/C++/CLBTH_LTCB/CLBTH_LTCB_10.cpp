/*
Cho một số nguyên dương n, hãy chuyển n từ hệ thập phân sang hệ nhị phân.

Input:

Gồm một số nguyên dương n duy nhất (n ≤ 10^18).

Output:

In ra số n dưới hệ nhị phân.

Ví dụ:


Input
5
Output
101
*/
#include <iostream>
using namespace std;
#define ll long long
int ChuyenCoSo(ll n, int base) {
    if (n == 0) return 0; 
    string result = "";
    while (n > 0) {
        result = to_string(n % base) + result; 
        n /= base; 
    }
    cout << result; 
    return 0;
}
int main(){
    ll n;
    cin >> n;
    ChuyenCoSo(n, 2);
    return 0;
}

/*
Cách 2:
#include <iostream>
using namespace std;
int main(){
    long long n;
    cin >> n;
    string kq = "";
    while(n > 0){
        kq = to_string(n % 2) + kq; 
        n /= 2; 
    }
    cout << kq; 
    return 0;
}
*/
/*
Cách 3: Sử dụng đệ quy
#include <iostream>
using namespace std;

void convertToBinary(long long n){
    if(n == 0) return;
    convertToBinary(n / 2);
    cout << n % 2;
}

int main(){
    long long n;
    cin >> n;
    
    if(n == 0){
        cout << 0;
    } else {
        convertToBinary(n);
    }
    
    return 0;
}
*/

/*Cách 4: Sử dụng stack
#include <iostream>
#include <stack>
using namespace std;

int main(){
    long long n;
    cin >> n;
    
    if(n == 0){
        cout << 0;
        return 0;
    }
    
    stack<int> s;
    
    while(n > 0){
        s.push(n % 2);
        n /= 2;
    }
    
    while(!s.empty()){
        cout << s.top();
        s.pop();
    }
    
    return 0;
}
*/

/*
Cách 5: Sử dụng mảng và in ngược
#include <iostream>
using namespace std;
int main(){
    long long n;
    cin >> n;
    int np[64]; //Lý do chọn 64 là vì 2^64 > 10^18, đủ để chứa tất cả các số trong khoảng này
    int temp = 0;
    while(n > 0){
        np[temp++] = n % 2;
        n /= 2;
    }
    for(int i = temp - 1; i >= 0; i--){
        cout << np[i];
    }
    return 0;
}
*/
