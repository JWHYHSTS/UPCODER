#include <bits/stdc++.h>
using namespace std;

struct Point2 {
    int x{0}, y{0};
    friend istream& operator>>(istream& is, Point2& p) {
        is >> p.x >> p.y;
        return is;
    }
    friend ostream& operator<<(ostream& os, const Point2& p) {
        os << "(" << p.x << "," << p.y << ")";
        return os;
    }
    double operator-(const Point2& other) const {
        double dx = double(x - other.x);
        double dy = double(y - other.y);
        return sqrt(dx*dx + dy*dy);
    }
    bool operator<(const Point2& other) const {
        if (x != other.x) return x < other.x;
        return y < other.y;
    }
};

struct Point3 {
    int x{0}, y{0}, z{0};
    friend istream& operator>>(istream& is, Point3& p) {
        is >> p.x >> p.y >> p.z;
        return is;
    }
    friend ostream& operator<<(ostream& os, const Point3& p) {
        os << "(" << p.x << "," << p.y << "," << p.z << ")";
        return os;
    }
    double operator-(const Point3& other) const {
        double dx = double(x - other.x);
        double dy = double(y - other.y);
        double dz = double(z - other.z);
        return sqrt(dx*dx + dy*dy + dz*dz);
    }
    bool operator<(const Point3& other) const {
        if (x != other.x) return x < other.x;
        if (y != other.y) return y < other.y;
        return z < other.z;
    }
};

template<typename T>
struct MyArray {
    vector<T> data;
    void push(const T& v){ data.push_back(v); }
    void sortAsc(){ sort(data.begin(), data.end()); }
    void sortDesc(){ sort(data.begin(), data.end(), [](const T& a, const T& b){ return b < a; }); }
    double maxDistance() const {
        double mx = 0.0;
        int n = (int)data.size();
        if (n < 2) return 0.0;
        for (int i = 0; i < n; ++i)
            for (int j = i+1; j < n; ++j)
                mx = max(mx, data[i] - data[j]);
        return mx;
    }
    friend ostream& operator<<(ostream& os, const MyArray<T>& arr){
        for (const auto& el : arr.data) {
            os << el << " ";
        }
        return os;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    MyArray<Point2> oxy;
    MyArray<Point3> oxyz;

    string tag;
    while (cin >> tag) {
        if (tag == "Oxy") {
            Point2 p;
            if (!(cin >> p.x >> p.y)) break;
            oxy.push(p);
        } else if (tag == "Oxyz") {
            Point3 p;
            if (!(cin >> p.x >> p.y >> p.z)) break;
            oxyz.push(p);
        } else {
            // unknown token: try to skip rest of the line
            string rest;
            getline(cin, rest);
        }
    }

    oxy.sortAsc();
    oxyz.sortDesc();

    // line 1: Oxy ascending
    cout << oxy << "\n";

    // line 2: Oxyz descending
    cout << oxyz << "\n";

    // line 3: max distance in Oxy, rounded to 3 decimals
    double d1 = oxy.maxDistance();
    float rd1 = roundf((float)d1 * 1000.0f) / 1000.0f;
    cout.setf(ios::fixed); cout<<setprecision(3);
    cout << rd1 << "\n";

    // line 4: max distance in Oxyz
    double d2 = oxyz.maxDistance();
    float rd2 = roundf((float)d2 * 1000.0f) / 1000.0f;
    cout << rd2 << "\n";

    return 0;
}