# SINH TEST cho 6 bai buoi 12 (Sap xep to-po)
#   Tren lop : MONHOC, CHUTRINH, SOHOCKY        Ve nha: CONGVIEC, TUDIEN, DINHHUONG
# Cau truc thu muc theo Themis: test/MONHOC/Test01/MONHOC.INP + MONHOC.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau (loi giai mau dung Kahn):
#   to-po bang DFS 3 mau khong de quy (thu tu hau tu dao nguoc), SOHOCKY va CONGVIEC lam QHD theo thu
#   tu DFS, CONGVIEC dem viec gang bang "duong dai nhat qua v = dau[v] + duoi[v] - t[v] == T",
#   TUDIEN chon tham chu nho nhat khong con cung vao bang cach quet lai O(26^2).
# MONHOC, CHUTRINH, DINHHUONG co nhieu dap an: file .OUT la MOT dap an dung, cham bang kiem_tra.py.
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py                -> sinh ca 6 bai (~20 giay)
#       python sinh_test.py MONHOC TUDIEN  -> chi sinh cac bai ke ten
# Moi bai co seed rieng (random.seed('MONHOC-2026'), ...) nen sinh rieng mot bai hay ca bo deu ra CUNG test.
import os, random, sys

GOC = 'test'

def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

def de_canh(n, canh, giua=''):
    return f'{n} {len(canh)}\n' + giua + ''.join(f'{u} {v}\n' for u, v in canh)

def dag(n, m, xich=False, lap=False):
    """m cung ngau nhien di "tien" theo mot hoan vi bi mat -> chac chan khong chu trinh.
    xich=True: co san duong di qua MOI dinh (do sau n). lap=True: cho phep cung trung."""
    hv = list(range(1, n + 1)); random.shuffle(hv)
    canh = [(hv[i], hv[i + 1]) for i in range(n - 1)] if xich else []
    da = set(canh)
    while len(canh) < m:
        i, j = random.sample(range(n), 2)
        if i > j: i, j = j, i
        e = (hv[i], hv[j])
        if lap or e not in da:
            da.add(e); canh.append(e)
    random.shuffle(canh)
    return canh, hv

def ke_va_bac(n, canh):
    adj = [[] for _ in range(n + 1)]
    for u, v in canh:
        adj[u].append(v)
    return adj

def dfs_topo(n, canh):
    """DFS 3 mau khong de quy. Tra ve (thu_tu_to_po, None) hoac (None, chu_trinh)."""
    adj = ke_va_bac(n, canh)
    mau = [0] * (n + 1)
    hau = []
    for s in range(1, n + 1):
        if mau[s]:
            continue
        st = [[s, 0]]; mau[s] = 1
        while st:
            top = st[-1]; u = top[0]
            if top[1] < len(adj[u]):
                v = adj[u][top[1]]; top[1] += 1
                if mau[v] == 0:
                    mau[v] = 1; st.append([v, 0])
                elif mau[v] == 1:
                    dinh = [x[0] for x in st]
                    return None, dinh[dinh.index(v):]
            else:
                mau[u] = 2; hau.append(u); st.pop()
    return hau[::-1], None

# ---------------- MONHOC ----------------
def dap_an_monhoc(n, canh):
    tt, ct = dfs_topo(n, canh)
    return '-1\n' if tt is None else ' '.join(map(str, tt)) + '\n'

def sinh_monhoc():
    for so in range(1, 11):
        if so == 1:
            n, canh = 5, [(1, 3), (2, 3), (3, 4), (3, 5), (2, 5)]       # vi du trong de
        elif so == 2:
            n, canh = 3, [(1, 2), (2, 3), (3, 1)]                       # vong 3 mon
        elif so == 3:
            n = 8; canh, _ = dag(n, 12)
        elif so == 4:                                                    # mon tien quyet cua chinh no
            n = 8; canh, _ = dag(n, 10); canh.append((5, 5)); random.shuffle(canh)
        elif so == 5:
            n = 1000; canh, _ = dag(n, 5000)
        elif so == 6:                                                    # DAG + 1 cung nguoc: vong dai
            n = 1000; canh, hv = dag(n, 4000, xich=True); canh.append((hv[900], hv[100]))
        elif so == 7:
            n, canh = 1000, []                                           # khong rang buoc nao
        elif so == 8:
            n = 2 * 10**5; canh, _ = dag(n, 2 * 10**5, xich=True)        # do sau 2*10^5
        elif so == 9:
            n = 2 * 10**5; canh, _ = dag(n, 2 * 10**5, lap=True)
        else:                                                            # vong 199 999 mon an trong DAG
            n = 2 * 10**5; canh, hv = dag(n, 2 * 10**5 - 1, xich=True); canh.append((hv[-1], hv[1]))
        ghi('MONHOC', so, de_canh(n, canh), dap_an_monhoc(n, canh))

# ---------------- CHUTRINH ----------------
def dap_an_chutrinh(n, canh):
    tt, ct = dfs_topo(n, canh)
    return '-1\n' if ct is None else f'{len(ct)}\n' + ' '.join(map(str, ct)) + '\n'

def sinh_chutrinh():
    for so in range(1, 11):
        if so == 1:
            n, canh = 5, [(1, 2), (2, 3), (3, 4), (4, 2), (4, 5), (1, 5)]   # vi du: 2 3 4
        elif so == 2:
            n = 8; canh, _ = dag(n, 15)
        elif so == 3:                                                     # chi co khuyen 6 -> 6
            n = 8; canh, _ = dag(n, 10); canh.append((6, 6)); random.shuffle(canh)
        elif so == 4:
            n = 8; canh = [tuple(random.sample(range(1, n + 1), 2)) for _ in range(12)]
        elif so == 5:
            n = 1000; canh, _ = dag(n, 3000)
        elif so == 6:
            n = 1000; canh, hv = dag(n, 3000, xich=True); canh.append((hv[999], hv[0]))
        elif so == 7:
            n = 1000; canh = [tuple(random.sample(range(1, n + 1), 2)) for _ in range(3000)]
        elif so == 8:
            n = 2 * 10**5; canh, _ = dag(n, 2 * 10**5, xich=True)        # khong vong, sau 2*10^5
        elif so == 9:                                                     # mot vong qua MOI dinh
            n = 2 * 10**5; canh, hv = dag(n, 2 * 10**5 - 1, xich=True); canh.append((hv[-1], hv[0]))
        else:                                                             # vong 2 dinh o cuoi xich dai
            n = 2 * 10**5; canh, hv = dag(n, 2 * 10**5 - 1, xich=True); canh.append((hv[-1], hv[-2]))
        ghi('CHUTRINH', so, de_canh(n, canh), dap_an_chutrinh(n, canh))

# ---------------- SOHOCKY ----------------
def dap_an_sohocky(n, canh):
    tt, ct = dfs_topo(n, canh)
    if tt is None:
        return '-1\n'
    adj = ke_va_bac(n, canh)
    g = [1] * (n + 1)                       # g[u] = so mon tren chuoi dai nhat BAT DAU tu u
    for u in reversed(tt):                  # duyet nguoc: cac mon sau u da tinh xong
        for v in adj[u]:
            if g[v] + 1 > g[u]:
                g[u] = g[v] + 1
    return str(max(g[1:])) + '\n'

def sinh_sohocky():
    for so in range(1, 11):
        if so == 1:
            n, canh = 6, [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (6, 5)]   # vi du: 4
        elif so == 2:
            n, canh = 5, []                                              # 1 ky la xong
        elif so == 3:
            n = 8; canh, hv = dag(n, 10); canh.append((hv[7], hv[0]))
        elif so == 4:
            n = 8; canh, _ = dag(n, 14)
        elif so == 5:
            n = 1000; canh, _ = dag(n, 2000)
        elif so == 6:
            n = 1000; canh, _ = dag(n, 1999, xich=True)                   # 1000 ky
        elif so == 7:
            n = 1000; canh, hv = dag(n, 1999); canh.append((hv[999], hv[0]))
        elif so == 8:
            n = 2 * 10**5; canh, _ = dag(n, 2 * 10**5 - 1, xich=True)     # 2*10^5 ky: mo phong chet
        elif so == 9:
            n = 2 * 10**5; canh, _ = dag(n, 2 * 10**5, lap=True)
        else:                                                            # xich 5*10^4 + nhieu canh tat
            n = 2 * 10**5; m = 2 * 10**5
            hv = list(range(1, n + 1)); random.shuffle(hv)
            canh = [(hv[i], hv[i + 1]) for i in range(50000)]
            while len(canh) < m:
                i = random.randrange(n - 3); j = i + random.randint(1, 3)
                canh.append((hv[i], hv[j]))
            random.shuffle(canh)
        ghi('SOHOCKY', so, de_canh(n, canh), dap_an_sohocky(n, canh))

# ---------------- CONGVIEC ----------------
def dap_an_congviec(n, t, canh):
    tt, ct = dfs_topo(n, canh)
    if tt is None:
        return '-1\n'
    adj = ke_va_bac(n, canh)
    nguoc = ke_va_bac(n, [(v, u) for u, v in canh])
    dau = [0] * (n + 1)                     # dau[v] = duong dai nhat KET THUC tai v (tinh ca t[v])
    for v in tt:
        dau[v] = t[v] + max((dau[u] for u in nguoc[v]), default=0)
    duoi = [0] * (n + 1)                    # duoi[v] = duong dai nhat BAT DAU tai v
    for v in reversed(tt):
        duoi[v] = t[v] + max((duoi[w] for w in adj[v]), default=0)
    T = max(dau[1:])
    gang = sum(1 for v in range(1, n + 1) if dau[v] + duoi[v] - t[v] == T)
    return f'{T} {gang}\n'

def sinh_congviec():
    for so in range(1, 11):
        if so == 1:
            n, t, canh = 5, [3, 2, 4, 1, 2], [(1, 3), (2, 3), (3, 4), (2, 5)]   # vi du: 8 3
        elif so == 2:
            n, t, canh = 6, [4, 7, 2, 7, 1, 7], []                   # khong rang buoc: 3 viec dai nhat
        elif so == 3:
            n = 6; t = [random.randint(1, 9) for _ in range(n)]
            canh, hv = dag(n, 7); canh.append((hv[5], hv[2]))
        elif so == 4:
            n = 10; t = [random.randint(1, 5) for _ in range(n)]; canh, _ = dag(n, 15)
        elif so == 5:                                                 # t nho -> rat nhieu duong gang
            n = 2000; t = [random.randint(1, 3) for _ in range(n)]; canh, _ = dag(n, 2000)
        elif so == 6:                                                 # chia lop, moi viec 1-2 ngay
            n = 2000; t = [random.randint(1, 2) for _ in range(n)]; L = 40
            canh = [(i, j) for i in range(1, n + 1 - L) for j in (i + L,)]
            canh += [(i, i + L + 1) for i in range(1, n - L, 3)]
        elif so == 7:
            n = 2000; t = [random.randint(1, 10**6) for _ in range(n)]
            canh, hv = dag(n, 1999); canh.append((hv[1500], hv[3]))
        elif so == 8:
            n = 10**5; t = [random.randint(1, 10**6) for _ in range(n)]
            canh, _ = dag(n, 10**5)
        elif so == 9:                                                 # xich qua moi viec: tat ca gang
            n = 10**5; t = [random.randint(1, 10**6) for _ in range(n)]
            canh, _ = dag(n, 10**5, xich=True)
        else:                                                         # t chi 1..2 -> nhieu hoa
            n = 10**5; t = [random.randint(1, 2) for _ in range(n)]
            hv = list(range(1, n + 1)); random.shuffle(hv)
            canh = []
            while len(canh) < 10**5:
                i = random.randrange(n - 5); canh.append((hv[i], hv[i + random.randint(1, 5)]))
            random.shuffle(canh)
        tt = [0] + t
        giua = ' '.join(map(str, t)) + '\n'
        ghi('CONGVIEC', so, de_canh(n, canh, giua), dap_an_congviec(n, tt, canh))

# ---------------- TUDIEN ----------------
def dap_an_tudien(w):
    chu = sorted(set(''.join(w)))
    vao = {c: set() for c in chu}           # vao[c] = cac chu phai dung TRUOC c
    for a, b in zip(w, w[1:]):
        k = 0
        while k < len(a) and k < len(b) and a[k] == b[k]:
            k += 1
        if k < len(a) and k < len(b):
            vao[b[k]].add(a[k])
        elif len(a) > len(b):
            return '-1\n'
    kq = []
    con = set(chu)
    while con:                               # quet lai: chu nho nhat khong con chu nao phai truoc
        c = next((c for c in sorted(con) if not (vao[c] & con)), None)
        if c is None:
            return '-1\n'
        kq.append(c); con.remove(c)
    return ''.join(kq) + '\n'

def tu_theo(hv, n, dai_min, dai_max, chu):
    """n tu ngau nhien tren tap chu 'chu', sap xep theo bang chu cai bi mat hv."""
    hang = {c: i for i, c in enumerate(hv)}
    w = [''.join(random.choice(chu) for _ in range(random.randint(dai_min, dai_max))) for _ in range(n)]
    w.sort(key=lambda x: [hang[c] for c in x])
    return w

def sinh_tudien():
    abc = 'abcdefghijklmnopqrstuvwxyz'
    for so in range(1, 11):
        if so == 1:
            w = ['baa', 'abcd', 'abca', 'cab', 'cad']                  # vi du
        elif so == 2:
            w = ['xyz', 'xy']                                          # tu dai dung truoc tien to -> -1
        elif so == 3:
            w = ['ab', 'ba', 'ca', 'cb', 'ac']                         # a < b, b < c, c < a -> -1
        elif so == 4:
            chu = random.sample(abc, 6); hv = chu[:]; random.shuffle(hv)
            w = tu_theo(hv, 100, 1, 5, chu)
        elif so == 5:                                                  # it tu -> it rang buoc, nhieu chu "tu do"
            hv = list(abc); random.shuffle(hv)
            w = tu_theo(hv, 30, 1, 8, abc)
        elif so == 6:
            w = ['zebra'] * 1000                                       # khong cung nao: in a..z co mat
        elif so == 7:                                                  # chi doi 1 cap tu -> mau thuan
            hv = list(abc); random.shuffle(hv)
            w = tu_theo(hv, 1000, 1, 8, abc)
            i = next(i for i in range(999) if w[i][0] != w[i + 1][0] and len(set(w[i][0] + w[i + 1][0])) == 2)
            w[i], w[i + 1] = w[i + 1], w[i]
        elif so == 8:
            hv = list(abc); random.shuffle(hv)
            w = tu_theo(hv, 10**5, 1, 18, abc)
        elif so == 9:                                                  # chi 6 chu dau tu co rang buoc
            dau = random.sample(abc, 6)
            duoi = {c: ''.join(random.sample(abc, 9)) for c in dau}   # moi chu dau mot duoi co dinh
            w = sorted((random.choice(dau) for _ in range(10**5)), key=dau.index)
            w = [c + duoi[c] for c in w]
        else:                                                          # 2 tu dai 5*10^5, chi khac o cuoi
            chu = random.sample(abc, 20)
            goc = ''.join(random.choice(chu) for _ in range(499999))
            w = [goc + 'q', goc + 'e']
        ghi('TUDIEN', so, f'{len(w)}\n' + '\n'.join(w) + '\n', dap_an_tudien(w))

# ---------------- DINHHUONG ----------------
def dap_an_dinhhuong(n, ds):
    co = [(u, v) for t, u, v in ds if t == 1]
    tt, ct = dfs_topo(n, co)
    if tt is None:
        return '-1\n'
    vt = [0] * (n + 1)
    for i, u in enumerate(tt):
        vt[u] = i
    return ''.join('0' if vt[u] < vt[v] else '1' for t, u, v in ds if t == 0) + '\n'

def tron(canh, ti_le_vo):
    """Bien mot phan cung thanh canh vo huong (dao chieu ngau nhien de khong lo thu tu)."""
    ds = []
    for u, v in canh:
        if random.random() < ti_le_vo:
            ds.append((0, u, v) if random.random() < 0.5 else (0, v, u))
        else:
            ds.append((1, u, v))
    return ds

def sinh_dinhhuong():
    for so in range(1, 11):
        if so == 1:
            n, ds = 4, [(1, 1, 2), (1, 2, 3), (0, 3, 1), (0, 4, 2), (1, 4, 3)]   # vi du
        elif so == 2:
            n, ds = 4, [(1, 1, 2), (0, 2, 4), (1, 2, 3), (1, 3, 1)]              # vong co huong -> -1
        elif so == 3:
            n = 8; canh, _ = dag(n, 12); ds = tron(canh, 1.0)                    # toan vo huong
        elif so == 4:
            n = 8; canh, _ = dag(n, 12); ds = tron(canh, 0.6)
        elif so == 5:
            n = 2000; canh, _ = dag(n, 2000); ds = tron(canh, 0.5)
        elif so == 6:                                                            # vong co huong 2000 dinh
            n = 2000; canh, hv = dag(n, 1999, xich=True)
            xich = set(canh)                                                     # xich giu co huong
            ds = [(1, u, v) if (u, v) in xich else e for e, (u, v) in zip(tron(canh, 0.5), canh)]
            ds.append((1, hv[1999], hv[0])); random.shuffle(ds)
        elif so == 7:
            n = 2000; canh, _ = dag(n, 2000); ds = tron(canh, 0.0)              # khong canh vo huong
        elif so == 8:
            n = 2 * 10**5; canh, _ = dag(n, 2 * 10**5, xich=True); ds = tron(canh, 0.5)
        elif so == 9:
            n = 2 * 10**5; canh, _ = dag(n, 2 * 10**5); ds = tron(canh, 0.9)
        else:                                                                    # vong co huong 3 dinh
            n = 2 * 10**5; canh, _ = dag(n, 2 * 10**5 - 3); ds = tron(canh, 0.5)
            a, b, c = random.sample(range(1, n + 1), 3)
            ds += [(1, a, b), (1, b, c), (1, c, a)]
            random.shuffle(ds)
        inp = f'{n} {len(ds)}\n' + ''.join(f'{t} {u} {v}\n' for t, u, v in ds)
        ghi('DINHHUONG', so, inp, dap_an_dinhhuong(n, ds))

SINH = {'MONHOC': sinh_monhoc, 'CHUTRINH': sinh_chutrinh, 'SOHOCKY': sinh_sohocky,
        'CONGVIEC': sinh_congviec, 'TUDIEN': sinh_tudien, 'DINHHUONG': sinh_dinhhuong}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        random.seed(bai + '-2026')
        SINH[bai]()
        print('Da sinh', bai)

main()
