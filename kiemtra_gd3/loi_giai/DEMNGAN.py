# DEMNGAN: do thi CO HUONG n dinh, m cung (moi cung di mat 1 phut). In do dai duong ngan nhat tu 1 den n
# va SO duong ngan nhat mod 10^9+7; khong toi duoc thi in -1.  n <= 10^5, m <= 2*10^5
# BFS tu 1 cho d[]. Cung u -> v nam tren MOT duong ngan nhat <=> d[v] == d[u] + 1. Cac cung do tao
# thanh mot DAG, va thu tu BFS lay dinh ra chinh la mot thu tu to-po cua DAG nay.
#   Trang thai : cnt[v] = so duong ngan nhat tu 1 den v
#   Truy hoi   : cnt[v] = tong cnt[u] voi u -> v va d[u] + 1 == d[v]
#   Khoi tao   : cnt[1] = 1
#   Thu tu     : thu tu BFS (dinh ra hang doi truoc da xong truoc) -> tinh ngay trong luc BFS
#   Dap an     : d[n] va cnt[n]
MOD = 10**9 + 7

def main():
    data = open('DEMNGAN.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    adj = [[] for _ in range(n + 1)]
    for i in range(2, 2 + 2 * m, 2):
        adj[int(data[i])].append(int(data[i + 1]))
    d = [-1] * (n + 1)
    cnt = [0] * (n + 1)
    d[1] = 0; cnt[1] = 1
    q = [1]
    for u in q:                              # BFS: lay ra theo thu tu tang dan cua d
        du = d[u] + 1; cu = cnt[u]
        for v in adj[u]:
            if d[v] < 0:                     # lan dau gap: d[v] = d[u] + 1
                d[v] = du; cnt[v] = cu; q.append(v)
            elif d[v] == du:                 # them mot nhom duong ngan nhat
                cnt[v] = (cnt[v] + cu) % MOD
    with open('DEMNGAN.OUT', 'w') as f:
        f.write(f'{d[n]} {cnt[n]}\n' if d[n] >= 0 else '-1\n')

main()
