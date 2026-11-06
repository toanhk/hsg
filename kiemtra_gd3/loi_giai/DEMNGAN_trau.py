# DEMNGAN - vet can (n <= 10): quay lui moi duong DON tu 1 den n (duong ngan nhat luon la duong don),
# ghi do dai nho nhat va so duong dat do dai do.
import sys

def main():
    sys.setrecursionlimit(10000)
    data = open('DEMNGAN.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        adj[int(data[2 + 2 * i])].append(int(data[3 + 2 * i]))
    tot = [10**9, 0]
    tham = [False] * (n + 1)

    def di(u, k):
        if u == n:
            if k < tot[0]: tot[0], tot[1] = k, 1
            elif k == tot[0]: tot[1] += 1
            return
        for v in adj[u]:                     # cung trung lap = duong khac nhau
            if not tham[v]:
                tham[v] = True; di(v, k + 1); tham[v] = False

    tham[1] = True; di(1, 0)
    with open('DEMNGAN.OUT', 'w') as f:
        f.write(f'{tot[0]} {tot[1] % (10**9 + 7)}\n' if tot[1] else '-1\n')

main()
