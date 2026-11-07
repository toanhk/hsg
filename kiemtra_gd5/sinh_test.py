# SINH TEST cho de kiem tra cuoi giai doan 5 (bai ket hop do thi + QHD, 150 phut): GIAMSAT, NGAMCANH, MUASAM
# Cau truc thu muc theo Themis: test/GIAMSAT/Test01/GIAMSAT.INP + GIAMSAT.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau de kiem cheo:
#   GIAMSAT QHD "gop dan tung con" voi trang thai (co camera?, da duoc giam sat?), duyet DFS ngan xep,
#   NGAMCANH Dijkstra tu 1 VA tu n, lay cac canh nam tren duong ngan nhat (d1[u] + w + dn[v] == D),
#     QHD tren DAG theo thu tu d1 tang dan (sap xep) thay vi theo thu tu lay ra khoi heap,
#   MUASAM QHD tren TAP CUA HANG da ghe (TSP tren cac cua hang) thay vi tren tap mon da mua.
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py              -> sinh ca 3 bai (~20 giay)
#       python sinh_test.py MUASAM       -> chi sinh bai ke ten
# Moi bai co seed rieng (random.seed('GIAMSAT-2026'), ...) nen sinh rieng mot bai hay ca bo deu ra CUNG test.
import os, random, sys, heapq

GOC = 'test'

def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

def tron_nhan(n, canh):
    """Doi so hieu dinh ngau nhien va tron thu tu canh (goc 1 cua cay thanh mot dinh bat ky)."""
    hv = list(range(1, n + 1)); random.shuffle(hv)
    hv = [0] + hv
    canh = [(hv[u], hv[v]) if random.random() < 0.5 else (hv[v], hv[u]) for u, v in canh]
    random.shuffle(canh)
    return canh

def cay(n, kieu='ngau_nhien'):
    if kieu == 'duong':
        return [(i, i + 1) for i in range(1, n)]
    if kieu == 'sao':
        return [(1, i) for i in range(2, n + 1)]
    if kieu == 'sau_rom':                                   # truc dai, moi dinh truc co vai la
        k = n // 3
        canh = [(i, i + 1) for i in range(1, k)]
        canh += [(random.randint(1, k), i) for i in range(k + 1, n + 1)]
        return canh
    return [(random.randint(max(1, i - 50) if kieu == 'sau' else 1, i - 1), i) for i in range(2, n + 1)]

# ---------------- GIAMSAT ----------------
def dap_an_giamsat(n, c, canh):
    adj = [[] for _ in range(n + 1)]
    for u, v in canh:
        adj[u].append(v); adj[v].append(u)
    INF = 10**18
    cha = [0] * (n + 1); cha[1] = -1
    thu_tu = []; st = [1]
    while st:                                               # DFS ngan xep: cha luon truoc con
        u = st.pop(); thu_tu.append(u)
        for v in adj[u]:
            if v != cha[u]:
                cha[v] = u; st.append(v)
    A = [0] * (n + 1); B = [0] * (n + 1); C = [0] * (n + 1)
    for v in reversed(thu_tu):
        co = c[v - 1]                                       # (camera, ...) gop dan
        k0 = 0; k1 = INF                                    # khong camera: chua / da duoc giam sat
        for w in adj[v]:
            if w == cha[v]:
                continue
            co += min(A[w], B[w], C[w])
            k1 = min(k1 + min(A[w], B[w]), k0 + A[w])
            k0 = min(INF, k0 + B[w])
        A[v], B[v], C[v] = co, min(k1, INF), k0
    return f'{min(A[1], B[1])}\n'

def sinh_giamsat():
    for so in range(1, 11):
        if so == 1:
            n = 6; c = [5, 2, 3, 1, 4, 6]; canh = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)]
        elif so == 2:
            n = 1; c = [7]; canh = []
        elif so == 3:
            n = 12; c = [random.randint(1, 20) for _ in range(n)]; canh = tron_nhan(n, cay(n))
        elif so == 4:                                       # bay tham lam: dinh trong dat, la re
            n = 15; canh = cay(n, 'sau_rom')
            bac = [0] * (n + 1)
            for u, v in canh:
                bac[u] += 1; bac[v] += 1
            c = [1 if bac[i] == 1 else 100 for i in range(1, n + 1)]
        elif so <= 7:                                       # subtask 2: moi c[i] = 1
            n = 10**5; c = [1] * n
            canh = tron_nhan(n, cay(n, {5: 'ngau_nhien', 6: 'duong', 7: 'sau_rom'}[so]))
        elif so == 8:
            n = 10**5; c = [random.randint(1, 10**9) for _ in range(n)]; canh = tron_nhan(n, cay(n))
        elif so == 9:                                       # duong dai: kiem tra khong de quy
            n = 10**5; c = [random.randint(1, 10**9) for _ in range(n)]; canh = tron_nhan(n, cay(n, 'duong'))
        else:
            n = 10**5; canh = tron_nhan(n, cay(n, 'sau'))
            bac = [0] * (n + 1)
            for u, v in canh:
                bac[u] += 1; bac[v] += 1
            c = [random.randint(1, 1000) if bac[i] == 1 else random.randint(500, 10**9) for i in range(1, n + 1)]
        inp = f'{n}\n' + ' '.join(map(str, c)) + '\n' + ''.join(f'{u} {v}\n' for u, v in canh)
        ghi('GIAMSAT', so, inp, dap_an_giamsat(n, c, canh))

# ---------------- NGAMCANH ----------------
def dijkstra_tuple(n, adj, s):
    INF = float('inf')
    d = [INF] * (n + 1); d[s] = 0
    pq = [(0, s)]
    while pq:
        du, u = heapq.heappop(pq)
        if du > d[u]:
            continue
        for v, w in adj[u]:
            if du + w < d[v]:
                d[v] = du + w; heapq.heappush(pq, (d[v], v))
    return d

def dap_an_ngamcanh(n, b, canh):
    adj = [[] for _ in range(n + 1)]
    for u, v, w in canh:
        adj[u].append((v, w)); adj[v].append((u, w))
    d1 = dijkstra_tuple(n, adj, 1)
    if d1[n] == float('inf'):
        return '-1\n'
    dn = dijkstra_tuple(n, adj, n)
    D = d1[n]
    vao = [[] for _ in range(n + 1)]                        # cac canh u -> v tren mot duong ngan nhat 1 -> n
    for u, v, w in canh:
        for x, y in ((u, v), (v, u)):
            if d1[x] + w + dn[y] == D:
                vao[y].append(x)
    tren = [v for v in range(1, n + 1) if d1[v] + dn[v] == D]
    tren.sort(key=lambda v: d1[v])
    g = [None] * (n + 1)
    for v in tren:
        if v == 1:
            g[v] = b[0]
        else:
            g[v] = b[v - 1] + max(g[u] for u in vao[v])
    return f'{D} {g[n]}\n'

def do_thi(n, m, wmax, lien_thong=True):
    canh = []
    if lien_thong:
        hv = list(range(1, n + 1)); random.shuffle(hv)
        for i in range(1, n):
            canh.append((hv[i], hv[random.randrange(i)], random.randint(1, wmax)))
    while len(canh) < m:
        u, v = random.sample(range(1, n + 1), 2)
        canh.append((u, v, random.randint(1, wmax)))
    random.shuffle(canh)
    return canh

def luoi_nhieu_duong(r, cot, wmax):
    """Luoi r x cot, 1 o goc tren trai, n o goc duoi phai: rat nhieu duong ngan nhat khi w nho."""
    so = lambda i, j: i * cot + j + 1
    canh = []
    for i in range(r):
        for j in range(cot):
            if i + 1 < r:
                canh.append((so(i, j), so(i + 1, j), random.randint(1, wmax)))
            if j + 1 < cot:
                canh.append((so(i, j), so(i, j + 1), random.randint(1, wmax)))
    random.shuffle(canh)
    return r * cot, canh

def sinh_ngamcanh():
    for so in range(1, 11):
        if so == 1:
            n = 5; b = [3, 1, 4, 1, 5]
            canh = [(1, 2, 2), (1, 3, 2), (2, 4, 3), (3, 4, 3), (4, 5, 1), (1, 5, 7)]   # vi du: 6 13
        elif so == 2:
            n = 6; b = [1, 2, 3, 4, 5, 6]; canh = [(1, 2, 1), (2, 3, 1), (4, 5, 1), (5, 6, 1)]   # -> -1
        elif so == 3:
            n = 10; b = [random.randint(0, 10) for _ in range(n)]; canh = do_thi(n, 18, 3)
        elif so == 4:
            n = 9; b = [random.randint(0, 10**9) for _ in range(n)]
            n, canh = luoi_nhieu_duong(3, 3, 1)
        elif so == 5:                                       # subtask 2: moi w = 1
            n = 5 * 10**4; b = [random.randint(0, 10**9) for _ in range(n)]; canh = do_thi(n, 10**5, 1)
        elif so == 6:
            n, canh = luoi_nhieu_duong(200, 250, 1); b = [random.randint(0, 10**9) for _ in range(n)]
        elif so == 7:
            n = 3 * 10**4; b = [random.randint(0, 10) for _ in range(n)]; canh = do_thi(n, 10**5, 1)
        elif so == 8:
            n = 5 * 10**4; b = [random.randint(0, 10**9) for _ in range(n)]; canh = do_thi(n, 10**5, 10**9)
        elif so == 9:                                       # w nho -> rat nhieu duong ngan nhat
            n, canh = luoi_nhieu_duong(200, 250, 2); b = [random.randint(0, 10**9) for _ in range(n)]
        else:
            n = 5 * 10**4; b = [random.randint(0, 10**9) for _ in range(n)]; canh = do_thi(n, 10**5, 5)
        inp = f'{n} {len(canh)}\n' + ' '.join(map(str, b)) + '\n' + ''.join(f'{u} {v} {w}\n' for u, v, w in canh)
        ghi('NGAMCANH', so, inp, dap_an_ngamcanh(n, b, canh))

# ---------------- MUASAM ----------------
def dap_an_muasam(n, k, canh, shop):
    s = len(shop)
    full = (1 << k) - 1
    mon = []
    for x, ds in shop:
        mk = 0
        for y in ds:
            mk |= 1 << (y - 1)
        mon.append(mk)
    tat_ca = 0
    for mk in mon:
        tat_ca |= mk
    if tat_ca != full:
        return '-1\n'
    adj = [[] for _ in range(n + 1)]
    for u, v, w in canh:
        adj[u].append((v, w)); adj[v].append((u, w))
    d1 = dijkstra_tuple(n, adj, 1)
    ds_ = [dijkstra_tuple(n, adj, x) for x, _ in shop]
    INF = float('inf')
    S = 1 << s
    f = [[INF] * s for _ in range(S)]                       # f[tap cua hang da ghe][cua hang cuoi]
    for j in range(s):
        f[1 << j][j] = d1[shop[j][0]]
    hop = [0] * S                                           # hop cac mon cua tap cua hang
    for T in range(1, S):
        low = (T & -T).bit_length() - 1
        hop[T] = hop[T ^ (1 << low)] | mon[low]
    best = INF
    for T in range(1, S):
        for j in range(s):
            x = f[T][j]
            if x == INF:
                continue
            if hop[T] == full:
                best = min(best, x + ds_[j][n])
            for t in range(s):
                if not T >> t & 1:
                    y = x + ds_[j][shop[t][0]]
                    if y < f[T | 1 << t][t]:
                        f[T | 1 << t][t] = y
    return f'{best if best < INF else -1}\n'

def cua_hang(n, s, k, moi_mon=2, nut=None):
    """s cua hang o cac nut ngau nhien; bao dam moi mon co o it nhat mot cua hang."""
    shop = []
    for j in range(s):
        x = nut[j] if nut else random.randint(1, n)
        shop.append((x, set(random.sample(range(1, k + 1), random.randint(1, min(k, moi_mon))))))
    for y in range(1, k + 1):
        if not any(y in ds for _, ds in shop):
            shop[random.randrange(s)][1].add(y)
    return [(x, sorted(ds)) for x, ds in shop]

def sinh_muasam():
    for so in range(1, 11):
        if so == 1:
            n, k = 5, 3
            canh = [(1, 2, 4), (2, 3, 3), (3, 5, 2), (1, 4, 1), (4, 5, 6), (2, 4, 2)]
            shop = [(2, [1, 2]), (4, [3]), (3, [2, 3])]
        elif so == 2:                                       # mon 3 khong ai ban -> -1
            n, k = 4, 3
            canh = [(1, 2, 1), (2, 3, 1), (3, 4, 1)]
            shop = [(2, [1]), (3, [2])]
        elif so == 3:
            n, k = 50, 4; canh = do_thi(n, 120, 100); shop = cua_hang(n, 6, k)
        elif so == 4:                                       # cua hang o nut 1, nut n, hai cua hang cung nut
            n, k = 100, 5; canh = do_thi(n, 300, 10**6)
            shop = cua_hang(n, 6, k, 3, nut=[1, n, 7, 7, 50, 80])
        elif so == 5:
            n, k = 100, 10; canh = do_thi(n, 300, 10**6); shop = cua_hang(n, 10, k, 3)
        elif so == 6:                                       # moi cua hang mot mon rieng: TSP thuan
            n, k = 100, 10; canh = do_thi(n, 400, 1000)
            nut = random.sample(range(2, n), 10)
            shop = [(nut[j], [j + 1]) for j in range(10)]
        elif so == 7:
            n, k = 100, 8; canh = do_thi(n, 250, 10**6); shop = cua_hang(n, 10, k, 4)
        elif so == 8:
            n, k = 10**4, 10; canh = do_thi(n, 3 * 10**4, 10**6); shop = cua_hang(n, 10, k, 3)
        elif so == 9:
            n, k = 10**4, 10; canh = do_thi(n, 3 * 10**4, 10**6)
            nut = random.sample(range(2, n), 10)
            shop = [(nut[j], [j + 1]) for j in range(10)]
        else:                                               # mot cua hang ban rat nhieu mon nhung o xa
            n, k = 10**4, 10; canh = do_thi(n, 3 * 10**4, 10**6); shop = cua_hang(n, 9, k, 2)
            shop.append((random.randint(1, n), list(range(1, k + 1))))
        if so > 2:
            random.shuffle(shop)
        inp = f'{n} {len(canh)} {k} {len(shop)}\n' + ''.join(f'{u} {v} {w}\n' for u, v, w in canh)
        inp += ''.join(f'{x} {len(ds)} ' + ' '.join(map(str, ds)) + '\n' for x, ds in shop)
        ghi('MUASAM', so, inp, dap_an_muasam(n, k, canh, shop))

SINH = {'GIAMSAT': sinh_giamsat, 'NGAMCANH': sinh_ngamcanh, 'MUASAM': sinh_muasam}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        random.seed(bai + '-2026')
        SINH[bai]()
        print('Da sinh', bai)

main()
