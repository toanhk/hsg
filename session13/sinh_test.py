# SINH TEST cho 6 bai buoi 13 (Dijkstra)
#   Tren lop : KHOANGCACH, HANHTRINH, QUATRAM        Ve nha: BENHVIEN, SUADUONG, TAUHOA
# Cau truc thu muc theo Themis: test/KHOANGCACH/Test01/KHOANGCACH.INP + KHOANGCACH.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau (loi giai mau dung heap chua tuple):
#   o day Dijkstra dung heap chua MOT so nguyen goi d * 2^17 + u (meo tang toc trong do_dijkstra.py),
#   BENHVIEN goi ca (d, so hieu benh vien, u) vao mot so, SUADUONG kiem tra canh theo huong d1[u] + w == d1[v]
#   tren "do thi ngan nhat" roi loang nguoc tu n, TAUHOA lam Dijkstra goi so voi ham cho tau.
# HANHTRINH co nhieu dap an: file .OUT la MOT dap an dung, cham bang kiem_tra.py.
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py                  -> sinh ca 6 bai (~30 giay)
#       python sinh_test.py KHOANGCACH TAUHOA -> chi sinh cac bai ke ten
# Moi bai co seed rieng (random.seed('KHOANGCACH-2026'), ...) nen sinh rieng mot bai hay ca bo deu ra CUNG test.
import os, random, sys, heapq

GOC = 'test'
VC = 1 << 62                                  # "vo cung" cho dap an (so nguyen, khong dung float)
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

def do_thi(n, m, wmin=1, wmax=W9, lien=True):
    """m canh vo huong ngau nhien (co the trung, khong khuyen). lien=True: co san mot cay khung."""
    canh = []
    if lien and n > 1:
        hv = list(range(1, n + 1)); random.shuffle(hv)
        for i in range(1, n):
            canh.append((hv[i], hv[random.randrange(i)], random.randint(wmin, wmax)))
    while len(canh) < m:
        u, v = random.sample(range(1, n + 1), 2)
        canh.append((u, v, random.randint(wmin, wmax)))
    random.shuffle(canh)
    return canh

def xich(n, w=None, them=0):
    """Duong 1 - ... - n qua moi dinh theo thu tu ngau nhien (1 o dau, n o cuoi), trong so w hoac ngau nhien."""
    giua = list(range(2, n)); random.shuffle(giua)
    hv = [1] + giua + [n]
    canh = [(hv[i], hv[i + 1], w or random.randint(1, W9)) for i in range(n - 1)]
    for _ in range(them):                     # canh tat dai hon: khong lam ngan duong
        i, j = sorted(random.sample(range(n), 2))
        canh.append((hv[i], hv[j], W9))
    random.shuffle(canh)
    return canh

def luoi(r, c, wmax):
    """Luoi r x c dinh (dinh 1 goc tren trai, dinh r*c goc duoi phai), canh ngang/doc trong so 1..wmax."""
    canh = []
    for i in range(r):
        for j in range(c):
            x = i * c + j + 1
            if j + 1 < c: canh.append((x, x + 1, random.randint(1, wmax)))
            if i + 1 < r: canh.append((x, x + c, random.randint(1, wmax)))
    random.shuffle(canh)
    return canh

def ke(n, canh, vo_huong=True):
    adj = [[] for _ in range(n + 1)]
    for u, v, w in canh:
        adj[u].append((v, w))
        if vo_huong:
            adj[v].append((u, w))
    return adj

def dij(adj, nguon, n):
    """Dijkstra heap so nguyen goi d << 17 | u. Tra ve (dist, tr) voi dist = VC neu khong toi."""
    dist = [VC] * (n + 1); tr = [0] * (n + 1)
    pq = []
    for s in nguon:
        dist[s] = 0; pq.append(s)
    heapq.heapify(pq)
    while pq:
        x = heapq.heappop(pq); d = x >> 17; u = x & 131071
        if d != dist[u]:
            continue
        for v, w in adj[u]:
            if d + w < dist[v]:
                dist[v] = d + w; tr[v] = u
                heapq.heappush(pq, (d + w) << 17 | v)
    return dist, tr

# ---------------- KHOANGCACH ----------------
def dap_an_khoangcach(n, canh):
    dist, _ = dij(ke(n, canh), [1], n)
    return ' '.join(str(x) if x < VC else '-1' for x in dist[1:]) + '\n'

def do_thi_bay(n, K):
    """Dinh 1 noi toi K dinh a_i (trong so i); a_i noi toi tam H (trong so 3K - 2i) -> dist qua a_i toi H
    giam dan theo i, H bi day vao heap K lan. H noi toi moi dinh con lai (la). Doi nhan ngau nhien (tru 1)."""
    hv = list(range(2, n + 1)); random.shuffle(hv)
    a = hv[:K]; H = hv[K]; la = hv[K + 1:]
    canh = [(1, a[i - 1], i) for i in range(1, K + 1)]
    canh += [(a[i - 1], H, 3 * K - 2 * i) for i in range(1, K + 1)]
    canh += [(H, x, random.randint(1, 10)) for x in la]
    random.shuffle(canh)
    return canh

def sinh_khoangcach():
    for so in range(1, 11):
        if so == 1:
            n, canh = 5, [(1, 2, 4), (1, 3, 1), (3, 2, 2), (2, 4, 5), (3, 4, 8)]   # vi du: 0 3 1 8 -1
        elif so == 2:
            n, canh = 1, []
        elif so == 3:                                                     # canh trung, 2 thanh phan
            n = 60; canh = do_thi(40, 80, 1, 20) + [(u + 40, v + 40, w) for u, v, w in do_thi(20, 30, 1, 20)]
        elif so == 4:
            n = 100; canh = do_thi(n, 200, 1, W9)
        elif so == 5:
            n = 2000; canh = do_thi(n, 10**5, 1, W9)                      # day
        elif so == 6:
            n = 2000; canh = xich(n, W9)                                  # khoang cach toi ~2*10^12
        elif so == 7:
            n = 2000; canh = do_thi(1500, 5000, 1, 5)                     # 500 dinh khong toi duoc, nhieu hoa
        elif so == 8:
            n = 10**5; canh = do_thi(n, 10**5, 1, W9)
        elif so == 9:
            n = 10**5; canh = xich(n, W9)                                 # duong dai 10^5 canh, dist 10^14
        else:
            n = 99000; canh = do_thi_bay(n, 1000)                         # bat ban quen bo dinh loi thoi
        ghi('KHOANGCACH', so, de_canh(f'{n} {len(canh)}\n', canh), dap_an_khoangcach(n, canh))

# ---------------- HANHTRINH ----------------
def dap_an_hanhtrinh(n, canh):
    dist, tr = dij(ke(n, canh), [1], n)
    if dist[n] == VC:
        return '-1\n'
    p = [n]
    while p[-1] != 1:
        p.append(tr[p[-1]])
    return f'{dist[n]}\n{len(p)}\n' + ' '.join(map(str, p[::-1])) + '\n'

def sinh_hanhtrinh():
    for so in range(1, 11):
        if so == 1:
            n, canh = 6, [(1, 2, 7), (1, 3, 9), (1, 6, 14), (2, 3, 10), (2, 4, 15), (3, 4, 11),
                          (3, 6, 2), (4, 5, 6), (5, 6, 9)]               # vi du: 11 / 1 3 6
        elif so == 2:
            n, canh = 4, [(1, 2, 3), (3, 4, 1)]                           # khong toi -> -1
        elif so == 3:
            n = 25; canh = luoi(5, 5, 1)                                  # rat nhieu duong cung ngan
        elif so == 4:
            n = 100; canh = do_thi(n, 300, 1, 10)
        elif so == 5:
            n = 2000; canh = do_thi(n, 10**4, 1, W9)
        elif so == 6:
            n = 2000; canh = xich(n, None, 3000)                          # dap an > 10^9: bat INF = 10^9
        elif so == 7:
            n = 1600; canh = luoi(40, 40, 2)
        elif so == 8:
            n = 10**5; canh = do_thi(n, 10**5, 1, W9)
        elif so == 9:
            n = 10**5; canh = xich(n, W9)                                 # duong 10^5 dinh, D ~ 10^14
        else:
            n = 10**5; canh = do_thi(n - 1, 10**5, 1, W9)                # dinh n co lap -> -1
        ghi('HANHTRINH', so, de_canh(f'{n} {len(canh)}\n', canh), dap_an_hanhtrinh(n, canh))

# ---------------- QUATRAM ----------------
def dap_an_quatram(n, a, b, canh):
    adj = ke(n, canh)
    d1, _ = dij(adj, [1], n); da, _ = dij(adj, [a], n); db, _ = dij(adj, [b], n)
    kq = min(d1[a] + da[b] + db[n], d1[b] + db[a] + da[n])
    return (str(kq) if kq < VC else '-1') + '\n'

def ep_b_truoc(n, canh):
    """Chon a, b sao cho di b truoc NGAN HON han di a truoc (de bat ban chi xet mot thu tu)."""
    adj = ke(n, canh)
    d1, _ = dij(adj, [1], n); dn, _ = dij(adj, [n], n)
    ung = [v for v in range(2, n) if d1[v] < VC]
    ung.sort(key=lambda v: d1[v] - dn[v])                             # dau: gan 1, cuoi: gan n
    k = max(1, len(ung) // 20)
    b = random.choice(ung[:k]); a = random.choice(ung[-k:])
    return a, b

def sinh_quatram():
    for so in range(1, 11):
        if so == 1:
            n, a, b = 5, 4, 2
            canh = [(1, 2, 2), (2, 3, 3), (3, 5, 1), (3, 4, 4), (4, 5, 2), (1, 4, 9)]  # vi du: 1-2-3-5-4-5 = 10
        elif so == 2:
            n, a, b = 6, 3, 3
            canh = [(1, 2, 1), (2, 6, 1), (1, 3, 5), (3, 6, 5), (4, 5, 1)]  # a = b
        elif so == 3:
            n = 8; a, b = 1, 8; canh = do_thi(n, 12, 1, 20)                # tram trung diem dau / cuoi
        elif so == 4:
            n = 100; canh = do_thi(n, 250, 1, 100); a, b = ep_b_truoc(n, canh)
        elif so == 5:
            n = 2000; canh = do_thi(n, 6000, 1, W9); a, b = ep_b_truoc(n, canh)
        elif so == 6:                                                      # b nam o thanh phan khac -> -1
            n = 2000; canh = do_thi(1999, 6000, 1, 1000); canh += [(1999, 2000, 7)]
            a, b = random.randint(2, 1998), 1500
            canh = [e for e in canh if 1500 not in e[:2]]
        elif so == 7:
            n = 2000; canh = do_thi(n, 6000, 1, 3); a, b = random.sample(range(2, n), 2)
        elif so == 8:
            n = 5 * 10**4; canh = do_thi(n, 5 * 10**4, 1, W9); a, b = ep_b_truoc(n, canh)
        elif so == 9:
            n = 5 * 10**4; canh = xich(n, W9); a, b = ep_b_truoc(n, canh)      # phai di nguoc lai tren xich
        else:
            n = 5 * 10**4; canh = do_thi(n, 5 * 10**4, 1, 10); a, b = random.sample(range(2, n), 2)
        ghi('QUATRAM', so, de_canh(f'{n} {len(canh)} {a} {b}\n', canh), dap_an_quatram(n, a, b, canh))

# ---------------- BENHVIEN ----------------
def dap_an_benhvien(n, bv, canh):
    adj = ke(n, canh)
    nhan = [VC] * (n + 1)                     # nhan = (d << 17 | h): so sanh mot so = so sanh cap (d, h)
    pq = []
    for h in bv:
        nhan[h] = h; pq.append(h << 17 | h)              # d = 0
    heapq.heapify(pq)
    while pq:
        x = heapq.heappop(pq); u = x & 131071; nh = x >> 17
        if nh != nhan[u]:
            continue
        d = nh >> 17; h = nh & 131071
        for v, w in adj[u]:
            t = (d + w) << 17 | h
            if t < nhan[v]:
                nhan[v] = t; heapq.heappush(pq, t << 17 | v)
    return '\n'.join(f'{x >> 17} {x & 131071}' if x < VC else '-1' for x in nhan[1:]) + '\n'

def sinh_benhvien():
    for so in range(1, 11):
        if so == 1:
            n, bv = 6, [2, 5]
            canh = [(1, 2, 3), (2, 3, 4), (3, 5, 4), (1, 4, 1), (4, 5, 6), (6, 5, 2)]  # vi du (dinh 3 hoa)
        elif so == 2:
            n, bv = 5, [4]; canh = [(1, 2, 1), (2, 3, 1), (4, 5, 2)]       # dinh 1-3 khong toi -> -1
        elif so == 3:
            n = 50; bv = random.sample(range(1, n + 1), 5); canh = do_thi(n, 120, 1, 3)   # nhieu hoa
        elif so == 4:
            n = 100; bv = list(range(1, n + 1)); canh = do_thi(n, 200)     # moi dinh deu la benh vien
        elif so == 5:
            n = 2000; bv = random.sample(range(1, n + 1), 10); canh = do_thi(n, 8000, 1, W9)
        elif so == 6:
            n = 2000; bv = random.sample(range(1, n + 1), 3); canh = do_thi(n, 8000, 1, 2)
        elif so == 7:
            n = 2000; bv = random.sample(range(1, 1001), 10); canh = do_thi(1000, 4000) + \
                [(u + 1000, v + 1000, w) for u, v, w in do_thi(1000, 4000)]
        elif so == 8:
            n = 5 * 10**4; bv = random.sample(range(1, n + 1), 5000); canh = do_thi(n, 5 * 10**4)
        elif so == 9:                                                       # k = n/2, trong so nho -> nhieu hoa
            n = 5 * 10**4; bv = random.sample(range(1, n + 1), n // 2); canh = do_thi(n, 5 * 10**4, 1, 2)
        else:
            n = 5 * 10**4; bv = random.sample(range(1, n + 1), 3); canh = xich(n, W9)
        inp = f'{n} {len(canh)} {len(bv)}\n' + ' '.join(map(str, bv)) + '\n'
        ghi('BENHVIEN', so, de_canh(inp, canh), dap_an_benhvien(n, bv, canh))

# ---------------- SUADUONG ----------------
def dap_an_suaduong(n, canh):
    adj = ke(n, canh)
    d1, _ = dij(adj, [1], n)
    if d1[n] == VC:
        return '0\n'
    # "do thi ngan nhat": canh i di huong u -> v neu d1[u] + w == d1[v]. Loang nguoc tu n tren do thi do:
    # dinh nao toi duoc n bang canh ngan nhat thi nam tren mot duong ngan nhat; canh vao dinh do cung vay.
    vao = [[] for _ in range(n + 1)]
    for i, (u, v, w) in enumerate(canh, 1):
        if d1[u] + w == d1[v]: vao[v].append((u, i))
        if d1[v] + w == d1[u]: vao[u].append((v, i))
    tren = [False] * (n + 1); tren[n] = True
    q = [n]; kq = []
    for v in q:
        for u, i in vao[v]:
            kq.append(i)
            if not tren[u]:
                tren[u] = True; q.append(u)
    kq.sort()
    return f'{len(kq)}\n' + ' '.join(map(str, kq)) + '\n'

def sinh_suaduong():
    for so in range(1, 11):
        if so == 1:
            n, canh = 5, [(1, 2, 2), (2, 5, 3), (1, 3, 1), (3, 4, 1), (4, 5, 3), (3, 5, 5), (2, 4, 1)]
        elif so == 2:
            n, canh = 4, [(1, 2, 1), (2, 1, 1), (3, 4, 1)]                 # khong toi -> 0
        elif so == 3:
            n, canh = 4, [(1, 2, 1), (2, 4, 1), (1, 2, 1), (1, 3, 1), (3, 4, 1), (2, 3, 5)]  # canh trung bang nhau
        elif so == 4:
            n = 8; canh = do_thi(n, 12, 1, 3)
        elif so == 5:
            n = 2000; canh = do_thi(n, 6000, 1, 3)
        elif so == 6:
            n = 1600; canh = luoi(40, 40, 1)                                # moi canh luoi deu tren duong ngan nhat
        elif so == 7:
            n = 2000; canh = do_thi(n, 6000, 1, W9)
        elif so == 8:
            n = 5 * 10**4; canh = do_thi(n, 5 * 10**4, 1, 2)
        elif so == 9:
            n = 49729; canh = luoi(223, 223, 2)
        else:
            n = 5 * 10**4; canh = xich(n, 1) + [(1, n, W9)]                     # duong dai 5*10^4, canh tat 1-n qua dai
            random.shuffle(canh)
        ghi('SUADUONG', so, de_canh(f'{n} {len(canh)}\n', canh), dap_an_suaduong(n, canh))

# ---------------- TAUHOA ----------------
def dap_an_tauhoa(n, tuyen):
    adj = [[] for _ in range(n + 1)]
    for u, v, c, p in tuyen:
        adj[u].append((v, c, p))
    t = [VC] * (n + 1); t[1] = 0
    pq = [1]
    while pq:
        x = heapq.heappop(pq); d = x >> 17; u = x & 131071
        if d != t[u]:
            continue
        for v, c, p in adj[u]:
            den = -(-d // p) * p + c
            if den < t[v]:
                t[v] = den; heapq.heappush(pq, den << 17 | v)
    return (str(t[n]) if t[n] < VC else '-1') + '\n'

def tau(n, m, cmax, pmax, xuoi=0):
    """m tuyen ngau nhien; xuoi > 0: them mot "xuong song" 1 -> ... -> n de chac chan toi duoc."""
    ds = []
    if xuoi:
        giua = list(range(2, n)); random.shuffle(giua); hv = [1] + giua + [n]
        ds = [(hv[i], hv[i + 1], random.randint(1, cmax), random.randint(1, pmax)) for i in range(n - 1)]
    while len(ds) < m:
        u, v = random.sample(range(1, n + 1), 2)
        ds.append((u, v, random.randint(1, cmax), random.randint(1, pmax)))
    random.shuffle(ds)
    return ds

def sinh_tauhoa():
    for so in range(1, 11):
        if so == 1:
            n, ds = 4, [(1, 2, 3, 5), (1, 3, 1, 1), (3, 2, 1, 10), (2, 4, 2, 4), (3, 4, 9, 1)]  # vi du: 6
        elif so == 2:
            n, ds = 3, [(1, 2, 1, 1), (3, 2, 1, 1)]                       # mot chieu: khong toi 3 -> -1
        elif so == 3:
            n = 30; ds = tau(n, 80, 20, 30)
        elif so == 4:                                                     # chu ky lon: cho tau rat lau
            n = 100; ds = tau(n, 200, 10, 10**9, xuoi=1)
        elif so == 5:
            n = 10**5; ds = [(u, v, c, 1) for u, v, c, _ in tau(n, 10**5, W9, 1, xuoi=1)]
        elif so == 6:
            n = 10**5; ds = [(u, v, c, 1) for u, v, c, _ in tau(n, 10**5, 100, 1)]
        elif so == 7:
            n = 2000; ds = [(u, v, c, 1) for u, v, c, _ in tau(n, 8000, 10, 1)]
        elif so == 8:
            n = 10**5; ds = tau(n, 10**5, 100, 100, xuoi=1)
        elif so == 9:
            n = 10**5; ds = tau(n, 10**5, W9, W9)
        else:
            n = 10**5; ds = tau(n, 10**5, 5, 60, xuoi=1)                  # c nho, chu ky lon: cho tau quyet dinh
        ghi('TAUHOA', so, de_canh(f'{n} {len(ds)}\n', ds), dap_an_tauhoa(n, ds))

SINH = {'KHOANGCACH': sinh_khoangcach, 'HANHTRINH': sinh_hanhtrinh, 'QUATRAM': sinh_quatram,
        'BENHVIEN': sinh_benhvien, 'SUADUONG': sinh_suaduong, 'TAUHOA': sinh_tauhoa}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        random.seed(bai + '-2026')
        SINH[bai]()
        print('Da sinh', bai)

main()
