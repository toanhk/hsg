# DO TOC DO DUYET CAY: cay n = 2*10^5 dinh (cay ngau nhien va cay "duong thang" sau 2*10^5).
# Muc dich: chon cach duyet cay KHONG de quy nhanh nhat va dat gioi han cho cac bai buoi 19.
# Chay: python do_cay.py   (~20 giay). Chay tren may phong thi de biet moc that su.
import random, sys, time
from collections import deque

def do(ten, ham, lan=3):
    tot = float('inf')
    for _ in range(lan):
        t = time.perf_counter(); kq = ham(); tot = min(tot, time.perf_counter() - t)
    print(f'{ten:64s} {tot:.3f} s   (kq = {kq})')

random.seed(1)
N = 2 * 10**5
hv = list(range(1, N + 1)); random.shuffle(hv)
canh_nn = [(hv[i], hv[random.randrange(i)]) for i in range(1, N)]          # cay ngau nhien (nong, ~ log n)
canh_dt = [(hv[i], hv[i - 1]) for i in range(1, N)]                           # duong thang (sau N)
def chuoi(canh):
    return (f'{N}\n' + ''.join(f'{u} {v}\n' for u, v in canh)).encode()
S_NN, S_DT = chuoi(canh_nn), chuoi(canh_dt)

def doc_ke(s):
    data = s.split()
    n = int(data[0])
    adj = [[] for _ in range(n + 1)]
    it = map(int, data[1:])
    for u, v in zip(it, it):
        adj[u].append(v); adj[v].append(u)
    return n, adj

n0, ADJ_NN = doc_ke(S_NN)
_, ADJ_DT = doc_ke(S_DT)

# 1) Lay thu tu BFS tu goc 1 + mang cha. 3 cach.
def bfs_list(adj):                       # list lam hang doi: "for u in order" tu dai ra khi append
    par = [0] * (n0 + 1); par[1] = -1
    order = [1]
    for u in order:
        for v in adj[u]:
            if v != par[u]:
                par[v] = u; order.append(v)
    return order, par

def bfs_deque(adj):
    par = [0] * (n0 + 1); par[1] = -1
    order = []; q = deque([1])
    while q:
        u = q.popleft(); order.append(u)
        for v in adj[u]:
            if v != par[u]:
                par[v] = u; q.append(v)
    return order, par

def dfs_stack(adj):                      # ngan xep: thu tu "cha truoc con" (tien thu tu), cung duyet nguoc duoc
    par = [0] * (n0 + 1); par[1] = -1
    order = []; st = [1]
    while st:
        u = st.pop(); order.append(u)
        pu = par[u]
        for v in adj[u]:
            if v != pu:
                par[v] = u; st.append(v)
    return order, par

# 2) Duyet NGUOC thu tu de tinh kich thuoc cay con
def kich_thuoc(order, par):
    sz = [1] * (n0 + 1)
    for u in reversed(order):            # con luon dung SAU cha trong order -> duyet nguoc thi con xong truoc
        p = par[u]
        if p > 0:
            sz[p] += sz[u]
    return sz

def ca_bai(s):                           # doc + BFS + kich thuoc: mot bai CAYCON hoan chinh
    n, adj = doc_ke(s)
    order, par = bfs_list(adj)
    return kich_thuoc(order, par)[1]

# 3) De quy (de so sanh). Voi cay duong thang can do sau N: Python 3.13 Linux co the chay neu tang
#    gioi han de quy, nhung Python cu / Windows (stack 1 MB) se vo -> KHONG dung trong phong thi.
def dequy(adj):
    sys.setrecursionlimit(10**6)
    sz = [1] * (n0 + 1)
    def dfs(u, p):
        for v in adj[u]:
            if v != p:
                dfs(v, u); sz[u] += sz[v]
    dfs(1, 0)
    return sz[1]

# 4) Tap doc lap lon nhat co trong so (DUTIEC): hai mang dp0, dp1
A = [random.randint(-10**4, 10**4) for _ in range(N + 1)]
def tap_doc_lap(order, par):
    d0 = [0] * (n0 + 1); d1 = A[:]
    for u in reversed(order):
        p = par[u]
        if p > 0:
            d0[p] += d0[u] if d0[u] > d1[u] else d1[u]
            d1[p] += d0[u]
    return max(d0[1], d1[1])

# 5) Cai tui tren cay (TIENQUYET): gop mang dp con vao cha, co chan kich thuoc. n dinh, chon k.
def tui_cay(n, k, chan=True, kieu='ngau nhien'):
    random.seed(7)
    if kieu == 'ngau nhien':
        par = [0, -1] + [random.randint(1, i - 1) for i in range(2, n + 1)]
    else:                                  # 'choi': goc 1 noi n/2 dinh, moi dinh mot la -> nhieu cay con co size vua
        par = [0, -1] + [1 if i <= n // 2 + 1 else i - n // 2 for i in range(2, n + 1)]
    val = [0] + [random.randint(-100, 100) for _ in range(n)]
    order = list(range(1, n + 1))          # cha < con nen thu tu 1..n da la "cha truoc con"
    NEG = -10**18
    dp = [None] * (n + 1)
    for u in reversed(order):
        if dp[u] is None:
            dp[u] = [0, val[u]]          # dp[u][j]: chon j dinh trong cay con u (j>=1 thi phai chon u)
        p = par[u]
        if p > 0:
            if dp[p] is None:
                dp[p] = [0, val[p]]
            a, b = dp[p], dp[u]
            la = len(a) - 1; lb = len(b) - 1
            gioi = min(la + lb, k) if chan else k
            c = [NEG] * (gioi + 1); c[0] = 0
            for i in range(1, min(la, gioi) + 1):
                ai = a[i]
                if ai == NEG:
                    continue
                for j in range(0, min(lb, gioi - i) + 1):
                    t = ai + b[j]
                    if t > c[i + j]:
                        c[i + j] = t
            dp[p] = c; dp[u] = None
    return dp[1][k] if len(dp[1]) > k else None

print('n =', N)
do('doc + danh sach ke', lambda: doc_ke(S_NN)[0])
do('BFS list-lam-hang-doi (cay ngau nhien)', lambda: len(bfs_list(ADJ_NN)[0]))
do('BFS deque (cay ngau nhien)', lambda: len(bfs_deque(ADJ_NN)[0]))
do('DFS ngan xep (cay ngau nhien)', lambda: len(dfs_stack(ADJ_NN)[0]))
do('BFS list (duong thang)', lambda: len(bfs_list(ADJ_DT)[0]))
o, p = bfs_list(ADJ_NN)
do('duyet nguoc tinh kich thuoc cay con', lambda: kich_thuoc(o, p)[1])
do('tap doc lap trong so dp0/dp1', lambda: tap_doc_lap(o, p))
do('CA BAI CAYCON: doc + BFS + duyet nguoc (cay ngau nhien)', lambda: ca_bai(S_NN))
do('CA BAI CAYCON (duong thang)', lambda: ca_bai(S_DT))
do('de quy dfs(u, p) (cay ngau nhien, nong)', lambda: dequy(ADJ_NN))
try:
    do('de quy dfs(u, p) (duong thang, sau 2*10^5)', lambda: dequy(ADJ_DT), lan=1)
except RecursionError as e:
    print('de quy duong thang: RecursionError', e)
for n, k in [(1000, 1000), (2000, 2000), (2000, 200), (5000, 100)]:
    do(f'cai tui tren cay n={n}, k={k} (co chan kich thuoc)', lambda: tui_cay(n, k), lan=1)
    do(f'cai tui tren cay n={n}, k={k} (cay choi)', lambda: tui_cay(n, k, kieu='choi'), lan=1)
do('cai tui tren cay n=1000, k=1000 KHONG chan (O(n*k^2))', lambda: tui_cay(1000, 1000, False), lan=1)
