keys = []
nb = int(input())
for _ in range(nb):
    keys.append(input().strip())

passcode = sorted(list(set(''.join(keys))))

for key in keys:
    # met les chiffres de key dans l'ordre dans passcode
    a = passcode.index(key[0])
    b = passcode.index(key[1])
    c = passcode.index(key[2])
    if a > b:
        passcode[a], passcode[b] = passcode[b], passcode[a]
        b = a
    if b > c:
        passcode[c], passcode[b] = passcode[b], passcode[c]

print(''.join(passcode))
