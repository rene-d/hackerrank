// Ad Infinitum 11 - Math Programming Contest > Fibonacci GCD Again
// Compute GCDs involving Fibonacci numbers... again.
//
// https://www.hackerrank.com/contests/infinitum11/challenges/fibonacci-gcd-again
// challenge id: 5105
//

#include <bits/stdc++.h>

using namespace std;

// nota: il faut un type signé
typedef long long ull;


#if __cplusplus < 201700L
// c++14 code here
ull gcd(ull u, ull v)
{
    while (v != 0)
    {
        ull r = u % v;
        u = v;
        v = r;
    }
    return u;
}
#endif


class mat2x2
{
    array<ull, 4> a;

public:
    mat2x2()
    {
        for (auto& i : a) { i = 0; }
    }

    ull& operator()(unsigned x, unsigned y)
    {
        return a[x + y * 2];
    }

    ull operator()(unsigned x, unsigned y) const
    {
        return a[x + y * 2];
    }

    mat2x2& operator=(const array<ull, 4>& x)
    {
        a = x;
        return *this;
    }
};


class vect2
{
    array<ull, 2> a;

public:
    vect2()
    {
        for (auto& i : a) { i = 0; }
    }

    ull& operator()(unsigned x)
    {
        return a[x];
    }

    ull operator()(unsigned x) const
    {
        return a[x];
    }

    vect2& operator=(const array<ull, 2>& x)
    {
        a = x;
        return *this;
    }
};


ostream& operator<<(ostream& out, const mat2x2& v)
{
    out << "[[" << v(0, 0) << ", " << v(1, 0) << "], [";
    out         << v(1, 0) << ", " << v(1, 1) << "]]";
    return out;
}

ostream& operator<<(ostream& out, const vect2& v)
{
    out << "[" << v(0) << ", " << v(1) << "]";
    return out;
}


// produit matriciel: A * B modulo MOD
mat2x2 multm(const mat2x2& a, const mat2x2& b, ull MOD)
{
    mat2x2  p;
    p(0, 0) = (a(0, 0) * b(0, 0) + a(1, 0) * b(0, 1)) % MOD;
    p(1, 0) = (a(0, 0) * b(1, 0) + a(1, 0) * b(1, 1)) % MOD;
    p(0, 1) = (a(0, 1) * b(0, 0) + a(1, 1) * b(0, 1)) % MOD;
    p(1, 1) = (a(0, 1) * b(1, 0) + a(1, 1) * b(1, 1)) % MOD;
    return p;
}


// produit matrice/vecteur: A * V module MOD
vect2 multv(const mat2x2& a, const vect2& b, ull MOD)
{
    vect2 p;
    p(0) = (a(0, 0) * b(0) + a(1, 0) * b(1)) % MOD;
    p(1) = (a(0, 1) * b(0) + a(1, 1) * b(1)) % MOD;
    return p;
}


// fast exponentiation M^k module MOD
mat2x2 power(mat2x2 M, ull k, ull MOD)
{
    mat2x2 P;
    P = { { 1, 0, 0, 1 } };

    if (k == 0)
        return P;

    if (k == 1)
        return M;

    while (k != 0)
    {
        if (k % 2 == 1)
            P = multm(P, M, MOD);
        M = multm(M, M, MOD);
        k /= 2;
    }
    return P;
}


// calcul de F(n)
vect2 F(ull n, ull MOD)
{
    mat2x2 A, An;
    vect2 F0, Fn;

    A = { { 1, 1, 1, 0 } };
    An = power(A, n, MOD);

    F0 = { { 1, 0 } };
    Fn = multv(An, F0, MOD);

    Fn = { { Fn(1), Fn(0) } };
    return Fn;
}


void solve()
{
    ull N, M;
    ull a0, a1, a2, b0, b1, b2;
    int t;
    ull r;

    cin >> t;
    while (t--)
    {
        cin >> N >> a0 >> a1 >> a2 >> b0 >> b1 >> b2 >> M;

        // calcul de G = gcd(a0*Fn0+a1*Fn1+a2*Fn2, b0*Fn0+b1*Fn1+b2*Fn2)

        // Etape 1
        // a0*Fn0+a1*Fn1+a2*Fn2 = a0*Fn0+a1*Fn1+a2*(Fn0+Fn1) = (a0+a2)*Fn0+(a1+a2)*Fn1
        a0 += a2;
        a1 += a2;
        b0 += b2;
        b1 += b2;
        // d'où G = gcd(a0*Fn0+a1*Fn1, b0*Fn0+b1*Fn1)   (a0,a1,b0,b1 modifiés)


        // Etape 2
        // trouvons (a0', a1') et b0' tels que G = gcd(a0'*Fn0+b0'*Fn1, b0'*Fn0)
        // par l'algorithme d'Euclide: gcd(a, b)=gcd(b, a mod b)
        // on applique l'algo jusqu'à b1'=0

        if (a1 == 0)
        {
            swap(a0, b0);
            swap(a1, b1);
        }

        while (b1 != 0)
        {
            if (b1 < a1)
            {
                swap(a0, b0);
                swap(a1, b1);
            }

            ull q = b1 / a1;
            b0 = b0 - a0 * q;
            b1 = b1 - a1 * q;
        }

        // Etape 3
        // ici G = gcd(a0*Fn0+a1*Fn1, b0*Fn0)

        if (b0 == 0)
        {
            // simplification!
            // G = gcd(a0*Fn0+a1*Fn1, 0)
            // gcd(a, 0) = a
            vect2 Fn = F(N, M);
            r = (a0 * Fn(0) + a1 * Fn(1)) % M;
        }

        else if (a1 == 0)
        {
            // simplification!
            // G = gcd(a0*Fn0, b0*Fn0)
            // = gcd(a0, b0) * Fn0
            vect2 Fn = F(N, M);
            r = (gcd(a0, b0) * Fn(0)) % M;
        }
        else
        {
            // cas général...
            ull g = gcd(a1, F(N, a1)(0));

            vect2 Fn = F(N, b0 * g);

            r = gcd(a0 * Fn(0) + a1 * Fn(1), b0 * g) % M;
            if (r < 0) r = -r;
        }

        cout << r << endl;
    }
}


int main()
{
    solve();
    return 0;
}
