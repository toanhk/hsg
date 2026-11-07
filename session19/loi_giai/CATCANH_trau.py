# CATCANH - vet can (n <= 2000): thu cat tung canh, BFS tu mot dau (khong di qua canh do) dem tong. O(n^2).
def main():
    data = open('CATCANH.INP', 'rb').read().split()
    n = int(data[0])
    a = [0] + list(map(int, data[1:n + 1]))
    canh = [(int(data[n + 1 + 2 * i]), int(data[n + 2 + 2 * i])) for i in range(n - 1)]
    adj = [[] for _ in range(n + 1)]
    for u, v in canh:
        adj[u].append(v); adj[v].append(u)
    S = sum(a)
    best = None
    for x, y in canh:
        da = [False] * (n + 1); da[x] = True
        q = [x]; t = 0
        for u in q:
            t += a[u]
            for v in adj[u]:
                if not da[v] and not (u == x and v == y):
                    da[v] = True; q.append(v)
        d = abs(S - 2 * t)
        if best is None or d < best:
            best = d
    with open('CATCANH.OUT', 'w') as f:
        f.write(str(best) + '\n')

main()
