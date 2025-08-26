/*

Nhập vào từ bàn phím một xâu ký tự S, in ra màn hình số lượng kí tự chỉ xuất hiện đúng 1 lần trong xâu S.

Input:

Một chuỗi S chỉ chứa các ký tự chữ cái và có không quá 255 kí tự.

Output:

Kết quả của bài toán.

Ví dụ:


Input
abbacdmedc

Output
2

Giải thích: Trong xâu kí tự được nhập từ bàn phím có 2 kí tự là m và e chỉ xuất hiện đúng 1 lần

*/

#include <iostream>
#include <string>
using namespace std;
int main(){
    string n;
    getline(cin, n);
    int dem = 0;
    for(int i = 0; i <n.length(); i++){
        int count = 0;
        for(int j = 0; j < n.length(); j++){
            if(n[i] == n[j]) count++; // VD code nhập "abbacdmedc" thì n[i] = 'a' và n[j] = 'a' thì count sẽ tăng lên 2, còn nếu n[i] = 'b' thì count sẽ tăng lên 2 còn đối với n[i] = 'm' thì count sẽ tăng lên 1 bởi vì chỉ có một ký tự 'm' trong chuỗi
        }
        if(count == 1) dem++;
    }
    cout << dem;
    return 0;
}

// Cách 2:
/*
#include <iostream>
#include <string>
using namespace std;
int main(){
    string n;
    getline(cin, n);
    int dem = 0;
    for(int i = 0; i < n.size(); i++){
        if(n.find(n[i]) == n.rfind(n[i])){ // Sử dụng find và rfind để kiểm tra xem ký tự n[i] chỉ xuất hiện một lần VD: nếu nhập "abbacdmedc" thì n.find('m') == n.rfind('m') == 7 và n.find('e') == n.rfind('e') == 8
            dem++;
        }
    }
    cout << dem;
    return 0;
}
*/