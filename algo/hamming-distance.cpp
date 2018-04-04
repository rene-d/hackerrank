// Hamming Distance
// You are given a string S, consisting of N small latin letters 'a'
// and 'b'. Process the given M queries.
// 
// https://www.hackerrank.com/challenges/hamming-distance/problem
// 

#include <bits/stdc++.h>

using namespace std;

int main()
{
    std::string str1, str2;
    size_t n, m;
    char cmd;

    cin >> n;
    cin >> str1;
    cin >> m;

    str2.resize(n);

    char *buf[2] = 
    {
         const_cast<char *>(str1.data()),
         const_cast<char *>(str2.data()),
    };
    
    int cur = 0;
    char *s = buf[0];

    while (m-- != 0)
    {
        cin >> cmd;
        if (cmd == 'C')
        {
            size_t l, r;
            char ch;
            cin >> l >> r >> ch;
            for (size_t i = l - 1; i < r; ++i) s[i] = ch;
        }
        else if (cmd == 'R')
        {
            size_t l, r;
            cin >> l >> r;
            for (size_t i = 0; i < (r - l + 1) / 2; ++i)
                swap(s[i + l - 1], s[r - i - 1]);
        }
        else if (cmd == 'W')
        {
            size_t l, r;
            cin >> l >> r;
            cout.write(s + l - 1, (streamsize)(r - l + 1));
            cout << endl;
        }
        else if (cmd == 'H')
        {
            size_t l1, l2, len;
            cin >> l1 >> l2 >> len;
            int h = 0;
            l1--; 
            l2--;
            for (size_t i = 0; i < len; ++i)
            {
                if (s[l1 + i] != s[l2 + i]) h++;
            }
            cout << h << endl;
        }
        else if (cmd == 'S')
        {
            size_t l1, r1, l2, r2;
            cin >> l1 >> r1 >> l2 >> r2;

            char *tmp = buf[1 - cur];
            #define COPY(a, b) if (b != 0) { memcpy(tmp, s + a, b); tmp += b; }
                
            COPY(0, l1 - 1);
            COPY(l2 - 1, r2 - l2 + 1);
            COPY(r1, l2 - r1 - 1);
            COPY(l1 - 1, r1 - l1 + 1);
            COPY(r2, n - r2);

            cur = 1 - cur;
            s = buf[cur];
        }
    }


    return 0;
}

