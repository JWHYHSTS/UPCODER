/*
Các giải đấu thể thao quốc tế luôn dành một phần thưởng lớn cho các đoàn có thứ hạng cao. Có hai cách để xếp hạng các đoàn:

Cách 1: 
Đoàn nào có tổng số huy chương lớn hơn thì xếp trên
Cách 2: 
Đoàn nào có nhiều huy chương vàng hơn thì xếp trên, nếu bằng nhau thì xét đến huy chương bạc, nếu bằng sẽ xét đến huy chương đồng.

Việt Nam và Thái Lan là hai cường quốc thể thao ở Đông Nam Á. Cho biết số lượng các huy chương của hai đoàn này cùng cách xếp hạng của ban tổ chức, hãy cho biết đội nào xếp trên.

Dữ liệu đầu vào: 
Dòng đầu tiên chứa 6 số nguyên không âm (không vượt quá 200) ghi lại số huy chương vàng, bạc, đồng của Việt Nam và số huy chương vàng, bạc, đồng của Thái Lan
Dòng tiếp theo chứa một số nguyên duy nhất 1 hoặc 2 ghi lại cách xếp hạng của ban tổ chức.

Dữ liệu đầu ra:
Nếu Việt Nam xếp trên thì xuất ra "VN".
Nếu Thái Lan xếp trên thì xuất ra "TL".
Nếu không phân định được thì xuất ra "TIE".

Ví dụ
input
20 15 30 12 24 35
1
output
TL

Ví dụ
input
20 15 30 12 24 35
2
output
VN
*/
#include <iostream>
using namespace std;

#define nhap cin
#define xuat cout
#define kt return 0
#define sn int

sn main(){
    sn VangVN, BacVN, DongVN, VangTL, BacTL, DongTL, key;
    nhap >> VangVN >> BacVN >> DongVN >> VangTL >> BacTL >> DongTL >> key;
    
    if(key == 1){
        sn sumVN = VangVN + BacVN + DongVN;
        sn sumTL = VangTL + BacTL + DongTL;
        if(sumVN > sumTL) xuat << "VN";
        else if(sumVN < sumTL) xuat << "TL";
        else xuat << "TIE";
    }
    if(key == 2){
        if(VangVN == VangTL && BacVN == BacTL && DongVN == DongTL) xuat <<"TIE";
        else if(VangVN > VangTL) xuat << "VN";
        else if(VangVN == VangTL && BacVN > BacTL) xuat << "VN";
        else if(VangVN == VangTL && BacVN == BacTL && DongVN > DongTL) xuat << "VN";
        else xuat << "TL";
    }
    kt;
}
