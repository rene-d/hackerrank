// Security > Cryptography > PRNG Sequence Guessing
// Given last ten output values of random.nextInt(), guess the next value to be output by the generator.
//
// https://www.hackerrank.com/challenges/prng-sequence-guessing/problem
// challenge id: 786
//

#include <iostream>
#include <cstdint>

using namespace std;


uint64_t next_int(uint64_t& seed)
{
    seed = (seed * 0x5DEECE66Dull + 0xB) & ((1ull << 48) - 1);

    return (seed >> 17) % 1000ull;
}


uint64_t find_seed(const uint64_t a[10])
{
    uint64_t seed0, seed1, seed;
    int i;

    for (seed0 = 0; seed0 < 1ull << 17; ++seed0)
    {
        seed = seed0 + ((a[0] % 8) << 17);

        for (i = 1; i < 10; ++i)
        {
            if (next_int(seed) % 8 != a[i] % 8)
                break;
        }

        if (i == 10)
        {
            for (seed1 = (a[0] << 17) + seed0; seed1 < (1ull << 48); seed1 += (1000ull << 17))
            {
                seed = seed1;
                for (i = 1; i < 10; ++i)
                {
                    if (next_int(seed) != a[i])
                        break;
                }
                if (i == 10)
                    return seed1;
            }
        }
    }

    return 0;
}


int main()
{
    int t, i;
    uint64_t a[10], seed, x;

    cin >> t;
    while (t--)
    {
        for (i = 0; i < 10; ++i)
            cin >> a[i];

        seed = find_seed(a);

        // nota: le premier nombre de la série est: (seed >> 17) % 1000

        for (i = 1; i < 20; ++i)
        {
            x = next_int(seed);
            if (i >= 10) cout << x << " ";
        }
        cout << endl;
    }
    return 0;
}
