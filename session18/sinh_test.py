# SINH TEST cho 6 bai buoi 18 (QHD tren DAG & tren do thi)
#   Tren lop : DUONGDAI, DEMLOTRINH, DUONGRE        Ve nha: TRUOTTUYET, THANGTHUA, CHUYENBAY
# Cau truc thu muc theo Themis: test/DUONGDAI/Test01/DUONGDAI.INP + DUONGDAI.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau (loi giai mau dung Kahn "day toi"):
#   DUONGDAI  : thu tu to-po bang DFS ngan xep (hau thu tu dao nguoc) + QHD "keo ve" theo cung vao
#   DEMLOTRINH: dem NGUOC g[u] = so duong tu u den n theo hau thu tu DFS, dap an g[1]
#   DUONGRE, CHUYENBAY: Dijkstra heap so nguyen goi d << 17 | u chi tinh dist, roi sap dinh theo dist va
#               QHD "keo ve" tren cac cung cua DAG duong ngan nhat (dist[u] + w == dist[v])
#   TRUOTTUYET: Kahn tren DAG an (ban bac vao = so o ke cao hon), g = duong dai nhat KET THUC tai o
#   THANGTHUA : phan tich nguoc (retrograde): the cuoi la thua, lan nguoc bang dem so nuoc con lai
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py                    -> sinh ca 6 bai (~30 giay)
#       python sinh_test.py DUONGDAI THANGTHUA  -> chi sinh cac bai ke ten
# Moi bai co seed rieng (random.seed('DUONGDAI-2026'), ...) nen sinh rieng mot bai hay ca bo deu ra CUNG test.
import os, random, sys, heapq

GOC = 'test'
P = 10**9 + 7
VC = 1 << 62
W9 = 10**9

def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

def de_canh(dau, canh):
    return dau + ''.join(' '.join(map(str, e)) + '\n' for e in canh)

def thu_tu_an(n, dau_cuoi=True):
    """Hoan vi bi mat lam thu tu to-po. dau_cuoi=True: dinh 1 dung dau, dinh n dung cuoi."""
    if dau_cuoi:
        giua = list(range(2, n)); random.shuffle(giua)
        return [1] + giua + [n] if n > 1 else [1]
    hv = list(range(1, n + 1)); random.shuffle(hv)
    return hv

def dag(n, m, hv, xich=False, gan=0):
    """m cung (i < j theo hv) ngau nhien, co the trung. xich: them duong hv[0] -> hv[1] -> ... (duong dai).
    gan > 0: cung chi noi toi dinh cach toi da gan buoc (DAG "hep", nhieu duong dai)."""
    canh = []
    if xich:
        canh = [(hv[i], hv[i + 1]) for i in range(n - 1)]
    while len(canh) < m:
        if gan:
            i = random.randrange(n - 1); j = min(n - 1, i + random.randint(1, gan))
        else:
            i, j = sorted(random.sample(range(n), 2))
        canh.append((hv[i], hv[j]))
    random.shuffle(canh)
    return canh[:m] if not xich else canh

def topo_dfs(n, adj):
    """Thu tu to-po bang DFS ngan xep: hau thu tu roi dao nguoc. adj[u] la list dinh (hoac (dinh, w))."""
    da = [False] * (n + 1); hau = []
    for s in range(1, n + 1):
        if da[s]:
            continue
        da[s] = True; st = [(s, 0)]
        while st:
            u, i = st[-1]
            if i < len(adj[u]):
                st[-1] = (u, i + 1)
                v = adj[u][i]
                if not da[v]:
                    da[v] = True; st.append((v, 0))
            else:
                hau.append(u); st.pop()
    return hau[::-1]

# ---------------- DUONGDAI ----------------
def dap_an_duongdai(n, canh):
    adj = [[] for _ in range(n + 1)]; vao = [[] for _ in range(n + 1)]
    for u, v, w in canh:
        adj[u].append(v); vao[v].append((u, w))
    AM = -VC
    f = [AM] * (n + 1); f[1] = 0
    for v in topo_dfs(n, adj):
        for u, w in vao[v]:                      # keo ve: moi u truoc v da xong
            if f[u] != AM and f[u] + w > f[v]:
                f[v] = f[u] + w
    return (str(f[n]) if f[n] != AM else 'KHONG') + '\n'

def gan_w(canh, lo, hi):
    return [(u, v, random.randint(lo, hi)) for u, v in canh]

def sinh_duongdai():
    for so in range(1, 11):
        if so == 1:
            n, canh = 6, [(1, 2, 3), (1, 3, 2), (2, 4, 4), (3, 4, 6), (2, 5, -1), (4, 6, 1), (5, 6, 10),
                          (3, 5, -5)]                                    # vi du: 12
        elif so == 2:                                                    # n khong toi duoc, nhanh khac dai
            n, canh = 6, [(1, 2, 5), (2, 3, 1), (4, 5, 100), (5, 6, 100), (4, 6, 7)]
        elif so == 3:                                                    # moi trong so am
            n = 9; canh = gan_w(dag(n, 18, thu_tu_an(n)), -50, -1)
        elif so == 4:
            n = 10; canh = gan_w(dag(n, 20, thu_tu_an(n)), -20, 30)
        elif so == 5:
            n = 1000; canh = gan_w(dag(n, 5000, thu_tu_an(n)), 1, 1000)
        elif so == 6:                                                    # dinh 1 o giua thu tu: nhieu dinh khong toi
            n = 1000; hv = thu_tu_an(n, False)
            canh = gan_w(dag(n, 5000, hv, gan=30), -W9, W9)
        elif so == 7:
            n = 1000; canh = gan_w(dag(n, 5000, thu_tu_an(n), xich=True), -10, 5)
        elif so == 8:                                                    # chuoi dai + cung tat, w lon
            n = 10**5; canh = gan_w(dag(n, 2 * 10**5, thu_tu_an(n), xich=True), 1, W9)
        elif so == 9:
            n = 10**5; canh = gan_w(dag(n, 2 * 10**5, thu_tu_an(n), xich=True, gan=50), -W9, W9)
        else:                                                            # 1 o giua, n o cuoi, nguon khac co duong lon
            n = 10**5; hv = thu_tu_an(n, False)
            hv.remove(1); hv.remove(n); hv.insert(n // 2, 1); hv.append(n)
            canh = gan_w(dag(n, 2 * 10**5 - 1, hv, gan=20), -1000, 1000)
            canh.append((hv[0], n, W9))
            random.shuffle(canh)
        ghi('DUONGDAI', so, de_canh(f'{n} {len(canh)}\n', canh), dap_an_duongdai(n, canh))

# ---------------- DEMLOTRINH ----------------
def dap_an_demlotrinh(n, canh):
    adj = [[] for _ in range(n + 1)]
    for u, v in canh:
        adj[u].append(v)
    g = [0] * (n + 1); g[n] = 1
    for u in reversed(topo_dfs(n, adj)):         # dinh sau truoc: g[u] = tong g[v]
        if u != n:
            g[u] = sum(g[v] for v in adj[u]) % P
    return f'{g[1]}\n'

def sinh_demlotrinh():
    for so in range(1, 11):
        if so == 1:
            n, canh = 5, [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)]   # vi du: 5
        elif so == 2:                                                    # cung lap; 1 -> n co 2 cung
            n, canh = 4, [(1, 2), (1, 2), (2, 4), (1, 4), (1, 4), (3, 1)]
        elif so == 3:                                                    # khong co duong: 0
            n = 8; hv = thu_tu_an(n); hv.remove(n); hv.insert(0, n)
            canh = dag(n, 15, hv)
        elif so == 4:
            n = 10; canh = dag(n, 20, thu_tu_an(n))
        elif so == 5:                                                    # day: so duong rat lon -> can mod
            n = 1000; canh = dag(n, 5000, thu_tu_an(n), gan=5)
        elif so == 6:
            n = 1000; canh = dag(n, 5000, thu_tu_an(n, False))
        elif so == 7:                                                    # "thang": i -> i+1, i -> i+2
            n = 1000; hv = thu_tu_an(n)
            canh = [(hv[i], hv[i + 1]) for i in range(n - 1)] + [(hv[i], hv[i + 2]) for i in range(n - 2)]
            canh += [(hv[0], hv[-1])] * (5000 - len(canh)); random.shuffle(canh)
        elif so == 8:                                                    # chuoi 2*10^5: giet de quy
            n = 2 * 10**5; canh = dag(n, 2 * 10**5, thu_tu_an(n), xich=True)
        elif so == 9:
            n = 10**5; canh = dag(n, 2 * 10**5, thu_tu_an(n), xich=True, gan=4)
        else:
            n = 10**5; hv = thu_tu_an(n)
            canh = [(hv[i], hv[i + 1]) for i in range(n - 1)] + [(hv[i], hv[i + 2]) for i in range(n - 2)]
            random.shuffle(canh)
        ghi('DEMLOTRINH', so, de_canh(f'{n} {len(canh)}\n', canh), dap_an_demlotrinh(n, canh))

# ---------------- DUONGRE & CHUYENBAY ----------------
def dag_ngan_nhat(n, canh):
    """Tra ve (dist, cnt, it, nhieu): Dijkstra goi so chi tinh dist, roi QHD keo ve theo dist tang dan."""
    adj = [[] for _ in range(n + 1)]; vao = [[] for _ in range(n + 1)]
    for u, v, w in canh:
        adj[u].append((v, w)); vao[v].append((u, w))
    dist = [VC] * (n + 1); dist[1] = 0
    pq = [1]
    while pq:
        x = heapq.heappop(pq); d = x >> 17; u = x & 131071
        if d != dist[u]:
            continue
        for v, w in adj[u]:
            if d + w < dist[v]:
                dist[v] = d + w; heapq.heappush(pq, (d + w) << 17 | v)
    cnt = [0] * (n + 1); it = [VC] * (n + 1); nhieu = [-1] * (n + 1)
    cnt[1] = 1; it[1] = 0; nhieu[1] = 0
    for v in sorted((v for v in range(2, n + 1) if dist[v] < VC), key=dist.__getitem__):
        for u, w in vao[v]:
            if dist[u] + w == dist[v]:           # cung thuoc DAG duong ngan nhat (u da tinh vi dist[u] < dist[v])
                cnt[v] += cnt[u]
                it[v] = min(it[v], it[u] + 1); nhieu[v] = max(nhieu[v], nhieu[u] + 1)
        cnt[v] %= P
    return dist, cnt, it, nhieu

def dap_an_duongre(n, canh):
    dist, cnt, _, _ = dag_ngan_nhat(n, canh)
    return '-1 0\n' if dist[n] == VC else f'{dist[n]} {cnt[n]}\n'

def dap_an_chuyenbay(n, canh):
    dist, cnt, it, nhieu = dag_ngan_nhat(n, canh)
    return f'{dist[n]} {cnt[n]} {it[n]} {nhieu[n]}\n'

def do_thi_co_huong(n, m, wmin, wmax, xuoi=True):
    """m cung co huong ngau nhien; xuoi: them duong 1 -> ... -> n qua moi dinh (bao dam toi duoc)."""
    canh = []
    if xuoi:
        hv = thu_tu_an(n)
        canh = [(hv[i], hv[i + 1], random.randint(wmin, wmax)) for i in range(n - 1)]
    while len(canh) < m:
        u, v = random.sample(range(1, n + 1), 2)
        canh.append((u, v, random.randint(wmin, wmax)))
    random.shuffle(canh)
    return canh

def luoi_co_huong(r, c, wmax):
    """Luoi r x c (dinh 1 goc tren trai, r*c goc duoi phai), moi canh ke co ca 2 chieu, trong so 1..wmax."""
    canh = []
    for i in range(r):
        for j in range(c):
            x = i * c + j + 1
            if j + 1 < c:
                canh.append((x, x + 1, random.randint(1, wmax))); canh.append((x + 1, x, random.randint(1, wmax)))
            if i + 1 < r:
                canh.append((x, x + c, random.randint(1, wmax))); canh.append((x + c, x, random.randint(1, wmax)))
    random.shuffle(canh)
    return canh

def bay_dem_trung(n, K, w_ra=1):
    """1 -> a_i (gia i), a_i -> H (gia 3K - 2i): dist[H] giam dan K lan -> H nam trong heap K lan.
    H -> n bang 2 lo trinh bang gia (H -> n va H -> b -> n). Ban quen bo cap loi thoi xu ly H K lan
    -> dem trung. Cac dinh con lai de co lap (them cung khac neu muon)."""
    hv = list(range(2, n)); random.shuffle(hv)
    a = hv[:K]; H = hv[K]; b = hv[K + 1]
    canh = [(1, a[i - 1], i) for i in range(1, K + 1)]
    canh += [(a[i - 1], H, 3 * K - 2 * i) for i in range(1, K + 1)]
    canh += [(H, n, 2 * w_ra), (H, b, w_ra), (b, n, w_ra)]
    random.shuffle(canh)
    return canh

def sinh_duongre():
    for so in range(1, 11):
        if so == 1:
            n, canh = 4, [(1, 2, 1), (1, 3, 1), (2, 4, 2), (3, 4, 2), (1, 4, 3)]    # vi du: 3 3
        elif so == 2:
            n, canh = 5, [(1, 2, 1), (2, 3, 1), (4, 5, 1), (5, 1, 1)]               # khong toi: -1 0
        elif so == 3:
            n = 8; canh = bay_dem_trung(n, 3)
        elif so == 4:
            n = 8; canh = do_thi_co_huong(n, 20, 1, 3)
        elif so == 5:                                                    # subtask 2: moi w = 1
            n = 30000; canh = do_thi_co_huong(n, 10**5, 1, 1)
        elif so == 6:
            n = 22500; canh = luoi_co_huong(150, 150, 1)                  # so duong = to hop, rat lon
        elif so == 7:
            n = 2000; canh = do_thi_co_huong(n, 10**5, 1, 1)
        elif so == 8:                                                    # luoi, w nho: rat nhieu duong bang nhau
            n = 22500; canh = luoi_co_huong(150, 150, 2)
        elif so == 9:
            n = 10**5; canh = bay_dem_trung(n, 30000)
            canh += do_thi_co_huong(n, 10**5 - len(canh), W9 - 10, W9, False)
        else:
            n = 30000; canh = do_thi_co_huong(n, 10**5, 1, 5)
        ghi('DUONGRE', so, de_canh(f'{n} {len(canh)}\n', canh), dap_an_duongre(n, canh))

def sinh_chuyenbay():
    for so in range(1, 11):
        if so == 1:
            n, canh = 4, [(1, 4, 10), (1, 2, 3), (2, 4, 4), (1, 3, 2), (3, 2, 1), (3, 4, 5)]  # vi du: 7 3 2 3
        elif so == 2:
            n, canh = 2, [(1, 2, 5), (1, 2, 5), (2, 1, 1)]
        elif so == 3:
            n = 8; canh = do_thi_co_huong(n, 20, 1, 3)
        elif so == 4:
            n = 8; canh = do_thi_co_huong(n, 14, 1, 10)
        elif so == 5:                                                    # subtask 2: moi w = 1
            n = 30000; canh = do_thi_co_huong(n, 10**5, 1, 1)
        elif so == 6:
            n = 22500; canh = luoi_co_huong(150, 150, 1)
        elif so == 7:
            n = 2000; canh = do_thi_co_huong(n, 10**5, 1, 1)
        elif so == 8:                                                    # it chuyen nhung dat duoc tim truoc
            n = 30000; canh = do_thi_co_huong(n, 10**5 - 1000, 1, 3)
            canh += [(1, random.randint(2, n), random.randint(5, 50)) for _ in range(1000)]
            random.shuffle(canh)
        elif so == 9:
            n = 12100; canh = luoi_co_huong(110, 110, 3)                  # luoi day du: toi duoc
            canh += [tuple(random.sample(range(1, n + 1), 2)) + (random.randint(2, 12),) for _ in range(30000)]
            random.shuffle(canh)
        else:
            n = 30000; canh = do_thi_co_huong(n, 10**5, 1, W9)
        ghi('CHUYENBAY', so, de_canh(f'{n} {len(canh)}\n', canh), dap_an_chuyenbay(n, canh))

# ---------------- TRUOTTUYET ----------------
def dap_an_truottuyet(r, c, h):
    N = r * c
    vao = [0] * N
    ke = []
    for p in range(N):
        i, j = divmod(p, c)
        k = []
        if i > 0: k.append(p - c)
        if i + 1 < r: k.append(p + c)
        if j > 0: k.append(p - 1)
        if j + 1 < c: k.append(p + 1)
        ke.append(k)
        vao[p] = sum(1 for q in k if h[q] > h[p])          # so o cao hon ke p (cung q -> p)
    g = [1] * N
    q = [p for p in range(N) if vao[p] == 0]
    for p in q:
        for x in ke[p]:
            if h[x] < h[p]:
                if g[p] + 1 > g[x]:
                    g[x] = g[p] + 1
                vao[x] -= 1
                if vao[x] == 0:
                    q.append(x)
    return f'{max(g)}\n'

def con_ran(r, c):
    """Do cao giam dan doc theo duong ran (hang chan trai->phai, hang le phai->trai): duong dai nhat = r*c."""
    h = [0] * (r * c); k = r * c
    for i in range(r):
        cot = range(c) if i % 2 == 0 else range(c - 1, -1, -1)
        for j in cot:
            h[i * c + j] = k; k -= 1
    return h

def xoan_oc(r, c):
    """Do cao giam dan theo hinh xoan oc tu ngoai vao trong."""
    h = [0] * (r * c); k = r * c
    t, b, l, rr = 0, r - 1, 0, c - 1
    while t <= b and l <= rr:
        for j in range(l, rr + 1): h[t * c + j] = k; k -= 1
        for i in range(t + 1, b + 1): h[i * c + rr] = k; k -= 1
        if t < b:
            for j in range(rr - 1, l - 1, -1): h[b * c + j] = k; k -= 1
        if l < rr:
            for i in range(b - 1, t, -1): h[i * c + l] = k; k -= 1
        t += 1; b -= 1; l += 1; rr -= 1
    return h

def sinh_truottuyet():
    for so in range(1, 11):
        if so == 1:
            r, c, h = 3, 4, [5, 6, 7, 8, 4, 1, 2, 9, 3, 12, 11, 10]           # vi du: 12 -> ... -> 1
        elif so == 2:
            r, c, h = 2, 3, [7] * 6                                           # bang nhau: 1
        elif so == 3:
            r, c = 4, 4; h = [random.randint(1, 3) for _ in range(16)]
        elif so == 4:
            r, c = 4, 4; h = [random.randint(1, W9) for _ in range(16)]
        elif so == 5:
            r, c = 100, 100; h = con_ran(r, c)
        elif so == 6:
            r, c = 100, 100; h = [random.randint(1, 10) for _ in range(r * c)]
        elif so == 7:
            r, c = 1, 100; h = [random.randint(1, W9) for _ in range(c)]
        elif so == 8:
            r, c = 500, 500; h = con_ran(r, c)
            h = [x * 1000 + random.randint(0, 999) for x in h]                # van giam ngat doc ran
        elif so == 9:
            r, c = 500, 500; h = xoan_oc(r, c)
        else:
            r, c = 500, 500; h = [random.randint(1, W9) for _ in range(r * c)]
        inp = f'{r} {c}\n' + ''.join(' '.join(map(str, h[i * c:(i + 1) * c])) + '\n' for i in range(r))
        ghi('TRUOTTUYET', so, inp, dap_an_truottuyet(r, c, h))

# ---------------- THANGTHUA ----------------
def dap_an_thangthua(n, canh):
    nguoc = [[] for _ in range(n + 1)]; ra = [0] * (n + 1)
    for u, v in canh:
        nguoc[v].append(u); ra[u] += 1
    kq = [0] * (n + 1)                          # 0 chua biet, 1 thang, 2 thua
    q = [u for u in range(1, n + 1) if ra[u] == 0]
    for u in q:
        kq[u] = 2
    for v in q:
        for u in nguoc[v]:
            if kq[u]:
                continue
            if kq[v] == 2:                      # u di toi the thua cua doi thu -> u thang
                kq[u] = 1; q.append(u)
            else:
                ra[u] -= 1
                if ra[u] == 0:                  # moi nuoc cua u deu toi the thang cua doi thu
                    kq[u] = 2; q.append(u)
    return ''.join('A' if kq[u] == 1 else 'B' for u in range(1, n + 1)) + '\n'

def sinh_thangthua():
    for so in range(1, 11):
        if so == 1:
            n, canh = 5, [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]        # vi du: ABBAB
        elif so == 2:
            n, canh = 3, [(1, 2), (2, 3)]                                # BAB
        elif so == 3:
            n = 10; canh = dag(n, 12, thu_tu_an(n, False))
        elif so == 4:
            n = 10; canh = dag(n, 25, thu_tu_an(n, False), gan=3)
        elif so == 5:
            n = 2000; canh = dag(n, 2000, thu_tu_an(n, False), xich=True)
        elif so == 6:
            n = 2000; canh = dag(n, 6000, thu_tu_an(n, False), gan=4)
        elif so == 7:
            n = 2000; canh = dag(n, 1500, thu_tu_an(n, False))
        elif so == 8:                                                    # chuoi dai: xen ke A/B
            n = 2 * 10**5; canh = dag(n, 2 * 10**5 - 1, thu_tu_an(n, False), xich=True)
        elif so == 9:
            n = 10**5; canh = dag(n, 2 * 10**5, thu_tu_an(n, False), gan=3)
        else:
            n = 2 * 10**5; canh = dag(n, 2 * 10**5, thu_tu_an(n, False))
        ghi('THANGTHUA', so, de_canh(f'{n} {len(canh)}\n', canh), dap_an_thangthua(n, canh))

SINH = {'DUONGDAI': sinh_duongdai, 'DEMLOTRINH': sinh_demlotrinh, 'DUONGRE': sinh_duongre,
        'TRUOTTUYET': sinh_truottuyet, 'THANGTHUA': sinh_thangthua, 'CHUYENBAY': sinh_chuyenbay}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        random.seed(bai + '-2026')
        SINH[bai]()
        print('Da sinh', bai)

main()
