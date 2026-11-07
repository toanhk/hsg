# CHONTUYEN - loi giai subtask 2 (moi w = c = 1): thay Dijkstra bang BFS. Dung y tuong "2 lan tim duong" nhung
# chi lay diem subtask 2 (subtask 1 va 3 co trong so khac 1 -> sai). Cham thu: 3/10 test.
def bfs(n, adj, s):
    d = [-1] * (n + 1); d[s] = 0; q = [s]
    for u in q:
        for v in adj[u]:
            if d[v] < 0:
                d[v] = d[u] + 1; q.append(v)
    return d

def main():
    data = open('CHONTUYEN.INP', 'rb').read().split()
    n, m, k = int(data[0]), int(data[1]), int(data[2])
    adj = [[] for _ in range(n + 1)]
    p = 3
    for _ in range(m):
        u, v = int(data[p]), int(data[p + 1]); p += 3
        adj[u].append(v); adj[v].append(u)
    d1 = bfs(n, adj, 1); dn = bfs(n, adj, n)
    INF = float('inf')
    best = d1[n] if d1[n] >= 0 else INF; tuyen = 0
    for i in range(1, k + 1):
        u, v = int(data[p]), int(data[p + 1]); p += 3
        t = INF
        if d1[u] >= 0 and dn[v] >= 0:
            t = d1[u] + 1 + dn[v]
        if d1[v] >= 0 and dn[u] >= 0:
            t = min(t, d1[v] + 1 + dn[u])
        if t < best:
            best = t; tuyen = i
    with open('CHONTUYEN.OUT', 'w') as f:
        f.write('-1\n' if best == INF else f'{best} {tuyen}\n')

main()
