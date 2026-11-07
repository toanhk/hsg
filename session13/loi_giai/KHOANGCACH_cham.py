# KHOANGCACH - ban CHAM: giong loi giai mau nhung QUEN dong "if d > dist[u]: continue".
# Van ra dung dap an, nhung cap loi thoi van duyet lai toan bo ke cua u. Do thi ngau nhien chi cham
# hon mot chut; Test10 la do thi "bay": dinh trung tam bac 10^5 bi cap nhat 1000 lan -> 10^8 phep, qua gio.
import heapq

def main():
    data = list(map(int, open('KHOANGCACH.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    it = iter(data[2:2 + 3 * m])
    for u, v, w in zip(it, it, it):
        adj[u].append((v, w))
        adj[v].append((u, w))
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)]
    while pq:
        d, u = heapq.heappop(pq)
        for v, w in adj[u]:              # THIEU: if d > dist[u]: continue
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    with open('KHOANGCACH.OUT', 'w') as f:
        f.write(' '.join(str(x) if x < INF else '-1' for x in dist[1:]) + '\n')

main()
