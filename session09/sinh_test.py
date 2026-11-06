# SINH TEST cho 6 bai buoi 9 (Bieu dien do thi & BFS)
#   Tren lop : THANHPHO, LOTRINH, BIENSO        Ve nha: MAKHOA, DUONGTD, DEMNGAN
# Cau truc thu muc theo Themis: test/THANHPHO/Test01/THANHPHO.INP + THANHPHO.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau de kiem cheo:
#   THANHPHO BFS theo tang tu t, LOTRINH BFS theo tang (chi in so canh + mot duong, cham bang
#   kiem_tra.py), BIENSO BFS NGUOC tu B, MAKHOA BFS tren xau tu T, DUONGTD sap xep ke + BFS tu 1,
#   DEMNGAN QHD "keo" theo thu tu dist da sap xep.
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py                  -> sinh ca 6 bai (~20 giay)
#       python sinh_test.py BIENSO MAKHOA    -> chi sinh cac bai ke ten
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

# ---------------- cac kieu do thi dung chung ----------------
def ngau_nhien(n, m, don=True, co_huong=False):
    # m canh ngau nhien; don=True: khong canh lap (ca hai chieu voi vo huong), khong khuyen
    da = set(); E = []
    while len(E) < m:
        u, v = random.randint(1, n), random.randint(1, n)
        if u == v:
            continue
        k = (u, v) if co_huong else (min(u, v), max(u, v))
        if don and k in da:
            continue
        da.add(k); E.append((u, v))
    return E

def tron_nhan(n, E, giu=()):
    # doi ten dinh ngau nhien (giu nguyen cac dinh trong 'giu') va xao thu tu canh
    p = list(range(n + 1))
    tu_do = [x for x in range(1, n + 1) if x not in giu]
    q = tu_do[:]; random.shuffle(q)
    for a, b in zip(tu_do, q):
        p[a] = b
    E = [(p[u], p[v]) for u, v in E]
    random.shuffle(E)
    return E

def xich(n):                              # 1 - 2 - ... - n
    return [(i, i + 1) for i in range(1, n)]

def phan_tang(so_tang, rong, p=1.0):
    # dinh 1 -> tang 1..so_tang (moi tang 'rong' dinh) -> dinh n; noi tang ke nhau voi xac suat p
    tang = [[1]]; n = 1
    for _ in range(so_tang):
        tang.append(list(range(n + 1, n + rong + 1))); n += rong
    n += 1; tang.append([n])
    E = []
    for t in range(len(tang) - 1):
        for u in tang[t]:
            for v in tang[t + 1]:
                if p >= 1 or random.random() < p:
                    E.append((u, v))
    return n, E

def bfs_tang(n, ke, goc):
    dist = [-1] * (n + 1); dist[goc] = 0
    tang = [goc]; d = 0
    while tang:
        d += 1; moi = []
        for u in tang:
            for v in ke[u]:
                if dist[v] < 0:
                    dist[v] = d; moi.append(v)
        tang = moi
    return dist

def ke_vo_huong(n, E):
    ke = [[] for _ in range(n + 1)]
    for u, v in E:
        ke[u].append(v); ke[v].append(u)
    return ke

def in_canh(dau, E):
    return dau + '\n' + '\n'.join(f'{u} {v}' for u, v in E) + ('\n' if E else '')

# ---------------- THANHPHO ----------------
def sinh_thanhpho():
    for so in range(1, 11):
        if so == 1:
            n, E, s, t = 6, [(1, 2), (2, 3), (3, 6), (1, 4), (4, 5), (5, 6), (2, 5)], 1, 6
        elif so == 2:
            n, E, s, t = 5, [(1, 2), (2, 3), (4, 5)], 1, 5           # khong di duoc -> -1
        elif so == 3:
            n = 10; E = ngau_nhien(n, 20, don=False); s = t = 7      # s = t -> 0, co canh lap
        elif so == 4:
            n = 10; E = tron_nhan(n, xich(n) + ngau_nhien(n, 3)); s, t = 1, 10
        elif so == 5:
            n = 2000; E = ngau_nhien(n, 5000, don=False); s, t = 1, n
        elif so == 6:
            n = 2000; E = tron_nhan(n, xich(n), giu=(1, n)); s, t = 1, n   # duong dai 1999
        elif so == 7:
            n = 2000; E = ngau_nhien(1000, 2500) + [(u + 1000, v + 1000) for u, v in ngau_nhien(1000, 2500)]
            s, t = 3, 1500                                         # hai cum tach roi -> -1
        elif so == 8:
            n = 2 * 10**5; E = ngau_nhien(n, 2 * 10**5, don=False); s, t = random.randint(1, n), random.randint(1, n)
        elif so == 9:                                              # hinh sao: hang doi dai 1,9*10^5 ngay buoc dau
            n = 2 * 10**5; h = 19 * 10**4
            E = [(1, v) for v in range(2, h + 1)] + xich(n)[h - 1:] + ngau_nhien(h, 10**4)
            E = tron_nhan(n, E, giu=(1,)); s, t = 1, n
        else:
            n = 2 * 10**5; E = tron_nhan(n, [(random.randint(1, v - 1), v) for v in range(2, n + 1)]); s, t = 1, n   # cay ngau nhien
        ke = ke_vo_huong(n, E)
        if so == 8:                                                # s nam trong thanh phan lon
            s = max(range(1, n + 1), key=lambda v: len(ke[v]))
        if so >= 8:                                                # t = dinh xa nhat tu s
            d = bfs_tang(n, ke, s); t = max(range(1, n + 1), key=lambda v: d[v])
        dap = bfs_tang(n, ke, t)[s]                                # BFS tu t (nguoc lai)
        ghi('THANHPHO', so, in_canh(f'{n} {len(E)} {s} {t}', E), f'{dap}\n')

# ---------------- LOTRINH ----------------
def dap_an_lotrinh(n, E):
    ke = [[] for _ in range(n + 1)]
    for u, v in E:
        ke[u].append(v)
    dist = bfs_tang(n, ke, 1)
    if dist[n] < 0:
        return '-1\n'
    # truy vet: tu n tim mot dinh u co canh u -> v va dist[u] = dist[v] - 1
    vao = [[] for _ in range(n + 1)]
    for u, v in E:
        vao[v].append(u)
    duong = [n]; v = n
    while v != 1:
        v = next(u for u in vao[v] if dist[u] == dist[v] - 1)
        duong.append(v)
    return f'{dist[n]}\n' + ' '.join(map(str, duong[::-1])) + '\n'

def nguoc_chieu(n, m):
    # m canh chi di LUI (tu so lon ve so nho): khong tao loi tat cho xich 1 -> 2 -> ... -> n
    return [(max(u, v), min(u, v)) for u, v in ngau_nhien(n, m)]

def sinh_lotrinh():
    for so in range(1, 11):
        if so == 1:
            n, E = 6, [(1, 2), (2, 3), (3, 6), (1, 4), (4, 5), (5, 6), (6, 1), (2, 5)]
        elif so == 2:
            n, E = 4, [(1, 2), (3, 2), (4, 3)]                     # chi co duong 4 -> 1, khong co 1 -> 4
        elif so == 3:
            n, E = 1, []                                           # n = 1: k = 0, lo trinh "1"
        elif so == 4:
            n = 10; E = ngau_nhien(n, 25, co_huong=True)
        elif so == 5:
            n = 2000; E = ngau_nhien(n, 5000, co_huong=True)
        elif so == 6:
            n = 2000; E = tron_nhan(n, xich(n) + nguoc_chieu(n, 3000), giu=(1, n))   # chi co 1 duong dai 1999
        elif so == 7:
            n, E = phan_tang(40, 20, 0.3); E = tron_nhan(n, E, giu=(1, n))
        elif so == 8:
            n = 10**5; E = ngau_nhien(n, 2 * 10**5, co_huong=True)
        elif so == 9:                                              # chuoi 10^5 nut: truy vet de quy se vo
            n = 10**5; E = tron_nhan(n, xich(n) + nguoc_chieu(n, 10**5), giu=(1, n))
        else:
            n, E = phan_tang(800, 60, 0.05); E = tron_nhan(n, E, giu=(1, n))
        ghi('LOTRINH', so, in_canh(f'{n} {len(E)}', E), dap_an_lotrinh(n, E))

# ---------------- BIENSO ----------------
def dap_an_bienso(A, B, L=10**6):
    # BFS NGUOC tu B: y den tu y-1 (bam +1), y+1 (bam -1), y/2 neu y chan (bam x2)
    dist = [-1] * (L + 1); dist[B] = 0
    q = deque([B])
    while dist[A] < 0:
        y = q.popleft()
        tr = [y - 1, y + 1] + ([y // 2] if y % 2 == 0 else [])
        for x in tr:
            if 0 <= x <= L and dist[x] < 0:
                dist[x] = dist[y] + 1; q.append(x)
    return dist[A]

def sinh_bienso():
    bo = [(3, 10), (5, 5), (0, 20), (2, 19),
          (1, 1000), (999, 0), (37, 777),
          (0, 10**6), (10**6, 1), (12345, 999999)]
    for so, (A, B) in enumerate(bo, 1):
        ghi('BIENSO', so, f'{A} {B}\n', f'{dap_an_bienso(A, B)}\n')

# ---------------- MAKHOA ----------------
def dap_an_makhoa(n, S, T, cam):
    if T in cam:
        return -1
    dist = {T: 0}; q = deque([T])                              # BFS tren xau, bat dau tu T
    while q:
        x = q.popleft()
        if x == S:
            return dist[x]
        for i in range(n):
            c = int(x[i])
            for c2 in ((c + 1) % 10, (c + 9) % 10):
                y = x[:i] + str(c2) + x[i + 1:]
                if y not in cam and y not in dist:
                    dist[y] = dist[x] + 1; q.append(y)
    return -1

def ma(n):
    return ''.join(random.choice('0123456789') for _ in range(n))

def sinh_makhoa():
    for so in range(1, 11):
        if so == 1:
            n, S, T, cam = 2, '00', '19', ['09', '10']
        elif so == 2:
            n, S, T, cam = 2, '55', '55', ['54', '56']             # S = T -> 0
        elif so == 3:
            n, S, T = 2, '00', '55'
            cam = ['45', '65', '54', '56']                         # T bi vay kin -> -1
        elif so == 4:
            n, S, T, cam = 1, '0', '7', []                         # xoay xuong 3 nac
        elif so == 5:
            n, S, T = 4, '0000', '5555'; cam = list({ma(4) for _ in range(500)})
        elif so == 6:
            n, S, T = 3, '123', '987'; cam = ['987']               # T bi cam -> -1
        elif so == 7:
            n, S, T = 4, ma(4), ma(4); cam = list({ma(4) for _ in range(3000)} - {T})
        elif so == 8:
            n, S, T = 5, '00000', '55555'; cam = list({ma(5) for _ in range(20000)})
        elif so == 9:
            n, S, T = 5, ma(5), ma(5); cam = list({ma(5) for _ in range(5000)})
        else:                                                     # tuong vay quanh T, chua 1 khe
            n, S, T = 5, '00000', '45454'
            cam = set()
            for i in range(5):
                for dc in (1, 9):
                    c = (int(T[i]) + dc) % 10
                    cam.add(T[:i] + str(c) + T[i + 1:])
            khe = sorted(cam)[3]; cam.discard(khe)
            cam = list(cam | {ma(5) for _ in range(10000)})
        cam = [c for c in cam if c != S]
        random.shuffle(cam)
        dap = dap_an_makhoa(n, S, T, set(cam))
        ghi('MAKHOA', so, f'{n} {len(cam)}\n{S}\n{T}\n' + ''.join(c + '\n' for c in cam), f'{dap}\n')

# ---------------- DUONGTD ----------------
def dap_an_duongtd(n, E):
    ke = ke_vo_huong(n, E)
    for x in ke:
        x.sort()
    cha = [-1] * (n + 1); cha[1] = 0
    q = deque([1])
    while q:
        u = q.popleft()
        for v in ke[u]:
            if cha[v] < 0:
                cha[v] = u; q.append(v)
    if cha[n] < 0:
        return '-1\n'
    duong = []; v = n
    while v:
        duong.append(v); v = cha[v]
    return f'{len(duong) - 1}\n' + ' '.join(map(str, duong[::-1])) + '\n'

def sinh_duongtd():
    for so in range(1, 11):
        if so == 1:
            n, E = 6, [(1, 2), (1, 3), (2, 4), (3, 4), (2, 5), (4, 6), (5, 6), (3, 6)]
        elif so == 2:                                              # bay: 2 nho nhat nhung la ngo cut
            n, E = 5, [(1, 2), (1, 3), (3, 4), (4, 5)]
        elif so == 3:
            n, E = 6, [(1, 2), (2, 3), (4, 5), (5, 6)]             # -1
        elif so == 4:
            n = 10; E = tron_nhan(n, xich(n) + ngau_nhien(n, 4), giu=(1, n))
        elif so == 5:
            n, E = phan_tang(30, 30, 0.15); E = tron_nhan(n, E, giu=(1, n))
        elif so == 6:
            n = 2000; E = ngau_nhien(n, 3000)
        elif so == 7:                                              # nhieu ngo cut so nho o tang tren
            n0, E = phan_tang(40, 30, 0.1)
            n = n0 + 400                                           # 400 la treo vao dinh ngau nhien
            E += [(random.randint(1, n0 - 1), v) for v in range(n0 + 1, n + 1)]
            E = tron_nhan(n, doi_dich(n0, n, E), giu=(1, n))
        elif so == 8:
            n = 10**5; E = ngau_nhien(n, 2 * 10**5)
        elif so == 9:
            n, E = phan_tang(1000, 100, 0.02); E = tron_nhan(n, E, giu=(1, n))
        else:                                                     # luoi 300 x 333: rat nhieu duong hoa
            R, C = 300, 333; n = R * C
            E = []
            for i in range(R):
                for j in range(C):
                    x = i * C + j + 1
                    if j + 1 < C: E.append((x, x + 1))
                    if i + 1 < R: E.append((x, x + C))
            E = tron_nhan(n, E, giu=(1, n))
        ghi('DUONGTD', so, in_canh(f'{n} {len(E)}', E), dap_an_duongtd(n, E))

def doi_dich(dich_cu, n, E):
    # doi ten dinh dich_cu <-> n de dinh n van la dich
    f = lambda x: n if x == dich_cu else (dich_cu if x == n else x)
    return [(f(u), f(v)) for u, v in E]

# ---------------- DEMNGAN ----------------
def dap_an_demngan(n, E):
    ke = ke_vo_huong(n, E)
    dist = bfs_tang(n, ke, 1)
    if dist[n] < 0:
        return '-1 0\n'
    thu_tu = sorted((v for v in range(1, n + 1) if dist[v] >= 0), key=lambda v: dist[v])
    cnt = [0] * (n + 1); cnt[1] = 1
    for v in thu_tu[1:]:                                          # "keo": cong tu cac dinh tang truoc
        cnt[v] = sum(cnt[u] for u in ke[v] if dist[u] == dist[v] - 1) % MOD
    return f'{dist[n]} {cnt[n]}\n'

def sinh_demngan():
    for so in range(1, 11):
        if so == 1:
            n, E = 6, [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 6), (5, 6)]
        elif so == 2:
            n, E = 4, [(1, 2), (3, 4)]                             # -1 0
        elif so == 3:
            n, E = phan_tang(2, 4); E += [(2, 3), (3, 4), (6, 7)]  # canh cung tang
        elif so == 4:
            n = 10; E = ngau_nhien(n, 20)
        elif so == 5:
            n, E = phan_tang(60, 8); E = tron_nhan(n, E, giu=(1, n))   # 8^60: phai lay mod
        elif so == 6:
            n = 2000; E = ngau_nhien(n, 5000)
        elif so == 7:
            n, E = phan_tang(100, 12, 0.6)
            E += [(u, u + 1) for u in range(2, n - 1) if random.random() < 0.3]   # canh trong tang / giua tang
            E = list({(min(u, v), max(u, v)) for u, v in E}); E = tron_nhan(n, E, giu=(1, n))
        elif so == 8:
            n = 10**5; E = ngau_nhien(n, 2 * 10**5)
        elif so == 9:
            n, E = phan_tang(2000, 10); E = tron_nhan(n, E, giu=(1, n))  # 2*10^5 canh, 10^2000 duong
        else:
            n, E = phan_tang(400, 50, 0.08)
            E += ngau_nhien(n, 2 * 10**5 - len(E))
            E = list({(min(u, v), max(u, v)) for u, v in E}); E = tron_nhan(n, E, giu=(1, n))
        ghi('DEMNGAN', so, in_canh(f'{n} {len(E)}', E), dap_an_demngan(n, E))

SINH = {'THANHPHO': sinh_thanhpho, 'LOTRINH': sinh_lotrinh, 'BIENSO': sinh_bienso,
        'MAKHOA': sinh_makhoa, 'DUONGTD': sinh_duongtd, 'DEMNGAN': sinh_demngan}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        SINH[bai]()
        print('Da sinh', bai)

main()
