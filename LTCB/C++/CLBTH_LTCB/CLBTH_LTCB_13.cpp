/*

Cho một dãy A gồm n số nguyên a1, a2, a3,…, an và hai số nguyên v, T. Hãy tìm cách thêm số T vào vị trí v trong dãy A (các số ban đầu vẫn giữ nguyên thứ tự).

Input:

Dòng thứ nhất gồm ba số nguyên n, v, T.

Dòng tiếp theo gồm n số nguyên a1, a2, a3,…, an.

Output:

In ra dãy n + 1 số (các số cách nhau một khoảng trắng) sau khi thêm số T vào vị trí v.

Ví dụ:


Input

5 2 9
8 6 2 10 5

Output
8 9 6 2 10 5

*/
#include <iostream>
using namespace std;
int main(){
    int n, v, T;
    cin >> n >> v >> T;
    int a[n];
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    for(int i = 0; i <= n; i++){
        if(i == v - 1){
            cout << T << " ";
        }
        if(i < n) cout << a[i] << " ";
    }
    return 0;
}

// Cách 2:
/*
#include <iostream>
using namespace std;
int main(){
    int n, v, T;
    cin >> n >> v >> T;
    int a[n];
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    
    // In các phần tử từ đầu đến trước vị trí v
    for(int i = 0; i < v - 1; i++){
        cout << a[i] << " ";
    }
    
    // In số T tại vị trí v
    cout << T << " ";
    
    // In các phần tử từ vị trí v trở đi
    for(int i = v - 1; i < n; i++){
        cout << a[i] << " ";
    }
    
    return 0;
}
*/