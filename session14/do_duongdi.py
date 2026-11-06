# DO TOC DO CAC BIEN THE DUONG DI (buoi 14): Floyd n = 200, BFS 0-1 so voi Dijkstra,
# Dijkstra tuple / so nguyen gop, Dijkstra nhieu tang (k ve), Bellman-Ford.
# Chay: python do_duongdi.py   (~20 giay). Chay tren may phong thi de biet moc that su.
import random, time
from heapq import heappush, heappop
from collections import deque

def do(ten, ham, lan=3):
    tot = float('inf')
    for _ in range(lan):
        t = time.perf_counter(); kq = ham(); tot = min(tot, time.perf_counter() - t)
    print(f'{ten:62s} {tot:.3f} s   (kq = {kq})')

random.seed(1)
INF = float('inf')

# ---------------- 1) FLOYD n = 200 (8*10^6 lan cap nhat) ----------------
N = 200
D0 = [[0 if i == j else random.randint(1, 10**6) for j in range(N)] for i in range(N)]

def floyd_3vong():                 # viet thang 3 vong lap - cach "sach giao khoa"
    d = [r[:] for r in D0]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    return sum(map(sum, d))

def floyd_hang():                  # lay san hang d[i], d[k] va d[i][k] ra bien cuc bo
    d = [r[:] for r in D0]
    for k in range(N):
        dk = d[k]
        for i in range(N):
            di = d[i]; dik = di[k]
            for j in range(N):
                if dik + dk[j] < di[j]:
                    di[j] = dik + dk[j]
    return sum(map(sum, d))

def floyd_enum():                  # lay hang ra + enumerate(dk): NHANH NHAT (dung trong KHOANGCACH.py)
    d = [r[:] for r in D0]
    for k in range(N):
        dk = d[k]
        for di in d:
            dik = di[k]
            for j, x in enumerate(dk):
                if dik + x < di[j]:
                    di[j] = dik + x
    return sum(map(sum, d))

def floyd_map():                   # vong trong cung cho C lam: map(min, hang cu, hang moi)
    d = [r[:] for r in D0]
    for k in range(N):
        dk = d[k]
        for i in range(N):
            dik = d[i][k]
            d[i] = list(map(min, d[i], [dik + x for x in dk]))
    return sum(map(sum, d))

def floyd_map_bo_qua():            # nhu tren + bo qua hang khong toi duoc k (INF) - huu ich khi do thi thua
    d = [[x if random.random() < 0.05 or i == j else INF for j, x in enumerate(r)] for i, r in enumerate(D0)]
    for k in range(N):
        dk = d[k]
        for i in range(N):
            dik = d[i][k]
            if dik == INF:
                continue
            d[i] = list(map(min, d[i], [dik + x for x in dk]))
    return sum(1 for r in d for x in r if x < INF)

do('Floyd 3 vong lap d[i][j] (n=200)', floyd_3vong, 1)
do('Floyd lay hang ra bien cuc bo', floyd_hang, 1)
do('Floyd lay hang + enumerate(dk)', floyd_enum)
do('Floyd map(min, d[i], [dik + x for x in dk])', floyd_map)
do('Floyd map + bo qua dik == INF (do thi thua 5%)', floyd_map_bo_qua)

# ---------------- 2) DIJKSTRA: tuple hay so nguyen gop ----------------
def do_thi(n, m, wmax):
    canh = [(i, random.randint(max(1, i - 50), i - 1), random.randint(1, wmax)) for i in range(2, n + 1)]
    while len(canh) < m:
        u, v = random.sample(range(1, n + 1), 2); canh.append((u, v, random.randint(1, wmax)))
    return canh

def ke_tuple(n, canh):
    adj = [[] for _ in range(n + 1)]
    for u, v, w in canh:
        adj[u].append((v, w)); adj[v].append((u, w))
    return adj

def dij_tuple(n, adj, s):
    d = [INF] * (n + 1); d[s] = 0; h = [(0, s)]
    while h:
        du, u = heappop(h)
        if du > d[u]:
            continue
        for v, w in adj[u]:
            nd = du + w
            if nd < d[v]:
                d[v] = nd; heappush(h, (nd, v))
    return d

def dij_gop(n, adj, s):            # phan tu heap la mot so: nd * B + v  (B > n)
    B = 1 << 17; M = B - 1
    d = [INF] * (n + 1); d[s] = 0; h = [s]
    while h:
        x = heappop(h); du = x >> 17; u = x & M
        if du > d[u]:
            continue
        for v, w in adj[u]:
            nd = du + w
            if nd < d[v]:
                d[v] = nd; heappush(h, (nd << 17) | v)
    return d

for n, m in ((5 * 10**4, 10**5), (10**5, 2 * 10**5)):
    C = do_thi(n, m, 10**9); A = ke_tuple(n, C)
    do(f'Dijkstra heap tuple n={n} m={m}', lambda: dij_tuple(n, A, 1)[n])
    do(f'Dijkstra heap so gop n={n} m={m}', lambda: dij_gop(n, A, 1)[n])
    do(f'  2 lan Dijkstra tuple (MIENPHI: tu 1 va tu n)', lambda: dij_tuple(n, A, 1)[n] + dij_tuple(n, A, n)[1])

# ---------------- 3) BFS 0-1 so voi Dijkstra (trong so 0/1) ----------------
n = m = 2 * 10**5
cung = [(random.randint(1, n), random.randint(1, n)) for _ in range(m)]
A01 = [[] for _ in range(n + 1)]
for u, v in cung:
    A01[u].append(v * 2); A01[v].append(u * 2 + 1)

def bfs01():
    d = [n + 1] * (n + 1); d[1] = 0; dq = deque([1])
    while dq:
        u = dq.popleft(); du = d[u]
        for x in A01[u]:
            v = x >> 1; nd = du + (x & 1)
            if nd < d[v]:
                d[v] = nd
                if x & 1: dq.append(v)
                else: dq.appendleft(v)
    return d[n]

def dij01():
    d = [n + 1] * (n + 1); d[1] = 0; h = [(0, 1)]
    while h:
        du, u = heappop(h)
        if du > d[u]:
            continue
        for x in A01[u]:
            v = x >> 1; nd = du + (x & 1)
            if nd < d[v]:
                d[v] = nd; heappush(h, (nd, v))
    return d[n]

do('BFS 0-1 deque n=m=2*10^5 (DAOCHIEU)', bfs01)
do('Dijkstra heap cung do thi do', dij01)

# ---------------- 4) Dijkstra nhieu tang: (dinh, so ve da dung) ----------------
def tang(n, m, k):
    C = do_thi(n, m, 10**6)
    adj = [[] for _ in range(n + 1)]
    for u, v, w in C:
        adj[u].append((v, w)); adj[v].append((u, w))
    def chay():
        S = k + 1
        d = [INF] * ((n + 1) * S); d[1 * S] = 0; h = [(0, 1 * S)]
        while h:
            du, x = heappop(h)
            if du > d[x]:
                continue
            u, j = divmod(x, S)
            for v, w in adj[u]:
                y = v * S + j; nd = du + w
                if nd < d[y]:
                    d[y] = nd; heappush(h, (nd, y))
                if j < k:
                    nd = du + w // 2
                    if nd < d[y + 1]:
                        d[y + 1] = nd; heappush(h, (nd, y + 1))
        return min(d[n * S: n * S + S])
    return chay

do('Dijkstra 2 tang (1 ve) n=5*10^4 m=10^5', tang(5 * 10**4, 10**5, 1))
do('Dijkstra 11 tang (k=10) n=10^4 m=2*10^4', tang(10**4, 2 * 10**4, 10))
do('Dijkstra 6 tang (k=5) n=2*10^4 m=4*10^4', tang(2 * 10**4, 4 * 10**4, 5))

# ---------------- 5) Bellman-Ford: truong hop xau (xich dai, canh xep nguoc) ----------------
def bellman(n, m):
    canh = [(i, i + 1, random.randint(-10, 10**4)) for i in range(1, n)]
    canh.reverse()                         # xep nguoc -> moi vong chi day them 1 dinh
    while len(canh) < m:
        u, v = random.sample(range(1, n + 1), 2)
        canh.append((u, v, 10**9))         # canh rat dat: khong bao gio la loi tat
    def chay():
        d = [INF] * (n + 1); d[1] = 0; vong = 0
        for _ in range(n - 1):
            vong += 1; doi = False
            for u, v, w in canh:
                if d[u] + w < d[v]:
                    d[v] = d[u] + w; doi = True
            if not doi:
                break
        return vong
    return chay

do('Bellman-Ford xau nhat n=500 m=2000 (so vong)', bellman(500, 2000), 1)
do('Bellman-Ford xau nhat n=1000 m=5000 (so vong)', bellman(1000, 5000), 1)
