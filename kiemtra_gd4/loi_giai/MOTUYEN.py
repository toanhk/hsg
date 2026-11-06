# MOTUYEN: n nut, m duong hai chieu (u, v, thoi gian w). Can di tu nut 1 den nut n. Thanh pho co k de xuat mo
# tuyen moi (de xuat thu i: duong hai chieu u_i - v_i, thoi gian c_i) va duoc mo TOI DA MOT tuyen.
# In thoi gian ngan nhat co the va so hieu tuyen nen mo (0 neu khong mo tuyen nao van tot nhat; nhieu tuyen
# cung tot thi in so hieu nho nhat). Khong the toi n thi in -1.  n, m, k <= 10^5; w, c <= 10^9.
# Hai lan Dijkstra: d1[] tu nut 1, dn[] tu nut n (do thi vo huong nen dn[v] = khoang cach v -> n).
# Mo tuyen (u, v, c): duong tot nhat CO dung tuyen nay = min(d1[u] + c + dn[v], d1[v] + c + dn[u]).
# Duong khong dung tuyen moi = d1[n]. Duyet k de xuat, O(1) moi de xuat.
# O((n + m) log m + k). Do: ~0,6 s voi n = m = k = 10^5.
import heapq

def dijkstra(n, adj, s):
    # Phan tu heap la MOT so nguyen d * 2^17 + u (u < 2^17 = 131072) thay vi tuple (d, u): so sanh so nguyen
    # nhanh hon so sanh tuple, Dijkstra nhanh hon ~30%. Lay lai: d = x >> 17, u = x & 131071.
    INF = 1 << 62
    d = [INF] * (n + 1)
    d[s] = 0
    pq = [s]                                   # 0 * 2^17 + s
    pop, push = heapq.heappop, heapq.heappush
    while pq:
        x = pop(pq)
        du = x >> 17; u = x & 131071
        if du > d[u]:
            continue                           # ban ghi loi thoi
        for v, w in adj[u]:
            nd = du + w
            if nd < d[v]:
                d[v] = nd
                push(pq, nd << 17 | v)
    return d

def main():
    data = open('MOTUYEN.INP', 'rb').read().split()
    n, m, k = int(data[0]), int(data[1]), int(data[2])
    U = list(map(int, data[3:3 + 3 * m:3]))
    V = list(map(int, data[4:4 + 3 * m:3]))
    W = list(map(int, data[5:5 + 3 * m:3]))
    adj = [[] for _ in range(n + 1)]
    for u, v, w in zip(U, V, W):
        adj[u].append((v, w)); adj[v].append((u, w))
    d1 = dijkstra(n, adj, 1)
    dn = dijkstra(n, adj, n)
    p = 3 + 3 * m
    A = list(map(int, data[p:p + 3 * k:3]))
    B = list(map(int, data[p + 1:p + 3 * k:3]))
    C = list(map(int, data[p + 2:p + 3 * k:3]))
    best = d1[n]; tuyen = 0
    for i in range(k):
        u = A[i]; v = B[i]
        t = min(d1[u] + dn[v], d1[v] + dn[u]) + C[i]
        if t < best:                           # chi doi khi TOT HON HAN -> giu so hieu nho nhat
            best = t; tuyen = i + 1
    with open('MOTUYEN.OUT', 'w') as f:
        f.write('-1\n' if best >= 1 << 62 else f'{best} {tuyen}\n')

main()
