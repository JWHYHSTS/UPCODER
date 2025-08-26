/*
Cho một chuỗi kí tự gồm n kí tự bất kỳ (chữ số hoặc chữ cái). Hãy đổi tất cả chữ hoa có trong chuỗi thành chữ thường. Xuất chuỗi ra màn hình.
Input:

Gồm một dòng duy nhất là một chuỗi kí tự (độ dài không quá 100).

Output:

In chuỗi đã đổi ra màn hình.

Ví dụ:


Input
4I1K2D14Ti

Output
4i1k2d14ti

*/
#include <iostream>
#include <string>
using namespace std;
int main(){
    string n;
    getline(cin, n);
    for(size_t i = 0; i < n.length(); i++){
        if(n[i] >= 'A' && n[i] <= 'Z'){
            n[i] += 32;
        }
    }
    cout << n;
    return 0;
}

/*
Cách 2: Sử dụng hàm tolower()
#include <iostream>
#include <string>
using namespace std;
int main(){
    string n;
    getline(cin, n);
    for(int i = 0; i < n.length(); i++){
        n[i] = tolower(n[i]); 
    }
    cout << n;
    return 0;
}

*/