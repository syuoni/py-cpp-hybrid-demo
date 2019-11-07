#include <iostream>
#include <math.h>
#include "rms.h"

using std::runtime_error;

void inverse_diff(double *seq, int n, double *outseq, int m){
    for (int i=0; i<n-1; i++){
        outseq[i] = seq[i] - seq[i+1];
    }
}

void dot_mat(double *mat1, int n1, int m1, double *mat2, int n2, int m2, double *mat3, int nm3){
    if (m1 != n2){
        throw runtime_error("Input matrix shapes NOT match!");
    }
    for (int i=0; i<n1; i++){
        for (int j=0; j<m2; j++){
            mat3[i*m2+j] = 0;
            for (int k=0; k<m1; k++){
                mat3[i*m2+j] += mat1[i*m1+k] * mat2[k*m2+j];
            }
        }
    }
}

double sum_mat(double *mat, int n, int m){
    double res = 0;
    for (int i=0; i<n; i++){
        for (int j=0; j<m; j++){
            res += mat[i*m + j];
        }
    }
    return res;
}

void make_array(double *outseq, int n){
    for (int i=0; i<n; i++){
        outseq[i] = 0;
    }
}

void sq_inplace(double *ipseq, int n){
    for (int i=0; i<n; i++){
        ipseq[i] *= ipseq[i];
    }
}

double rms(double *seq, int n){
    double ss = 0;
    for (int i=0; i<n; i++){
        ss += (seq[i] * seq[i]);
    }
    return sqrt(ss / n);
}

double sum(double *seq, int m){
    double s = 0;
    for (int i=0; i<m; i++){
        s += seq[i];
    }
    return s;
}

double dot(double *seq1, int n1, double *seq2, int n2){
    if (n1 != n2){
        throw runtime_error("Input vector shapes NOT match!");
    }
    double res = 0;
    for (int i=0; i<n1; i++){
        res += seq1[i] * seq2[i];
    }
    return res;
}