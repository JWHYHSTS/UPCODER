#include <bits/stdc++.h>
using namespace std;

string mul2(const string &s){
    string res = s;
    int carry = 0;
    for(int i = (int)res.size()-1; i>=0; --i){
        int d = (res[i]-'0')*2 + carry;
        res[i] = char('0' + d%10);
        carry = d/10;
    }
    if(carry) res.insert(res.begin(), char('0'+carry));
    return res;
}
string add1(const string &s){
    string res = s;
    int carry = 1;
    for(int i = (int)res.size()-1; i>=0 && carry; --i){
        int d = (res[i]-'0') + carry;
        res[i] = char('0' + d%10);
        carry = d/10;
    }
    if(carry) res.insert(res.begin(), '1');
    return res;
}
string binToDec(const string &bin){
    string dec = "0";
    for(char c: bin){
        dec = mul2(dec);
        if(c=='1') dec = add1(dec);
    }
    // strip leading zeros
    size_t p = dec.find_first_not_of('0');
    if(p==string::npos) return "0";
    return dec.substr(p);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if(!(cin>>n)) return 0;
    vector<vector<int>> g(n, vector<int>(n));
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            cin>>g[i][j];

    vector<vector<string>> best(n, vector<string>(n));
    for(int i=n-1;i>=0;--i){
        for(int j=n-1;j>=0;--j){
            char bit = g[i][j] ? '1':'0';
            if(i==n-1 && j==n-1){
                best[i][j]=string(1,bit);
            }else{
                string opt1, opt2;
                if(i+1<n) opt1 = bit + best[i+1][j];
                if(j+1<n) opt2 = bit + best[i][j+1];
                if(opt1.empty()) best[i][j]=opt2;
                else if(opt2.empty()) best[i][j]=opt1;
                else best[i][j] = max(opt1, opt2); // same length, lexicographic compares value
            }
        }
    }
    string binStr = best[0][0];
    cout << binToDec(binStr);
    return 0;
}