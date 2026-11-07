# MIENPHI - Cach 2: do thi TRANG THAI. Trang thai (v, j): dang o v, j = 1 neu da dung ve, 0 neu chua.
#   (u, j) -> (v, j)      ton w        (tra tien)
#   (u, 0) -> (v, 1)      ton 0        (dung ve cho tuyen nay)
# Dijkstra tren 2n trang thai; dap an = min(d[n][0], d[n][1]). Chay dung nhung cham hon Cach 1
# khoang 1,5 lan; uu diem: mo rong ngay cho k ve (bai GIAMGIA) - Cach 1 thi khong.
from heapq import heappush, heappop

def main():
    data = open('MIENPHI.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    adj = [[] for _ in range(n + 1)]
    for i in range(2, 2 + 3 * m, 3):
        u = int(data[i]); v = int(data[i + 1]); w = int(data[i + 2])
        adj[u].append((v, w)); adj[v].append((u, w))
    INF = float('inf')
    d0 = [INF] * (n + 1)                   # tang 0: chua dung ve
    d1 = [INF] * (n + 1)                   # tang 1: da dung ve
    d0[1] = 0
    h = [(0, 0, 1)]                        # (khoang cach, tang, dinh)
    while h:
        du, j, u = heappop(h)
        if j == 0:
            if du > d0[u]:
                continue
            for v, w in adj[u]:
                if du + w < d0[v]:
                    d0[v] = du + w; heappush(h, (du + w, 0, v))
                if du < d1[v]:             # dung ve: sang tang 1, khong mat tien
                    d1[v] = du; heappush(h, (du, 1, v))
        else:
            if du > d1[u]:
                continue
            for v, w in adj[u]:
                if du + w < d1[v]:
                    d1[v] = du + w; heappush(h, (du + w, 1, v))
    kq = min(d0[n], d1[n])
    with open('MIENPHI.OUT', 'w') as f:
        f.write(str(kq if kq < INF else -1) + '\n')

main()
