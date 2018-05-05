// Digit factorial chains
//
// https://projecteuler.net/problem=74
// https://www.hackerrank.com/contests/projecteuler/challenges/euler074

#include <bits/stdc++.h>


const unsigned fact10[] = { 1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880 };

unsigned sum_fact_digits(unsigned n)
{
    unsigned sum = 0;
    do {
        sum += fact10[n % 10];
        n /= 10;
    } while (n != 0);
    return sum;
}


int main()
{
    unsigned nb = 0;
    std::vector<unsigned char> lengths(4000000, 0);

    // cas spéciaux des boucles
    lengths[169] = 3;
    lengths[1454] = 3;
    lengths[363601] = 3;

    lengths[871] = 2;
    lengths[872] = 2;
    lengths[45361] = 2;
    lengths[45362] = 2;

    for (unsigned n = 0; n < 1000000; ++n)
    {
        std::set<unsigned> visited;
        unsigned i = n;
        unsigned k = 0;

        while (visited.count(i) == 0)
        {
            if (i >= 4000000) exit(2);
            if (lengths[i] != 0)
            {
                k += lengths[i];
                break;
            }
            k++;
            visited.insert(i);
            i = sum_fact_digits(i);

            //if (i == n) std::cout << "LOOP " << n << " " << k << std::endl;
        }
        if (k == 60)
        {
            nb++;
        }
        if (k > 250) exit(2);
        lengths[n] = (unsigned char) k;
    }

    if (false)
    {
        std::cout << nb << std::endl;
    }
    else
    {
        unsigned T;
        std::cin >> T;
        while (T--)
        {
            unsigned N, L;
            bool found = false;

            std::cin >> N >> L;

            for (unsigned i = 0; i <= N; ++i)
            {
                if (lengths[i] == L)
                {
                    std::cout << i << " ";
                    found = true;
                }
            }

            if (! found)
                std::cout << "-1";

            std::cout << std::endl;
        }
    }

    return 0;
}
