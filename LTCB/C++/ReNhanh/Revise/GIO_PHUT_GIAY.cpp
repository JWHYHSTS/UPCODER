/*
Viết chương trình nhập vào giờ, phút, giây. Kiểm tra giờ, phút, giây đó có hợp lệ hay không, nếu hợp lệ hãy cho biết giờ sau đó 1 giây là bao nhiêu?
Dữ liệu vào: 3 số nguyên lần lượt là giờ, phút, giây.
Dữ liệu ra: 
- Dòng đầu xuất "YES" nếu hợp lệ, ngược lại xuất "NO" nếu không hợp lệ.
- Dòng thứ hai xuất giờ sau đó 1 giây nếu hợp lệ.

Ví dụ:

Input	
3 
59 
60
Output
NO
Input	
1 
59 
59
Output
YES
2:0:0

*/

#include <iostream>
using namespace std;
int main(){
    int g,p,s;
    cin >> g >> p >> s;
    if(g < 0 || g > 23 || p < 0 || p > 59 || s < 0 || s > 59){
        cout << "NO";
    }else {
        cout << "YES" << endl;
        s++;
        if(s == 60){
            s = 0;
            p++;
            if(p == 60){
                p = 0;
                g++;
                if(g == 24) g = 0;
            }
        }
        cout << g << ":" << p << ":" << s;
    }
    return 0;
}