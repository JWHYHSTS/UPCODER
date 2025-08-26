/*
SMG Gateway là một thiết bị để quản lý hàng loạt SIM điện thoại. Mỗi thiết bị có thể chứa N slot để gắn SIM. Mỗi slot như vậy sẽ có các thông tin như: mã số (kiểu chuỗi, tối đa 10 kí tự), số điện thoại của SIM (kiểu chuỗi, tối đa 11 kí tự i), nhà mạng cung cấp (kiểu chuỗi, tối đa 20 kí tự).

Hãy xây dựng chương trình để quản lý SMG Gateway với các chức năng sau:

Hàm nhập thông tin cho N slot
Hàm xuất thông tin cho N slot
Hàm nhập vào số điện thoại (tối đa 11 chữ số), sau đó tìm và in ra thông tin của các slot có cùng nhà mạng cung cấp với số điện thoại nhập vào (dựa theo đầu số là 3 kí tự đầu của số điện thoại)


Input:

- Dòng đầu tiên là số nguyên N cho biết số lượng slot

- N dòng tiếp theo, mỗi dòng là thông tin của từng slot, bao gồm: mã số, số điện thoại, nhà mạng. Mỗi thông tin cách nhau 1 khoảng trắng

- Dòng cuối cùng chứa số điện thoại để tìm slot có cùng nhà mạng

Output:

- Lần lượt in ra thông tin của các slot tìm được, mỗi slot là một dòng có các thông tin: mã số, số điện thoại, nhà mạng cung cấp. Mỗi thông tin cách nhau 1 dấu hai chấm “:”

 

Ví dụ:

Input:

3

S01 0903334455 Mobi

S02 0981234567 Viettel

S03 0919999999 Vinaphone

0907773177



Output:

S01:0903334455:Mobi
*/

#include <iostream>
using namespace std;

#define sn int
#define nhap cin 
#define xuat cout 
#define kt return 0

struct slot{
    string maso;
    string sdt;
    string nhamang;
    void nhaps(){
        nhap >> maso >> sdt >> nhamang;
    }
    void xuats(){
        xuat << maso << ":" << sdt << ":" << nhamang << endl;
    }
    string getsodau(){
        return sdt.substr(0,3);
    }
};

string xacdinhnhamang(string sodau){
    if(sodau == "090" || sodau == "091" || sodau == "092") return "Mobi";
    else if(sodau == "098" || sodau == "097" || sodau == "096") return "Viettel";
    else if(sodau == "093" || sodau == "094" || sodau == "095") return "Vinaphone";
    else return "";
}

sn main(){
    sn n;
    nhap >> n;
    slot slots[100];

    for(sn i = 0; i < n; i++){
        slots[i].nhaps();
    }
    
    string sdtcantim;
    nhap >> sdtcantim;

    string sodaucantim = sdtcantim.substr(0,3);
    string nhamangcantim = xacdinhnhamang(sodaucantim);

    for(sn i = 0; i < n; i++){
        string sodauslot = slots[i].getsodau();
        string nhamangslot = slots[i].nhamang;
        if(nhamangslot == nhamangcantim){
            slots[i].xuats();
        }
    }
    kt;
}