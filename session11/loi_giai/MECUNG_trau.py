# MECUNG - vet can kieu "lap cho den khi on dinh": dist[S] = 0, lap lai viec cap nhat
# dist[o] = min(dist[o ke] + 1) cho moi o, cho den khi mot luot quet khong doi gi.
# Dung (giong Bellman-Ford) nhung moi luot O(m*n), co the can toi m*n luot -> chi subtask 1.
def main():
    data = open('MECUNG.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    g = [r.decode() for r in data[2:2 + m]]
    VC = 10**9
    d = [[VC] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if g[i][j] == 'S':
                d[i][j] = 0
            if g[i][j] == 'E':
                ei, ej = i, j
    doi = True
    while doi:
        doi = False
        for i in range(m):
            for j in range(n):
                if g[i][j] == '#':
                    continue
                for u, v in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= u < m and 0 <= v < n and d[u][v] + 1 < d[i][j]:
                        d[i][j] = d[u][v] + 1
                        doi = True
    kq = d[ei][ej] if d[ei][ej] < VC else -1
    with open('MECUNG.OUT', 'w') as f:
        f.write(str(kq) + '\n')

main()
