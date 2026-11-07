# DO TOC DO CAY KHUNG: n = 10^5 dinh, m = 2*10^5 canh co trong so (w <= 10^9),
# va do thi DAY (n diem tren mat phang, moi cap mot canh) de chuan bi de kiem tra giai doan 4.
# Chay: python do_khung.py   (~15 giay). Chay tren may phong thi de biet moc that su.
import random, time, heapq

def do(ten, ham, lan=3):
    tot = float('inf')
    for _ in range(lan):
        t = time.perf_counter(); kq = ham(); tot = min(tot, time.perf_counter() - t)
    print(f'{ten:64s} {tot:.3f} s   (kq = {kq})')

random.seed(1)
N, M = 10**5, 2 * 10**5
canh = [(i, random.randint(1, i - 1), random.randint(1, 10**9)) for i in range(2, N + 1)]   # cay ngau nhien
while len(canh) < M:
    u, v = random.sample(range(1, N + 1), 2)
    canh.append((u, v, random.randint(1, 10**9)))
random.shuffle(canh)
s = (f'{N} {M}\n' + ''.join(f'{u} {v} {w}\n' for u, v, w in canh)).encode()

def doc():
    data = s.split()
    n, m = int(data[0]), int(data[1])
    U = list(map(int, data[2:2 + 3 * m:3]))
    V = list(map(int, data[3:3 + 3 * m:3]))
    W = list(map(int, data[4:4 + 3 * m:3]))
    return n, m, U, V, W

n0, m0, U0, V0, W0 = doc()

# 1) Sap xep canh: 3 cach
def s1():
    e = sorted(zip(W0, U0, V0))                       # tuple (w, u, v)
    return e[0][0]

def s2():
    e = sorted(range(m0), key=W0.__getitem__)         # sap chi so theo w
    return W0[e[0]]

def s3():
    e = sorted([w << 18 | i for i, w in enumerate(W0)])   # gop (w, i) vao MOT so nguyen
    return e[0] >> 18

# 2) Kruskal day du: sap + DSU (find vong lap, nen duong) - hop theo kich thuoc
def kruskal(e_sorted_idx):
    parent = list(range(n0 + 1))
    size = [1] * (n0 + 1)
    tong = 0; dem = 0
    for i in e_sorted_idx:
        a = U0[i]
        while parent[a] != a:
            parent[a] = parent[parent[a]]             # nen nua duong (path halving): 1 vong lap
            a = parent[a]
        b = V0[i]
        while parent[b] != b:
            parent[b] = parent[parent[b]]
            b = parent[b]
        if a != b:
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a; size[a] += size[b]
            tong += W0[i]; dem += 1
            if dem == n0 - 1:
                break
    return tong

def k1():
    return kruskal(sorted(range(m0), key=W0.__getitem__))

def k2():
    return kruskal([x & 262143 for x in sorted([w << 18 | i for i, w in enumerate(W0)])])

# 3) Kruskal voi find dang ham (goi ham ton thoi gian)
def k3():
    parent = list(range(n0 + 1))
    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root
    tong = 0
    for i in sorted(range(m0), key=W0.__getitem__):
        a = find(U0[i]); b = find(V0[i])
        if a != b:
            parent[a] = b; tong += W0[i]
    return tong

# 4) Prim voi heapq tren danh sach ke
def p1():
    adj = [[] for _ in range(n0 + 1)]
    for u, v, w in zip(U0, V0, W0):
        adj[u].append((w, v)); adj[v].append((w, u))
    vao = [False] * (n0 + 1)
    pq = [(0, 1)]; tong = 0; dem = 0
    while pq:
        w, u = heapq.heappop(pq)
        if vao[u]:
            continue
        vao[u] = True; tong += w; dem += 1
        for wv in adj[u]:
            if not vao[wv[1]]:
                heapq.heappush(pq, wv)
    return tong

# 5) Do thi day: n diem, khoang cach Manhattan
P = 1000
X = [random.randint(0, 10**6) for _ in range(P)]
Y = [random.randint(0, 10**6) for _ in range(P)]

def d1():                                             # Kruskal: sinh n(n-1)/2 canh roi sap
    e = []
    for i in range(P):
        xi = X[i]; yi = Y[i]
        for j in range(i + 1, P):
            e.append((abs(xi - X[j]) + abs(yi - Y[j])) << 20 | i << 10 | j)
    e.sort()
    return len(e)

def d2():                                             # Prim O(n^2) bang vong lap thuong
    INF = 1 << 60
    dist = [INF] * P; vao = [False] * P
    dist[0] = 0; tong = 0
    for _ in range(P):
        u = -1; best = INF
        for v in range(P):
            if not vao[v] and dist[v] < best:
                best = dist[v]; u = v
        vao[u] = True; tong += best
        xu = X[u]; yu = Y[u]
        for v in range(P):
            if not vao[v]:
                d = abs(xu - X[v]) + abs(yu - Y[v])
                if d < dist[v]:
                    dist[v] = d
    return tong

def d3():                                             # Prim O(n^2): chi giu danh sach dinh CHUA vao cay
    con = list(range(1, P))                           # cac dinh chua vao cay
    dist = [abs(X[0] - X[v]) + abs(Y[0] - Y[v]) for v in con]
    tong = 0
    while con:
        k = min(range(len(dist)), key=dist.__getitem__)
        tong += dist[k]
        u = con[k]
        con[k] = con[-1]; con.pop(); dist[k] = dist[-1]; dist.pop()   # xoa O(1): doi cho phan tu cuoi
        xu = X[u]; yu = Y[u]
        dist = [min(d, abs(xu - X[v]) + abs(yu - Y[v])) for d, v in zip(dist, con)]
    return tong

def main():
    do('Doc 2*10^5 canh (cat lat data[2::3])', lambda: doc()[1])
    do('Sap 2*10^5 tuple (w, u, v)', s1)
    do('Sap chi so key=W.__getitem__', s2)
    do('Sap so nguyen gop w << 18 | i', s3)
    do('Kruskal: sap chi so + DSU nen nua duong viet thang', k1)
    do('Kruskal: sap so nguyen gop + DSU viet thang', k2)
    do('Kruskal: find la HAM (goi ham moi canh)', k3)
    do('Prim heapq tren danh sach ke', p1)
    do(f'Do thi day n={P}: Kruskal sinh + sap {P*(P-1)//2} canh', d1, 1)
    do(f'Do thi day n={P}: Prim O(n^2) vong lap thuong', d2, 1)
    do(f'Do thi day n={P}: Prim O(n^2) list comprehension + xoa O(1)', d3, 1)

main()
