#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include "my_cpp_functions.h"

using std::string;
using std::vector;
using std::swap;
using std::accumulate;
using std::runtime_error;

double my_variable = 4.4;

void throw_exception(){
    throw runtime_error("An exception raise!");
}

double average(vector<int> v){
    return accumulate(v.cbegin(), v.cend(), 0.0) / v.size();
}

vector<double> half(const vector<double> &v){
    vector<double> w;
    for (auto vi: v){
        w.push_back(vi / 2);
    }
    return w;
}

void half_in_place(vector<double> &v){
    for (auto &vi: v){
        vi /= 2;
    }
}


string double_str(const string &s){
    return s + s;
}

char *half_str(char *s, int n){
    char *h = new char[n/2 + 1];
    for (int i=0; i<n/2; i++){
        h[i] = s[i];
    }
    h[n/2] = '\0';
    return h;
}

int sum_array(int *arr, int n){
    int res = 0;
    for(int i=0; i < n; i++){
        res += arr[i];
    }
    return res;
}

void add(int x, int y, int *res){
    *res = x + y;
}

int sub(int *x, int *y){
    return *x - *y;
}

void negate(int *z){
    *z = -(*z);
}

void next_fab(int *a1, int *a2){
    *a1 += *a2;
    swap(*a1, *a2);
}

int fact(int n){
    if (n <= 1){
        return 1;
    }else{
        return n * fact(n-1);
    }
}

int my_mod(int n, int m){
    return n % m;
}

void Wall::setWall(int _s){
    s = _s;
}

int Wall::getWall(){
    return s;
}
