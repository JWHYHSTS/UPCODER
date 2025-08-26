/*
Hàng ngày vào mỗi buổi sáng sớm, Tèo thường rủ Tý ra công viên chạy bộ. Vào một ngày nọ, Tèo thấy vui nên muốn chơi một trò chơi nhỏ với Tý. Tèo chọn 3 gốc cây trong công viên, 3 gốc cây này tạo thành một hình tam giác như hình vẽ:
Từ A đến B: 15
Từ B đến C: 10
Từ C đến A: 20

(Khoảng cách giữa các cây với nhau là tùy ý).

Tèo sẽ bắt đầu chạy từ A đến B, rồi từ B đến C, rồi lại quay về A. Cứ chạy tiếp như vậy. Mỗi giây Tèo chạy được 1 mét. Tèo đố Tý rằng sau t giây kể từ lúc bắt đầu chạy, Tèo đang ở vị trí nào? (Câu trả lời chỉ là ở A, B, C hoặc trên quãng đường AB, BC, CA)
Bạn hãy giúp Tý trả lời câu hỏi này nhé!

Input:
Dòng 1: 3 số nguyên dương là khoảng cách giữa 3 gốc cây (mét). Lần lượt theo thứ tự là AB, BC, CA (mỗi số cách nhau một khoảng trắng).
Dòng 2: số nguyên dương t - thời gian Tèo sẽ chạy.
Output:
Vị trí của Tèo sau t giây (tại A, B, C, hoặc là trên đường AB, BC, CA)

Ví dụ:
Input:
15 10 20
32
Output:
CA
Input:
15 10 20
25
Output:
C
*/

#include <iostream>
using namespace std;
int main(){
    int AB, BC, CA, t;
    cin >> AB >> BC >> CA >> t;
    int tong = AB + BC + CA;
    int vt = t % tong;
    
    if(vt == 0) cout << "A";
    else if(vt == AB) cout << "B";
    else if(vt == AB + BC) cout << "C";
    else if(vt > 0 && vt < AB) cout << "AB";
    else if(vt > AB && vt < AB + BC) cout << "BC";
    else if(vt > AB + BC && vt < AB + BC + CA) cout << "CA";
    
    return 0;
}