/*
Trong mùa đông này, Tỷ được giao nhiệm vụ thống kê và báo cáo nhiệt độ của các ngày trong tuần. Việc thống kê thì đã quá dễ dàng vì Tỷ có thể Google và hàng chục triệu kết quả sẽ hiện ra trước mắt. Nhưng còn việc viết báo cáo, vì Tỷ mãi chơi và lười nghĩ nên Tỷ quyết định nhờ các bạn thực hiện công việc hộ Tỷ.

Một bản báo cáo nhiệt độ cần có các thông tin như sau:

- Nhiệt độ của các ngày lạnh hơn 10ºC.

- Nhiệt độ của ngày lạnh nhất và nóng nhất.

Vậy đó, mặc dù biết cổ xúy cho việc lười biếng là không tốt, các bạn hãy giúp Tỷ lần này nhé!

Input:

Gồm bảy số thực, lần lượt là nhiệt độ các ngày trong tuần.

Output:

Dòng thứ nhất in ra nhiệt độ của các ngày lạnh hơn 10ºC. Nếu có nhiều ngày thỏa mãn thì in theo thứ tự ngày trong tuần.

Dòng thứ hai in ra nhiệt độ của ngày lạnh nhất.

Dòng thứ ba in ra nhiệt độ của ngày nóng nhất.

Ví dụ:


Input
12.8 15.3 20.1 15.9 9.0 8.9 12.6 
Output
9 8.9
8.9
20.1
*/
#include <iostream>
using namespace std;
int main(){
    float a[7];
    for(int i = 0; i < 7; i++){
        cin >> a[i];
    }
    for(int i = 0; i < 7; i++){
        if(a[i] < 10){
            cout << a[i] << " ";
        }
    }
    cout << endl;
    float min = a[0], max = a[0];
    for(int i = 0; i < 7; i++){
        if(a[i] < min) min = a[i];
        if(a[i] > max) max = a[i];
    }
    cout << min << endl << max;
    return 0;
}