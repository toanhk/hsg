# HANHTRINH - ban SAI: dat INF = 10**9 "cho quen tay" nhu khi lam BFS. Trong so toi 10^9 va duong di toi
# 10^5 canh nen khoang cach that co the vuot 10^9: dinh do bi coi la "chua toi duoc" -> in -1 sai,
# hoac khong bao gio duoc noi long. Bai hoc: INF phai lon hon (so canh toi da) x (trong so toi da).
import heapq

def main():
    data = list(map(int, open('HANHTRINH.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    it = iter(data[2:2 + 3 * m])
    for u, v, w in zip(it, it, it):
        adj[u].append((v, w))
        adj[v].append((u, w))
    INF = 10**9                          # SAI: qua nho
    dist = [INF] * (n + 1)
    tr = [0] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                tr[v] = u
                heapq.heappush(pq, (nd, v))
    with open('HANHTRINH.OUT', 'w') as f:
        if dist[n] >= INF:
            f.write('-1\n')
            return
        duong = []
        v = n
        while v:
            duong.append(v)
            v = tr[v]
        duong.reverse()
        f.write(f'{dist[n]}\n{len(duong)}\n' + ' '.join(map(str, duong)) + '\n')

main()
