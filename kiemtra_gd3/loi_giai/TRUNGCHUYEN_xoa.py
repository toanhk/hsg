# TRUNGCHUYEN - ban trung gian O(n * (n + m)): nut v (khac 1, n) nam tren moi duong ngan nhat <=> XOA v
# di thi khoang cach 1 -> n tang len (hoac khong toi duoc). Dung cho subtask 2 (n <= 2000).
from collections import deque

def bfs(adj, n, s, cam=0):
    d = [-1] * (n + 1)
    d[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v != cam and d[v] < 0:
                d[v] = d[u] + 1; q.append(v)
    return d

def main():
    data = open('TRUNGCHUYEN.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v = int(data[2 + 2 * i]), int(data[3 + 2 * i])
        adj[u].append(v); adj[v].append(u)
    d1 = bfs(adj, n, 1)
    D = d1[n]
    if D < 0:
        out = '-1'
    else:
        dn = bfs(adj, n, n)
        tren = [v for v in range(1, n + 1) if d1[v] >= 0 and d1[v] + dn[v] == D]
        B = 0
        for v in tren:
            if v == 1 or v == n:
                B += 1
            else:
                k = bfs(adj, n, 1, cam=v)[n]
                if k < 0 or k > D:
                    B += 1
        out = f'{D} {len(tren)} {B}'
    with open('TRUNGCHUYEN.OUT', 'w') as f:
        f.write(out + '\n')

main()
