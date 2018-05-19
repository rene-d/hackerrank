// Mathematics > Fundamentals > Mutual Recurrences
// Compute terms in a mutual recurrence.
//
// https://www.hackerrank.com/challenges/mutual-recurrences/problem
// https://www.hackerrank.com/contests/infinitum14/challenges/mutual-recurrences
// challenge id: 15898
//

#include <bits/stdc++.h>
using namespace std;

#pragma GCC diagnostic ignored "-Wsign-conversion"

constexpr long MOD = 1e9;

class Vecteur
{
    vector<long> a;
    size_t n;

  public:
    Vecteur(size_t n)
    {
        this->n = n;
        a.resize(n, 0L);
    }

    size_t dim() const
    {
        return n;
    }

    long operator()(size_t x) const
    {
        assert(x < n);
        return a[x];
    }

    long &operator()(size_t x)
    {
        assert(x < n);
        return a[x];
    }
};

class Matrice
{
    vector<long> a;
    size_t n;

  public:
    Matrice(size_t n)
    {
        this->n = n;
        a.resize(n * n, 0L);
    }

    static Matrice I(size_t n)
    {
        Matrice M(n);
        for (size_t i = 0; i < n; ++i)
            M(i, i) = 1;
        return M;
    }

    long operator()(size_t x, size_t y) const
    {
        assert(x < n && y < n);
        return a[x + y * n];
    }

    long &operator()(size_t x, size_t y)
    {
        assert(x < n && y < n);
        return a[x + y * n];
    }

    Matrice &operator%=(long m)
    {
        for (auto &&i : a)
            i %= m;
        return *this;
    }

    Matrice &operator*=(const Matrice &B)
    {
        assert(n == B.n);

        Matrice &A = *this;
        Matrice C(n);

        for (size_t x = 0; x < n; ++x)
        {
            for (size_t y = 0; y < n; ++y)
            {
                long s = 0;
                for (size_t i = 0; i < n; ++i)
                    s += (A(i, y) * B(x, i)) % MOD;
                C(x, y) = s % MOD;
            }
        }
        a = C.a;
        return *this;
    }

    Vecteur operator*(const Vecteur &V) const
    {
        assert(n == V.dim());
        const Matrice &A = *this;
        Vecteur C(n);

        for (size_t y = 0; y < n; ++y)
        {
            long s = 0;
            for (size_t i = 0; i < n; ++i)
                s += (A(i, y) * V(i)) % MOD;
            C(y) = s % MOD;
        }

        return C;
    }

    Matrice &operator^=(unsigned long k)
    {
        if (k == 1)
            return *this;

        Matrice &M = *this;
        Matrice P = Matrice::I(n);

        while (k != 0)
        {
            if (k % 2 == 1)
                P *= M;
            M *= M;
            k /= 2;
        }

        a = P.a;
        return *this;
    }

    void print() const
    {
        const Matrice &A = *this;

        for (size_t y = 0; y < n; ++y)
        {
            cout << ((y == 0) ? '[' : ' ');
            for (size_t x = 0; x < n; ++x)
            {
                cout << A(x, y);
                if (x == n - 1)
                {
                    if (y == n - 1)
                        cout << "]\n";
                    else
                        cout << "\n";
                }
                else
                {
                    cout << " ";
                }
            }
        }
    }
};

long fibonacci_easy(long a, long b, unsigned long n)
{
    Matrice A(2);

    A(0, 0) = 1;
    A(0, 1) = 1;
    A(1, 0) = 1;
    A(1, 1) = 0;

    A ^= n;

    Vecteur F(2);
    F(0) = b;
    F(1) = a;

    F = A * F;

    return F(1);
}

// Complete the solve function below.
void solve(int a, int b, int c, int d, int e, int f, int g, int h, unsigned long n)
{
    Matrice A(20 + 4);

    A(a - 1, 0) += 1;      // x(n) =  x(n - a)
    A(10 + b - 1, 0) += 1; //                  + y(n - b)
    A(10 + c - 1, 0) += 1; //                             + y(n - c)
    A(20 + 2, 0) += 1;     //                                        + n * d ** n

    A(10 + e - 1, 10) += 1; // y(n) = y(n - e)
    A(f - 1, 10) += 1;      //                 + x(n - f)
    A(g - 1, 10) += 1;      //                             + x(n - g)
    A(20, 10) += 1;         //                                        + n * h ** n

    for (size_t i = 1; i < 10; ++i)
    {
        A(i - 1, i) += 1;
        A(10 + i - 1, 10 + i) += 1;
    }

    A(20, 20) = h;
    A(20 + 1, 20) = h;
    A(20 + 1, 20 + 1) = h;

    A(20 + 2, 20 + 2) = d;
    A(20 + 3, 20 + 2) = d;
    A(20 + 3, 20 + 3) = d;

    //A.print();

    Vecteur F(20 + 4);
    for (size_t i = 0; i < 20 + 4; ++i)
        F(i) = 1;
    F(20) = 0;
    F(20 + 2) = 0;

    A ^= (n + 1);
    F = A * F;
    cout << F(0) << " " << F(10) << endl;
}

int main()
{
    // cerr << fibonacci_easy(2, 4, 9) << endl;        // [55, 34, 34, 21]  178

    int t;
    cin >> t;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    while (t--)
    {
        int a, b, c, d, e, f, g, h;
        unsigned long n;
        cin >> a >> b >> c >> d >> e >> f >> g >> h >> n;
        solve(a, b, c, d, e, f, g, h, n);
    }

    return 0;
}
