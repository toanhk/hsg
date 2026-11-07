# DUONGDAI: do thi CO HUONG KHONG CHU TRINH (DAG) n dinh, m cung u -> v trong so w (|w| <= 10^9, co the AM).
# Tim tong trong so LON NHAT cua mot duong di tu 1 den n. Khong co duong: in KHONG. n, m <= 2*10^5.
# Tren do thi bat ky bai "duong dai nhat" rat kho (phai thu moi duong don); tren DAG thi la QHD:
#   Trang thai : f[v] = tong lon nhat cua duong di tu 1 den v  (AM = "chua toi duoc")
#   Truy hoi   : f[v] = max (f[u] + w) voi moi cung u -> v ma f[u] da toi duoc
#   Khoi tao   : f[1] = 0, moi dinh khac AM
#   Thu tu     : thu tu to-po (Kahn) - khi lay u ra thi moi cung VAO u da duoc xet, f[u] da chot
#   Dap an     : f[n]
# Chu y: Kahn phai bat dau tu MOI dinh co ban bac vao 0 (khong chi dinh 1), neu khong cac dinh co cung
# vao tu phan "khong toi duoc" se khong bao gio ve 0 va bi bo sot.  O(n + m)
def main():
    data = list(map(int, open('DUONGDAI.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    it = iter(data[2:2 + 3 * m])
    for u, v, w in zip(it, it, it):
        adj[u].append((v, w)); deg[v] += 1
    AM = -(1 << 62)                           # "am vo cung": nho hon moi tong that (>= -2*10^14)
    f = [AM] * (n + 1)
    f[1] = 0
    q = [u for u in range(1, n + 1) if deg[u] == 0]
    for u in q:                               # list lam hang doi: vua duyet vua append
        fu = f[u]
        for v, w in adj[u]:
            if fu != AM and fu + w > f[v]:    # chi "day" tu dinh da toi duoc
                f[v] = fu + w
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    with open('DUONGDAI.OUT', 'w') as fo:
        fo.write((str(f[n]) if f[n] != AM else 'KHONG') + '\n')

main()
