# DUONGKINH - vet can (n <= 2000): tu MOI dinh duyet ca cay tinh khoang cach, lay max. O(n^2).
def main():
    data = open('DUONGKINH.INP', 'rb').read().split()
    n = int(data[0])
    adj = [[] for _ in range(n + 1)]
    for i in range(1, 3 * n - 2, 3):
        u, v, w = int(data[i]), int(data[i + 1]), int(data[i + 2])
        adj[u].append((v, w)); adj[v].append((u, w))
    best = 0
    for s in range(1, n + 1):
        d = [-1] * (n + 1); d[s] = 0
        q = [s]
        for u in q:
            for v, w in adj[u]:
                if d[v] < 0:
                    d[v] = d[u] + w; q.append(v)
        best = max(best, max(d))
    with open('DUONGKINH.OUT', 'w') as f:
        f.write(str(best) + '\n')

main()
