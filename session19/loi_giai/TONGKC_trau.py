# TONGKC - vet can (n <= 2000): BFS tu moi dinh, cong khoang cach. O(n^2).
def main():
    data = open('TONGKC.INP', 'rb').read().split()
    n = int(data[0])
    adj = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        u, v = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        adj[u].append(v); adj[v].append(u)
    kq = []
    for s in range(1, n + 1):
        d = [-1] * (n + 1); d[s] = 0
        q = [s]
        for u in q:
            for v in adj[u]:
                if d[v] < 0:
                    d[v] = d[u] + 1; q.append(v)
        kq.append(sum(d) + 1)                  # d[0] = -1 bu lai
    with open('TONGKC.OUT', 'w') as f:
        f.write(' '.join(map(str, kq)) + '\n')

main()
