# SINH TEST cho 6 bai buoi 17 (QHD tren doan)
#   Tren lop : GOPSOI, NHANMT, LAYSO        Ve nha: CATDX, BANBONG, DAYNGOAC
# Cau truc thu muc theo Themis: test/GOPSOI/Test01/GOPSOI.INP + GOPSOI.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau (loi giai mau la QHD bottom-up):
#   GOPSOI bang toi uu Knuth O(n^2) (diem cat tot nhat opt[l][r-1] <= opt[l][r] <= opt[l+1][r]),
#   NHANMT, BANBONG bang de quy co nho (top-down, do sau <= n),
#   LAYSO bang "diem tot nhat cua nguoi dang di" = tong doan - diem tot nhat cua doi thu (cong don),
#   CATDX danh dau doan doi xung bang LOANG TU TAM (moi tam mo rong ra hai ben),
#   DAYNGOAC bang day con DUNG dai nhat (dap an = n - do dai do), de quy co nho.
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py                  -> sinh ca 6 bai (~5 giay)
#       python sinh_test.py GOPSOI CATDX     -> chi sinh cac bai ke ten
# Moi bai co seed rieng (random.seed('GOPSOI-2026'), ...) nen sinh rieng mot bai hay ca bo deu ra CUNG test.
import os, random, sys
from functools import lru_cache

GOC = 'test'
sys.setrecursionlimit(10000)

def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

def day(n, lo, hi):
    return [random.randint(lo, hi) for _ in range(n)]

# ---------------- GOPSOI ----------------
def dap_an_gopsoi(a):
    n = len(a)
    P = [0]
    for x in a:
        P.append(P[-1] + x)
    f = [[0] * n for _ in range(n)]
    opt = [[i] * n for i in range(n)]              # opt[l][r] = k tot nhat; opt[i][i] = i
    for d in range(1, n):
        for l in range(n - d):
            r = l + d
            best, bk = None, l
            for k in range(opt[l][r - 1], min(opt[l + 1][r], r - 1) + 1):
                c = f[l][k] + f[k + 1][r]
                if best is None or c < best:
                    best, bk = c, k
            f[l][r] = best + P[r + 1] - P[l]
            opt[l][r] = bk
    return f[0][n - 1]

def sinh_gopsoi():
    random.seed('GOPSOI-2026')
    for so in range(1, 11):
        if so == 1:
            a = [5, 2, 4, 4]                                   # vi du: 30
        elif so == 2:
            a = [7]                                            # mot dong: 0
        elif so <= 4:
            a = day(8, 1, 10 if so == 3 else 10**9)
        elif so == 5:
            a = day(100, 1, 10**9)
        elif so == 6:
            a = [1] * 100
        elif so == 7:
            a = day(97, 1, 20)
        elif so == 8:
            a = day(300, 1, 10**9)
        elif so == 9:                                          # tang dan: tham lam gop tu trai
            a = sorted(day(300, 1, 10**9))
        else:
            a = [random.choice([1, 10**9]) for _ in range(300)]
        ghi('GOPSOI', so, f'{len(a)}\n' + ' '.join(map(str, a)) + '\n', f'{dap_an_gopsoi(a)}\n')

# ---------------- NHANMT ----------------
def dap_an_nhanmt(p):
    n = len(p) - 1
    nho = {}
    def g(l, r):
        if l == r:
            return 0
        if (l, r) not in nho:
            nho[l, r] = min(g(l, k) + g(k + 1, r) + p[l] * p[k + 1] * p[r + 1] for k in range(l, r))
        return nho[l, r]
    for d in range(n):                                     # goi tu doan ngan -> do sau de quy nho
        for l in range(n - d):
            g(l, l + d)
    return g(0, n - 1)

def sinh_nhanmt():
    random.seed('NHANMT-2026')
    for so in range(1, 11):
        if so == 1:
            p = [10, 30, 5, 60]                                # vi du: 4500
        elif so == 2:
            p = [7, 9]                                         # mot ma tran: 0
        elif so == 3:
            p = [3, 2, 6, 8]                                   # bat ban sai thu tu: 144
        elif so == 4:
            p = day(9, 1, 100)
        elif so <= 7:
            p = day(51, 1, 1000) if so != 6 else [random.choice([1, 1000]) for _ in range(51)]
        elif so == 8:
            p = day(201, 1, 1000)
        elif so == 9:
            p = [1000] * 201
        else:
            p = [random.choice([1, 2, 999, 1000]) for _ in range(201)]
        ghi('NHANMT', so, f'{len(p) - 1}\n' + ' '.join(map(str, p)) + '\n', f'{dap_an_nhanmt(p)}\n')

# ---------------- LAYSO ----------------
def dap_an_layso(a):
    n = len(a)
    P = [0]
    for x in a:
        P.append(P[-1] + x)
    D = a[:]                                               # D[l] = diem tot nhat cua nguoi dang di tren a[l..l+d]
    for d in range(1, n):
        D = [P[l + d + 1] - P[l] - min(D[l + 1], D[l]) for l in range(n - d)]
    return D[0]

def sinh_layso():
    random.seed('LAYSO-2026')
    for so in range(1, 11):
        if so == 1:
            a = [3, 9, 1, 2]                                   # vi du: 11 (tham lam ra 5)
        elif so == 2:
            a = [42]
        elif so <= 4:
            a = day(20 if so == 4 else 15, 1, 10**9 if so == 4 else 20)
        elif so == 5:
            a = day(300, 1, 10**9)
        elif so == 6:                                          # bay tham lam: so lon nap sau so nho
            a = []
            for _ in range(75):
                a += [random.randint(1, 10), random.randint(10**8, 10**9)] if random.random() < .5 else \
                     [random.randint(10**8, 10**9), random.randint(1, 10)]
                a += day(2, 1, 1000)
        elif so == 7:
            a = [5] * 299
        elif so == 8:
            a = day(2000, 1, 10**9)
        elif so == 9:
            a = [random.choice([1, 10**9]) for _ in range(2000)]
        else:
            a = day(1999, 1, 1000)
        ghi('LAYSO', so, f'{len(a)}\n' + ' '.join(map(str, a)) + '\n', f'{dap_an_layso(a)}\n')

# ---------------- CATDX ----------------
def dap_an_catdx(s):
    n = len(s)
    ket = [[] for _ in range(n)]                           # ket[r] = cac l de s[l..r] doi xung
    for tam in range(2 * n - 1):                           # tam = 2i: le quanh s[i]; 2i+1: chan giua s[i], s[i+1]
        l, r = tam // 2, (tam + 1) // 2
        while l >= 0 and r < n and s[l] == s[r]:
            ket[r].append(l)
            l -= 1; r += 1
    g = [0] + [n + 1] * n
    for r in range(n):
        g[r + 1] = min(g[l] for l in ket[r]) + 1
    return g[n]

def sinh_catdx():
    random.seed('CATDX-2026')
    for so in range(1, 11):
        if so == 1:
            s = 'abaab'                                        # vi du: 2 (a | baab)
        elif so == 2:
            s = 'z'
        elif so == 3:
            s = ''.join(random.choice('ab') for _ in range(15))
        elif so == 4:
            s = ''.join(random.choice('abc') for _ in range(14))
        elif so == 5:
            s = ''.join(random.choice('ab') for _ in range(200))
        elif so == 6:
            t = ''.join(random.choice('abc') for _ in range(60))
            s = t + t[::-1] + ''.join(random.choice('abc') for _ in range(80))
        elif so == 7:
            s = 'abcdefghij' * 20                               # khong co doan doi xung dai > 1: 200
        elif so == 8:
            s = ''.join(random.choice('ab') for _ in range(2000))
        elif so == 9:
            s = 'a' * 2000                                      # ca xau doi xung: 1 (ban O(n^3) cham nhat)
        else:
            t = ''.join(random.choice('ab') for _ in range(700))
            s = t + 'c' + t[::-1] + 'b' + ''.join(random.choice('aab') for _ in range(598))
        ghi('CATDX', so, s + '\n', f'{dap_an_catdx(s)}\n')

# ---------------- BANBONG ----------------
def dap_an_banbong(a):
    b = [1] + a + [1]
    m = len(b)
    @lru_cache(maxsize=None)
    def g(l, r):                                           # diem lon nhat khi ban het cac qua giua l va r
        if r - l < 2:
            return 0
        return max(g(l, k) + g(k, r) + b[l] * b[k] * b[r] for k in range(l + 1, r))
    for d in range(2, m):
        for l in range(m - d):
            g(l, l + d)
    return g(0, m - 1)

def sinh_banbong():
    random.seed('BANBONG-2026')
    for so in range(1, 11):
        if so == 1:
            a = [3, 1, 5, 8]                                   # vi du: 167
        elif so == 2:
            a = [9]
        elif so <= 4:
            a = day(8 if so == 4 else 6, 1, 100 if so == 4 else 9)
        elif so <= 7:
            a = day(50, 1, 100) if so != 7 else [random.choice([1, 100]) for _ in range(50)]
        elif so == 8:
            a = day(200, 1, 100)
        elif so == 9:
            a = [100] * 200
        else:
            a = [random.choice([1, 2, 100]) for _ in range(200)]
        ghi('BANBONG', so, f'{len(a)}\n' + ' '.join(map(str, a)) + '\n', f'{dap_an_banbong(a)}\n')

# ---------------- DAYNGOAC ----------------
def dap_an_dayngoac(s):
    n = len(s)
    @lru_cache(maxsize=None)
    def L(l, r):                                           # day con dung dai nhat cua s[l..r]
        if l >= r:
            return 0
        best = L(l + 1, r)
        if s[l] in '([':
            dong = ')' if s[l] == '(' else ']'
            for k in range(l + 1, r + 1):
                if s[k] == dong:
                    best = max(best, 2 + L(l + 1, k - 1) + L(k + 1, r))
        return best
    for d in range(n):
        for l in range(n - d):
            L(l, l + d)
    return n - L(0, n - 1)

def ngoac_dung(n):
    """Sinh mot day ngoac dung do dai n (n chan)."""
    t, st = [], []
    while len(t) + len(st) < n:
        if st and (random.random() < .5 or len(t) + 2 * len(st) >= n):
            t.append(st.pop())
        else:
            c = random.choice('([')
            t.append(c); st.append(')' if c == '(' else ']')
    return ''.join(t + st[::-1])

def sinh_dayngoac():
    random.seed('DAYNGOAC-2026')
    for so in range(1, 11):
        if so == 1:
            s = '([)]'                                         # vi du: 2
        elif so == 2:
            s = '()[]()'                                       # da dung: 0 (ban sai in 2)
        elif so == 3:
            s = ''.join(random.choice('()[]') for _ in range(16))
        elif so == 4:
            s = ngoac_dung(16)[3:] + '('                      # cat dau day dung: thua ngoac dong
        elif so == 5:
            s = ''.join(random.choice('()[]') for _ in range(50))
        elif so == 6:
            t = list(ngoac_dung(50))
            for _ in range(5):
                i = random.randrange(50); t[i] = random.choice('()[]')
            s = ''.join(t)
        elif so == 7:
            s = ')' * 25 + '[' * 24
        elif so == 8:
            s = ''.join(random.choice('()[]') for _ in range(200))
        elif so == 9:
            s = ngoac_dung(200)
        else:
            t = list(ngoac_dung(200))
            for _ in range(20):
                i = random.randrange(200); t[i] = random.choice('()[]')
            s = ''.join(t)
        ghi('DAYNGOAC', so, s + '\n', f'{dap_an_dayngoac(s)}\n')

SINH = {'GOPSOI': sinh_gopsoi, 'NHANMT': sinh_nhanmt, 'LAYSO': sinh_layso,
        'CATDX': sinh_catdx, 'BANBONG': sinh_banbong, 'DAYNGOAC': sinh_dayngoac}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        SINH[bai]()
        print('Da sinh', bai)

main()
