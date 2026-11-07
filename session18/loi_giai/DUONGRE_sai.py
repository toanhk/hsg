# DUONGRE - ban SAI: quen bo qua cap loi thoi (thieu dong "if d > dist[u]: continue").
# Mot dinh u co the nam trong heap nhieu lan. Lan lay ra thu hai, vong for chay lai va voi moi v ma
# dist[u] + w == dist[v] lai cong cnt[u] vao cnt[v] lan nua -> dem TRUNG. Khoang cach van dung (chi them
# viec thua), nen loi nay rat kho thay khi chi thu vi du nho. Ngoai ra con co the cham toi O(n*m).
import heapq

P = 10**9 + 7

def main():
    data = list(map(int, open('DUONGRE.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    it = iter(data[2:2 + 3 * m])
    for u, v, w in zip(it, it, it):
        adj[u].append((v, w))
    INF = float('inf')
    dist = [INF] * (n + 1)
    cnt = [0] * (n + 1)
    dist[1] = 0; cnt[1] = 1
    pq = [(0, 1)]
    while pq:
        d, u = heapq.heappop(pq)
        for v, w in adj[u]:             # SAI: khong kiem tra d > dist[u]
            nd = dist[u] + w
            if nd < dist[v]:
                dist[v] = nd; cnt[v] = cnt[u] % P
                heapq.heappush(pq, (nd, v))
            elif nd == dist[v]:
                cnt[v] = (cnt[v] + cnt[u]) % P
    with open('DUONGRE.OUT', 'w') as fo:
        fo.write('-1 0\n' if dist[n] == INF else f'{dist[n]} {cnt[n] % P}\n')

main()
