# SINH TEST cho 6 bai buoi 16 (Cay khung nho nhat)
#   Tren lop : NOILANG, DOCTHAP, MANGDIEN        Ve nha: GIACOCAU, CHENHLECH, XETAI
# Cau truc thu muc theo Themis: test/NOILANG/Test01/NOILANG.INP + NOILANG.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau (loi giai mau dung Kruskal + DSU):
#   NOILANG, MANGDIEN bang Prim + heapq (MANGDIEN moc cay tu dinh ao 0), DOCTHAP bang nhi phan dap an + BFS,
#   GIACOCAU bang Prim cay khung lon nhat voi trong so w + 10^15 * t (canh bat buoc "nang vo cung"),
#   CHENHLECH bang hai con tro tren cac gia tri w + BFS kiem tra lien thong,
#   XETAI: test nho BFS tung truy van, test cung L gan nhan thanh phan bang BFS, test lon tron canh va truy van
#   thanh MOT danh sach su kien sap xep chung.
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py                 -> sinh ca 6 bai (~60 giay)
#       python sinh_test.py NOILANG XETAI   -> chi sinh cac bai ke ten
# Moi bai co seed rieng (random.seed('NOILANG-2026'), ...) nen sinh rieng mot bai hay ca bo deu ra CUNG test.
import os, random, sys, heapq

GOC = 'test'

def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

def do_thi(n, m, wmax, lien_thong=True, wmin=1):
    """m canh (u, v, w), u != v, co the trung canh. lien_thong=True: co san mot cay khung ngau nhien."""
    canh = []
    if lien_thong:
        hv = list(range(1, n + 1)); random.shuffle(hv)
        for i in range(1, n):
            canh.append((hv[i], hv[random.randrange(i)], random.randint(wmin, wmax)))
    while len(canh) < m:
        u, v = random.sample(range(1, n + 1), 2)
        canh.append((u, v, random.randint(wmin, wmax)))
    random.shuffle(canh)
    return canh[:m] if not lien_thong else canh

def hai_manh(n, m, wmax):
    """Do thi KHONG lien thong: hai manh rieng (dinh duoc tron ngau nhien)."""
    hv = list(range(1, n + 1)); random.shuffle(hv)
    k = random.randint(1, n - 1)
    A, B = hv[:k], hv[k:]
    canh = []
    for nhom in (A, B):
        for i in range(1, len(nhom)):
            canh.append((nhom[i], nhom[random.randrange(i)], random.randint(1, wmax)))
    while len(canh) < m:
        nhom = A if random.random() < len(A) / n else B
        if len(nhom) < 2:
            continue
        u, v = random.sample(nhom, 2)
        canh.append((u, v, random.randint(1, wmax)))
    random.shuffle(canh)
    return canh

def dong(canh):
    return ''.join(f'{u} {v} {w}\n' for u, v, w in canh)

def prim(n, canh, goc=1, dinh_dau=1):
    """Prim heapq. Tra ve (tong, so dinh vao cay). Dinh danh so dinh_dau..n."""
    adj = [[] for _ in range(n + 1)]
    for u, v, w in canh:
        adj[u].append((w, v)); adj[v].append((w, u))
    vao = [False] * (n + 1)
    pq = [(0, goc)]; tong = 0; dem = 0
    while pq:
        w, u = heapq.heappop(pq)
        if vao[u]:
            continue
        vao[u] = True; tong += w; dem += 1
        for e in adj[u]:
            if not vao[e[1]]:
                heapq.heappush(pq, e)
    return tong, dem

# ---------------- NOILANG ----------------
def dap_an_noilang(n, canh):
    tong, dem = prim(n, canh)
    return f'{tong if dem == n else -1}\n'

def sinh_noilang():
    for so in range(1, 11):
        if so == 1:
            n, canh = 5, [(1, 2, 4), (1, 3, 1), (2, 3, 2), (2, 4, 7), (3, 4, 5), (4, 5, 3), (3, 5, 8)]   # vi du: 11
        elif so == 2:
            n, canh = 6, [(1, 2, 3), (2, 3, 1), (1, 3, 2), (4, 5, 1), (5, 6, 2)]                     # 2 manh -> -1
        elif so == 3:
            n = 8; canh = do_thi(n, 12, 20)
        elif so == 4:                                                    # nhieu chi phi bang nhau, canh trung
            n = 8; canh = do_thi(n, 12, 3)
            canh.append(canh[0]); canh.pop(1)
        elif so == 5:
            n = 1000; canh = do_thi(n, 5000, 10**9)
        elif so == 6:
            n = 1000; canh = hai_manh(n, 5000, 10**6)
        elif so == 7:                                                    # chi co cay: dung n-1 canh
            n = 1000; canh = do_thi(n, 999, 10**9)
        elif so == 8:
            n = 10**5; canh = do_thi(n, 2 * 10**5, 10**9)
        elif so == 9:                                                    # duong thang, chi phi tang dan:
            n = 10**5                                                    # DSU khong hop theo kich thuoc -> xich dai
            canh = [(i, i + 1, i) for i in range(1, n)]
            canh += [(random.randint(1, n), random.randint(1, n), 10**9) for _ in range(10**5 + 1)]
            canh = [e for e in canh if e[0] != e[1]]
        else:                                                            # lang 1 bi co lap -> -1 o cuoi
            n = 10**5
            canh = [(u + 1, v + 1, w) for u, v, w in do_thi(n - 1, 2 * 10**5, 10**9)]
        ghi('NOILANG', so, f'{n} {len(canh)}\n' + dong(canh), dap_an_noilang(n, canh))

# ---------------- DOCTHAP ----------------
def dap_an_docthap(n, s, t, canh):
    if s == t:
        return '0\n'
    adj = [[] for _ in range(n + 1)]
    for u, v, h in canh:
        adj[u].append((v, h)); adj[v].append((u, h))
    hs = sorted(set(h for u, v, h in canh))
    lo, hi, kq = 0, len(hs) - 1, -1
    while lo <= hi:
        mid = (lo + hi) // 2; X = hs[mid]
        da = [False] * (n + 1); da[s] = True; q = [s]
        for u in q:
            for v, h in adj[u]:
                if h <= X and not da[v]:
                    da[v] = True; q.append(v)
        if da[t]:
            kq = X; hi = mid - 1
        else:
            lo = mid + 1
    return f'{kq}\n'

def sinh_docthap():
    for so in range(1, 11):
        s = t = None
        if so == 1:
            n, s, t = 6, 1, 6
            canh = [(1, 2, 5), (1, 3, 8), (2, 4, 9), (3, 4, 3), (4, 6, 4), (2, 5, 2), (5, 6, 10)]    # vi du: 8
        elif so == 2:
            n, s, t = 5, 3, 3; canh = do_thi(n, 6, 10)                    # s = t -> 0
        elif so == 3:
            n = 8; canh = hai_manh(n, 10, 50)                             # co the khong toi duoc
        elif so == 4:
            n = 8; canh = do_thi(n, 12, 30)
        elif so == 5:
            n = 1000; canh = do_thi(n, 1000, 10**9)
        elif so == 6:
            n = 1000; canh = hai_manh(n, 1000, 10**9)
        elif so == 7:                                                     # moi doan cung do doc
            n = 1000; canh = do_thi(n, 1000, 7, wmin=7)
        elif so == 8:
            n = 10**5; canh = do_thi(n, 2 * 10**5, 10**9)
        elif so == 9:                                                     # duong thang 1 - 2 - ... - n, s = 1, t = n
            n = 10**5; s, t = 1, n
            canh = [(i, i + 1, random.randint(1, 10**9)) for i in range(1, n)]
            canh += [(i, i + 2, 10**9) for i in range(1, n - 1, 2)][:10**5 + 1]
            random.shuffle(canh)
        else:
            n = 10**5; canh = do_thi(n, 2 * 10**5, 10**6)
        if s is None:
            s, t = random.sample(range(1, n + 1), 2)
        ghi('DOCTHAP', so, f'{n} {len(canh)} {s} {t}\n' + dong(canh), dap_an_docthap(n, s, t, canh))

# ---------------- MANGDIEN ----------------
def dap_an_mangdien(n, c, canh):
    tong, dem = prim(n, canh + [(0, i, c[i - 1]) for i in range(1, n + 1)], goc=0)
    return f'{tong}\n'

def sinh_mangdien():
    for so in range(1, 11):
        if so == 1:
            n, c = 5, [8, 4, 9, 7, 3]
            canh = [(1, 2, 2), (2, 3, 5), (1, 3, 6), (3, 4, 6), (4, 5, 10)]      # vi du: 20
        elif so == 2:
            n, c = 4, [5, 5, 5, 5]; canh = [(1, 2, 100), (2, 3, 100), (3, 4, 100)]   # moi lang tu xay: 20
        elif so == 3:
            n = 8; c = [random.randint(1, 30) for _ in range(n)]; canh = hai_manh(n, 10, 20)
        elif so == 4:
            n = 8; c = [random.randint(1, 60) for _ in range(n)]; canh = do_thi(n, 12, 20)
        elif so == 5:
            n = 1000; c = [random.randint(1, 10**9) for _ in range(n)]; canh = do_thi(n, 5000, 10**9)
        elif so == 6:                                                    # tram re ngang day -> nhieu tram
            n = 1000; c = [random.randint(1, 1000) for _ in range(n)]; canh = do_thi(n, 5000, 2000)
        elif so == 7:
            n = 1000; c = [random.randint(10**8, 10**9) for _ in range(n)]
            canh = hai_manh(n, 5000, 10**5)
        elif so == 8:
            n = 10**5; c = [random.randint(1, 10**9) for _ in range(n)]; canh = do_thi(n, 2 * 10**5, 10**9)
        elif so == 9:
            n = 10**5; c = [random.randint(1, 10**6) for _ in range(n)]; canh = do_thi(n, 2 * 10**5, 3 * 10**6)
        else:                                                            # khong co day nao
            n = 10**5; c = [random.randint(1, 10**9) for _ in range(n)]; canh = []
        inp = f'{n} {len(canh)}\n' + ' '.join(map(str, c)) + '\n' + dong(canh)
        ghi('MANGDIEN', so, inp, dap_an_mangdien(n, c, canh))

# ---------------- GIACOCAU ----------------
def dap_an_giacocau(n, ds):
    BIG = 10**15
    can = sum(t for u, v, w, t in ds)
    adj = [[] for _ in range(n + 1)]
    for u, v, w, t in ds:
        key = -(w + BIG * t)                    # heap nho nhat -> dung -w de lay canh LON nhat
        adj[u].append((key, v, t)); adj[v].append((key, u, t))
    vao = [False] * (n + 1)
    pq = [(0, 1, 0)]; tong = 0; dem = 0; co = 0
    while pq:
        key, u, t = heapq.heappop(pq)
        if vao[u]:
            continue
        vao[u] = True; tong -= key; dem += 1; co += t
        for e in adj[u]:
            if not vao[e[1]]:
                heapq.heappush(pq, e)
    if dem < n or co < can:
        return '-1\n'
    return f'{tong - BIG * co}\n'

def gan_bat_buoc(canh, k, vong=False):
    """Danh dau k canh bat buoc. vong=False: chon tren mot rung (khong chu trinh)."""
    ds = [[u, v, w, 0] for u, v, w in canh]
    if vong:
        for i in random.sample(range(len(ds)), k):
            ds[i][3] = 1
    else:
        par = list(range(max(max(e[0], e[1]) for e in ds) + 1))
        def f(x):
            while par[x] != x:
                par[x] = par[par[x]]; x = par[x]
            return x
        thu_tu = list(range(len(ds))); random.shuffle(thu_tu)
        for i in thu_tu:
            if k == 0:
                break
            a, b = f(ds[i][0]), f(ds[i][1])
            if a != b:
                par[a] = b; ds[i][3] = 1; k -= 1
    return [tuple(e) for e in ds]

def sinh_giacocau():
    for so in range(1, 11):
        if so == 1:
            n = 4
            ds = [(1, 2, 3, 0), (2, 3, 8, 0), (3, 4, 5, 1), (1, 4, 6, 0), (1, 3, 9, 0)]   # vi du: 22
        elif so == 2:
            n = 4; ds = [(1, 2, 5, 1), (2, 3, 5, 1), (1, 3, 9, 1), (3, 4, 2, 0)]            # bat buoc co vong -> -1
        elif so == 3:
            n = 8; ds = gan_bat_buoc(do_thi(n, 12, 20), 3)
        elif so == 4:
            n = 8; ds = gan_bat_buoc(hai_manh(n, 12, 20), 2) if random.random() < 0 else gan_bat_buoc(do_thi(n, 12, 20), 4, vong=True)
        elif so == 5:                                                   # subtask 2: khong co cau bat buoc
            n = 10**5; ds = gan_bat_buoc(do_thi(n, 2 * 10**5, 10**9), 0)
        elif so == 6:
            n = 10**5; ds = gan_bat_buoc(hai_manh(n, 2 * 10**5, 10**9), 0)
        elif so == 7:
            n = 1000; ds = gan_bat_buoc(do_thi(n, 3000, 10**6), 0)
        elif so == 8:                                                   # nhieu bat buoc (re), khong vong
            n = 10**5; ds = gan_bat_buoc(do_thi(n, 2 * 10**5, 10**9), 50000)
        elif so == 9:                                                   # mot vong bat buoc dau tien gay -1
            n = 10**5; ds = gan_bat_buoc(do_thi(n, 2 * 10**5 - 3, 10**9), 3000)
            a, b, c = random.sample(range(1, n + 1), 3)
            ds += [(a, b, 7, 1), (b, c, 7, 1), (a, c, 7, 1)]
            random.shuffle(ds)
        else:                                                           # bat buoc la cay khung tron ven -> tong co dinh
            n = 10**5; ds = gan_bat_buoc(do_thi(n, 2 * 10**5, 10**9), n - 1)
        inp = f'{n} {len(ds)}\n' + ''.join(f'{u} {v} {w} {t}\n' for u, v, w, t in ds)
        ghi('GIACOCAU', so, inp, dap_an_giacocau(n, ds))

# ---------------- CHENHLECH ----------------
def dap_an_chenhlech(n, canh):
    ws = sorted(set(w for u, v, w in canh))
    def noi_het(lo, hi):                      # chi dung canh co lo <= w <= hi: co lien thong khong?
        adj = [[] for _ in range(n + 1)]
        for u, v, w in canh:
            if lo <= w <= hi:
                adj[u].append(v); adj[v].append(u)
        da = [False] * (n + 1); da[1] = True; q = [1]
        for u in q:
            for v in adj[u]:
                if not da[v]:
                    da[v] = True; q.append(v)
        return len(q) == n
    best = -1; j = 0
    for i in range(len(ws)):                  # hai con tro: lo = ws[i] tang thi hi nho nhat khong giam
        if j < i:
            j = i
        while j < len(ws) and not noi_het(ws[i], ws[j]):
            j += 1
        if j == len(ws):
            break
        if best < 0 or ws[j] - ws[i] < best:
            best = ws[j] - ws[i]
    return f'{best}\n'

def sinh_chenhlech():
    for so in range(1, 11):
        if so == 1:
            n = 4; canh = [(1, 2, 3), (1, 3, 5), (1, 4, 6), (2, 4, 6), (3, 4, 7)]     # vi du: 1
        elif so == 2:
            n = 5; canh = [(1, 2, 1), (2, 3, 4), (3, 1, 9), (4, 5, 2)]             # khong lien thong -> -1
        elif so == 3:
            n = 6; canh = do_thi(n, 12, 30)
        elif so == 4:
            n = 6; canh = do_thi(n, 5, 10**9)                                      # chi co mot cay
        elif so == 5:
            n = 50; canh = do_thi(n, 300, 1000)
        elif so == 6:
            n = 100; canh = hai_manh(n, 300, 10**9)
        elif so == 7:
            n = 100; canh = do_thi(n, 300, 10**9)
        elif so == 8:
            n = 100; canh = do_thi(n, 1000, 10**9)
        elif so == 9:                                     # dinh n chi noi bang MOT canh rat nang -> quet het
            n = 100; canh = do_thi(n - 1, 999, 10**6) + [(n, random.randint(1, n - 1), 10**9)]
            random.shuffle(canh)
        else:                                             # w nho, nhieu canh bang nhau
            n = 100; canh = do_thi(n, 1000, 50)
        ghi('CHENHLECH', so, f'{n} {len(canh)}\n' + dong(canh), dap_an_chenhlech(n, canh))

# ---------------- XETAI ----------------
def dap_an_xetai(n, canh, qs):
    if len(qs) * (n + len(canh)) <= 10**6:                 # nho: BFS tung truy van
        adj = [[] for _ in range(n + 1)]
        for u, v, w in canh:
            adj[u].append((v, w)); adj[v].append((u, w))
        out = []
        for s, L in qs:
            da = [False] * (n + 1); da[s] = True; hd = [s]
            for u in hd:
                for v, w in adj[u]:
                    if w >= L and not da[v]:
                        da[v] = True; hd.append(v)
            out.append(len(hd))
        return '\n'.join(map(str, out)) + '\n'
    if len(set(L for s, L in qs)) == 1:                    # cung L: gan nhan thanh phan mot lan bang BFS
        L = qs[0][1]
        adj = [[] for _ in range(n + 1)]
        for u, v, w in canh:
            if w >= L:
                adj[u].append(v); adj[v].append(u)
        nhan = [0] * (n + 1); co = [0]
        for s0 in range(1, n + 1):
            if nhan[s0] == 0:
                nhan[s0] = len(co); hd = [s0]
                for u in hd:
                    for v in adj[u]:
                        if nhan[v] == 0:
                            nhan[v] = len(co); hd.append(v)
                co.append(len(hd))
        return '\n'.join(str(co[nhan[s]]) for s, L in qs) + '\n'
    # lon: tron su kien (-gia tri, loai, chi so); loai 0 = cau (them truoc truy van cung muc), 1 = truy van
    sk = [(-w, 0, i) for i, (u, v, w) in enumerate(canh)] + [(-L, 1, k) for k, (s, L) in enumerate(qs)]
    sk.sort()
    par = list(range(n + 1)); sz = [1] * (n + 1)
    def f(x):
        r = x
        while par[r] != r:
            r = par[r]
        while par[x] != r:
            par[x], x = r, par[x]
        return r
    kq = [0] * len(qs)
    for g, loai, i in sk:
        if loai == 0:
            a, b = f(canh[i][0]), f(canh[i][1])
            if a != b:
                if sz[a] < sz[b]:
                    a, b = b, a
                par[b] = a; sz[a] += sz[b]
        else:
            kq[i] = sz[f(qs[i][0])]
    return '\n'.join(map(str, kq)) + '\n'

def sinh_xetai():
    for so in range(1, 11):
        if so == 1:
            n = 5; canh = [(1, 2, 10), (2, 3, 4), (3, 4, 7), (4, 5, 2), (1, 3, 6)]
            qs = [(1, 5), (1, 7), (4, 3), (5, 1), (2, 11)]          # vi du: 4 2 4 5 1
        elif so <= 4:
            n = random.randint(50, 300); m = random.randint(n, 300)
            canh = do_thi(n, m, 10 if so == 2 else 10**9, lien_thong=(so != 3))
            qs = [(random.randint(1, n), random.randint(1, 10 if so == 2 else 10**9)) for _ in range(300)]
        elif so <= 7:                                                 # subtask 2: moi truy van cung L
            n = 10**5; m = 10**5
            canh = do_thi(n, m, 10**9) if so != 6 else hai_manh(n, m, 10**9)
            L = random.choice([5 * 10**8, 9 * 10**8, 10**8])
            qs = [(random.randint(1, n), L) for _ in range(10**5)]
        else:
            n = 10**5; m = 10**5
            wmax = 10**9 if so != 9 else 100                          # so 9: nhieu cau cung tai trong
            canh = do_thi(n, m, wmax)
            qs = [(random.randint(1, n), random.randint(1, wmax)) for _ in range(10**5)]
            if so == 10:                                              # L lon hon moi cau / nho hon moi cau
                qs[:1000] = [(random.randint(1, n), random.choice([1, 10**9])) for _ in range(1000)]
        inp = f'{n} {len(canh)} {len(qs)}\n' + dong(canh) + ''.join(f'{s} {L}\n' for s, L in qs)
        ghi('XETAI', so, inp, dap_an_xetai(n, canh, qs))

SINH = {'NOILANG': sinh_noilang, 'DOCTHAP': sinh_docthap, 'MANGDIEN': sinh_mangdien,
        'GIACOCAU': sinh_giacocau, 'CHENHLECH': sinh_chenhlech, 'XETAI': sinh_xetai}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        random.seed(bai + '-2026')
        SINH[bai]()
        print('Da sinh', bai)

main()
