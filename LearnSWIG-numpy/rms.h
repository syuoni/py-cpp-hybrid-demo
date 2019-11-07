// In declaration, the variable names should be exactly same as those
// in the "%apply" directive in the SWIG Interface File (i.e., rms.i).
// While, the variable names in the definition has no effects...

double rms(double* seq, int n);
double sum(double* seq, int m);
double dot(double *seq1, int n1, double *seq2, int n2);
void sq_inplace(double *ipseq, int n);
void make_array(double *outseq, int n);
double sum_mat(double *mat, int n, int m);
void dot_mat(double *mat1, int n1, int m1, double *mat2, int n2, int m2, double *mat3, int nm3);
void inverse_diff(double *seq, int n, double *outseq, int m);
