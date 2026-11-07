# SINH TEST cho 6 bai buoi 19 (QHD tren cay)
#   Tren lop : CAYCON, DUTIEC, DUONGKINH        Ve nha: CATCANH, TONGKC, TIENQUYET
# Cau truc thu muc theo Themis: test/CAYCON/Test01/CAYCON.INP + CAYCON.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau (loi giai mau: BFS lay thu tu + duyet nguoc):
#   CAYCON, DUTIEC, CATCANH bang DFS ngan xep "hau thu tu" (dinh duoc lay ra lan 2 thi moi con da xong),
#   DUONGKINH bang hai lan duyet (dinh xa nhat cua dinh xa nhat),
#   TONGKC bang dem dong gop tung canh: canh (cha, v) nam tren sz[v]*(n - sz[v]) cap -> tong moi cap,
#     roi doi goc bang DFS ngan xep,
#   TIENQUYET bang cai tui tren THU TU DFS (tien thu tu): o vi tri i, hoac chon dinh i -> sang i+1,
#     hoac bo ca cay con cua i -> nhay sang i + sz.
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
#   CAYCON   : n <= 1000           | n <= 2*10^5, cay ngau nhien (nong) | n <= 2*10^5, co cay sau (duong thang)
#   DUTIEC   : n <= 20             | n <= 2*10^5, p[i] < i             | n <= 2*10^5 bat ky
#   DUONGKINH: n <= 2000           | n <= 2*10^5, w = 1                | n <= 2*10^5, w <= 10^9
#   CATCANH  : n <= 2000           | n <= 2*10^5, cay nong              | n <= 2*10^5 bat ky
#   TONGKC   : n <= 2000           | n <= 2*10^5, cay nong              | n <= 2*10^5 bat ky
#   TIENQUYET: n <= 15             | n <= 200                          | n <= 2000
# Chay: python sinh_test.py                 -> sinh ca 6 bai (~60 giay)
#       python sinh_test.py CAYCON TONGKC   -> chi sinh cac bai ke ten
# Moi bai co seed rieng (random.seed('CAYCON-2026'), ...) nen sinh rieng mot bai hay ca bo deu ra CUNG test.
import os, random, sys

GOC = 'test'

def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

# ---------------- Sinh cay ----------------
def cha_theo_kieu(n, kieu):
    """Tra ve par[2..n] voi par[i] < i (dinh 1 la goc). Kieu:
       'nn'     : cha ngau nhien trong 1..i-1 (cay nong, do sau ~ ln n)
       'dt'     : duong thang 1-2-...-n (do sau n)
       'sao'    : moi dinh noi vao 1
       'choi'   : duong dai n/2 roi moi dinh con lai la la treo vao duong (cay "cai choi")
       'sau'    : cha trong i-3..i-1 (cay sau ~ n/2, nhieu nhanh ngan)
       'nhiphan': cay nhi phan day du"""
    par = [0, 0]
    for i in range(2, n + 1):
        if kieu == 'nn':
            par.append(random.randint(1, i - 1))
        elif kieu == 'dt':
            par.append(i - 1)
        elif kieu == 'sao':
            par.append(1)
        elif kieu == 'choi':
            par.append(i - 1 if i <= n // 2 else random.randint(1, n // 2))
        elif kieu == 'sau':
            par.append(random.randint(max(1, i - 3), i - 1))
        else:
            par.append(i // 2)
    return par

def cay(n, kieu, tron=True, giu_goc=True):
    """Danh sach canh (u, v) cua cay n dinh. tron=True: doi nhan ngau nhien (dinh 1 van la goc neu giu_goc),
       dao chieu tung canh va tron thu tu canh."""
    par = cha_theo_kieu(n, kieu)
    nhan = list(range(n + 1))
    if tron:
        t = list(range(2, n + 1)) if giu_goc else list(range(1, n + 1))
        random.shuffle(t)
        nhan = [0, 1] + t if giu_goc else [0] + t
    canh = []
    for i in range(2, n + 1):
        u, v = nhan[i], nhan[par[i]]
        canh.append((u, v) if random.random() < 0.5 else (v, u))
    if tron:
        random.shuffle(canh)
    return canh

def ke(n, canh):
    adj = [[] for _ in range(n + 1)]
    for e in canh:
        adj[e[0]].append(e[1]); adj[e[1]].append(e[0])
    return adj

def hau_thu_tu(n, adj, goc=1):
    """DFS ngan xep: tra ve (post, par) - post la thu tu 'con xong truoc cha'."""
    par = [0] * (n + 1); par[goc] = -1
    post = []; st = [(goc, False)]
    while st:
        u, xong = st.pop()
        if xong:
            post.append(u); continue
        st.append((u, True))
        for v in adj[u]:
            if v != par[u]:
                par[v] = u; st.append((v, False))
    return post, par

def dong2(canh):
    return ''.join(f'{u} {v}\n' for u, v in canh)

# ---------------- CAYCON ----------------
def dap_an_caycon(n, canh):
    post, par = hau_thu_tu(n, ke(n, canh))
    sz = [1] * (n + 1)
    for u in post:
        if par[u] > 0:
            sz[par[u]] += sz[u]
    return ' '.join(map(str, sz[1:])) + '\n'

def sinh_caycon():
    for so in range(1, 11):
        if so == 1:
            n, canh = 7, [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7)]     # vi du: 7 3 3 1 1 2 1
        elif so == 2:
            n, canh = 1, []
        elif so == 3:
            n = 1000; canh = cay(n, 'dt')
        elif so == 4:
            n = 1000; canh = cay(n, random.choice(['nn', 'sao']))
        elif so <= 7:
            n = 2 * 10**5; canh = cay(n, ['nn', 'sao', 'nhiphan'][so - 5])
        else:
            n = 2 * 10**5; canh = cay(n, ['dt', 'choi', 'sau'][so - 8])
        ghi('CAYCON', so, f'{n}\n' + dong2(canh), dap_an_caycon(n, canh))

# ---------------- DUTIEC ----------------
def dap_an_dutiec(n, a, p):
    con = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        con[p[i]].append(i)
    d0 = [0] * (n + 1); d1 = [0] * (n + 1)
    st = [(1, False)]
    while st:
        u, xong = st.pop()
        if not xong:
            st.append((u, True)); st.extend((v, False) for v in con[u]); continue
        d1[u] = a[u] + sum(d0[v] for v in con[u])
        d0[u] = sum(max(d0[v], d1[v]) for v in con[u])
    return f'{max(d0[1], d1[1])}\n'

def sinh_dutiec():
    for so in range(1, 11):
        if so == 1:
            n = 6; a = [0, 3, 5, 2, 4, -1, 6]; p = [0, 0, 1, 1, 2, 2, 3]          # vi du: 13
        else:
            if so == 2:
                n, kieu, A = 1, 'nn', 10**4
            elif so <= 4:
                n, kieu, A = 20, ['nn', 'dt'][so - 3], 10**4
            elif so <= 7:
                n, kieu, A = 2 * 10**5, ['nn', 'sao', 'dt'][so - 5], 10**4
            else:
                n, kieu, A = 2 * 10**5, ['nn', 'choi', 'sau'][so - 8], 10**4
            a = [0] + [random.randint(-A, A) for _ in range(n)]
            if so == 2:
                a = [0, -5]                                                  # chi co giam doc, do vui am -> 0
            if so == 10:                                                     # phan lon do vui am
                a = [0] + [random.randint(-10**4, 500) for _ in range(n)]
            par = cha_theo_kieu(n, kieu)
            if so <= 4 or so >= 8:                                           # doi nhan: sep co the so lon hon
                t = list(range(2, n + 1)); random.shuffle(t); nhan = [0, 1] + t
                p = [0] * (n + 1); aa = [0] * (n + 1); aa[1] = a[1]
                for i in range(2, n + 1):
                    p[nhan[i]] = nhan[par[i]]; aa[nhan[i]] = a[i]
                a = aa
            else:
                p = par
        inp = f'{n}\n' + ' '.join(map(str, a[1:])) + '\n' + ' '.join(map(str, p[2:])) + '\n'
        ghi('DUTIEC', so, inp, dap_an_dutiec(n, a, p))

# ---------------- DUONGKINH ----------------
def dap_an_duongkinh(n, canh):
    adj = [[] for _ in range(n + 1)]
    for u, v, w in canh:
        adj[u].append((v, w)); adj[v].append((u, w))
    def xa(s):
        d = [-1] * (n + 1); d[s] = 0; st = [s]
        while st:
            u = st.pop()
            for v, w in adj[u]:
                if d[v] < 0:
                    d[v] = d[u] + w; st.append(v)
        t = max(range(1, n + 1), key=lambda x: d[x])
        return t, d[t]
    A, _ = xa(1)
    return f'{xa(A)[1]}\n'

def sinh_duongkinh():
    for so in range(1, 11):
        if so == 1:
            n = 6; canh = [(1, 2, 3), (2, 3, 4), (2, 4, 2), (1, 5, 7), (4, 6, 6)]  # vi du: 18
        else:
            if so == 2:
                n, kieu, W = 2, 'nn', 10**9
            elif so == 3:
                n, kieu, W = 2000, 'nn', 1000
            elif so == 4:
                n, kieu, W = 2000, 'choi', 10**9
            elif so <= 7:
                n, kieu, W = 2 * 10**5, ['nn', 'dt', 'sao'][so - 5], 1
            else:
                n, kieu, W = 2 * 10**5, ['nn', 'choi', 'sau'][so - 8], 10**9
            canh = [(u, v, random.randint(1, W)) for u, v in cay(n, kieu, giu_goc=False)]
        ghi('DUONGKINH', so, f'{n}\n' + ''.join(f'{u} {v} {w}\n' for u, v, w in canh),
            dap_an_duongkinh(n, canh))

# ---------------- CATCANH ----------------
def dap_an_catcanh(n, a, canh):
    post, par = hau_thu_tu(n, ke(n, canh))
    s = a[:]
    for u in post:
        if par[u] > 0:
            s[par[u]] += s[u]
    return f'{min(abs(s[1] - 2 * s[v]) for v in range(2, n + 1))}\n'

def sinh_catcanh():
    for so in range(1, 11):
        if so == 1:
            n = 5; a = [0, 10, 20, 30, 40, 50]; canh = [(1, 2), (1, 3), (3, 4), (3, 5)]   # vi du: 50
        else:
            if so == 2:
                n, kieu, A = 2, 'nn', 10**9
            elif so <= 4:
                n, kieu, A = 2000, ['nn', 'dt'][so - 3], [10**9, 5][so - 3]
            elif so <= 7:
                n, kieu, A = 2 * 10**5, ['nn', 'sao', 'nhiphan'][so - 5], 10**9
            else:
                n, kieu, A = 2 * 10**5, ['dt', 'choi', 'sau'][so - 8], [10**9, 10**9, 3][so - 8]
            a = [0] + [random.randint(1, A) for _ in range(n)]
            canh = cay(n, kieu, giu_goc=False)
        inp = f'{n}\n' + ' '.join(map(str, a[1:])) + '\n' + dong2(canh)
        ghi('CATCANH', so, inp, dap_an_catcanh(n, a, canh))

# ---------------- TONGKC ----------------
def dap_an_tongkc(n, canh):
    adj = ke(n, canh)
    post, par = hau_thu_tu(n, adj)
    sz = [1] * (n + 1)
    for u in post:
        if par[u] > 0:
            sz[par[u]] += sz[u]
    # tong moi cap = tong dong gop tung canh; f[1] = tong do sau. Tinh do sau bang ngan xep.
    sau = [0] * (n + 1)
    for u in reversed(post):                   # nguoc hau thu tu: cha truoc con
        if par[u] > 0:
            sau[u] = sau[par[u]] + 1
    f = [0] * (n + 1); f[1] = sum(sau)
    for u in reversed(post):
        if par[u] > 0:
            f[u] = f[par[u]] - sz[u] + (n - sz[u])
    return ' '.join(map(str, f[1:])) + '\n'

def sinh_tongkc():
    for so in range(1, 11):
        if so == 1:
            n, canh = 5, [(1, 2), (2, 3), (2, 4), (4, 5)]                         # vi du: 8 5 8 6 9
        elif so == 2:
            n, canh = 1, []
        elif so <= 4:
            n = 2000; canh = cay(n, ['nn', 'dt'][so - 3], giu_goc=False)
        elif so <= 7:
            n = 2 * 10**5; canh = cay(n, ['nn', 'sao', 'nhiphan'][so - 5], giu_goc=False)
        else:
            n = 2 * 10**5; canh = cay(n, ['dt', 'choi', 'sau'][so - 8], giu_goc=False)
        ghi('TONGKC', so, f'{n}\n' + dong2(canh), dap_an_tongkc(n, canh))

# ---------------- TIENQUYET ----------------
def dap_an_tienquyet(n, k, p, c):
    con = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        con[p[i]].append(i)
    pre = []; st = [0]                         # tien thu tu tu goc ao 0
    while st:
        u = st.pop(); pre.append(u); st.extend(reversed(con[u]))
    m = len(pre)                               # = n + 1
    sz = [1] * (n + 1)
    for u in reversed(pre):
        for v in con[u]:
            sz[u] += sz[v]
    NEG = -10**18
    K = k + 1
    # f[i][j]: tong lon nhat chon j dinh trong cac dinh pre[i..m-1] (vi tri i tro di), hop le
    nxt = [NEG] * (K + 1); nxt[0] = 0          # i = m
    hang = [None] * (m + 1); hang[m] = nxt
    for i in range(m - 1, -1, -1):
        u = pre[i]
        lay = hang[i + 1]; bo = hang[i + sz[u]]
        cu = [NEG] * (K + 1)
        for j in range(K + 1):
            x = bo[j]
            if j > 0 and lay[j - 1] > NEG and lay[j - 1] + c[u] > x:
                x = lay[j - 1] + c[u]
            cu[j] = x
        hang[i] = cu
    return f'{hang[0][K]}\n'

def sinh_tienquyet():
    for so in range(1, 11):
        if so == 1:
            n, k = 6, 3
            p = [0, 0, 1, 1, 0, 4, 3]; c = [0, 2, 5, -3, 1, 6, 11]                # vi du: 10
        else:
            if so == 2:
                n, k, kieu = 1, 1, 'nn'
            elif so <= 4:
                n, kieu = 15, ['nn', 'dt'][so - 3]; k = random.randint(1, n)
            elif so <= 7:
                n, kieu = 200, ['nn', 'choi', 'sao'][so - 5]; k = [200, 120, 37][so - 5]
            else:
                n, kieu = 2000, ['nn', 'choi', 'sau'][so - 8]; k = [2000, 1000, 1500][so - 8]
            # rung: goc ao 0 la cha cua 'dinh 1' trong cay sinh ra; them vai goc khac de thanh rung
            par = cha_theo_kieu(n + 1, kieu)       # dinh 1..n+1, goc 1 se la goc ao 0
            t = list(range(1, n + 1)); random.shuffle(t)
            nhan = [0, 0] + t                      # dinh i cua cay sinh -> mon nhan[i]; dinh 1 -> 0
            p = [0] * (n + 1)
            for i in range(2, n + 2):
                p[nhan[i]] = nhan[par[i]]
            c = [0] + [random.randint(-10**4, 10**4) for _ in range(n)]
        inp = f'{n} {k}\n' + ''.join(f'{p[i]} {c[i]}\n' for i in range(1, n + 1))
        ghi('TIENQUYET', so, inp, dap_an_tienquyet(n, k, p, c))

SINH = {'CAYCON': sinh_caycon, 'DUTIEC': sinh_dutiec, 'DUONGKINH': sinh_duongkinh,
        'CATCANH': sinh_catcanh, 'TONGKC': sinh_tongkc, 'TIENQUYET': sinh_tienquyet}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        random.seed(bai + '-2026')
        SINH[bai]()
        print('Da sinh', bai)

main()
