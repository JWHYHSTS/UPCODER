#include <bits/stdc++.h>
using namespace std;

bool parse_ll(const string &s, long long &out) {
    try {
        size_t idx = 0;
        long long v = stoll(s, &idx);
        if (idx != s.size()) return false;
        out = v;
        return true;
    } catch(...) {
        return false;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string t;
    if (!(cin >> t)) return 0;
    for (auto &ch : t) ch = toupper((unsigned char)ch);
    vector<string> tok;
    string s;
    while (cin >> s) tok.push_back(s);
    if (t == "N") {
        vector<long long> vals;
        for (auto &x : tok) {
            long long v;
            if (parse_ll(x, v)) vals.push_back(v);
        }
        if (vals.empty()) return 0;
        long long mn = vals[0], sum = 0;
        for (auto v : vals) { sum += v; if (v < mn) mn = v; }
        cout << mn << "\n" << sum << "\n";
    } else if (t == "H") {
        vector<pair<long long,long long>> v;
        for (size_t i = 0; i + 1 < tok.size(); ) {
            long long w, h;
            if (parse_ll(tok[i], w) && parse_ll(tok[i+1], h)) {
                v.emplace_back(w,h);
                i += 2;
            } else {
                // skip the token that failed
                if (!parse_ll(tok[i], w)) ++i;
                else ++i; // if second failed, advance by one to try next pairing
            }
        }
        if (v.empty()) return 0;
        auto cmp = [](const pair<long long,long long>& a, const pair<long long,long long>& b){
            long long A = a.first * a.second;
            long long B = b.first * b.second;
            if (A != B) return A < B;
            if (a.first != b.first) return a.first < b.first;
            return a.second < b.second;
        };
        auto mn = *min_element(v.begin(), v.end(), cmp);
        long double total_per = 0.0L;
        for (auto &p : v) total_per += 2.0L * (p.first + p.second);
        cout << "[HCN] " << mn.first << "," << mn.second << "\n";
        cout.setf(ios::fixed);
        cout << setprecision(1) << (double)total_per << "\n";
    }
    return 0;
}