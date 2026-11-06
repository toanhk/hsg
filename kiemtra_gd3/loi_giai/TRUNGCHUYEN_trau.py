# TRUNGCHUYEN - vet can (n <= 10): quay lui moi duong DON tu 1 den n, giu cac duong ngan nhat,
# A = hop cac tap nut, B = giao cac tap nut.
import sys

def main():
    sys.setrecursionlimit(10000)
    data = open('TRUNGCHUYEN.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v = int(data[2 + 2 * i]), int(data[3 + 2 * i])
        adj[u].append(v); adj[v].append(u)
    tot = [10**9, None, None]                # do dai, hop, giao
    duong = [1]

    def di(u):
        if u == n:
            k = len(duong) - 1; s = set(duong)
            if k < tot[0]:
                tot[0], tot[1], tot[2] = k, set(s), set(s)
            elif k == tot[0]:
                tot[1] |= s; tot[2] &= s
            return
        for v in adj[u]:
            if v not in duong:
                duong.append(v); di(v); duong.pop()

    di(1)
    out = '-1' if tot[1] is None else f'{tot[0]} {len(tot[1])} {len(tot[2])}'
    with open('TRUNGCHUYEN.OUT', 'w') as f:
        f.write(out + '\n')

main()
