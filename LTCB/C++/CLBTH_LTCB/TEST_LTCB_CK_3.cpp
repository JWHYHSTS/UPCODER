/*
Cho n điểm trong mặt phẳng tọa độ Oxy (n không quá 300). Mỗi điểm có tọa độ nguyên (x, y). Hãy đếm xem có bao nhiêu điểm trong số đó nằm trên trục hoành (Ox) hoặc trục tung (Oy).
Ví dụ:

Input
5
0 3
1 0
0 1
2 2
-3 0

Output
4

*/
#include <iostream>
using namespace std;
int main(){
    int n, x, y, dem = 0;
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> x >> y;
        if(x == 0 || y == 0) dem++;
    }
    cout << dem;
}