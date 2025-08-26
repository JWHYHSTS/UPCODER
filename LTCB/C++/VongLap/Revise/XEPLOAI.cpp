/*
Nhập vào điểm các môn học của một sinh viên (là các số nguyên từ 0 đến 10), yêu cầu xuất ra xếp loại của sinh viên đó.

Cách xếp loại dựa vào điểm trung bình (ĐTB) của sinh viên được xếp như sau.

- Nếu ĐTB <4 xếp loại F

- Nếu 4 <= ĐTB  <5.5 xếp loại D

- Nếu 5.5 <= ĐTB < 7.0 xếp loại C

- Nếu 7.0 <= ĐTB < 8.5 xếp loại B

- Nếu 8.5 <= ĐTB xếp loại A

Input:

Gồm nhiều dòng, mỗi dòng là 1 điểm kết thúc là số -1 

(lưu ý -1 chỉ là ký hiệu kết thúc, không tính vào điểm số của sinh viên)

Output:

Xuất ra xếp loại của sinh viên

Ví dụ:

Input:
10 
9 
5
-1
output:
B
*/

#include <iostream>
using namespace std;

int main(){
    int d, tong = 0, dem = 0;
    while(cin >> d && d != -1){
        tong += d;
        dem++;
    }
    double dtb = static_cast<double>(tong) / dem;
    if(dtb < 4) cout << "F";
    else if(4 <= dtb && dtb < 5.5) cout << "D";
    else if(5.5 <= dtb && dtb < 7) cout << "C";
    else if(7 <= dtb && dtb < 8.5) cout << "B";
    else cout << "A";
    return 0;
}
