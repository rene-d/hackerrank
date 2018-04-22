# Mathematics > Fundamentals > Jim and the Jokes
# Jim is running out of jokes! Help him finding new jokes.
#
# https://www.hackerrank.com/challenges/jim-and-the-jokes/problem
#

# algo: créer une table qui compte les nombres lus dans la base indiquée

jokes = {}
for _ in range(int(input())):
    b, x = input().split()
    try:
        f = int(x, int(b))
        jokes[f] = jokes.get(f, 0) + 1
    except ValueError:
        # erreur de conversion dans la base donnée
        pass

# attention: quand il y a plusieurs fois le même nombre, toutes les valeurs comptent
print(sum(f * (f - 1) // 2 for f in jokes.values() if f >= 1))
