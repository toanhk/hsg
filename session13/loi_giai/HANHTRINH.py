# HANHTRINH: do thi vo huong co trong so, n, m <= 10^5. Tim duong di ngan nhat tu 1 den n va IN RA
# duong di: dong 1 la do dai D, dong 2 la so dinh k, dong 3 la k dinh tu 1 den n. Khong toi duoc: -1.
# Truy vet: moi khi dist[v] giam nho canh u -> v thi ghi tr[v] = u (dinh dung TRUOC v tren duong tot nhat).
# Xong Dijkstra, di nguoc tu n theo tr ve 1 roi dao nguoc danh sach. Nhieu duong cung ngan -> in duong nao
# cung duoc (cham bang kiem_tra.py).
import heapq

def main():
    data = list(map(int, open('HANHTRINH.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    it = iter(data[2:2 + 3 * m])
    for u, v, w in zip(it, it, it):
        adj[u].append((v, w))
        adj[v].append((u, w))
    INF = float('inf')
    dist = [INF] * (n + 1)
    tr = [0] * (n + 1)                   # tr[v] = dinh truoc v; tr[1] = 0 la diem dung khi truy vet
    dist[1] = 0
    pq = [(0, 1)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        if u == n:                       # n da chot -> dung som duoc
            break
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                tr[v] = u
                heapq.heappush(pq, (nd, v))
    with open('HANHTRINH.OUT', 'w') as f:
        if dist[n] == INF:
            f.write('-1\n')
            return
        duong = []
        v = n
        while v:                         # n -> tr[n] -> ... -> 1 -> 0 (dung)
            duong.append(v)
            v = tr[v]
        duong.reverse()
        f.write(f'{dist[n]}\n{len(duong)}\n' + ' '.join(map(str, duong)) + '\n')

main()
