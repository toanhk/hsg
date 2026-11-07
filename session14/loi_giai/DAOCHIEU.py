# DAOCHIEU: n nga tu, m duong MOT CHIEU u -> v. Duoc phep dao chieu mot so duong. Hoi it nhat phai dao
# chieu bao nhieu duong de co the di tu nga tu 1 den nga tu n (-1 neu khong the). n, m <= 10^5
# Mo hinh: moi duong u -> v cho 2 canh:  u -> v ton 0 (di dung chieu),  v -> u ton 1 (phai dao chieu).
# Trong so chi 0 hoac 1 -> BFS 0-1 voi deque, O(n + m), khong can heap:
#   canh 0 -> dua dinh vao DAU deque (cung "tang" voi u),  canh 1 -> dua vao CUOI (tang sau).
#   Deque luon chi chua 2 tang lien tiep d va d+1 theo thu tu tang dan -> lay ra dau la dung.
from collections import deque

def main():
    data = list(map(int, open('DAOCHIEU.INP', 'rb').read().split()))   # map(int) mot lan: nhanh hon
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]       # gop (v, w) thanh mot so v*2 + w  (w = 0 hoac 1)
    it = iter(data[2:2 + 2 * m])
    for u, v in zip(it, it):               # lay tung cap (u, v)
        adj[u].append(v * 2)               # dung chieu: ton 0
        adj[v].append(u * 2 + 1)           # nguoc chieu: ton 1
    INF = m + 1
    d = [INF] * (n + 1)
    xong = bytearray(n + 1)
    d[1] = 0
    dq = deque([1])
    while dq:
        u = dq.popleft()
        if xong[u]:                        # mot dinh co the vao deque 2 lan: lan sau bo qua
            continue
        xong[u] = 1
        du = d[u]
        for x in adj[u]:
            v = x >> 1
            nd = du + (x & 1)
            if nd < d[v]:                  # NOI LONG roi moi dua vao (khong danh dau khi dua vao!)
                d[v] = nd
                if x & 1:
                    dq.append(v)
                else:
                    dq.appendleft(v)
    with open('DAOCHIEU.OUT', 'w') as f:
        f.write(str(d[n] if d[n] < INF else -1) + '\n')

main()
