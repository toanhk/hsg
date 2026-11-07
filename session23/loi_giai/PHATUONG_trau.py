# PHATUONG - vet can: thu "khong pha" va pha tung o tuong mot, moi lan BFS lai. O(so tuong * r * c), luoi nho.
from collections import deque

def bfs(g, r, c, s, e):
    d = {s: 0}; q = deque([s])
    while q:
        i, j = q.popleft()
        if (i, j) == e:
            return d[(i, j)]
        for a, b in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= a < r and 0 <= b < c and g[a][b] != '#' and (a, b) not in d:
                d[(a, b)] = d[(i, j)] + 1; q.append((a, b))
    return -1

def main():
    data = open('PHATUONG.INP', 'rb').read().split()
    t = int(data[0]); pos = 1
    out = []
    for _ in range(t):
        r, c = int(data[pos]), int(data[pos + 1]); pos += 2
        g = [list(data[pos + i].decode()) for i in range(r)]; pos += r
        s = next((i, j) for i in range(r) for j in range(c) if g[i][j] == 'S')
        e = next((i, j) for i in range(r) for j in range(c) if g[i][j] == 'T')
        best = bfs(g, r, c, s, e)
        for i in range(r):
            for j in range(c):
                if g[i][j] == '#':
                    g[i][j] = '.'
                    v = bfs(g, r, c, s, e)
                    g[i][j] = '#'
                    if v != -1 and (best == -1 or v < best):
                        best = v
        out.append(best)
    with open('PHATUONG.OUT', 'w') as f:
        f.write('\n'.join(map(str, out)) + '\n')

main()
