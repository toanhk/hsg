# MOICAP - vet can (subtask 1, n <= 50): moi cau hoi chay Bellman-Ford tu u (n - 1 vong duyet canh).
# Cache theo dinh xuat phat de khong chay lai. O(n * n * m) toi da.
def main():
    data = open('MOICAP.INP', 'rb').read().split()
    n, m, q = int(data[0]), int(data[1]), int(data[2])
    canh = []
    p = 3
    for _ in range(m):
        u = int(data[p]); v = int(data[p + 1]); w = int(data[p + 2]); p += 3
        canh.append((u, v, w)); canh.append((v, u, w))
    INF = float('inf')
    nho = {}
    out = []
    for _ in range(q):
        s = int(data[p]); t = int(data[p + 1]); p += 2
        if s not in nho:
            d = [INF] * (n + 1); d[s] = 0
            for _ in range(n - 1):
                for u, v, w in canh:
                    if d[u] + w < d[v]:
                        d[v] = d[u] + w
            nho[s] = d
        out.append(str(nho[s][t]) if nho[s][t] < INF else '-1')
    with open('MOICAP.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
