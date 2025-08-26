/*
Cau 3:
Cho mảng 1 chiều n số nguyên (n<1000), hãy đếm số phần tử xuất hiện nhiều hơn 1 lần trong dãy.
Ví dụ:
Input
8
1 4 2 3 1 3 5 6
Output
2
Giải thích:
1 và 3 xuất hiện 2 lần
các số còn lại xuất hiện 1 lần

*/
#include <iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    int a[1000];
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    int dem = 0;
    for(int i = 0; i < n; i++){
        int count = 0;
        for(int j = 0; j < n; j++){
            if(a[i] == a[j]) count++;
        }
        if(count > 1) dem++;
    }
    cout << dem / 2;
    return 0;
}

/*

#include <iostream>
using namespace std;

int main(){
    int n, a[1000], dem[1000] = {0};
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    int trung = 0;
    for (int i = 0; i < n; i++){
        if (dem[i] == 0) {
            int lan = 1;
            for (int j = i + 1; j < n; j++){
                if (a[i] == a[j]){
                    lan++;
                    dem[j] = 1;
                }
            }
            if (lan > 1) trung++;
        }
    }
    cout << trung;
    return 0;
}
    
*/

/*


#include <iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    int a[1000];
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    int dem = 0;
    for(int i = 0; i < n; i++){
        bool ktr = true;
        for(int j = 0; j < i; j++){
            if(a[j] == a[i]){
                ktr = false;
                break;
            }
        }
        if(ktr){
            int count = 0;
            for(int j = 0; j < n; j++){
                if(a[j] == a[i]) count ++;
            }
            if(count > 1) dem++;
        }
    }
    cout << dem;
}
    
*/