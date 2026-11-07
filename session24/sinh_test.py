# SINH TEST buoi 24 - de khoi dong (90 phut, 3 bai ngan): SONT, NOIMANG, LATGACH
# Cau truc thu muc theo Themis: test/SONT/Test01/SONT.INP + SONT.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau de kiem cheo:
#   SONT sang bang list + vong for (loi giai mau: bytearray + gan lat cat),
#   NOIMANG BFS tung thanh phan (loi giai mau: DSU),
#   LATGACH QHD theo "ho so cot" 4 trang thai (bitmask 2 o) (loi giai mau: cong thuc f[i-1] + 2 f[i-2]).
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py              -> sinh ca 3 bai (~10 giay)
import os, random, sys
from collections import deque

GOC = 'test'

def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

# ---------------- SONT ----------------
def dap_an_sont(qs):
    M = max(r for l, r in qs)
    nt = [True] * (M + 1); nt[0] = False
    if M >= 1:
        nt[1] = False
    for i in range(2, int(M ** 0.5) + 1):
        if nt[i]:
            for j in range(i * i, M + 1, i):
                nt[j] = False
    s = [0] * (M + 1)
    for x in range(1, M + 1):
        s[x] = s[x - 1] + nt[x]
    return '\n'.join(str(s[r] - s[l - 1]) for l, r in qs) + '\n'

def sinh_sont():
    for so in range(1, 11):
        if so == 1:
            qs = [(1, 10), (11, 20), (2, 2), (1, 1)]                          # vi du: 4 4 1 0
        elif so <= 4:
            qs = []
            for _ in range(100):
                l = random.randint(1, 1000); qs.append((l, random.randint(l, 1000)))
        elif so <= 7:
            qs = []
            for _ in range(1000):
                l = random.randint(1, 10**5); qs.append((l, random.randint(l, 10**5)))
        else:
            qs = []
            for _ in range(10**5):
                l = random.randint(1, 10**6) if so != 10 else random.randint(1, 10)
                qs.append((l, random.randint(l, 10**6) if so != 9 else min(10**6, l + random.randint(0, 100))))
        inp = f'{len(qs)}\n' + ''.join(f'{l} {r}\n' for l, r in qs)
        ghi('SONT', so, inp, dap_an_sont(qs))

# ---------------- NOIMANG ----------------
def dap_an_noimang(n, canh):
    adj = [[] for _ in range(n + 1)]
    for u, v in canh:
        adj[u].append(v); adj[v].append(u)
    seen = [False] * (n + 1); cum = 0; lon = 0
    for s in range(1, n + 1):
        if not seen[s]:
            cum += 1; seen[s] = True; q = deque([s]); dem = 0
            while q:
                u = q.popleft(); dem += 1
                for v in adj[u]:
                    if not seen[v]:
                        seen[v] = True; q.append(v)
            lon = max(lon, dem)
    return f'{cum - 1}\n{lon}\n'

def sinh_noimang():
    for so in range(1, 11):
        if so == 1:
            n = 6; canh = [(1, 2), (2, 3), (4, 5), (5, 5)]                    # vi du: 2 va 3
        elif so == 2:
            n = 1; canh = []
        elif so <= 4:
            n = 100; canh = [tuple(random.sample(range(1, n + 1), 2)) for _ in range(random.randint(10, 80))]
        elif so <= 7:
            n = 5000; canh = [(random.randint(1, n), random.randint(1, n)) for _ in range([1000, 4000, 20000][so - 5])]
        else:
            n = 2 * 10**5
            if so == 8:
                canh = [(random.randint(1, n), random.randint(1, n)) for _ in range(n)]
            elif so == 9:                                                     # mot chuoi dai: bay de quy
                p = list(range(1, n + 1)); random.shuffle(p)
                canh = [(p[i], p[i + 1]) for i in range(n - 1)]
            else:
                canh = [(1, 2)] * n                                           # canh trung lap
        inp = f'{n} {len(canh)}\n' + ''.join(f'{u} {v}\n' for u, v in canh)
        ghi('NOIMANG', so, inp, dap_an_noimang(n, canh))

# ---------------- LATGACH ----------------
def dap_an_latgach(ns):
    MOD = 10**9 + 7
    M = max(ns)
    # QHD "ho so cot": dp[mask] = so cach khi cac cot truoc da kin, cot hien tai da bi lap san cac o trong mask
    # (bit 0 = o tren, bit 1 = o duoi). Tu mask cu sinh mask cua cot sau bang cach lap not cot hien tai.
    #   0 (cot sach): 1 gach doc -> 0; 2 gach ngang -> 3; 1 gach 2x2 -> 3
    #   1 (tren da lap): o duoi dat gach ngang -> 2;  2 (duoi da lap): o tren dat gach ngang -> 1
    #   3 (kin): cot sau sach -> 0
    chuyen = {0: [0, 3, 3], 1: [2], 2: [1], 3: [0]}
    kq = [0] * (M + 1)
    dp = [1, 0, 0, 0]
    kq[0] = 1
    for i in range(1, M + 1):
        moi = [0, 0, 0, 0]
        for m in range(4):
            if dp[m]:
                for nm in chuyen[m]:
                    moi[nm] = (moi[nm] + dp[m]) % MOD
        dp = moi
        kq[i] = dp[0]
    return '\n'.join(str(kq[n]) for n in ns) + '\n'

def sinh_latgach():
    for so in range(1, 11):
        if so == 1:
            ns = [1, 2, 3, 4]                                                 # vi du: 1 3 5 11
        elif so <= 4:
            ns = [random.randint(1, 12) for _ in range(20)]
        elif so <= 7:
            ns = [random.randint(1, 1000) for _ in range(1000)]
        else:
            ns = [random.randint(1, 10**6) for _ in range(10**5)]
            if so == 10:
                ns[0] = 10**6
        inp = f'{len(ns)}\n' + ' '.join(map(str, ns)) + '\n'
        ghi('LATGACH', so, inp, dap_an_latgach(ns))

SINH = {'SONT': sinh_sont, 'NOIMANG': sinh_noimang, 'LATGACH': sinh_latgach}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        random.seed(bai + '-2026')
        SINH[bai]()
        print('Da sinh', bai)

main()
