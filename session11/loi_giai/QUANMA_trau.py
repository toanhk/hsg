# QUANMA - vet can: lap cap nhat d[o] = min(d[o ma nhay toi] + 1) cho den khi on dinh.
# Moi luot O(8 n^2), so luot co the toi ~n^2/2 -> chi subtask 1 (n <= 20).
def main():
    data = open('QUANMA.INP', 'rb').read().split()
    n = int(data[0])
    x1, y1, x2, y2 = map(int, data[1:5])
    g = [r.decode() for r in data[5:5 + n]]
    VC = 10**9
    d = [[VC] * n for _ in range(n)]
    d[x1 - 1][y1 - 1] = 0
    buoc = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    doi = True
    while doi:
        doi = False
        for i in range(n):
            for j in range(n):
                if g[i][j] == '#':
                    continue
                for a, b in buoc:
                    u, v = i + a, j + b
                    if 0 <= u < n and 0 <= v < n and d[u][v] + 1 < d[i][j]:
                        d[i][j] = d[u][v] + 1
                        doi = True
    kq = d[x2 - 1][y2 - 1]
    with open('QUANMA.OUT', 'w') as f:
        f.write(str(kq if kq < VC else -1) + '\n')

main()
