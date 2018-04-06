// Path sum: two ways
//
// https://projecteuler.net/problem=81
// https://www.hackerrank.com/contests/projecteuler/challenges/euler081

#include <vector>
#include <queue>
#include <iostream>
#include <fstream>
#include <string>
#include <locale>
#include <cassert>


typedef unsigned long long  MatrixValue;


struct Matrix : public std::vector<MatrixValue>
{
    size_type n;

    MatrixValue v(size_type x, size_type y) const
    {
        return at(x + y * n);
    }
};


struct Visited : public std::vector<bool>
{
    size_type n;

    bool v(size_type x, size_type y) const
    {
        return at(x + y * n);
    }

    void set(size_type x, size_type y)
    {
        at(x + y * n) = true;
    }
};


struct Cell
{
    size_t      x, y;
    MatrixValue v;

    Cell(size_t x, size_t y, MatrixValue v) : x(x), y(y), v(v)
    {
    }

    bool operator<(const Cell& r) const
    {
        return v > r.v;
    }
};


struct comma_is_space : std::ctype<char>
{
    comma_is_space() : std::ctype<char>(get_table()) {}
    static mask const* get_table()
    {
        static mask rc[table_size];
        rc[static_cast<size_t>(',')] = std::ctype_base::space;
        rc[static_cast<size_t>('\n')] = std::ctype_base::space;
        return &rc[0];
    }
};


bool read(Matrix& matrix)
{
    matrix.n = 80;
    matrix.resize(matrix.n * matrix.n);

    std::ifstream f("p081_matrix.txt");
    if (f.is_open())
    {
        size_t i = 0;

        // modifie le séparateur de lecture
        f.imbue(std::locale(f.getloc(), new comma_is_space));

        while (!f.eof() && i < matrix.size())
            f >> matrix[i++];

        return i == matrix.size();
    }
    return false;
}


MatrixValue solve(const Matrix& matrix)
{
    const size_t                n = matrix.n;
    Visited                     visited;
    std::priority_queue<Cell>   stack;

    visited.n = n;
    visited.resize(matrix.size(), false);

    stack.push(Cell(0, 0, matrix.v(0, 0)));

    while (! stack.empty())
    {
        Cell e = stack.top();
        stack.pop();

        if (visited.v(e.x, e.y))
            continue;

        visited.set(e.x, e.y);

        if (e.x == n - 1 && e.y == n - 1)
            return e.v;

        if (e.x < n - 1)
            stack.push(Cell(e.x + 1, e.y, e.v + matrix.v(e.x + 1, e.y)));

        if (e.y < n - 1)
            stack.push(Cell(e.x, e.y + 1, e.v + matrix.v(e.x, e.y + 1)));
    }

    return 0;
}


int main()
{
    Matrix  matrix;

    if (! read(matrix))
    {
        // HackerRank
        std::cin >> matrix.n;
        matrix.resize(matrix.n * matrix.n);
        for (size_t i = 0; i < matrix.n * matrix.n; ++i)
            std::cin >> matrix[i];
    }

    std::cout << solve(matrix) << std::endl;

    return 0;
}
