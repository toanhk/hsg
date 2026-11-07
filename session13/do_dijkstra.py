# DO TOC DO DIJKSTRA: n = 10^5 dinh, m = 2*10^5 canh vo huong co trong so (toi 10^9).
# So sanh: heap chua tuple (d, u) / heap chua mot so nguyen d*N + u; ke la list tuple / hai list song song;
# co va khong co dong "if d > dist[u]: continue"; va Dijkstra O(n^2) (khong heap) voi n = 2000.
# Chay: python do_dijkstra.py   (~15 giay). Chay tren may phong thi de biet moc that su.
import random, time, heapq

def do(ten, ham, lan=3):
    tot = float('inf')
    for _ in range(lan):
        t = time.perf_counter(); kq = ham(); tot = min(tot, time.perf_counter() - t)
    print(f'{ten:62s} {tot:.3f} s   (kq = {kq})')

random.seed(1)
N, M = 10**5, 2 * 10**5
canh = [(i, random.randint(1, i - 1), random.randint(1, 10**9)) for i in range(2, N + 1)]  # cay -> lien thong
while len(canh) < M:
    u, v = random.sample(range(1, N + 1), 2)
    canh.append((u, v, random.randint(1, 10**9)))
random.shuffle(canh)
s = (f'{N} {M}\n' + ''.join(f'{u} {v} {w}\n' for u, v, w in canh)).encode()

# 1) Doc + danh sach ke (list cac tuple (v, w))
def doc_tuple():
    data = s.split()
    n, m = int(data[0]), int(data[1])
    adj = [[] for _ in range(n + 1)]
    for i in range(2, 2 + 3 * m, 3):
        u = int(data[i]); v = int(data[i + 1]); w = int(data[i + 2])
        adj[u].append((v, w)); adj[v].append((u, w))
    return n, adj

def doc_map():
    data = list(map(int, s.split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    it = iter(data[2:2 + 3 * m])
    for u, v, w in zip(it, it, it):
        adj[u].append((v, w)); adj[v].append((u, w))
    return n, adj

n0, ADJ = doc_map()
INF = float('inf')

# 2) Dijkstra chuan trong lo trinh: heap tuple, bo qua dinh loi thoi
def dij_tuple():
    dist = [INF] * (n0 + 1); dist[1] = 0
    pq = [(0, 1)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in ADJ[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist[n0]

# 3) Nhu 2 nhung dist khoi tao bang so nguyen lon thay cho float('inf')
def dij_tuple_int():
    VC = 1 << 62
    dist = [VC] * (n0 + 1); dist[1] = 0
    pq = [(0, 1)]
    pop, push = heapq.heappop, heapq.heappush
    while pq:
        d, u = pop(pq)
        if d > dist[u]:
            continue
        for v, w in ADJ[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                push(pq, (nd, v))
    return dist[n0]

# 4) Heap chua mot so nguyen: khoa = d * 2^17 + u (u < 2^17 = 131072)
def dij_goi():
    VC = 1 << 62
    dist = [VC] * (n0 + 1); dist[1] = 0
    pq = [1]                                   # 0 * 2^17 + 1
    pop, push = heapq.heappop, heapq.heappush
    while pq:
        x = pop(pq)
        d = x >> 17; u = x & 131071
        if d > dist[u]:
            continue
        for v, w in ADJ[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                push(pq, nd << 17 | v)
    return dist[n0]

# 5) Bo dong "if d > dist[u]: continue" (do thi ngau nhien - chua thay chenh lech lon)
def dij_khong_bo():
    dist = [INF] * (n0 + 1); dist[1] = 0
    pq = [(0, 1)]
    while pq:
        d, u = heapq.heappop(pq)
        for v, w in ADJ[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist[n0]

# 6) Do thi "bay": dinh H bac 10^5 bi cap nhat K = 1000 lan. Khong bo qua dinh loi thoi -> K * 10^5 phep.
K, B = 1000, 10**5
bay = [[] for _ in range(K + B + 2)]           # dinh 1, a_i = 1+i (i=1..K), H = K+2, la: K+3..
H = K + 2
for i in range(1, K + 1):
    bay[1].append((1 + i, i)); bay[1 + i].append((H, 3 * K - 2 * i))   # di qua a_i toi H: 3K - i, giam dan
for j in range(B - 1):
    bay[H].append((K + 3 + j, 1))
NB = K + B + 1

def bay_dij(bo_qua):
    def f():
        dist = [INF] * (NB + 1); dist[1] = 0
        pq = [(0, 1)]; lan = 0
        while pq:
            d, u = heapq.heappop(pq)
            if bo_qua and d > dist[u]:
                continue
            for v, w in bay[u]:
                lan += 1
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        return lan
    return f

# 7) Dijkstra O(n^2) khong heap, n = 2000 do thi day (m = 10^5 canh)
n2 = 2000
A = [[INF] * (n2 + 1) for _ in range(n2 + 1)]
for _ in range(10**5):
    u, v = random.sample(range(1, n2 + 1), 2); w = random.randint(1, 10**9)
    if w < A[u][v]:
        A[u][v] = A[v][u] = w

def dij_n2():
    dist = [INF] * (n2 + 1); dist[1] = 0
    xong = [False] * (n2 + 1)
    for _ in range(n2):
        u, best = -1, INF
        for x in range(1, n2 + 1):
            if not xong[x] and dist[x] < best:
                u, best = x, dist[x]
        if u == -1:
            break
        xong[u] = True
        hang = A[u]
        for v in range(1, n2 + 1):
            nd = best + hang[v]
            if nd < dist[v]:
                dist[v] = nd
    return dist[n2]

def main():
    do('Doc + ke tuple, int() tung so', lambda: len(doc_tuple()[1]))
    do('Doc + ke tuple, map(int) + zip', lambda: len(doc_map()[1]))
    do('Dijkstra heap tuple, INF = float(inf)', dij_tuple)
    do('Dijkstra heap tuple, INF = 1<<62, gan pop/push', dij_tuple_int)
    do('Dijkstra heap so nguyen goi d<<17|u', dij_goi)
    do('Dijkstra KHONG bo qua dinh loi thoi (ngau nhien)', dij_khong_bo)
    do('Do thi bay: CO bo qua dinh loi thoi (dem phep duyet canh)', bay_dij(True))
    do('Do thi bay: KHONG bo qua (dem phep duyet canh)', bay_dij(False), lan=1)
    do('Dijkstra O(n^2) khong heap, n = 2000', dij_n2, lan=1)

main()
