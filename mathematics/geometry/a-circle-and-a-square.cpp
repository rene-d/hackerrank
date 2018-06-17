// Mathematics > Geometry > A Circle and a Square
// Draw a circle and a square at specific coordinates within a raster image.
//
// https://www.hackerrank.com/challenges/a-circle-and-a-square/problem
// https://www.hackerrank.com/contests/w29/challenges/a-circle-and-a-square
// challenge id: 30440
//

#include <bits/stdc++.h>

using namespace std;


struct point
{
    int x;
    int y;
};

int sign(const point& p1, const point& p2, const point& p3)
{
    return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y);
}

bool pntriangle(const point& pt, const point& v1, const point& v2, const point& v3)
{
    bool b1, b2, b3;

    b1 = sign(pt, v1, v2) < 0;
    b2 = sign(pt, v2, v3) < 0;
    b3 = sign(pt, v3, v1) < 0;

    return ((b1 == b2) && (b2 == b3));
}

bool pisquare(const int x[4], const int y[4], int testx, int testy)
{
    point pt { testx, testy};

    point v1 { x[0], y[0] },
          v2 { x[1], y[1] },
          v3 { x[2], y[2] },
          v4 { x[3], y[3] };

    return pntriangle(pt, v1, v2, v3) || pntriangle(pt, v1, v3, v4);
}

int main()
{
    int w, h;
    int xc, yc, r;
    int xs[4], ys[4];
    int x, y;

    cin >> w >> h;
    cin >> xc >> yc >> r;
    cin >> xs[0] >> ys[0] >> xs[2] >> ys[2];

    // l'astuce consiste à doubler les coordonnées du carré pour gérer les cas où
    // les deux autres sommets ont des coordonnées en 0.5
    xs[0] *= 2;
    ys[0] *= 2;
    xs[2] *= 2;
    ys[2] *= 2;

    // calcul des deux autres sommets du carré
    x = (xs[0] + xs[2]) / 2;
    y = (ys[0] + ys[2]) / 2;

    xs[1] = x + (y - ys[0]);
    ys[1] = y - (x - xs[0]);

    xs[3] = x - (y - ys[0]);
    ys[3] = y + (x - xs[0]);


    for (int y = 0; y < h; ++y)
    {
        for (int x = 0; x < w; ++x)
        {
            char c = '.';

            // est-ce que (x, y) est dans le cercle ?
            if ((x - xc) * (x - xc) + (y - yc) * (y - yc) <= r * r)
            {
                c = '#';
            }

            // est-ce que le point est dans le carré ?
            else if (pisquare(xs, ys, x * 2, y * 2))
            {
                c = '#';
            }

            cout << c;
        }
        cout << endl;
    }

    return 0;
}
