# GIAOHANG - vet can (n <= 9): thu moi thu tu tham n-1 diem con lai. O((n-1)! * n).
from itertools import permutations

def main():
    data = open('GIAOHANG.INP', 'rb').read().split()
    n = int(data[0])
    d = [list(map(int, data[1 + i * n:1 + (i + 1) * n])) for i in range(n)]
    best = 0 if n == 1 else None
    for p in permutations(range(1, n)) if n > 1 else ():
        t = d[0][p[0]] + d[p[-1]][0]
        for i in range(len(p) - 1):
            t += d[p[i]][p[i + 1]]
        if best is None or t < best:
            best = t
    with open('GIAOHANG.OUT', 'w') as f:
        f.write(str(best) + '\n')

main()
