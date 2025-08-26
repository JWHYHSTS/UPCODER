#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

#define sn int
#define nhap cin
#define xuat cout 
#define kt return 0

sn main(){
    sn n, m;
    nhap >> n >> m;
    // Khởi tạo chồng đĩa ban đầu: 1,2....,n
    vector<sn> stack;
    for(sn i = 1; i <= n; i++){
        stack.push_back(i);
    }
    // Xử lý m lần rút đĩa
    for(sn i = 0; i < m; i++){
        sn disc;
        nhap >> disc;
        // Tìm và xóa đĩa khỏi chồng
        auto it = find(stack.begin(), stack.end(), disc);
        if(it != stack.end()){
            stack.erase(it);
        }
        // Chèn đĩa vào đầu stack (đặt đĩa lên đầu chồng)
        stack.insert(stack.begin(), disc);
    }
    // Xuất các đĩa trong stack
    for(sn i = 0; i < n; i++){
        xuat << stack[i];
        if(i < n - 1) xuat << " ";  
    }
    kt;
}
