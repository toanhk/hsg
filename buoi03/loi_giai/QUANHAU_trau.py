# QUANHAU - vet can: moi hang mot quan, cac cot khac nhau -> moi cach la mot hoan vi p
# (hang r dat o cot p[r]). Duyet ca n! hoan vi, kiem tra o cam va duong cheo: O(n! * n^2)
# Chi qua n <= 8 (40320 hoan vi)
from itertools import permutations

def main():
    data = open('QUANHAU.INP', 'rb').read().split()
    n = int(data[0])
    ban = [data[1 + r].decode() for r in range(n)]
    dem = 0
    for p in permutations(range(n)):
        ok = all(ban[r][p[r]] == '.' for r in range(n))
        for r1 in range(n):
            for r2 in range(r1 + 1, n):
                if abs(p[r1] - p[r2]) == r2 - r1:
                    ok = False
        if ok:
            dem += 1
    with open('QUANHAU.OUT', 'w') as f:
        f.write(str(dem) + '\n')

main()
