/*
Để quảng bá cho kì thi Olympic Tin Học Sinh Viên Toàn Quốc & Kỳ Thi Lập Trình Viên Quốc Tế (gọi tắt là OLP&ACM/ICPC), ban tổ chức phát động cuộc thi ảnh "Khoảnh khắc OLP&ACM/ICPC".

Các đội tuyển sẽ đăng ảnh của đội mình vào fanpage của cuộc thi. Dựa vào số lượt tương tác (like, comment, share), ban tổ chức sẽ chọn ra ba bức ảnh có điểm cao nhất để trao quà.

Cách tính điểm như sau: mỗi lượt like được 1 điểm, comment được 2 điểm và share được 3 điểm.

Ban tổ chức đã nhờ người thống kê số lượt tương tác của từng đội, việc còn lại của bạn là tính điểm và xác định 3 đội được trao quà.

Dữ liệu đầu vào: gồm nhiều đội tuyển, dữ liệu mỗi đội tuyển bao gồm 4 dòng:
- Tên đội (không có khoảng trắng)
- Số lượt like
- Số lượt comment
- Số lượt share
Dữ liệu đầu vào kết thúc khi tên đội là "000"

Dữ liệu đầu ra: gồm 3 dòng ghi tên lần lượt 3 đội được trao quà theo thứ tự điểm cao đến thấp (dữ liệu vào đảm bảo không có 2 đội nào bằng điểm)


Ví dụ:
Input:
UP_Balloons
456
215
34
UP_Unlimited
654
45
21
UP_Explorer
452
142
15
UP_Ashe
356
654
78
000

Output:
UP_Ashe
UP_Balloons
UP_Unlimited
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

#define sn int
#define nhap cin 
#define xuat cout 
#define kt return 0

struct Team {
    string name;
    sn like, comment, share;
    sn diemtong;
    void tinhdiem(){
        diemtong = like + comment * 2 + share * 3;
    }
};

bool sosanh(const Team& a, const Team& b){
        return a.diemtong > b.diemtong;
}

sn main(){
    vector<Team> team;
    Team t;
    while(nhap >> t.name){
        if(t.name == "000") break;
        nhap >> t.like >> t.comment >> t.share;
        t.tinhdiem();
        team.push_back(t);
    }
    sort(team.begin(), team.end(), sosanh);
    for(sn i = 0; i < 3 && i < static_cast<int>(team.size()); i++){
        xuat << team[i].name << endl;
    }
    kt;
    
}