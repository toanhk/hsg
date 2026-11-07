# BENHVIEN: do thi vo huong co trong so, n, m <= 5*10^4, co k benh vien dat o k dinh khac nhau.
# Voi moi dinh v in khoang cach toi benh vien GAN NHAT va so hieu (dinh) cua benh vien do; nhieu benh vien
# cung gan nhat thi chon so hieu nho nhat. Khong toi duoc benh vien nao: in -1.
# Dijkstra NHIEU NGUON: cho ca k benh vien vao pq ngay tu dau voi khoang cach 0 (giong BFS nhieu nguon
# o buoi 11). Nhan cua moi dinh la CAP (d, h); so sanh cap theo thu tu tu dien: d nho hon thang, bang d
# thi h nho hon thang. Cap (d + w, h) khong bao gio nho hon (d, h) nen Dijkstra van dung voi nhan cap.
# Chi 1 lan Dijkstra: O((n + m) log m). Chay k lan Dijkstra rieng se la O(k (n + m) log m) -> qua gio.
import heapq

def main():
    data = list(map(int, open('BENHVIEN.INP', 'rb').read().split()))
    n, m, k = data[0], data[1], data[2]
    bv = data[3:3 + k]
    adj = [[] for _ in range(n + 1)]
    it = iter(data[3 + k:3 + k + 3 * m])
    for u, v, w in zip(it, it, it):
        adj[u].append((v, w))
        adj[v].append((u, w))
    INF = float('inf')
    dist = [INF] * (n + 1)
    gan = [0] * (n + 1)                  # gan[v] = benh vien gan v nhat (theo cap (dist, so hieu))
    pq = []
    for h in bv:
        dist[h] = 0
        gan[h] = h
        pq.append((0, h, h))             # (khoang cach, benh vien, dinh)
    heapq.heapify(pq)
    while pq:
        d, h, u = heapq.heappop(pq)
        if d != dist[u] or h != gan[u]:  # cap loi thoi (nhan cua u da duoc lam nho hon)
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v] or (nd == dist[v] and h < gan[v]):
                dist[v] = nd
                gan[v] = h
                heapq.heappush(pq, (nd, h, v))
    out = [f'{dist[v]} {gan[v]}' if gan[v] else '-1' for v in range(1, n + 1)]
    with open('BENHVIEN.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
