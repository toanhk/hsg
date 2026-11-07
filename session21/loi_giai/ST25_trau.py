# ST25 - vet can cho n nho (n <= 100): Floyd lay moi khoang cach, thu moi h, moi hoan vi K dai ly.
from itertools import permutations

def main():
    data = open('ST25.INP', 'rb').read().split()
    n, m, K = int(data[0]), int(data[1]), int(data[2])
    x = [int(v) for v in data[3:3 + K]]
    INF = float('inf')
    D = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        D[i][i] = 0
    pos = 3 + K
    for _ in range(m):
        u, v, w = int(data[pos]), int(data[pos + 1]), int(data[pos + 2]); pos += 3
        if w < D[u][v]:
            D[u][v] = D[v][u] = w
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
    best, bh = INF, -1
    for h in range(1, n + 1):
        if h in x:
            continue
        for p in permutations(x):
            s = D[h][p[0]] + D[p[-1]][h]
            for i in range(K - 1):
                s += D[p[i]][p[i + 1]]
            if s < best:
                best, bh = s, h
    with open('ST25.OUT', 'w') as f:
        f.write(f'{bh} {best}\n')

main()
