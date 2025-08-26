/*
Cho một số nguyên dương n, hãy phân tích n thành tích các thừa số nguyên tố.

Input:

Gồm một số nguyên dương n duy nhất (2 ≤ n ≤ 10^6).

Output:

Gồm một dòng in ra các thừa số nguyên tố (sau khi phân tích n) theo thứ tự từ bé đến lớn.

Ví dụ:


Input
60
Output
2 2 3 5
// Giải thích lý do tại sao đầu vào là 60 và đầu ra là 2 2 3 5:
// 60 có thể được phân tích thành 2 * 2 * 3 * 5.
// Các thừa số nguyên tố của 60 là 2, 3 và 5
*/
#include <iostream>
#include <cmath>
using namespace std;
int main() {
    int n;
    cin >> n;
    for (int i = 2; i <= sqrt(n); i++) {
        while (n % i == 0) {
            cout << i << " ";
            n /= i; // Chia n cho i để tiếp tục phân tích 
        }
    }
    if (n > 1) { // Điều kiện if(n > 1) để in ra thừa số nguyên tố cuối cùng nếu n còn lớn hơn 1
        // Nếu n còn lớn hơn 1, thì n chính là một thừa số nguyên tố
        cout << n;  
    }
    return 0;
}
/*

#include <iostream>
#include <cmath>
using namespace std;
int SNT(int n){
    if(n < 2) return 0;
    for(int i = 2; i <= sqrt(n); i++){
        if(n % i == 0) return 0;
    }
    return 1;
}
int main(){
    int n;
    cin >> n;
    for(int i = 2; i <= n; i++){
        while(n % i == 0 && SNT(i)){
            cout << i << " ";
            n /= i;
        }
    }
    return 0;
}
*/
// VD: Lý do tại sao nhập n = 60 thì kết quả là 2 2 3 5:
// 60 = 2 * 30
// 30 = 2 * 15
// 15 = 3 * 5
// Như vậy, 60 được phân tích thành 2 * 2 * 3 * 5.
// Các thừa số nguyên tố của 60 là 2, 3 và 5