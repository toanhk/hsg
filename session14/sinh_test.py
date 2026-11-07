# SINH TEST cho 6 bai buoi 14 (Bien the duong di)
#   Tren lop : DAOCHIEU, MIENPHI, MOICAP        Ve nha: GIAMGIA, MOTUYEN, THUONGPHAT
# Cau truc thu muc theo Themis: test/DAOCHIEU/Test01/DAOCHIEU.INP + DAOCHIEU.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau:
#   DAOCHIEU  : Dijkstra heapq (loi giai mau: BFS 0-1)
#   MIENPHI   : Dijkstra 2 tang (loi giai mau: 2 lan Dijkstra tu 1 va tu n)
#   MOICAP: Dijkstra O(n^2) tu moi dinh (loi giai mau: Floyd)
#   GIAMGIA   : tinh TUNG tang j = 0..k, moi tang mot lan Dijkstra nhieu nguon (loi giai mau: Dijkstra chung)
#   MOTUYEN   : sau moi tuyen chay 2 buoc Floyd voi k = u roi k = v (loi giai mau: cong thuc qua tuyen)
#   THUONGPHAT: Bellman-Ford roi chay them toi n vong lan "-vo cuc" (loi giai mau: vong thu n + BFS)
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py                  -> sinh ca 6 bai (~20 giay)
#       python sinh_test.py MIENPHI GIAMGIA  -> chi sinh cac bai ke ten
# Moi bai co seed rieng (random.seed('MIENPHI-2026'), ...) nen sinh rieng mot bai hay ca bo deu ra CUNG test.
import os, random, sys
from heapq import heappush, heappop

GOC = 'test'
INF = float('inf')

def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

def dong(ds):
    return ''.join(' '.join(map(str, x)) + '\n' for x in ds)

def cay_ngau_nhien(n, sau=False):
    """n - 1 canh noi dinh 1..n thanh mot cay (ten dinh xao tron, dinh 1 va n giu nguyen vai tro ngau nhien).
    sau=True: cay gan nhu mot xich dai (moi dinh noi voi 1 trong 3 dinh ngay truoc no)."""
    hv = list(range(1, n + 1)); random.shuffle(hv)
    canh = []
    for i in range(1, n):
        j = random.randint(max(0, i - 3), i - 1) if sau else random.randrange(i)
        canh.append((hv[j], hv[i]))
    return canh

def them_canh(n, canh, m):
    canh = canh[:]
    while len(canh) < m:
        canh.append(tuple(random.sample(range(1, n + 1), 2)))
    random.shuffle(canh)
    return canh

def dijkstra(n, adj, nguon):
    """adj[u] = [(v, w)], nguon = [(dinh, khoang cach ban dau)]"""
    d = [INF] * (n + 1)
    h = []
    for s, x in nguon:
        if x < d[s]:
            d[s] = x; heappush(h, (x, s))
    while h:
        du, u = heappop(h)
        if du > d[u]:
            continue
        for v, w in adj[u]:
            if du + w < d[v]:
                d[v] = du + w; heappush(h, (d[v], v))
    return d

# ---------------- DAOCHIEU ----------------
def dap_an_daochieu(n, cung):
    adj = [[] for _ in range(n + 1)]
    for u, v in cung:
        adj[u].append((v, 0)); adj[v].append((u, 1))
    x = dijkstra(n, adj, [(1, 0)])[n]
    return f'{x if x < INF else -1}\n'

def dao_ngau_nhien(canh, p=0.5):
    return [(v, u) if random.random() < p else (u, v) for u, v in canh]

def sinh_daochieu():
    for so in range(1, 11):
        if so == 1:
            n, cung = 5, [(1, 2), (3, 2), (3, 4), (5, 4), (4, 1)]           # vi du: 2
        elif so == 2:                                                       # bay cho ban "danh dau som"
            n, cung = 4, [(2, 1), (1, 3), (3, 2), (2, 4)]                  # dap an 0
        elif so == 3:
            n, cung = 6, [(1, 2), (3, 2), (2, 1), (4, 5), (6, 5)]          # 1 va 6 khac thanh phan: -1
        elif so == 4:
            n = 100; cung = dao_ngau_nhien(them_canh(n, cay_ngau_nhien(n), 150))
        elif so == 5:                                                       # cay sau, dao ngau nhien
            n = 2 * 10**4; cung = dao_ngau_nhien(them_canh(n, cay_ngau_nhien(n, True), 2 * 10**4))
        elif so == 6:                                                       # 5000 bay "canh 1 truoc canh 0":
            g = 5000; n = 3 * g + 1; cung = []                              # x -> z -> y ton 0, nhung y lien
            for t in range(g):                                              # ke x qua canh nguoc (ton 1)
                x, z, y = 3 * t + 1, 3 * t + 2, 3 * t + 3                   # duoc liet ke TRUOC. Dap an 0.
                cung += [(y, x), (x, z), (z, y), (y, y + 1)]
        elif so == 7:                                                       # 2 nua roi nhau: -1
            n = 2 * 10**4; h = n // 2
            cung = [(random.randint(1, h), random.randint(1, h)) for _ in range(10**4)]
            cung += [(random.randint(h + 1, n), random.randint(h + 1, n)) for _ in range(10**4)]
        elif so == 8:                                                       # xich dai, dap an ~ 5*10^4
            n = 10**5; cung = dao_ngau_nhien(them_canh(n, cay_ngau_nhien(n, True), 10**5))
        elif so == 9:
            n = 10**5; cung = [tuple(random.sample(range(1, n + 1), 2)) for _ in range(10**5)]
        else:                                                               # xich nguoc 1 <- 2 <- ... <- n
            n = 10**5; m = 10**5                                    # + cac loi tat dung chieu
            hv = [1] + random.sample(range(2, n), n - 2) + [n]
            cung = [(hv[i + 1], hv[i]) for i in range(n - 1)]
            while len(cung) < m:
                i = random.randrange(n - 10); cung.append((hv[i], hv[i + random.randint(2, 10)]))
            random.shuffle(cung)
        ghi('DAOCHIEU', so, f'{n} {len(cung)}\n' + dong(cung), dap_an_daochieu(n, cung))

# ---------------- MIENPHI ----------------
def dap_an_mienphi(n, canh):
    adj = [[] for _ in range(n + 1)]
    for u, v, w in canh:
        adj[u].append((v, w)); adj[v].append((u, w))
    d = [[INF] * (n + 1) for _ in range(2)]
    d[0][1] = 0; h = [(0, 0, 1)]
    while h:
        du, j, u = heappop(h)
        if du > d[j][u]:
            continue
        for v, w in adj[u]:
            for j2, c in ((j, w), (1, 0)) if j == 0 else ((1, w),):
                if du + c < d[j2][v]:
                    d[j2][v] = du + c; heappush(h, (du + c, j2, v))
    x = min(d[0][n], d[1][n])
    return f'{x if x < INF else -1}\n'

def gan_gia(canh, lo, hi):
    return [(u, v, random.randint(lo, hi)) for u, v in canh]

def sinh_mienphi():
    for so in range(1, 11):
        if so == 1:
            n, canh = 4, [(1, 2, 5), (2, 4, 5), (1, 3, 2), (3, 4, 20)]       # vi du: 2
        elif so == 2:
            n, canh = 5, [(1, 2, 3), (2, 3, 4), (4, 5, 1)]                  # khong toi: -1
        elif so == 3:
            n = 100; canh = gan_gia(them_canh(n, cay_ngau_nhien(n), 200), 1, 1000)
        elif so == 4:                                                       # 1 tuyen cuc dat la loi tat
            n = 100; canh = gan_gia(cay_ngau_nhien(n, True), 1, 100)
            canh += [(1, n, 10**9)] + gan_gia([tuple(random.sample(range(1, n + 1), 2)) for _ in range(50)], 10**4, 10**5)
        elif so == 5:                                                       # subtask 2: cung gia
            n = 1000; canh = gan_gia(them_canh(n, cay_ngau_nhien(n, True), 2000), 7, 7)
        elif so == 6:
            n = 3 * 10**4; canh = gan_gia(them_canh(n, cay_ngau_nhien(n, True), 6 * 10**4), 10**9, 10**9)
        elif so == 7:
            n = 3 * 10**4; h = n // 2
            canh = gan_gia(them_canh(h, cay_ngau_nhien(h), 3 * 10**4), 5, 5)
            canh += [(u + h, v + h, 5) for u, v in them_canh(h, cay_ngau_nhien(h), 3 * 10**4)]   # -1
        elif so == 8:
            n = 3 * 10**4; canh = gan_gia(them_canh(n, cay_ngau_nhien(n), 6 * 10**4), 1, 10**9)
        elif so == 9:                                                       # xich dai + vai cau rat dat
            n = 3 * 10**4; canh = gan_gia(them_canh(n, cay_ngau_nhien(n, True), 6 * 10**4 - 30), 1, 10**4)
            canh += [(*random.sample(range(1, n + 1), 2), random.randint(10**8, 10**9)) for _ in range(30)]
        else:
            n = 3 * 10**4; canh = gan_gia(them_canh(n, cay_ngau_nhien(n, True), 6 * 10**4), 1, 10**9)
        if so > 2:
            random.shuffle(canh)
        ghi('MIENPHI', so, f'{n} {len(canh)}\n' + dong(canh), dap_an_mienphi(n, canh))

# ---------------- MOICAP ----------------
def dap_an_moicap(n, canh, hoi):
    g = [[INF] * (n + 1) for _ in range(n + 1)]
    for u, v, w in canh:
        if w < g[u][v]:
            g[u][v] = g[v][u] = w
    can = sorted(set(u for u, v in hoi))
    D = {}
    for s in can:                          # Dijkstra O(n^2) (do thi day)
        d = [INF] * (n + 1); d[s] = 0
        xong = [False] * (n + 1)
        for _ in range(n):
            u, best = -1, INF
            for x in range(1, n + 1):
                if not xong[x] and d[x] < best:
                    u, best = x, d[x]
            if u == -1:
                break
            xong[u] = True
            gu = g[u]
            for v in range(1, n + 1):
                if best + gu[v] < d[v]:
                    d[v] = best + gu[v]
        D[s] = d
    return ''.join(f'{D[u][v] if D[u][v] < INF else -1}\n' for u, v in hoi)

def hoi_ngau_nhien(n, q):
    return [(random.randint(1, n), random.randint(1, n)) for _ in range(q)]

def sinh_moicap():
    for so in range(1, 11):
        if so == 1:
            n, canh = 4, [(1, 2, 3), (2, 3, 4), (1, 3, 10), (3, 4, 1)]
            hoi = [(1, 3), (4, 1), (2, 2)]                                  # vi du: 7 8 0
        elif so == 2:                                                       # xich xao ten: bat ban sai thu tu vong
            n = 50; hv = list(range(1, n + 1)); random.shuffle(hv)
            canh = [(hv[i], hv[i + 1], random.randint(1, 100)) for i in range(n - 1)]
            hoi = hoi_ngau_nhien(n, 500)
        elif so == 3:                                                       # nhieu manh + canh lap
            n = 30; canh = []
            for _ in range(60):
                u, v = random.sample(range(1, 11), 2) if random.random() < 0.5 else random.sample(range(11, 26), 2)
                canh.append((u, v, random.randint(1, 50)))
            hoi = hoi_ngau_nhien(n, 300)
        elif so == 4:
            n = 50; canh = gan_gia(them_canh(n, cay_ngau_nhien(n), 600), 1, 10**6); hoi = hoi_ngau_nhien(n, 2000)
        elif so == 5:
            n = 200; canh = gan_gia(them_canh(n, cay_ngau_nhien(n, True), 400), 1, 10**6); hoi = hoi_ngau_nhien(n, 10)
        elif so == 6:
            n = 200; canh = gan_gia(them_canh(n, [], 2 * 10**4), 1, 10**6); hoi = hoi_ngau_nhien(n, 10)
        elif so == 7:
            n = 200; canh = gan_gia([tuple(random.sample(range(1, 101), 2)) for _ in range(3000)], 1, 10**6)
            hoi = hoi_ngau_nhien(n, 10)
        elif so == 8:                                                       # do thi day du
            n = 200; canh = [(i, j, random.randint(1, 10**6)) for i in range(1, n + 1) for j in range(i + 1, n + 1)]
            hoi = hoi_ngau_nhien(n, 10**5)
        elif so == 9:                                                       # gan nhu xich: duong rat dai
            n = 200; canh = gan_gia(them_canh(n, cay_ngau_nhien(n, True), 220), 1, 10**6); hoi = hoi_ngau_nhien(n, 10**5)
        else:                                                               # 2 nua roi nhau, nhieu canh lap
            n = 200; canh = []
            for _ in range(2 * 10**4):
                lo = 1 if random.random() < 0.5 else 101
                u, v = random.sample(range(lo, lo + 100), 2); canh.append((u, v, random.randint(1, 10**6)))
            hoi = hoi_ngau_nhien(n, 10**5)
        if so > 1:
            random.shuffle(canh)
        inp = f'{n} {len(canh)} {len(hoi)}\n' + dong(canh) + dong(hoi)
        ghi('MOICAP', so, inp, dap_an_moicap(n, canh, hoi))

# ---------------- GIAMGIA ----------------
def dap_an_giamgia(n, k, cung):
    adj = [[] for _ in range(n + 1)]
    for u, v, w in cung:
        adj[u].append((v, w))
    tang = dijkstra(n, adj, [(1, 0)])              # tang 0: chua dung ve
    kq = tang[n]
    for _ in range(k):                              # tang j: vao bang 1 chuyen giam gia tu tang j - 1
        nguon = [(v, tang[u] + w // 2) for u, v, w in cung if tang[u] < INF]
        tang = dijkstra(n, adj, nguon + [(1, 0)])
        kq = min(kq, tang[n])
    return f'{kq if kq < INF else -1}\n'

def sinh_giamgia():
    for so in range(1, 11):
        if so == 1:
            n, k = 4, 1
            cung = [(1, 2, 10), (2, 4, 10), (1, 3, 3), (3, 4, 15), (4, 1, 1)]   # vi du: 10
        elif so == 2:
            n, k = 6, 0; cung = gan_gia([tuple(random.sample(range(1, 7), 2)) for _ in range(12)], 1, 20)
            cung.append((1, 6, 99))
        elif so == 3:                                                       # mot chieu: toi n khong duoc
            n, k = 5, 2; cung = [(1, 2, 5), (2, 3, 7), (5, 4, 1), (4, 1, 1), (3, 1, 9)]
        elif so == 4:
            n, k = 100, 3; cung = gan_gia(dao_ngau_nhien(them_canh(n, cay_ngau_nhien(n), 500)), 1, 999)
        elif so == 5:                                                       # xich liet ke nguoc (giong test 9), k = 1
            n, k = 10**4, 1
            cung = [(i, i + 1, random.randint(1, 10**4)) for i in range(n - 1, 0, -1)]
            cung += gan_gia([tuple(random.sample(range(1, n + 1), 2)) for _ in range(3 * 10**4 - len(cung))], 3 * 10**8, 10**9)
        elif so == 6:
            n, k = 10**4, 1; cung = gan_gia(dao_ngau_nhien(them_canh(n, cay_ngau_nhien(n), 3 * 10**4)), 1, 10**9)
        elif so == 7:                                                       # 1 chuyen cuc dat la loi tat
            n, k = 10**4, 1; cung = gan_gia(dao_ngau_nhien(them_canh(n, cay_ngau_nhien(n, True), 3 * 10**4 - 1), 0.2), 1, 10**3)
            cung.append((1, n, 10**9 - 1))
        elif so == 8:
            n, k = 10**4, 5; cung = gan_gia(dao_ngau_nhien(them_canh(n, cay_ngau_nhien(n, True), 3 * 10**4), 0.3), 1, 10**9)
        elif so == 9:                                                       # xich dai, liet ke NGUOC: chan Bellman-Ford
            # Duong re nhat la xich 1 -> 2 -> ... -> n (tong <= 10^8); cac chuyen them deu >= 3*10^8 nen
            # du giam nua gia van khong lam loi tat. Liet ke cung xich tu cuoi ve dau va KHONG tron:
            # moi luot Bellman-Ford chi noi them mot dinh -> can ~n luot -> GIAMGIA_trau qua gio.
            n, k = 10**4, 5
            cung = [(i, i + 1, random.randint(1, 10**4)) for i in range(n - 1, 0, -1)]
            cung += gan_gia([tuple(random.sample(range(1, n + 1), 2)) for _ in range(3 * 10**4 - len(cung))], 3 * 10**8, 10**9)
        else:                                                               # vai chuyen rat dat tren duong
            n, k = 10**4, 5; cung = gan_gia(dao_ngau_nhien(them_canh(n, cay_ngau_nhien(n, True), 3 * 10**4), 0.2), 1, 10**4)
            cung = [(u, v, w * 99991 if random.random() < 0.05 else w) for u, v, w in cung]
        if so > 1 and so not in (5, 9):
            random.shuffle(cung)
        ghi('GIAMGIA', so, f'{n} {len(cung)} {k}\n' + dong(cung), dap_an_giamgia(n, k, cung))

# ---------------- MOTUYEN ----------------
def dap_an_motuyen(n, canh, moi):
    B = 10**18
    d = [[B] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        d[i][i] = 0
    for u, v, w in canh:
        d[u][v] = d[v][u] = min(d[u][v], w)
    def buoc(k):                           # mot buoc Floyd voi dinh trung gian k
        dk = d[k]
        for i in range(1, n + 1):
            di = d[i]; dik = di[k]
            for j in range(1, n + 1):
                if dik + dk[j] < di[j]:
                    di[j] = dik + dk[j]
    for k in range(1, n + 1):
        buoc(k)
    out = []
    for u, v, w in moi:
        if w < d[u][v]:
            d[u][v] = d[v][u] = w
            buoc(u); buoc(v)
        out.append(sum(d[i][j] for i in range(1, n + 1) for j in range(i + 1, n + 1)))
    return ''.join(f'{x}\n' for x in out)

def sinh_motuyen():
    for so in range(1, 11):
        if so == 1:
            n, canh = 4, [(1, 2, 4), (2, 3, 4), (3, 4, 4)]
            moi = [(1, 4, 5), (2, 4, 1), (1, 3, 100)]                         # vi du: 34 23 23
        elif so == 2:                                                       # tuyen moi deu khong re hon
            n = 10; canh = [(i, j, 1) for i in range(1, n + 1) for j in range(i + 1, n + 1)]
            moi = [(*random.sample(range(1, n + 1), 2), random.randint(1, 9)) for _ in range(10)]
        elif so == 3:
            n = 50; canh = gan_gia(them_canh(n, cay_ngau_nhien(n), 80), 1, 10**6)
            moi = [(*random.sample(range(1, n + 1), 2), random.randint(1, 10**6)) for _ in range(20)]
        elif so == 4:
            n = 2; canh = [(1, 2, 10), (2, 1, 7)]; moi = [(1, 2, 8), (2, 1, 3), (1, 2, 3)]
        elif so in (5, 6, 7):
            n = 200; canh = gan_gia(them_canh(n, cay_ngau_nhien(n, so == 5), 250 if so < 7 else 5000), 10**5, 10**6)
            moi = [(*random.sample(range(1, n + 1), 2), random.randint(1, 10**5)) for _ in range(20)]
        elif so == 8:                                                       # xich dai, tuyen moi ngay cang re
            n = 200; canh = gan_gia(cay_ngau_nhien(n, True), 10**5, 10**6)
            moi = [(*random.sample(range(1, n + 1), 2), 10**5 - 400 * t) for t in range(200)]
        elif so == 9:
            n = 200; canh = gan_gia(them_canh(n, cay_ngau_nhien(n), 1000), 1, 10**6)
            moi = [(*random.sample(range(1, n + 1), 2), random.randint(1, 10**6)) for _ in range(200)]
        else:
            n = 200; canh = gan_gia(cay_ngau_nhien(n, True), 10**6, 10**6)
            moi = [(*random.sample(range(1, n + 1), 2), random.randint(1, 1000)) for _ in range(200)]
        if so > 1:
            random.shuffle(canh)
        inp = f'{n} {len(canh)} {len(moi)}\n' + dong(canh) + dong(moi)
        ghi('MOTUYEN', so, inp, dap_an_motuyen(n, canh, moi))

# ---------------- THUONGPHAT ----------------
def dap_an_thuongphat(n, cung):
    d = [INF] * (n + 1); d[1] = 0
    for _ in range(n - 1):
        doi = False
        for u, v, w in cung:
            if d[u] + w < d[v]:
                d[v] = d[u] + w; doi = True
        if not doi:
            break
    for _ in range(n):                     # lan "-vo cuc": dinh nao con giam hoac dung sau dinh -vo cuc
        doi = False
        for u, v, w in cung:
            if d[u] != INF and d[v] != -INF and (d[u] == -INF or d[u] + w < d[v]):
                d[v] = -INF; doi = True
        if not doi:
            break
    if d[n] == -INF:
        return 'VOCUC\n'
    return 'KHONG\n' if d[n] == INF else f'{d[n]}\n'

def the_vi(n, cung, c_lo=0, c_hi=50):
    """Gan trong so w = c + p[u] - p[v] (c >= 0): co canh am nhung MOI chu trinh co tong >= 0."""
    p = [random.randint(-5000, 5000) for _ in range(n + 1)]
    out = []
    for u, v in cung:
        w = random.randint(c_lo, c_hi) + p[u] - p[v]
        out.append((u, v, max(-10**4, min(10**4, w))))
    return out

def vong_am(dinh, tong=-1):
    """Chu trinh qua cac dinh 'dinh' co tong trong so = tong < 0."""
    k = len(dinh)
    w = [random.randint(-50, 50) for _ in range(k - 1)]
    w.append(tong - sum(w))
    return [(dinh[i], dinh[(i + 1) % k], w[i]) for i in range(k)]

def sinh_thuongphat():
    for so in range(1, 11):
        if so == 1:
            n, cung = 4, [(1, 2, 5), (2, 4, 3), (1, 3, 2), (3, 2, -4), (3, 4, 4)]     # vi du: 1
        elif so == 2:
            n, cung = 4, [(1, 2, 1), (2, 3, -2), (3, 2, 1), (3, 4, 7)]              # vi du: VOCUC
        elif so == 3:                                                               # chu trinh am o nhanh cut
            n = 8; cung = [(1, 2, 3), (2, 8, 4), (1, 5, -1), (5, 6, -2), (6, 7, 1), (7, 5, 0), (3, 4, 2)]
        elif so == 4:                                                               # KHONG + chu trinh am
            n = 100; cung = gan_gia(them_canh(n - 1, cay_ngau_nhien(n - 1), 300), -50, 200)
            cung += vong_am(random.sample(range(1, n), 5)) + [(n, 1, 5)]
        elif so == 5:
            n = 1000; cung = the_vi(n, dao_ngau_nhien(them_canh(n, cay_ngau_nhien(n), 5000)))
        elif so == 6:
            n = 1000; cung = gan_gia(dao_ngau_nhien(them_canh(n, cay_ngau_nhien(n, True), 5000)), 0, 10**4)
        elif so == 7:                                                               # Bellman-Ford xau nhat:
            n = 1000; hv = [1] + random.sample(range(2, n), n - 2) + [n]            # xich 1 -> ... -> n
            ch = [(hv[i], hv[i + 1]) for i in range(n - 1)]
            cung = the_vi(n, ch, 0, 3)[::-1]                                        # xep nguoc thu tu
            cung += [(*random.sample(range(1, n + 1), 2), 10**4) for _ in range(5000 - len(cung))]
        elif so == 8:                                                               # chu trinh am tren duong
            n = 1000; cung = the_vi(n, dao_ngau_nhien(them_canh(n, cay_ngau_nhien(n, True), 4990)))
            cung += vong_am(random.sample(range(2, n), 10), -3)
        elif so == 9:                                                               # chu trinh am o nhanh cut
            n = 1000; h = 900
            cung = the_vi(h, dao_ngau_nhien(them_canh(h, cay_ngau_nhien(h), 3000)))
            cung = [(n if u == h else u, n if v == h else v, w) for u, v, w in cung]   # dinh h doi ten thanh n
            cung += [(random.randint(1, h - 1), random.randint(h, n - 1), random.randint(-100, 100)) for _ in range(50)]
            cung += [(random.randint(h, n - 1), random.randint(h, n - 1), random.randint(0, 100)) for _ in range(1900)]
            cung += vong_am(random.sample(range(h, n), 30), -7)
        else:                                                                       # xich xau nhat qua 900 dinh
            n = 1000; hv = [1] + random.sample(range(2, n), 898) + [n]              # + chu trinh am o 100 dinh
            ch = [(hv[i], hv[i + 1]) for i in range(len(hv) - 1)]                   # con lai, KHONG toi duoc tu 1
            cung = the_vi(n, ch, 0, 3)[::-1]                                        # (nhung tu do toi duoc n)
            ngoai = sorted(set(range(1, n + 1)) - set(hv))
            cung += vong_am(random.sample(ngoai, 8), -5)
            cung += [(random.choice(ngoai), random.choice(hv), random.randint(-100, 100)) for _ in range(300)]
            while len(cung) < 5000:
                i, j = random.sample(range(len(hv)), 2); cung.append((hv[i], hv[j], 10**4))
        if 2 < so < 7 or so in (8, 9):
            random.shuffle(cung)
        ghi('THUONGPHAT', so, f'{n} {len(cung)}\n' + dong(cung), dap_an_thuongphat(n, cung))

SINH = {'DAOCHIEU': sinh_daochieu, 'MIENPHI': sinh_mienphi, 'MOICAP': sinh_moicap,
        'GIAMGIA': sinh_giamgia, 'MOTUYEN': sinh_motuyen, 'THUONGPHAT': sinh_thuongphat}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        random.seed(bai + '-2026')
        SINH[bai]()
        print('Da sinh', bai)

main()
