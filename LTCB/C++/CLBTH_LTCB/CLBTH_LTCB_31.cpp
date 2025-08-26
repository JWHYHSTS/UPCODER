/*
Cho một dãy gồm n số nguyên dương A1, A2, …, An. Một cặp số được gọi là cặp tương đồng với x, nếu cặp số này có tổng bằng số x cho trước nào đó.
Hãy đếm xem trong dãy số A có bao nhiêu cặp số (Ai, Aj) tương đồng với x (có nghĩa là Ai + Aj = x) với i < j.
Input:
Dòng đầu tiên chứa số n và x.
Dòng thứ 2 gồm n số nguyên dương A1, A2, …, An.
Output:
Ghi ra một số nguyên là cặp đôi tương đồng của dãy số.
Ví dụ:

Input

Output

7 6

1 2 4 3 4 5 3

4

*/

#include <iostream>
using namespace std;

int main(){
    int n, x;
    cin >> n >> x;
    int a[n];
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    int dem = 0;
    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            if(a[i] + a[j] == x) dem++;
        }
    }
    cout << dem;
    return 0;
}