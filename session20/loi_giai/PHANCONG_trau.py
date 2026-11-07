# PHANCONG - vet can (n <= 9): thu moi hoan vi p, nguoi i lam viec p[i]. O(n! * n).
from itertools import permutations

def main():
    data = open('PHANCONG.INP', 'rb').read().split()
    n = int(data[0])
    c = [list(map(int, data[1 + i * n:1 + (i + 1) * n])) for i in range(n)]
    best = min(sum(c[i][p[i]] for i in range(n)) for p in permutations(range(n)))
    with open('PHANCONG.OUT', 'w') as f:
        f.write(str(best) + '\n')

main()
