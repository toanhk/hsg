# GIAMGIA: n san bay, m chuyen bay MOT CHIEU u -> v gia w. Co k ve giam gia: moi ve dung cho mot chuyen,
# chuyen do chi tra w // 2. Moi chuyen dung toi da 1 ve. Tim tien it nhat di tu 1 den n (-1 neu khong toi).
# n <= 10^4, m <= 3*10^4, k <= 5, w <= 10^9.
# Do thi trang thai: (v, j) = dang o v, DA DUNG j ve (0 <= j <= k)  ->  (k+1)*n trang thai.
#   (u, j) -> (v, j)       ton w
#   (u, j) -> (v, j + 1)   ton w // 2     (neu j < k)
# Dijkstra tren do thi trang thai: O((k+1) * m * log). Dap an = min d[j][n] voi j = 0..k.
# Luu d thanh k+1 hang d[j][v] (khong gop chi so v*(k+1)+j de khoi divmod - do: nhanh hon ~15%).
from heapq import heappush, heappop

def main():
    data = open('GIAMGIA.INP', 'rb').read().split()
    n, m, k = int(data[0]), int(data[1]), int(data[2])
    adj = [[] for _ in range(n + 1)]
    for i in range(3, 3 + 3 * m, 3):
        adj[int(data[i])].append((int(data[i + 1]), int(data[i + 2])))
    INF = float('inf')
    d = [[INF] * (n + 1) for _ in range(k + 1)]
    d[0][1] = 0
    h = [(0, 0, 1)]                        # (khoang cach, so ve da dung, dinh)
    while h:
        du, j, u = heappop(h)
        dj = d[j]
        if du > dj[u]:
            continue                       # ban ghi loi thoi
        for v, w in adj[u]:                # tra du tien: o lai tang j
            nd = du + w
            if nd < dj[v]:
                dj[v] = nd; heappush(h, (nd, j, v))
        if j < k:                          # dung them 1 ve: sang tang j + 1
            dj1 = d[j + 1]; j1 = j + 1
            for v, w in adj[u]:
                nd = du + (w >> 1)
                if nd < dj1[v]:
                    dj1[v] = nd; heappush(h, (nd, j1, v))
    kq = min(d[j][n] for j in range(k + 1))
    with open('GIAMGIA.OUT', 'w') as f:
        f.write(str(kq if kq < INF else -1) + '\n')

main()
