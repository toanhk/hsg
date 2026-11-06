# DEMNGAN: do thi VO HUONG n dinh, m canh (khong co canh lap, khong co khuyen). In so canh it nhat
# tu 1 den n va SO DUONG DI co dung so canh do, lay du cho 10^9 + 7. Khong co duong: in "-1 0".
# n <= 10^5, m <= 2*10^5.
# QHD tren cac tang BFS (cau noi sang QHD tren DAG):
#   Trang thai : cnt[v] = so duong ngan nhat tu 1 den v (mod p)
#   Truy hoi   : cnt[v] = tong cnt[u] voi moi u ke v ma dist[u] = dist[v] - 1
#   Khoi tao   : cnt[1] = 1
#   Thu tu     : thu tu lay ra khoi hang doi BFS (dist tang dan) - khi u duoc lay ra, moi dinh
#                tang truoc da cong xong vao cnt[u] nen cnt[u] da chot
#   Dap an     : dist[n], cnt[n]
# Canh noi hai dinh CUNG tang hoac di nguoc tang KHONG duoc cong (xem DEMNGAN_sai.py).
from collections import deque

MOD = 10**9 + 7

def main():
    a = list(map(int, open('DEMNGAN.INP', 'rb').read().split()))
    n, m = a[0], a[1]
    ke = [[] for _ in range(n + 1)]
    it = iter(a[2:2 + 2 * m])
    for u, v in zip(it, it):
        ke[u].append(v); ke[v].append(u)
    dist = [-1] * (n + 1)
    cnt = [0] * (n + 1)
    dist[1] = 0; cnt[1] = 1
    q = deque([1])
    while q:
        u = q.popleft()
        du = dist[u] + 1
        cu = cnt[u]
        for v in ke[u]:
            if dist[v] < 0:                    # lan dau gap v: v o tang du
                dist[v] = du
                cnt[v] = cu
                q.append(v)
            elif dist[v] == du:                # gap lai v tu mot dinh khac cua tang truoc
                cnt[v] = (cnt[v] + cu) % MOD
    with open('DEMNGAN.OUT', 'w') as f:
        f.write(f'{dist[n]} {cnt[n]}\n')

main()
