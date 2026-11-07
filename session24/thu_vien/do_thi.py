# THU VIEN CODE MAU - DO THI (buoi 9-16). Moi ham ngan, khong de quy, dung lai duoc trong phong thi.
# Quy uoc: dinh danh so 1..n, adj[u] = list dinh ke (khong trong so) hoac list (v, w) (co trong so).
# Kiem thu: python kiem_thu_thu_vien.py  (so voi vet can tren hang tram do thi ngau nhien nho).
from collections import deque
import heapq

def doc_do_thi(data, pos, n, m, co_huong=False, trong_so=False):
    """Doc m canh tu mang 'data' (bytes da split) bat dau o pos. Tra ve (adj, pos moi)."""
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = int(data[pos]), int(data[pos + 1]); pos += 2
        if trong_so:
            w = int(data[pos]); pos += 1
            adj[u].append((v, w))
            if not co_huong:
                adj[v].append((u, w))
        else:
            adj[u].append(v)
            if not co_huong:
                adj[v].append(u)
    return adj, pos

def bfs(adj, s, n):
    """Khoang cach (so canh) tu s; -1 neu khong toi. Kem mang cha de truy vet (buoi 9)."""
    dist = [-1] * (n + 1); cha = [0] * (n + 1)
    dist[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1; cha[v] = u
                q.append(v)
    return dist, cha

def truy_vet(cha, s, t):
    """Duong di s -> t tu mang cha (goi sau khi chac chan t den duoc)."""
    duong = [t]
    while duong[-1] != s:
        duong.append(cha[duong[-1]])
    return duong[::-1]

def thanh_phan(adj, n):
    """Gan nhan thanh phan lien thong (DFS bang ngan xep, buoi 10). Tra ve (so thanh phan, nhan[1..n])."""
    nhan = [0] * (n + 1); c = 0
    for s in range(1, n + 1):
        if nhan[s]:
            continue
        c += 1; nhan[s] = c; st = [s]
        while st:
            u = st.pop()
            for v in adj[u]:
                if not nhan[v]:
                    nhan[v] = c; st.append(v)
    return c, nhan

def hai_phia(adj, n):
    """To 2 mau (0/1) neu do thi hai phia, nguoc lai tra ve None (buoi 10)."""
    mau = [-1] * (n + 1)
    for s in range(1, n + 1):
        if mau[s] != -1:
            continue
        mau[s] = 0; st = [s]
        while st:
            u = st.pop()
            for v in adj[u]:
                if mau[v] == -1:
                    mau[v] = mau[u] ^ 1; st.append(v)
                elif mau[v] == mau[u]:
                    return None
    return mau

def bfs_luoi(g, m, n, nguon, cam=ord('#')):
    """BFS tren luoi m x n (list cac bytes), nhieu nguon [(i, j), ...]. Luoi co VIEN, o ma hoa p = (i+1)*W + (j+1)
    (buoi 11). Tra ve (dist, W): dist[p] = so buoc, -1 neu khong toi, -2 la o cam/vien."""
    W = n + 2
    dist = [-2] * (W * (m + 2))
    for i in range(m):
        row = g[i]; base = (i + 1) * W + 1
        for j in range(n):
            if row[j] != cam:
                dist[base + j] = -1
    tang = []
    for i, j in nguon:
        p = (i + 1) * W + j + 1
        dist[p] = 0; tang.append(p)
    k = 0
    while tang:
        k += 1; moi = []
        for p in tang:
            for q in (p - 1, p + 1, p - W, p + W):
                if dist[q] == -1:
                    dist[q] = k; moi.append(q)
        tang = moi
    return dist, W

def topo_kahn(adj, n):
    """Thu tu to-po (Kahn, buoi 12). Tra ve list n dinh, hoac None neu co chu trinh."""
    vao = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in adj[u]:
            vao[v] += 1
    q = deque(u for u in range(1, n + 1) if vao[u] == 0)
    order = []
    while q:
        u = q.popleft(); order.append(u)
        for v in adj[u]:
            vao[v] -= 1
            if vao[v] == 0:
                q.append(v)
    return order if len(order) == n else None

def dijkstra(adj, s, n):
    """adj[u] = list (v, w), w >= 0 (buoi 13). Tra ve (dist, cha); dist = INF neu khong toi."""
    INF = float('inf')
    dist = [INF] * (n + 1); cha = [0] * (n + 1)
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue                       # cap loi thoi
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd; cha[v] = u
                heapq.heappush(pq, (nd, v))
    return dist, cha

def bfs01(adj, s, n):
    """Trong so chi 0 hoac 1 (buoi 14): deque, canh 0 day vao dau, canh 1 day vao cuoi."""
    INF = float('inf')
    dist = [INF] * (n + 1); dist[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if w == 0:
                    q.appendleft(v)
                else:
                    q.append(v)
    return dist

def floyd(n, canh):
    """Khoang cach moi cap, n <= 200 (buoi 14). canh = list (u, v, w) vo huong. Chi so 1..n."""
    INF = float('inf')
    d = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        d[i][i] = 0
    for u, v, w in canh:
        if w < d[u][v]:
            d[u][v] = d[v][u] = w
    for k in range(1, n + 1):
        dk = d[k]
        for i in range(1, n + 1):
            di = d[i]; dik = di[k]
            if dik == INF:
                continue
            for j, x in enumerate(dk):     # lay hang + enumerate: nhanh hon d[i][k] + d[k][j] (buoi 14)
                if dik + x < di[j]:
                    di[j] = dik + x
    return d

def bellman_ford(n, canh_co_huong, s):
    """Cho phep trong so am (buoi 14). Tra ve (dist, co_chu_trinh_am_toi_duoc)."""
    INF = float('inf')
    dist = [INF] * (n + 1); dist[s] = 0
    for _ in range(n - 1):
        doi = False
        for u, v, w in canh_co_huong:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w; doi = True
        if not doi:
            break
    am = any(dist[u] != INF and dist[u] + w < dist[v] for u, v, w in canh_co_huong)
    return dist, am

def make_dsu(n):
    """DSU nen duong + hop theo kich thuoc, find KHONG de quy (buoi 15). Tra ve (find, union, size)."""
    par = list(range(n + 1)); size = [1] * (n + 1)

    def find(x):
        root = x
        while par[root] != root:
            root = par[root]
        while par[x] != root:
            par[x], x = root, par[x]
        return root

    def union(a, b):
        a, b = find(a), find(b)
        if a == b:
            return False
        if size[a] < size[b]:
            a, b = b, a
        par[b] = a; size[a] += size[b]
        return True

    return find, union, size

def kruskal(n, canh):
    """Cay khung nho nhat (buoi 16). canh = list (w, u, v). Tra ve tong trong so, hoac None neu khong lien thong."""
    find, union, _ = make_dsu(n)
    tong = 0; so = 0
    for w, u, v in sorted(canh):
        if union(u, v):
            tong += w; so += 1
            if so == n - 1:
                break
    return tong if so == n - 1 else None

def thu_tu_cay(adj, goc, n):
    """Duyet cay khong de quy (buoi 19). Duyet reversed(order) de xu ly con truoc cha."""
    cha = [0] * (n + 1); cha[goc] = -1
    order = []; st = [goc]
    while st:
        u = st.pop(); order.append(u)
        for v in adj[u]:
            if v != cha[u]:
                cha[v] = u; st.append(v)
    return order, cha
