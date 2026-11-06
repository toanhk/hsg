# DEMNGAN - vet can: quay lui moi duong don tu 1 den n, dem so duong theo do dai, lay do dai nho
# nhat (duong ngan nhat luon la duong don). Chi subtask 1 (n <= 10).
import sys

def main():
    a = list(map(int, open('DEMNGAN.INP', 'rb').read().split()))
    n, m = a[0], a[1]
    ke = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v = a[2 + 2 * i], a[3 + 2 * i]
        ke[u].append(v); ke[v].append(u)
    sys.setrecursionlimit(10000)
    dem = {}
    tham = [False] * (n + 1); tham[1] = True

    def thu(u, d):
        if u == n:
            dem[d] = dem.get(d, 0) + 1
            return
        for v in ke[u]:
            if not tham[v]:
                tham[v] = True
                thu(v, d + 1)
                tham[v] = False

    thu(1, 0)
    if dem:
        d = min(dem)
        res = f'{d} {dem[d] % (10**9 + 7)}\n'
    else:
        res = '-1 0\n'
    with open('DEMNGAN.OUT', 'w') as f:
        f.write(res)

main()
