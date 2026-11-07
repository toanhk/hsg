# KHOBAU - vet can (k <= 7): BFS tu moi diem quan trong nhu ban chinh, roi thu MOI thu tu nhat kho bau (k!).
from itertools import permutations
from collections import deque

def main():
    data = open('KHOBAU.INP', 'rb').read().split()
    R, C = int(data[0]), int(data[1])
    g = [data[2 + i].decode() for i in range(R)]
    diem = [None]
    for i in range(R):
        for j in range(C):
            if g[i][j] == 'S':
                diem[0] = (i, j)
            elif g[i][j] == '*':
                diem.append((i, j))
    D = []
    for si, sj in diem:
        dist = [[-1] * C for _ in range(R)]
        dist[si][sj] = 0
        q = deque([(si, sj)])
        while q:
            i, j = q.popleft()
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < R and 0 <= y < C and g[x][y] != '#' and dist[x][y] < 0:
                    dist[x][y] = dist[i][j] + 1
                    q.append((x, y))
        D.append([dist[x][y] for x, y in diem])
    k = len(diem) - 1
    if any(x < 0 for x in D[0]):
        best = -1
    else:
        best = 0 if k == 0 else None
        for p in permutations(range(1, k + 1)) if k > 0 else ():
            t = D[0][p[0]] + sum(D[p[i]][p[i + 1]] for i in range(k - 1))
            if best is None or t < best:
                best = t
    with open('KHOBAU.OUT', 'w') as f:
        f.write(str(best) + '\n')

main()
