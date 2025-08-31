#include <bits/stdc++.h>
using namespace std;

const double TOL = 1e-4;
const double PI = acos(-1.0);

double sin_series(double x, double term, int n, double acc){
    if(fabs(term) < TOL) return acc;
    double next_term = -term * x * x / ((2*n+2)*(2*n+3));
    return sin_series(x, next_term, n+1, acc + next_term);
}

double cos_series(double x, double term, int n, double acc){
    if(fabs(term) < TOL) return acc;
    double next_term = -term * x * x / ((2*n+1)*(2*n+2));
    return cos_series(x, next_term, n+1, acc + next_term);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    double x;
    if(!(cin >> x)) return 0;
    x = fmod(x + PI, 2*PI);
    if(x < 0) x += 2*PI;
    x -= PI;

    double sinx = sin_series(x, x, 0, x);     // term0 = x
    double cosx = cos_series(x, 1.0, 0, 1.0); // term0 = 1

    // Làm tròn 2 chữ số
    sinx = floor(sinx*100 + 0.5)/100.0;
    cosx = floor(cosx*100 + 0.5)/100.0;

    cout.setf(ios::fixed); cout<<setprecision(2)<<sinx<<"\n"<<cosx<<"\n";
    return 0;
}