# Linux Shell > Bash > Functions and Fractals - Recursive Trees - Bash!
# Create a Fractal Tree
#
# https://www.hackerrank.com/challenges/fractal-trees-all/problem
#

# un jour, peut-être, je réécrirai en bash ;-)

cat <<'EOF' > toto.py
ligne = ["_"] * 100
Y = []
for i in range(63):
    Y.append(ligne[:])
def gen(y, x, n, iter):
    for i in range(n):
        Y[y - i - n][x - 1 - i] = '1'
        Y[y - i - n][x + 1 + i] = '1'
    for i in range(n):
        Y[y - i][x] = '1'
    if n > 1 and iter > 0:
        gen(y - n * 2, x - n, n // 2, iter - 1)
        gen(y - n * 2, x + n, n // 2, iter - 1)
gen(62, 49, 16, int(input()) - 1)
for i in Y:
    print(''.join(i))
EOF
python3 toto.py
