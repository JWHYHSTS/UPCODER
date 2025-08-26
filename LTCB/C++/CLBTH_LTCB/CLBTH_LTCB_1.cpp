/*
Hiện nay có một loại virus đang hoành hành với một tốc độ tăng trưởng rất nhanh. Sau mỗi ngày số virus sẽ tăng lên gấp đôi. Ví dụ, trong tế bào có chứa 1 con virus, thì sau ngày thứ nhất nó tăng lên thành 2 con, sau ngày thứ hai nó tăng lên thành 4 con,…

Cho biết có n con virus đang kí sinh trong các tế bào, sau ít nhất bao nhiêu ngày thì số lượng con virus vượt quá 1 tỉ?

Input:

Gồm một số nguyên dương n duy nhất.

Output:

Số ngày ít nhất để số virus vượt quá 1 tỉ.

Ví dụ:


Input
1000
Output
20

*/

#include <iostream>
using namespace std;
int main(){
    long long n;
    cin >> n;
    long long dem = 0;
    while(n <= 1000000000){
        n *= 2;
        dem++;
    }
    cout << dem;
    return 0;
}
// VD: Lý do tại sao nhập n = 1000 thì kết quả là 20:
// Ngày 1: 1000 * 2 = 2000
// Ngày 2: 2000 * 2 = 4000
// Ngày 3: 4000 * 2 = 8000
// Ngày 4: 8000 * 2 = 16000
// Ngày 5: 16000 * 2 = 32000
// Ngày 6: 32000 * 2 = 64000
// Ngày 7: 64000 * 2 = 128000
// Ngày 8: 128000 * 2 = 256000      
// Ngày 9: 256000 * 2 = 512000
// Ngày 10: 512000 * 2 = 1024000
// Ngày 11: 1024000 * 2 = 2048000
// Ngày 12: 2048000 * 2 = 4096000
// Ngày 13: 4096000 * 2 = 8192000
// Ngày 14: 8192000 * 2 = 16384000
// Ngày 15: 16384000 * 2 = 32768000
// Ngày 16: 32768000 * 2 = 65536000
// Ngày 17: 65536000 * 2 = 131072000
// Ngày 18: 131072000 * 2 = 262144000
// Ngày 19: 262144000 * 2 = 524288000
// Ngày 20: 524288000 * 2 = 1048576000
// Như vậy sau 20 ngày thì số virus sẽ vượt quá 1 tỉ.