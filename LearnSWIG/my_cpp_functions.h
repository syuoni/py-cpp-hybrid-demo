#include <string>
#include <vector>

using std::string;
using std::vector;
using std::runtime_error;

extern double my_variable;

void throw_exception();

double average(vector<int> v);
vector<double> half(const vector<double> &v);
void half_in_place(vector<double> &v);

string double_str(const string &s);
char *half_str(char *s, int n);

int sum_array(int *arr, int n);

void add(int x, int y, int *res);
int sub(int *x, int *y);
void negate(int *z);
void next_fab(int *a1, int *a2);

int fact(int n);
int my_mod(int n, int m);

class Wall{
    public:
        Wall() = default;
        Wall(int _s): s(_s) {};
        void setWall(int _s);
        int getWall();
        int x[16];
    private:
        int s;
};
