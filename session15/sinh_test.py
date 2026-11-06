# SINH TEST cho 6 bai buoi 15 (DSU - Disjoint Set Union)
#   Tren lop : KETBAN, DEMNHOM, QUYNHOM        Ve nha: DAONOI, CATDIEN, SONHANG
# Cau truc thu muc theo Themis: test/KETBAN/Test01/KETBAN.INP + KETBAN.OUT
# Dap an tinh bang cach KHAC loi giai mau (loi giai mau dung DSU co nen duong + hop theo kich thuoc):
#   KETBAN, DEMNHOM, QUYNHOM, DAONOI, CATDIEN dung "nhan nhom + gop danh sach nho vao lon"
#   (moi phan tu doi nhan toi da log2(n) lan); SONHANG dung duong quet + heapq (lan son moi nhat
#   dang phu len coc i), khong dung DSU.
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py                -> sinh ca 6 bai (~25 giay)
#       python sinh_test.py KETBAN SONHANG  -> chi sinh cac bai ke ten
# Moi bai co seed rieng (random.seed('KETBAN-2026'), ...) nen sinh rieng mot bai hay ca bo deu ra CUNG test.
import os, random, sys, heapq

GOC = 'test'

def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

class Nhan:
    """Gan nhan nhom cho tung phan tu; gop thi doi nhan cua nhom NHO hon sang nhan nhom lon."""
    def __init__(self, n):
        self.nhan = list(range(n + 1))
        self.tv = [[x] for x in range(n + 1)]       # tv[l] = cac thanh vien cua nhom nhan l
    def gop(self, u, v):
        a, b = self.nhan[u], self.nhan[v]
        if a == b:
            return None
        if len(self.tv[a]) < len(self.tv[b]):
            a, b = b, a
        for x in self.tv[b]:
            self.nhan[x] = a
        self.tv[a] += self.tv[b]
        self.tv[b] = []
        return a, b                                  # a: nhan giu lai, b: nhan bi xoa

def cap(n):
    u, v = random.sample(range(1, n + 1), 2)
    return u, v

# ---------------- KETBAN ----------------
def dap_an_ketban(n, ds):
    g = Nhan(n); out = []
    for t, u, v in ds:
        if t == 1:
            g.gop(u, v)
        else:
            out.append('CO' if g.nhan[u] == g.nhan[v] else 'KHONG')
    return '\n'.join(out) + '\n'

def tron_ketban(n, q, ti_le_hop, k=None):
    """q thao tac, ti_le_hop phan la ket ban. k: chi ket ban trong k 'lop' (so du theo k) -> it nhom to."""
    ds = []
    for _ in range(q):
        if k:
            u = random.randint(1, n); v = random.randrange(u % k or k, n + 1, k) if n >= k else u
            if v < 1: v = u
        else:
            u, v = cap(n)
        ds.append((1 if random.random() < ti_le_hop else 2, u, v))
    return ds

def sinh_ketban():
    for so in range(1, 11):
        if so == 1:
            n, ds = 5, [(1, 1, 2), (2, 1, 3), (1, 2, 3), (2, 1, 3), (1, 4, 5), (2, 3, 5)]   # vi du
        elif so == 2:
            n, ds = 1, [(2, 1, 1), (1, 1, 1), (2, 1, 1)]                                  # u = v
        elif so == 3:
            n = 10; ds = tron_ketban(n, 30, 0.4)
        elif so == 4:
            n = 1000; ds = tron_ketban(n, 1000, 0.6)
        elif so == 5:                                                     # chuoi ngan cho ban ngay tho
            n = 5000; ds = [(1, 1, i) for i in range(2, 2501)] + tron_ketban(n, 2500, 0.2)
        elif so == 6:                                                     # nhom to roi hoi nhieu: giet BFS
            n = 5000; ds = [(1,) + cap(1500) for _ in range(2500)]
            ds += [(2, random.randint(1, 1500), random.randint(1, n)) for _ in range(2500)]
        elif so == 7:
            n = 5000; ds = tron_ketban(n, 5000, 0.3, k=7)
        elif so == 8:                                                     # chuoi dai: giet ban ngay tho
            n = 2 * 10**5
            ds = [(1, 1, i) for i in range(2, 10**5 + 2)]
            ds += [(2, random.randint(1, n), random.randint(1, 10**5)) for _ in range(10**5 - 1)]
            ds += [(2, 1, 10**5 + 1)]
        elif so == 9:
            n = 2 * 10**5; ds = tron_ketban(n, 2 * 10**5, 0.5)
        else:                                                             # chuoi 1-2-3-...: hoi tu dau chuoi
            n = 2 * 10**5
            ds = [(1, i, i + 1) for i in range(1, 10**5 + 1)] + tron_ketban(n, 5 * 10**4, 0.5, k=2)
            ds += [(2, 1, random.randint(1, n)) for _ in range(5 * 10**4)]
        inp = f'{n} {len(ds)}\n' + ''.join(f'{t} {u} {v}\n' for t, u, v in ds)
        ghi('KETBAN', so, inp, dap_an_ketban(n, ds))

# ---------------- DEMNHOM ----------------
def dap_an_demnhom(n, canh):
    g = Nhan(n); nhom, lon = n, 1; out = []
    for u, v in canh:
        r = g.gop(u, v)
        if r:
            nhom -= 1; lon = max(lon, len(g.tv[r[0]]))
        out.append(f'{nhom} {lon}')
    return '\n'.join(out) + '\n'

def cay_ngau_nhien(n):
    hv = list(range(1, n + 1)); random.shuffle(hv)
    canh = [(hv[i], hv[random.randrange(i)]) for i in range(1, n)]
    random.shuffle(canh)
    return canh

def sinh_demnhom():
    for so in range(1, 11):
        if so == 1:
            n, canh = 6, [(1, 2), (3, 4), (2, 3), (1, 4), (5, 6), (4, 6)]        # vi du
        elif so == 2:
            n, canh = 1000, [cap(1000) for _ in range(1)]
        elif so == 3:
            n = 10; canh = [cap(n) for _ in range(20)]
        elif so == 4:
            n = 1000; canh = [cap(n) for _ in range(1000)]
        elif so == 5:
            n = 2000; canh = cay_ngau_nhien(n)[:1999]
        elif so == 6:
            n = 2000; canh = [cap(n) for _ in range(2000)]
        elif so == 7:                                                          # duong 1-2-...-n
            n = 2000; canh = [(i, i + 1) for i in range(1, n)] + [(1, n)]
        elif so == 8:
            n = 2 * 10**5; canh = cay_ngau_nhien(n) + [cap(n)]
        elif so == 9:
            n = 2 * 10**5; canh = [cap(n) for _ in range(2 * 10**5)]
        else:                                                                  # nhieu cau thua
            n = 2 * 10**5; c = cay_ngau_nhien(10**5); canh = c + c[:10**5 + 1]; random.shuffle(canh)
        inp = f'{n} {len(canh)}\n' + ''.join(f'{u} {v}\n' for u, v in canh)
        ghi('DEMNHOM', so, inp, dap_an_demnhom(n, canh))

# ---------------- QUYNHOM ----------------
def dap_an_quynhom(n, a, ds):
    g = Nhan(n); tong = [0] + a[:]; out = []           # tong theo NHAN
    for op in ds:
        if op[0] == 1:
            r = g.gop(op[1], op[2])
            if r:
                tong[r[0]] += tong[r[1]]; tong[r[1]] = 0
        elif op[0] == 2:
            tong[g.nhan[op[1]]] += op[2]
        else:
            out.append(str(tong[g.nhan[op[1]]]))
    return '\n'.join(out) + '\n'

def tron_quynhom(n, q, p1, p2, gmax=10**9, khong_lap=False):
    ds = []; g = Nhan(n) if khong_lap else None
    while len(ds) < q:
        r = random.random()
        if r < p1:
            u, v = cap(n)
            if khong_lap:
                if g.nhan[u] == g.nhan[v]:
                    continue
                g.gop(u, v)
            ds.append((1, u, v))
        elif r < p1 + p2:
            ds.append((2, random.randint(1, n), random.randint(1, gmax)))
        else:
            ds.append((3, random.randint(1, n)))
    return ds

def sinh_quynhom():
    for so in range(1, 11):
        if so == 1:
            n, a = 4, [5, 3, 2, 7]
            ds = [(1, 1, 2), (3, 2), (2, 3, 10), (1, 3, 4), (3, 4), (1, 2, 4), (3, 1)]  # vi du
        else:
            n, q, gmax = [None, None, (8, 30, 9), (1000, 1000, 10**9), (1000, 1000, 10**9),
                          (5000, 5000, 10**9), (5000, 5000, 10**9), (5000, 5000, 10**9),
                          (2 * 10**5,) * 2 + (10**9,), (2 * 10**5,) * 2 + (10**9,),
                          (2 * 10**5,) * 2 + (10**9,)][so]
            a = [random.randint(0, gmax) for _ in range(n)]
            if so == 3:
                ds = tron_quynhom(n, q, 0.3, 0.3, gmax)
            elif so == 4:                                                    # khong gop lap: ban sai van dung
                ds = tron_quynhom(n, q, 0.3, 0.3, gmax, khong_lap=True)
            elif so == 5:
                ds = tron_quynhom(n, q, 0.7, 0.1, gmax)
            elif so == 6:                                                    # nhom to roi hoi lien tuc
                ds = [(1,) + cap(1500) for _ in range(2500)]
                ds += [(3, random.randint(1, 1500)) if random.random() < 0.8 else
                       (2, random.randint(1, n), random.randint(1, gmax)) for _ in range(2500)]
            elif so == 7:
                ds = tron_quynhom(n, q, 0.3, 0.3, gmax, khong_lap=True)
            elif so == 8:
                ds = tron_quynhom(n, q, 0.4, 0.3, gmax)
            elif so == 9:                                                    # chuoi gop vao nguoi 1
                ds = [(1, 1, i) for i in range(2, 10**5 + 2)]
                ds += [random.choice([(2, random.randint(1, n), gmax), (3, random.randint(1, n))])
                       for _ in range(10**5 - 1)]
            else:                                                            # nhieu lan gop hai ban da cung nhom
                ds = tron_quynhom(n, q, 0.8, 0.1, gmax)
        inp = (f'{n} {len(ds)}\n' + ' '.join(map(str, a)) + '\n'
               + ''.join(' '.join(map(str, op)) + '\n' for op in ds))
        ghi('QUYNHOM', so, inp, dap_an_quynhom(n, a, ds))

# ---------------- DAONOI ----------------
def dap_an_daonoi(R, C, ds):
    g = Nhan(R * C); dat = bytearray(R * C + 1); dao = 0; out = []
    for i, j in ds:
        p = (i - 1) * C + j                                   # danh so 1..R*C
        if not dat[p]:
            dat[p] = 1; dao += 1
            ke = []
            if i > 1: ke.append(p - C)
            if i < R: ke.append(p + C)
            if j > 1: ke.append(p - 1)
            if j < C: ke.append(p + 1)
            for v in ke:
                if dat[v] and g.gop(p, v):
                    dao -= 1
        out.append(str(dao))
    return '\n'.join(out) + '\n'

def sinh_daonoi():
    for so in range(1, 11):
        if so == 1:
            R, C, ds = 3, 3, [(1, 1), (1, 3), (2, 2), (1, 2), (3, 3), (2, 3), (2, 3)]   # vi du
        elif so == 2:
            R, C = 1, 20; ds = [(1, j) for j in random.sample(range(1, 21), 20)]
        elif so == 3:
            R, C = 20, 20; ds = [(random.randint(1, R), random.randint(1, C)) for _ in range(200)]
        elif so == 4:                                                     # ban co: dao roi rac roi noi
            R, C = 20, 20
            ds = [(i, j) for i in range(1, 21) for j in range(1, 21) if (i + j) % 2 == 0][:150]
            ds += [(random.randint(1, R), random.randint(1, C)) for _ in range(50)]
        elif so in (5, 6, 7):
            R, C = [(300, 300), (1, 1000), (1000, 1000)][so - 5]
            ds = [(random.randint(1, R), random.randint(1, C)) for _ in range(2000)]
        elif so == 8:
            R, C = 1000, 1000
            ds = [(random.randint(1, R), random.randint(1, C)) for _ in range(2 * 10**5)]
        elif so == 9:                                                     # ran: cot chan day, noi dau xen ke
            R, C = 1000, 1000; ds = []
            for j in range(1, C + 1, 2):
                ds += [(i, j) for i in range(1, 101)]
            ds = ds[:10**5]
            ds += [(1 if (j // 2) % 2 == 0 else 100, j) for j in range(2, C + 1, 2)]
            ds += [(random.randint(1, R), random.randint(1, C)) for _ in range(2 * 10**5 - len(ds))]
        else:                                                             # tap trung 400x400 -> nhieu hop
            R, C = 1000, 1000
            ds = [(random.randint(301, 700), random.randint(301, 700)) for _ in range(2 * 10**5)]
        inp = f'{R} {C} {len(ds)}\n' + ''.join(f'{i} {j}\n' for i, j in ds)
        ghi('DAONOI', so, inp, dap_an_daonoi(R, C, ds))

# ---------------- CATDIEN ----------------
def dap_an_catdien(n, canh, cat):
    bi = set(cat); g = Nhan(n); vung = n
    for e, (u, v) in enumerate(canh):
        if e not in bi and g.gop(u, v):
            vung -= 1
    kq = []
    for e in reversed(cat):
        kq.append(vung)
        u, v = canh[e]
        if g.gop(u, v):
            vung -= 1
    return '\n'.join(map(str, reversed(kq))) + '\n'

def sinh_catdien():
    for so in range(1, 11):
        if so == 1:
            n = 5; canh = [(1, 2), (2, 3), (3, 1), (3, 4), (4, 5)]; cat = [2, 4, 1, 3]        # 1-based
        else:
            n, m, q = [None, None, (8, 10, 5), (100, 100, 100), (100, 300, 100), (2000, 2000, 1000),
                       (1000, 2000, 1000), (2000, 2000, 1000), (10**5,) * 3,
                       (10**5, 10**5, 5 * 10**4), (5 * 10**4, 10**5, 10**5)][so]
            if so in (5, 8):                                              # cay: cat canh nao cung tach
                canh = cay_ngau_nhien(n) + [cap(n)]
                canh = canh[:m]
            else:
                canh = [cap(n) for _ in range(m)]
            cat = [e + 1 for e in random.sample(range(m), q)]
        inp = (f'{n} {len(canh)} {len(cat)}\n' + ''.join(f'{u} {v}\n' for u, v in canh)
               + ''.join(f'{e}\n' for e in cat))
        ghi('CATDIEN', so, inp, dap_an_catdien(n, canh, [e - 1 for e in cat]))

# ---------------- SONHANG ----------------
def dap_an_sonhang(n, ds):
    bat_dau = [[] for _ in range(n + 2)]
    for idx, (l, r, c) in enumerate(ds):
        bat_dau[l].append(idx)
    h = []; kq = []
    for i in range(1, n + 1):
        for idx in bat_dau[i]:
            heapq.heappush(h, -idx)                   # lan son moi nhat o dinh heap
        while h and ds[-h[0]][1] < i:                 # doan da het truoc coc i -> bo
            heapq.heappop(h)
        kq.append(str(ds[-h[0]][2]) if h else '0')
    return ' '.join(kq) + '\n'

def doan(n, dmax):
    l = random.randint(1, n); r = min(n, l + random.randint(0, dmax - 1))
    return l, r, random.randint(1, 10**9)

def sinh_sonhang():
    for so in range(1, 11):
        if so == 1:
            n, ds = 8, [(2, 6, 4), (1, 3, 7), (5, 5, 9)]                                 # vi du
        elif so == 2:
            n, ds = 10, [doan(10, 10) for _ in range(6)]
        elif so == 3:
            n = 1000; ds = [doan(n, 1000) for _ in range(1000)]
        elif so == 4:
            n = 1000; ds = [doan(n, 3) for _ in range(300)]                 # nhieu coc chua son
        elif so == 5:
            n = 3 * 10**5; ds = [doan(n, 100) for _ in range(2 * 10**5)]     # tong do dai <= 2*10^7
        elif so == 6:
            n = 3 * 10**5; ds = [doan(n, 20) for _ in range(2 * 10**5)]
        elif so == 7:
            n = 3 * 10**5; ds = [(1, n, 5)] + [doan(n, 50) for _ in range(10**5)]
        elif so == 8:
            n = 3 * 10**5; ds = [doan(n, n) for _ in range(2 * 10**5)]
        elif so == 9:                                                       # doan lon dan, toan bo hang rao
            n = 3 * 10**5; ds = [(1, n, random.randint(1, 10**9)) for _ in range(2 * 10**5)]
        else:                                                               # doan ngan cuoi, doan dai truoc
            n = 3 * 10**5
            ds = [doan(n, n) for _ in range(10**5)] + [doan(n, 5) for _ in range(10**5)]
        inp = f'{n} {len(ds)}\n' + ''.join(f'{l} {r} {c}\n' for l, r, c in ds)
        ghi('SONHANG', so, inp, dap_an_sonhang(n, ds))

SINH = {'KETBAN': sinh_ketban, 'DEMNHOM': sinh_demnhom, 'QUYNHOM': sinh_quynhom,
        'DAONOI': sinh_daonoi, 'CATDIEN': sinh_catdien, 'SONHANG': sinh_sonhang}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        random.seed(bai + '-2026')
        SINH[bai]()
        print('Da sinh', bai)

main()
