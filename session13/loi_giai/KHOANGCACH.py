# KHOANGCACH: do thi vo huong n dinh, m canh co trong so (w <= 10^9). In khoang cach ngan nhat tu
# dinh 1 toi tung dinh 1..n, -1 neu khong toi duoc. n, m <= 10^5.
# Dijkstra voi heapq (dung khung trong lo trinh):
#   - pq chua cap (d, u): "co mot duong di toi u dai d". Lay ra cap co d nho nhat.
#   - Mot dinh co the nam trong pq nhieu lan (moi lan dist giam lai day vao). Cap lay ra co d > dist[u]
#     la cap LOI THOI -> bo qua ngay, neu khong se duyet lai ke cua u (de bi O(n*m), xem do_dijkstra.py).
#   - Lan dau u duoc lay ra voi d == dist[u] thi dist[u] da la dap an cuoi cung (trong so khong am).
# O((n + m) log m).
import heapq

def main():
    data = list(map(int, open('KHOANGCACH.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    it = iter(data[2:2 + 3 * m])
    for u, v, w in zip(it, it, it):
        adj[u].append((v, w))
        adj[v].append((u, w))           # vo huong: them ca hai chieu
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:                 # cap loi thoi: u da duoc chot voi khoang cach nho hon
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    with open('KHOANGCACH.OUT', 'w') as f:
        f.write(' '.join(str(x) if x < INF else '-1' for x in dist[1:]) + '\n')

main()
