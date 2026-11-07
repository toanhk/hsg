# DO TOC DO QHD TREN DAG & TREN DO THI (buoi 18)
#   DAG n = 10^5 dinh, m = 2*10^5 cung (co mot duong qua moi dinh), trong so am/duong
#   Dijkstra + dem tren do thi co huong n = 3*10^4 .. 10^5, m = 10^5 .. 2*10^5
#   Luoi do cao 500 x 500 va 1000 x 1000 (bai TRUOTTUYET)
# Chay: python do_dag.py   (~20 giay). Chay tren may phong thi de biet moc that su.
import random, time, heapq, subprocess, sys

def do(ten, ham, lan=3):
    tot = float('inf')
    for _ in range(lan):
        t = time.perf_counter(); kq = ham(); tot = min(tot, time.perf_counter() - t)
    print(f'{ten:64s} {tot:.3f} s   (kq = {str(kq)[:20]})')

def moc():
    s = 0
    for i in range(10**7):
        s += i
    return s

random.seed(18)
P = 10**9 + 7
N, M = 10**5, 2 * 10**5
hv = [1] + random.sample(range(2, N), N - 2) + [N]
canh = [(hv[i], hv[i + 1], random.randint(-10**9, 10**9)) for i in range(N - 1)]
while len(canh) < M:
    i, j = sorted(random.sample(range(N), 2))
    canh.append((hv[i], hv[j], random.randint(-10**9, 10**9)))
random.shuffle(canh)
s_dag = (f'{N} {M}\n' + ''.join(f'{u} {v} {w}\n' for u, v, w in canh)).encode()

def doc_dag():
    data = list(map(int, s_dag.split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]; deg = [0] * (n + 1)
    it = iter(data[2:2 + 3 * m])
    for u, v, w in zip(it, it, it):
        adj[u].append((v, w)); deg[v] += 1
    return n, adj, deg

n0, ADJ, DEG = doc_dag()
ADJ0 = [[v for v, w in a] for a in ADJ]           # ban khong trong so (dem duong)

def kahn_dai():                                   # DUONGDAI: Kahn + "day toi"
    deg = DEG[:]; AM = -(1 << 62)
    f = [AM] * (n0 + 1); f[1] = 0
    q = [u for u in range(1, n0 + 1) if deg[u] == 0]
    for u in q:
        fu = f[u]
        for v, w in ADJ[u]:
            if fu != AM and fu + w > f[v]:
                f[v] = fu + w
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    return f[n0]

def topo():
    deg = DEG[:]
    q = [u for u in range(1, n0 + 1) if deg[u] == 0]
    for u in q:
        for v in ADJ0[u]:
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    return q

TOPO = topo()

def dem_mod_moi_lan():                            # % o MOI phep cong
    c = [0] * (n0 + 1); c[1] = 1
    for u in TOPO:
        cu = c[u]
        for v in ADJ0[u]:
            c[v] = (c[v] + cu) % P
    return c[n0]

def dem_mod_mot_lan():                            # % mot lan khi dinh duoc chot
    c = [0] * (n0 + 1); c[1] = 1
    for u in TOPO:
        cu = c[u] % P; c[u] = cu
        for v in ADJ0[u]:
            c[v] += cu
    return c[n0] % P

L = 10**5                                        # "thang" i -> i+1, i -> i+2: so duong = Fibonacci

def thang(mod):
    c = [0] * (L + 2); c[1] = 1
    for u in range(1, L):
        cu = c[u] % P if mod else c[u]
        c[u + 1] += cu; c[u + 2] += cu
    return c[L] % P

DEQUY = '''
import sys
sys.setrecursionlimit(10**6)
n = %d
def f(u):
    return 1 if u == n else f(u + 1)
print(f(1))
'''

def de_quy_sau(n):
    r = subprocess.run([sys.executable, '-c', DEQUY % n], capture_output=True, text=True)
    return 'chay duoc' if r.returncode == 0 else f'VO (ma {r.returncode})'

# Dijkstra + dem: do thi co huong co duong 1 -> ... -> n, w nho (nhieu duong bang nhau)
def tao_dt(n, m, wmax):
    hv = [1] + random.sample(range(2, n), n - 2) + [n]
    c = [(hv[i], hv[i + 1], random.randint(1, wmax)) for i in range(n - 1)]
    while len(c) < m:
        u, v = random.sample(range(1, n + 1), 2)
        c.append((u, v, random.randint(1, wmax)))
    adj = [[] for _ in range(n + 1)]
    for u, v, w in c:
        adj[u].append((v, w))
    return n, adj

def dij_tuple(G):
    n, adj = G
    INF = float('inf'); dist = [INF] * (n + 1); cnt = [0] * (n + 1)
    dist[1] = 0; cnt[1] = 1; pq = [(0, 1)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        cu = cnt[u] % P
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd; cnt[v] = cu; heapq.heappush(pq, (nd, v))
            elif nd == dist[v]:
                cnt[v] += cu
    return cnt[n] % P

def dij_goi(G):                                   # heap chua MOT so nguyen d << 17 | u
    n, adj = G
    INF = 1 << 62; dist = [INF] * (n + 1); cnt = [0] * (n + 1)
    dist[1] = 0; cnt[1] = 1; pq = [1]
    while pq:
        x = heapq.heappop(pq); d = x >> 17; u = x & 131071
        if d != dist[u]:
            continue
        cu = cnt[u] % P
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd; cnt[v] = cu; heapq.heappush(pq, nd << 17 | v)
            elif nd == dist[v]:
                cnt[v] += cu
    return cnt[n] % P

G1 = tao_dt(30000, 10**5, 5)
G2 = tao_dt(10**5, 2 * 10**5, 10**9)

def truot(r, c):
    W = c + 2; h = [1 << 40] * (W * (r + 2))
    for i in range(1, r + 1):
        h[i * W + 1:i * W + 1 + c] = [random.randint(1, 10**9) for _ in range(c)]
    o = [i * W + j for i in range(1, r + 1) for j in range(1, c + 1)]

    def chay():
        oo = sorted(o, key=h.__getitem__)
        f = [1] * len(h)
        for x in oo:
            hx = h[x]; best = 1
            for y in (x - W, x + W, x - 1, x + 1):
                if h[y] < hx and f[y] >= best:
                    best = f[y] + 1
            f[x] = best
        return max(f)
    return chay

do('moc: 10^7 phep cong trong ham', moc, lan=1)
do('doc DAG 10^5 dinh / 2*10^5 cung co trong so + dung ke', doc_dag)
do('DUONGDAI: Kahn + day toi (trong so am/duong)', kahn_dai)
do('DEMLOTRINH: % o moi phep cong', dem_mod_moi_lan)
do('DEMLOTRINH: % mot lan khi chot dinh', dem_mod_mot_lan)
do('dem tren "thang" 10^5 dinh: CO lay mod', lambda: thang(True))
do('dem tren "thang" 10^5 dinh: KHONG mod (so ~7*10^4 bit)', lambda: thang(False), lan=1)
do('de quy co nho sau 10^5 tang (tien trinh rieng)', lambda: de_quy_sau(10**5), lan=1)
do('de quy co nho sau 2*10^5 tang (tien trinh rieng)', lambda: de_quy_sau(2 * 10**5), lan=1)
do('Dijkstra + dem, n=3*10^4, m=10^5, w<=5: heap tuple', lambda: dij_tuple(G1))
do('Dijkstra + dem, n=3*10^4, m=10^5, w<=5: heap so goi', lambda: dij_goi(G1))
do('Dijkstra + dem, n=10^5, m=2*10^5, w<=10^9: heap tuple', lambda: dij_tuple(G2))
do('Dijkstra + dem, n=10^5, m=2*10^5, w<=10^9: heap so goi', lambda: dij_goi(G2))
do('TRUOTTUYET 500 x 500: sap theo do cao + QHD', truot(500, 500))
do('TRUOTTUYET 1000 x 1000: sap theo do cao + QHD', truot(1000, 1000), lan=1)
