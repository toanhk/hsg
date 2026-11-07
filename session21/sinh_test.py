# SINH TEST buoi 21 - thi thu de that: HSG THPT cap tinh Ninh Binh 2023-2024
#   Ngay 06/10/2023 (thi tren lop, 180 phut): PAIRCOUNT, KPRIMESUB, ST25
#   Ngay 07/10/2023 (bai ve nha):             SEQ, RBGAME
# Test do chung ta tu sinh theo dung rang buoc va ti le subtask cua de (khong phai bo test chinh thuc cua So).
# Cau truc thu muc theo Themis: test/PAIRCOUNT/Test01/PAIRCOUNT.INP + PAIRCOUNT.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau de kiem cheo:
#   PAIRCOUNT gom vi tri theo gia tri roi dem cap bang hai con tro (loi giai mau: dict dem tu trai sang),
#   KPRIMESUB hai con tro O(N) moi test (loi giai mau: gop theo so nguyen to),
#   ST25 QHD bitmask tren K dai ly (loi giai mau: duyet hoan vi),
#   SEQ DSU co ham find (loi giai mau: luu do dai tai hai dau mut),
#   RBGAME QHD cung viet de quy co nho, n <= 20 thi minimax tren day thang tung vi tri cat.
# Chay: python sinh_test.py              -> sinh ca 5 bai (~1 phut)
#       python sinh_test.py ST25         -> chi sinh bai ke ten
# Moi bai co seed rieng (random.seed('ST25-2026')) nen sinh rieng mot bai hay ca bo deu ra CUNG test.
import os, random, sys, heapq, bisect
from functools import lru_cache

GOC = 'test'

def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

# ---------------- PAIRCOUNT ----------------
def dap_an_paircount(n, k, a):
    vt = {}
    for i, x in enumerate(a):
        vt.setdefault(x, []).append(i)
    ans = 0
    for v, P in vt.items():
        Q = vt.get(v + k)
        if not Q:
            continue
        j = 0                                   # dem cap p in P, q in Q, p < q
        for q in Q:
            while j < len(P) and P[j] < q:
                j += 1
            ans += j
    return f'{ans}\n'

def sinh_paircount():
    for so in range(1, 11):
        if so == 1:
            n, k, a = 5, 1, [1, 2, 3, 2, 4]                                   # vi du: 4
        elif so == 2:
            n, k = 1000, 1; a = [random.randint(0, 20) for _ in range(n)]
        elif so == 3:
            n, k = 1000, 10**9; a = [random.choice((-10**9, 0, 10**9, 5)) for _ in range(n)]
        elif so == 4:
            n, k = 2, 3; a = [5, 2]                                           # j truoc i: 0
        elif so == 5:
            n, k = 10**5, 1; a = [random.randint(0, 10**6) for _ in range(n)]
        elif so == 6:
            n, k = 10**5, 3; a = [random.randint(0, 100) for _ in range(n)]   # dap an ~ 10^8
        elif so == 7:
            n, k = 10**5, 10**6; a = [random.choice((0, 10**6)) for _ in range(n)]
        elif so == 8:
            n, k = 10**6, 10**9
            goc = [random.randint(-10**9, 0) for _ in range(1000)]
            a = [b + k * random.randint(0, 1) for b in (random.choice(goc) for _ in range(n))]
        elif so == 9:
            n, k = 10**6, 1; a = [random.randint(-5, 5) for _ in range(n)]    # dap an ~ 9*10^10
        else:
            n, k = 10**6, random.randint(1, 10**9); a = [random.randint(-10**9, 10**9) for _ in range(n)]
            for i in range(0, n, 1000):                                       # cai them it cap dung
                a[i] = max(-10**9, min(10**9, a[i - 1] + k if i else a[i]))
        inp = f'{n} {k}\n' + ' '.join(map(str, a)) + '\n'
        ghi('PAIRCOUNT', so, inp, dap_an_paircount(n, k, a))

# ---------------- KPRIMESUB ----------------
SANG = None

def dap_an_kprimesub(q):
    out = []
    for N, K in q:
        ans = 0; R = 1; dem = 0
        for L in range(2, N + 1):
            while R < N and dem < K:
                R += 1; dem += SANG[R]
            if dem >= K:
                ans += N - max(R, L) + 1
            if R >= L:
                dem -= SANG[L]
            else:
                R = L
        out.append(ans)
    return '\n'.join(map(str, out)) + '\n'

def sinh_kprimesub():
    global SANG
    M = 10**5
    SANG = [1] * (M + 1); SANG[0] = SANG[1] = 0
    for i in range(2, 317):
        if SANG[i]:
            for j in range(i * i, M + 1, i):
                SANG[j] = 0
    for so in range(1, 11):
        if so == 1:
            q = [(5, 2)]                                                      # vi du 1: 4
        elif so == 2:
            q = [(5, 2), (5, 1), (9, 3)]                                      # vi du 2: 4 9 8
        elif so == 3:
            q = [(2, 0), (2, 1), (2, 2), (100, 0), (100, 25), (100, 26)]      # bien: K = 0, K > pi(N)
        elif so == 4:
            q = [(random.randint(2, 100), random.randint(0, 30)) for _ in range(50)]
        elif so <= 7:
            q = [(random.randint(101, 1000), random.randint(0, 170)) for _ in range(50)]
            if so == 7:
                q[0] = (1000, 168); q[1] = (1000, 169); q[2] = (1000, 0)
        else:
            t = 100
            if so == 8:
                q = [(10**5, random.randint(0, 9592)) for _ in range(t)]
            elif so == 9:
                q = [(random.randint(2, 10**5), random.randint(0, 10**4)) for _ in range(t)]
            else:
                q = [(10**5, random.randint(1, 10)) for _ in range(t)]
                q[0] = (10**5, 0)                                             # dap an ~ 5*10^9
        inp = f'{len(q)}\n' + ''.join(f'{N} {K}\n' for N, K in q)
        ghi('KPRIMESUB', so, inp, dap_an_kprimesub(q))

# ---------------- ST25 ----------------
def dap_an_st25(n, x, canh):
    adj = [[] for _ in range(n + 1)]
    for u, v, w in canh:
        adj[u].append(v << 11 | w); adj[v].append(u << 11 | w)          # w <= 10^3 < 2^11
    K = len(x)
    d = []
    for s in x:
        dist = [1 << 60] * (n + 1); dist[s] = 0
        pq = [s]                                                        # heap so nguyen: d << 14 | u
        while pq:
            t = heapq.heappop(pq); du, u = t >> 14, t & 16383
            if du > dist[u]:
                continue
            for e in adj[u]:
                v, w = e >> 11, e & 2047
                if du + w < dist[v]:
                    dist[v] = du + w; heapq.heappush(pq, (du + w) << 14 | v)
        d.append(dist)
    INF = 1 << 60
    full = (1 << K) - 1
    g = []                                                              # g[a][b]: qua het K diem, dau a cuoi b
    for a in range(K):
        f = [[INF] * K for _ in range(1 << K)]
        f[1 << a][a] = 0
        for mask in range(1 << K):
            for b in range(K):
                if f[mask][b] == INF:
                    continue
                for c in range(K):
                    if not mask >> c & 1:
                        nv = f[mask][b] + d[b][x[c]]
                        if nv < f[mask | 1 << c][c]:
                            f[mask | 1 << c][c] = nv
        g.append(f[full])
    best, bh = INF, -1
    for h in range(1, n + 1):
        if h in x:
            continue
        c = min(d[a][h] + g[a][b] + d[b][h] for a in range(K) for b in range(K))
        if c < best:
            best, bh = c, h
    return f'{bh} {best}\n'

def do_thi_st25(n, m, wmax):
    hv = list(range(1, n + 1)); random.shuffle(hv)
    canh = [(hv[i], hv[random.randrange(max(0, i - 50), i)], random.randint(1, wmax)) for i in range(1, n)]
    while len(canh) < m:
        u, v = random.sample(range(1, n + 1), 2)
        canh.append((u, v, random.randint(1, wmax)))
    random.shuffle(canh)
    return canh

def sinh_st25():
    for so in range(1, 11):
        if so == 1:                                                     # vi du: 4 7
            n, x = 5, [1, 2, 3]
            canh = [(1, 2, 1), (1, 5, 2), (3, 2, 3), (3, 4, 1), (4, 2, 7), (4, 5, 10), (5, 3, 1), (4, 1, 2)]
        elif so == 2:
            n = 2; x = [2]; canh = [(1, 2, 5), (2, 1, 3)]               # canh lap: 1 6
        elif so == 3:
            n = 100; x = [random.randint(1, n)]; canh = do_thi_st25(n, 300, 3)        # nhieu tru so hoa
        elif so == 4:
            n = 100; x = random.sample(range(1, n + 1), 2); canh = do_thi_st25(n, 400, 1000)
        elif so == 5:
            n = 1000; x = random.sample(range(1, n + 1), 2); canh = do_thi_st25(n, 5000, 1000)
        elif so == 6:                                                   # duong thang 1-2-...-n
            n = 1000; x = [1, n]; canh = [(i, i + 1, random.randint(1, 1000)) for i in range(1, n)]
        elif so == 7:
            n = 10**4; x = random.sample(range(1, n + 1), 5); canh = do_thi_st25(n, 5 * 10**4, 1000)
        elif so == 8:
            n = 10**4; x = random.sample(range(1, n + 1), 3); canh = do_thi_st25(n, 5 * 10**4, 1000)
        elif so == 9:
            n = 10**4; x = random.sample(range(1, n + 1), 5); canh = do_thi_st25(n, 5 * 10**4, 2)
        else:                                                           # thua: gan nhu cay, K = 5
            n = 10**4; x = random.sample(range(1, n + 1), 5); canh = do_thi_st25(n, n + 100, 1000)
        inp = f'{n} {len(canh)} {len(x)}\n' + ''.join(f'{v}\n' for v in x) + ''.join(f'{u} {v} {w}\n' for u, v, w in canh)
        ghi('ST25', so, inp, dap_an_st25(n, x, canh))

# ---------------- SEQ ----------------
def dap_an_seq(n, a, ks):
    par = list(range(n)); sz = [1] * n; on = [False] * n
    def find(u):
        while par[u] != u:
            par[u] = par[par[u]]; u = par[u]
        return u
    ord_a = sorted(range(n), key=lambda i: a[i])
    ord_q = sorted(range(len(ks)), key=lambda i: ks[i])
    res = [0] * len(ks); p = 0; best = 0
    for qi in ord_q:
        while p < n and a[ord_a[p]] <= ks[qi]:
            i = ord_a[p]; on[i] = True; p += 1
            for j in (i - 1, i + 1):
                if 0 <= j < n and on[j]:
                    r1, r2 = find(i), find(j)
                    if r1 != r2:
                        par[r1] = r2; sz[r2] += sz[r1]
            best = max(best, sz[find(i)])
        res[qi] = best
    return '\n'.join(map(str, res)) + '\n'

def sinh_seq():
    for so in range(1, 11):
        if so == 1:
            a = [-2, 5, 6, 10, -5, 0]; ks = [-10, 5, -4, 11]                 # vi du: 0 2 1 6
        elif so == 2:
            a = [random.randint(-10, 10) for _ in range(100)]; ks = [random.randint(-12, 12) for _ in range(5)]
        elif so <= 6:
            n = 1000; q = 1000
            if so == 3:
                a = [random.randint(-10**9, 10**9) for _ in range(n)]
            elif so == 4:
                a = [random.randint(1, 5) for _ in range(n)]
            elif so == 5:
                a = sorted(random.randint(-10**6, 10**6) for _ in range(n))
            else:
                a = [7] * n
            ks = [random.choice(a) + random.randint(-1, 1) for _ in range(q)]
            ks[0] = -10**9; ks[1] = 10**9
        else:
            n = q = 10**5
            if so == 7:
                a = [random.randint(-10**9, 10**9) for _ in range(n)]
            elif so == 8:
                a = [random.randint(0, 100) for _ in range(n)]
            elif so == 9:
                a = [abs(i - n // 2) for i in range(n)]                        # hinh chu V
            else:
                a = [random.randint(-10**9, 10**9) if random.random() < 0.01 else random.randint(-100, 100)
                     for _ in range(n)]
            ks = [random.choice(a) + random.randint(-2, 2) if random.random() < 0.8 else random.randint(-10**9, 10**9)
                  for _ in range(q)]
        n = len(a)
        inp = f'{n} {len(ks)}\n' + ' '.join(map(str, a)) + '\n' + ''.join(f'{k}\n' for k in ks)
        ghi('SEQ', so, inp, dap_an_seq(n, a, ks))

# ---------------- RBGAME ----------------
def dap_an_rbgame(n, k, s):
    if n <= 20:                                   # minimax tren day thang, tung vi tri cat
        ans = 0
        for cut in range(n):
            line = s[cut:] + s[:cut]
            @lru_cache(maxsize=None)
            def thang(l, r, x, y):
                for c in (l, r):
                    nx = x + (line[c] == 'B')
                    if nx == k:
                        continue
                    nl, nr = (l + 1, r) if c == l else (l, r - 1)
                    if nl > nr or not thang(nl, nr, y, nx):
                        return True
                return False
            ans += thang(0, n - 1, 0, 0)
        return f'{ans}\n'
    b = [ch == 'B' for ch in s]; B = sum(b)
    pre = [0] * (2 * n + 1)
    for i in range(2 * n):
        pre[i + 1] = pre[i] + b[i % n]
    sys.setrecursionlimit(10000)
    @lru_cache(maxsize=None)
    def thang(st, L, x):                           # cung (st, L), nguoi den luot co x hat B
        xanh = pre[st + L] - pre[st]
        y = B - xanh - x
        for c, nst in ((st, (st + 1) % n), ((st + L - 1) % n, st)):
            if b[c] and x + 1 == k:
                continue
            if not thang(nst, L - 1, y):
                return True
        return False
    ans = 0
    for i in range(n):
        ok = (not (b[i] and k == 1) and not thang((i + 1) % n, n - 1, 0)) or \
             (not (b[i - 1] and k == 1) and not thang(i, n - 1, 0))
        ans += ok
    return f'{ans}\n'

def chuoi_hat(n, k, ti_le):
    while True:
        s = ''.join('B' if random.random() < ti_le else 'R' for _ in range(n))
        if s.count('B') >= 2 * k - 1:
            return s

def sinh_rbgame():
    for so in range(1, 11):
        if so == 1:
            n, k, s = 5, 1, 'RBRBR'                                          # vi du: 2
        elif so == 2:
            n, k = 20, 3; s = chuoi_hat(n, k, 0.5)
        elif so == 3:
            n, k = 19, 10; s = 'B' * 19
        elif so <= 6:
            n = random.randint(40, 60); k = [5, 12, 20][so - 4]; s = chuoi_hat(n, k, 0.6 + 0.1 * (so - 4))
        else:
            n = random.choice([97, 99, 100]); k = [1, 10, 25, 30][so - 7]
            s = chuoi_hat(n, k, [0.2, 0.4, 0.6, 0.8][so - 7])
        inp = f'{n} {k}\n{s}\n'
        ghi('RBGAME', so, inp, dap_an_rbgame(n, k, s))

SINH = {'PAIRCOUNT': sinh_paircount, 'KPRIMESUB': sinh_kprimesub, 'ST25': sinh_st25,
        'SEQ': sinh_seq, 'RBGAME': sinh_rbgame}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        random.seed(bai + '-2026')
        SINH[bai]()
        print('Da sinh', bai)

main()
