# SINH TEST cho 6 bai buoi 10 (DFS & lien thong)
#   Tren lop : LIENTHONG, CHUTRINH, HAIPHIA        Ve nha: NHOMBAN, HAIPHE, CHIADOI
# Cau truc thu muc theo Themis: test/LIENTHONG/Test01/LIENTHONG.INP + LIENTHONG.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau (loi giai mau dung DFS) de kiem cheo:
#   LIENTHONG, NHOMBAN dung DSU (hop nhat tap, se hoc buoi 15); CHUTRINH dung DSU + dem canh
#   (thanh phan k dinh co chu trinh <=> so canh >= k); HAIPHIA dung BFS va do chan le cua tang;
#   HAIPHE dung DSU co chan le; CHIADOI dung BFS + mang bit KHONG gom nhom (cham hon, chi de doi chieu).
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py                  -> sinh ca 6 bai (~30 giay)
#       python sinh_test.py HAIPHE CHIADOI   -> chi sinh cac bai ke ten
import os, random, sys
from collections import deque

random.seed(2026)
GOC = 'test'
MOD = 10**9 + 7

def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

def dang_do_thi(n, canh):
    return f'{n} {len(canh)}\n' + ''.join(f'{u} {v}\n' for u, v in canh)

# ---------------- cac kieu do thi ----------------
def tron(n, canh):
    # doi ten dinh ngau nhien + tron thu tu canh + dao chieu ngau nhien (de duong thang khong la 1-2-3...)
    p = list(range(1, n + 1)); random.shuffle(p); p = [0] + p
    c = [(p[u], p[v]) if random.random() < 0.5 else (p[v], p[u]) for u, v in canh]
    random.shuffle(c)
    return c

def ngau_nhien(n, m, don=True):
    # m canh ngau nhien; don=True: khong khuyen, khong canh lap
    if not don:
        return [(random.randint(1, n), random.randint(1, n)) for _ in range(m)]
    m = min(m, n * (n - 1) // 2)
    da = set(); c = []
    while len(c) < m:
        u, v = random.randint(1, n), random.randint(1, n)
        if u == v: continue
        k = (min(u, v), max(u, v))
        if k in da: continue
        da.add(k); c.append((u, v))
    return c

def cay(ds_dinh):
    # cay ngau nhien tren danh sach dinh: dinh thu i noi voi mot dinh dung truoc
    return [(ds_dinh[i], ds_dinh[random.randrange(max(0, i - 50) if random.random() < 0.5 else 0, i)])
            for i in range(1, len(ds_dinh))]

def rung(n, so_cay):
    # chia 1..n thanh so_cay khuc lien tiep, moi khuc mot cay
    so_cay = min(so_cay, n)
    cat = sorted(random.sample(range(2, n + 1), so_cay - 1)) if so_cay > 1 else []
    bien = [1] + cat + [n + 1]
    c = []
    for i in range(len(bien) - 1):
        c += cay(list(range(bien[i], bien[i + 1])))
    return c, bien

def duong(n):
    return [(i, i + 1) for i in range(1, n)]

def hai_phia(n, m, so_tp=1):
    # do thi hai phia ngau nhien: chia dinh thanh so_tp nhom, moi nhom co cay khung hai phia + canh cheo
    phia = [random.randint(0, 1) for _ in range(n + 1)]
    so_tp = min(so_tp, n)
    cat = sorted(random.sample(range(2, n + 1), so_tp - 1)) if so_tp > 1 else []
    bien = [1] + cat + [n + 1]
    da = set(); c = []
    def them(u, v):
        k = (min(u, v), max(u, v))
        if u != v and phia[u] != phia[v] and k not in da:
            da.add(k); c.append((u, v)); return True
        return False
    nhom = []
    for i in range(len(bien) - 1):
        ds = list(range(bien[i], bien[i + 1]))
        nhom.append(ds)
        for j in range(1, len(ds)):            # noi ds[j] voi mot dinh truoc khac phia (neu co)
            ung = [x for x in random.sample(ds[:j], min(j, 5)) if phia[x] != phia[ds[j]]]
            if ung: them(ds[j], ung[0])
    thu = 0
    while len(c) < m and thu < 20 * m:
        thu += 1
        g = random.choice(nhom)
        them(random.choice(g), random.choice(g))
    return c, phia

# ---------------- DSU (chi dung de tinh dap an) ----------------
def tao_dsu(n):
    return list(range(n + 1))

def tim(cha, x):
    r = x
    while cha[r] != r: r = cha[r]
    while cha[x] != r: cha[x], x = r, cha[x]
    return r

# ---------------- LIENTHONG ----------------
def dap_an_lienthong(n, canh):
    cha = tao_dsu(n)
    for u, v in canh:
        a, b = tim(cha, u), tim(cha, v)
        if a != b: cha[a] = b
    dem = {}
    for u in range(1, n + 1):
        r = tim(cha, u); dem[r] = dem.get(r, 0) + 1
    return f'{len(dem)} {max(dem.values())}\n'

def sinh_lienthong():
    for so in range(1, 11):
        if so == 1:
            n, canh = 7, [(1, 2), (2, 3), (4, 5), (6, 6), (5, 4)]   # vi du trong de
        elif so == 2:
            n, canh = 1, []
        elif so == 3:
            n = 1000; canh = ngau_nhien(n, 600, don=False)
        elif so == 4:
            n = 1000; canh = tron(n, rung(n, 7)[0])
        elif so == 5:
            n = 10**4; canh = ngau_nhien(n, 2 * 10**4, don=False)
        elif so == 6:
            n = 10**4; canh = ngau_nhien(n, 4000)                  # nhieu thanh phan nho
        elif so == 7:
            n = 10**4; canh = duong(n)                             # duong thang: bay de quy
        elif so == 8:
            n = 10**5; canh = ngau_nhien(n, 2 * 10**5, don=False)
        elif so == 9:
            n = 10**5; canh = tron(n, duong(n))                    # duong thang tron ten dinh
        else:
            n = 10**5; canh = tron(n, rung(n, 1000)[0]) + ngau_nhien(n, 10**5, don=False)
        ghi('LIENTHONG', so, dang_do_thi(n, canh), dap_an_lienthong(n, canh))

# ---------------- CHUTRINH ----------------
def dap_an_chutrinh(n, canh):
    cha = tao_dsu(n)
    for u, v in canh:
        a, b = tim(cha, u), tim(cha, v)
        if a != b: cha[a] = b
    so_dinh = {}; so_canh = {}
    for u in range(1, n + 1):
        r = tim(cha, u); so_dinh[r] = so_dinh.get(r, 0) + 1
    for u, v in canh:
        r = tim(cha, u); so_canh[r] = so_canh.get(r, 0) + 1
    return str(sum(1 for r in so_dinh if so_canh.get(r, 0) >= so_dinh[r])) + '\n'

def rung_co_chu_trinh(n, so_cay, ty_le):
    # rung so_cay cay, roi them 1-2 canh trong mot so cay (ty_le) de tao chu trinh
    c, bien = rung(n, so_cay)
    da = set((min(u, v), max(u, v)) for u, v in c)
    for i in range(len(bien) - 1):
        lo, hi = bien[i], bien[i + 1] - 1
        if hi - lo + 1 >= 3 and random.random() < ty_le:
            for _ in range(random.randint(1, 2)):
                u, v = random.randint(lo, hi), random.randint(lo, hi)
                k = (min(u, v), max(u, v))
                if u != v and k not in da:
                    da.add(k); c.append((u, v))
    return c

def sinh_chutrinh():
    for so in range(1, 11):
        if so == 1:
            n, canh = 8, [(1, 2), (2, 3), (3, 1), (3, 4), (5, 6), (7, 8), (8, 6), (6, 7)]
        elif so == 2:
            n, canh = 5, [(1, 2), (2, 3), (3, 4), (4, 5)]          # mot cay -> 0
        elif so == 3:
            n = 500; canh = tron(n, rung_co_chu_trinh(n, 40, 0.5))
        elif so == 4:
            n = 500; canh = ngau_nhien(n, 500)
        elif so == 5:
            n = 10**4; canh = tron(n, rung_co_chu_trinh(n, 300, 0.5))
        elif so == 6:
            n = 10**4; canh = tron(n, rung(n, 50)[0])               # rung -> 0
        elif so == 7:
            n = 10**4; canh = tron(n, duong(n) + [(1, n)])          # mot chu trinh dai 10^4
        elif so == 8:
            n = 10**5; canh = tron(n, rung_co_chu_trinh(n, 3000, 0.3))
        elif so == 9:
            n = 10**5; canh = ngau_nhien(n, 2 * 10**5)
        else:
            n = 10**5; canh = tron(n, rung_co_chu_trinh(n, 20000, 0.5))
        ghi('CHUTRINH', so, dang_do_thi(n, canh), dap_an_chutrinh(n, canh))

# ---------------- HAIPHIA ----------------
def dap_an_haiphia_mot(n, canh):
    # BFS: tang[v] = so canh it nhat tu goc. Hai phia <=> moi canh noi hai dinh khac chan le tang.
    ke = [[] for _ in range(n + 1)]
    for u, v in canh:
        ke[u].append(v); ke[v].append(u)
    tang = [-1] * (n + 1)
    for s in range(1, n + 1):
        if tang[s] != -1: continue
        tang[s] = 0; q = deque([s])
        while q:
            u = q.popleft()
            for v in ke[u]:
                if tang[v] == -1:
                    tang[v] = tang[u] + 1; q.append(v)
    return all((tang[u] - tang[v]) % 2 == 1 for u, v in canh)

def bo_haiphia(n, m, so_tp, pha):
    # pha = True: them mot canh noi hai dinh CUNG phia -> co chu trinh le
    canh, phia = hai_phia(n, m, so_tp)
    if pha and n >= 3:
        for _ in range(1000):
            u, v = random.randint(1, n), random.randint(1, n)
            if u != v and phia[u] == phia[v] and (u, v) not in canh and (v, u) not in canh:
                canh.append((u, v)); break
    return n, tron(n, canh)

def sinh_haiphia():
    for so in range(1, 11):
        bo = []
        if so == 1:
            bo = [(4, [(1, 2), (2, 3), (3, 4), (4, 1)]), (3, [(1, 2), (2, 3), (3, 1)]), (3, [])]
        elif so == 2:
            bo = [(1, []), (2, [(1, 2)]), (5, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])]
        elif so in (3, 4):
            for _ in range(10):
                n = random.randint(1, 15)
                bo.append(bo_haiphia(n, random.randint(0, 25), random.randint(1, 3), random.random() < 0.5))
        elif so in (5, 6):
            tong = 0
            while tong < 1800:
                n = random.randint(2, 200)
                bo.append(bo_haiphia(n, random.randint(n // 2, 2 * n), random.randint(1, 4), random.random() < 0.5))
                tong += n + len(bo[-1][1])
        elif so == 7:                          # bay quen reset: nhieu bo nho lien tiep
            for _ in range(300):
                n = random.randint(2, 4)
                bo.append(bo_haiphia(n, random.randint(1, 4), 1, random.random() < 0.3))
        elif so == 8:
            bo = [bo_haiphia(10**5, 2 * 10**5, 5, False)]
        elif so == 9:
            bo = [bo_haiphia(10**5, 2 * 10**5 - 1, 5, True)]
        else:                                  # chu trinh le DAI nhat: duong 1..n-1 va canh noi ve 1 (n le)
            n = 99999
            bo = [(n, tron(n, duong(n) + [(n, 1)])), bo_haiphia(10**5, 10**5 - 10, 3, False)]
        inp = [str(len(bo))]; out = []
        for n, canh in bo:
            inp.append(dang_do_thi(n, canh).rstrip('\n'))
            out.append('YES' if dap_an_haiphia_mot(n, canh) else 'NO')
        ghi('HAIPHIA', so, '\n'.join(inp) + '\n', '\n'.join(out) + '\n')

# ---------------- NHOMBAN ----------------
def dap_an_nhomban(n, canh):
    cha = tao_dsu(n)
    for u, v in canh:
        a, b = tim(cha, u), tim(cha, v)
        if a != b: cha[a] = b
    dem = {}
    for u in range(1, n + 1):
        r = tim(cha, u); dem[r] = dem.get(r, 0) + 1
    khac = 0; da_xet = 0
    for s in dem.values():                     # nhom moi ghep voi moi nguoi o cac nhom truoc
        khac += s * da_xet; da_xet += s
    return f'{len(dem)}\n{khac}\n'

def sinh_nhomban():
    for so in range(1, 11):
        if so == 1:
            n, canh = 6, [(1, 2), (2, 3), (4, 5)]
        elif so == 2:
            n, canh = 5, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]   # mot nhom -> 0 cap
        elif so == 3:
            n = 1000; canh = []                                    # khong ai quen ai
        elif so == 4:
            n = 1000; canh = ngau_nhien(n, 700)
        elif so == 5:
            n = 10**4; canh = ngau_nhien(n, 8000)
        elif so == 6:
            n = 10**4; canh = tron(n, rung(n, 30)[0])
        elif so == 7:
            n = 10**4; canh = tron(n, duong(n))
        elif so == 8:
            n = 10**5; canh = []                                   # dap an lon nhat ~5*10^9
        elif so == 9:
            n = 10**5; canh = ngau_nhien(n, 70000)
        else:
            n = 10**5; canh = tron(n, rung(n, 2)[0])                # hai nhom lon
        ghi('NHOMBAN', so, dang_do_thi(n, canh), dap_an_nhomban(n, canh))

# ---------------- HAIPHE ----------------
def dap_an_haiphe(n, rb):
    # DSU co chan le: lech[x] = phe[x] XOR phe[cha[x]]
    cha = list(range(n + 1)); lech = [0] * (n + 1)
    def tim_p(x):
        duong_di = []
        while cha[x] != x:
            duong_di.append(x); x = cha[x]
        r = x; acc = 0
        for y in reversed(duong_di):           # nen duong, tinh lech toi goc
            acc ^= lech[y]; lech[y] = acc; cha[y] = r
        return r
    c = n
    for u, v, t in rb:
        a, b = tim_p(u), tim_p(v)
        if a == b:
            if lech[u] ^ lech[v] != t: return '0\n'
        else:
            cha[a] = b; lech[a] = lech[u] ^ lech[v] ^ t; c -= 1
    return str(pow(2, c, MOD)) + '\n'

def bo_haiphe(n, m, so_tp, chi_khac, pha):
    phe = [random.randint(0, 1) for _ in range(n + 1)]
    so_tp = min(so_tp, n)
    cat = sorted(random.sample(range(2, n + 1), so_tp - 1)) if so_tp > 1 else []
    bien = [1] + cat + [n + 1]
    rb = []
    def them(u, v):
        t = phe[u] ^ phe[v]
        if chi_khac and t == 0: return
        rb.append((u, v, t))
    for i in range(len(bien) - 1):
        ds = list(range(bien[i], bien[i + 1]))
        for j in range(1, len(ds)):
            if chi_khac:
                ung = [x for x in random.sample(ds[:j], min(j, 5)) if phe[x] != phe[ds[j]]]
                if ung: them(ds[j], ung[0])
            else:
                them(ds[j], random.choice(ds[max(0, j - 30):j]))
    while len(rb) < m:
        i = random.randrange(len(bien) - 1)
        lo, hi = bien[i], bien[i + 1] - 1
        if hi > lo:
            u, v = random.sample(range(lo, hi + 1), 2); them(u, v)
        elif len(bien) == 2:
            break
    if pha and rb:
        if not chi_khac:                       # mau thuan truc tiep: lap lai mot cap voi t nguoc
            u, v, t = random.choice(rb)
            rb.append((u, v, 1 - t))
        else:                                  # chi t = 1: noi hai dinh CUNG phe trong cung thanh phan
            for _ in range(1000):
                i = random.randrange(len(bien) - 1)
                lo, hi = bien[i], bien[i + 1] - 1
                if hi - lo < 2: continue
                x, y = random.sample(range(lo, hi + 1), 2)
                if phe[x] == phe[y]:
                    rb.append((x, y, 1)); break
    p = list(range(1, n + 1)); random.shuffle(p); p = [0] + p
    rb = [(p[u], p[v], t) for u, v, t in rb]
    random.shuffle(rb)
    return n, rb

def sinh_haiphe():
    for so in range(1, 11):
        if so == 1:
            n, rb = 5, [(1, 2, 1), (2, 3, 0), (4, 5, 1)]
        elif so == 2:
            n, rb = 3, [(1, 2, 1), (2, 3, 1), (1, 3, 1)]           # chu trinh le -> 0
        elif so == 3:
            n, rb = bo_haiphe(15, 10, 6, False, False)
        elif so == 4:
            n, rb = bo_haiphe(15, 20, 2, False, True)
        elif so == 5:
            n, rb = bo_haiphe(10**5, 2 * 10**5, 100, True, False)
        elif so == 6:
            n, rb = bo_haiphe(10**5, 2 * 10**5, 3, True, True)
        elif so == 7:
            n, rb = bo_haiphe(10**5, 50000, 60000, True, False)    # nhieu thanh phan -> 2^c lon
        elif so == 8:
            n, rb = bo_haiphe(10**5, 2 * 10**5, 500, False, False)
        elif so == 9:
            n, rb = bo_haiphe(10**5, 2 * 10**5, 5, False, True)
        else:
            n, rb = bo_haiphe(10**5, 10**5, 40000, False, False)
        inp = f'{n} {len(rb)}\n' + ''.join(f'{u} {v} {t}\n' for u, v, t in rb)
        ghi('HAIPHE', so, inp, dap_an_haiphe(n, rb))

# ---------------- CHIADOI ----------------
def dap_an_chiadoi(n, canh):
    ke = [[] for _ in range(n + 1)]
    for u, v in canh:
        ke[u].append(v); ke[v].append(u)
    tang = [-1] * (n + 1); ds = []
    for s in range(1, n + 1):
        if tang[s] != -1: continue
        tang[s] = 0; q = deque([s]); dem = [0, 0]
        while q:
            u = q.popleft(); dem[tang[u] & 1] += 1
            for v in ke[u]:
                if tang[v] == -1:
                    tang[v] = tang[u] + 1; q.append(v)
                elif (tang[v] - tang[u]) % 2 == 0:
                    return '-1\n'
        ds.append(dem)
    # mang bit tren TONG SO NGUOI DOI 1 (khong dung chenh lech), moi thanh phan mot buoc
    bits = 1
    for a, b in ds:
        bits = (bits << a) | (bits << b)
    best = n
    for x in range(n + 1):
        if bits >> x & 1:
            best = min(best, abs(n - 2 * x))
    return str(best) + '\n'

def bo_chiadoi(n, m, so_tp, lech, pha):
    # lech = True: thanh phan co hai phia rat chenh (nhu hinh sao) -> dap an khac 0, 1
    canh, phia = hai_phia(n, m, so_tp) if not lech else (None, None)
    if lech:
        so_tp = min(so_tp, n)
        cat = sorted(random.sample(range(2, n + 1), so_tp - 1)) if so_tp > 1 else []
        bien = [1] + cat + [n + 1]
        canh = []
        phia = [0] * (n + 1)
        for i in range(len(bien) - 1):
            ds = list(range(bien[i], bien[i + 1]))
            k = max(1, len(ds) // random.randint(2, 12))  # k dinh "tam" phia 1, con lai phia 0
            for x in ds[:k]: phia[x] = 1
            tam = ds[:k]
            for x in ds[k:]: canh.append((x, random.choice(tam)))
            for x in tam[1:]:
                if len(ds) > k: canh.append((x, random.choice(ds[k:])))
    if pha:
        for _ in range(1000):
            u, v = random.randint(1, n), random.randint(1, n)
            if u != v and phia[u] == phia[v] and (u, v) not in canh and (v, u) not in canh:
                canh.append((u, v)); break
    return n, tron(n, canh)

def chiadoi_tu_tp(tp, m_them, pha=False):
    # tp = danh sach (a, b): thanh phan co a dinh phia trai, b dinh phia phai (a, b >= 0, a + b >= 1).
    # Them toi da m_them canh cheo (giua hai phia cua cung mot thanh phan).
    canh = []; da = set(); nhom = []; dinh = 1
    for a, b in tp:
        A = list(range(dinh, dinh + a)); B = list(range(dinh + a, dinh + a + b)); dinh += a + b
        nhom.append((A, B))
        if not A or not B: continue
        for x in A:                            # cay khung: moi dinh A noi B[0], moi dinh B khac noi mot dinh A
            canh.append((x, B[0])); da.add((min(x, B[0]), max(x, B[0])))
        for y in B[1:]:
            x = random.choice(A); canh.append((x, y)); da.add((min(x, y), max(x, y)))
    n = dinh - 1
    co_ca_hai = [g for g in nhom if g[0] and g[1]]
    thu = 0
    while m_them > 0 and co_ca_hai and thu < 5 * m_them + 100:
        thu += 1
        A, B = random.choice(co_ca_hai)
        x, y = random.choice(A), random.choice(B); k = (min(x, y), max(x, y))
        if k not in da: canh.append((x, y)); da.add(k); m_them -= 1
    if pha:                                    # canh trong CUNG mot phia -> chu trinh le
        A, B = max(nhom, key=lambda g: len(g[0]))
        x, y = random.sample(A, 2); canh.append((x, y))
    return n, tron(n, canh)

def sao_boi(k, so_tp, du_le):
    # so_tp thanh phan, chenh lech moi thanh phan la boi cua k; du_le=True -> D/k le -> dap an >= k
    while True:
        ds = [k * random.randint(1, 6) for _ in range(so_tp)]
        if (sum(ds) // k) % 2 == (1 if du_le else 0): break
    tp = []
    for d in ds:
        b = random.randint(1, 25); tp.append((b + d, b))
    return tp

def sinh_chiadoi():
    for so in range(1, 11):
        if so == 1:
            n, canh = 7, [(1, 2), (1, 3), (1, 4), (5, 6)]   # {1}|{2,3,4}, {5}|{6}, {7}: chenh lech 1
        elif so == 2:
            n, canh = 4, [(1, 2), (2, 3), (3, 1)]           # tam giac -> -1
        elif so == 3:
            n, canh = chiadoi_tu_tp([(5, 1), (3, 1), (1, 0), (2, 2)], 3)     # 15 dinh
        elif so == 4:
            n, canh = bo_chiadoi(14, 25, 3, False, True)
        elif so == 5:
            n, canh = chiadoi_tu_tp(sao_boi(6, 12, True), 500)              # dap an 6
        elif so == 6:
            n, canh = bo_chiadoi(2000, 4000, 300, True, False)
        elif so == 7:
            n, canh = chiadoi_tu_tp([(700, 100), (300, 250), (200, 150)] + [(1, 0)] * 50, 2000, pha=True)
        elif so == 8:                              # 1400 thanh phan, chenh lech boi 10, D/10 le
            n, canh = chiadoi_tu_tp(sao_boi(10, 1400, True), 10**5)
        elif so == 9:                              # rat nhieu thanh phan nho, nhieu dinh co lap
            n, canh = bo_chiadoi(10**5, 30000, 70000, True, False)
        else:                                      # mot thanh phan lech rat manh + nhieu thanh phan nho
            tp = [(60000, 1000)] + [(random.randint(1, 20), random.randint(0, 20)) for _ in range(1500)]
            n, canh = chiadoi_tu_tp(tp, 2 * 10**5 - 80000)
        ghi('CHIADOI', so, dang_do_thi(n, canh), dap_an_chiadoi(n, canh))

SINH = {'LIENTHONG': sinh_lienthong, 'CHUTRINH': sinh_chutrinh, 'HAIPHIA': sinh_haiphia,
        'NHOMBAN': sinh_nhomban, 'HAIPHE': sinh_haiphe, 'CHIADOI': sinh_chiadoi}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        SINH[bai]()
        print('Da sinh', bai)

main()
