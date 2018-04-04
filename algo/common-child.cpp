// Common Child
// Given two strings a and b of equal length, what's the longest string (s) that can be constructed such that s is a child to both a and b?
//
// https://www.hackerrank.com/challenges/common-child/problem
//

// ref: https://en.wikipedia.org/wiki/Longest_common_subsequence_problem

#include <bits/stdc++.h>

size_t lcs_length(const std::string& s1, const std::string& s2)
{
    size_t m = s1.size();
    size_t n = s2.size();

    std::vector<size_t> C((m + 1) * (n + 1), 0);

    size_t K = n + 1;

    for (size_t i = 0; i < m; ++i)
    {
        for (size_t j = 0; j < n; ++j)
        {
            if (s1[i] == s2[j])
                C[i + 1 + (j + 1) * K] = C[i + j * K] + 1;
            else
                C[i + 1 + (j + 1) * K] = std::max(C[(i + 1) + j * K], C[i + (j + 1) * K]);
        }
    }
    return C[m + n * K];
}

int main()
{
    std::string s1;
    std::string s2;

    std::cin >> s1 >> s2;
    std::cout << lcs_length(s1, s2) << std::endl;

    return 0;
}
