# SINH TEST cho 6 bai buoi 4 (Tu de quy den QHD)
#   Tren lop : FIBO, CAUTHANG, DOITIEN        Ve nha: CATGO, DEMXAU, VE1
# Cau truc thu muc theo Themis: test/FIBO/Test01/FIBO.INP + FIBO.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau de kiem cheo:
#   FIBO nhan doi nhanh, CAUTHANG QHD "day toi", DOITIEN bang 2 hang, CATGO thu tu vong nguoc lai,
#   DEMXAU cong thuc g[i] = 2g[i-1] - g[i-k-1], VE1 QHD bottom-up tren tap trang thai thua.
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py               -> sinh ca 6 bai (~20 giay)
#       python sinh_test.py FIBO DOITIEN  -> chi sinh cac bai ke ten
import os, random, sys

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

# ---------------- FIBO ----------------
def fib_nhan_doi(n):                  # tra ve (F(n), F(n+1)) mod MOD, O(log n), khong de quy
    a, b = 0, 1                       # (F(0), F(1))
    for bit in bin(n)[2:]:
        c = a * (2 * b - a) % MOD     # F(2k)
        d = (a * a + b * b) % MOD     # F(2k+1)
        a, b = (d, (c + d) % MOD) if bit == '1' else (c, d)
    return a

def sinh_fibo():
    CO = [(1, 0, 0), (1, 1, 1), (1, 25, 25), (1, 30, 30),          # (T, n nho nhat, n lon nhat)
          (1000, 0, 5000), (1000, 4000, 5000), (1000, 5000, 5000),
          (10**5, 0, 10**6), (10**5, 10**6, 10**6), (1, 10**6, 10**6)]
    nho = {}
    for so, (t, lo, hi) in enumerate(CO, 1):
        q = [random.randint(lo, hi) for _ in range(t)]
        if t > 1:
            q[0] = hi
        kq = []
        for n in q:
            if n not in nho:
                nho[n] = fib_nhan_doi(n)
            kq.append(str(nho[n]))
        ghi('FIBO', so, f'{t}\n' + ' '.join(map(str, q)) + '\n', '\n'.join(kq) + '\n')

# ---------------- CAUTHANG ----------------
def dap_an_cauthang(n, hong):
    hs = set(hong)
    f = [0] * (n + 1)
    f[0] = 1
    for i in range(n):                # "day toi": tu bac i cong so cach sang i+1, i+2, i+3
        if f[i]:
            for b in (1, 2, 3):
                j = i + b
                if j <= n and j not in hs:
                    f[j] = (f[j] + f[i]) % MOD
    return f[n]

def sinh_cauthang():
    CO = [(1, 0), (4, 1), (15, 4), (20, 3),
          (10**6, 0), (999999, 0), (500000, 0),
          (10**6, 10**5), (10**6, 5 * 10**5), (10**6, 3)]
    for so, (n, k) in enumerate(CO, 1):
        if so == 10:                  # 3 bac hong lien tiep -> khong len duoc, dap an 0
            hong = [777777, 777778, 777779]
        elif so == 3:                 # nhieu cap bac hong ke nhau nhung khong 3 bac lien tiep
            hong = [3, 4, 9, 10]
        else:
            hong = random.sample(range(1, n), k) if k else []
        ghi('CAUTHANG', so, f'{n} {len(hong)}\n' + ' '.join(map(str, hong)) + '\n',
            str(dap_an_cauthang(n, hong)) + '\n')

# ---------------- DOITIEN ----------------
def dap_an_doitien(c, S):
    truoc = [1] + [0] * S             # hang i-1: chi dung cac loai dau
    for x in c:
        hang = truoc[:]               # hang i: g[i][s] = g[i-1][s] + g[i][s - x]
        for s in range(x, S + 1):
            hang[s] = (truoc[s] + hang[s - x]) % MOD
        truoc = hang
    return truoc[S]

def sinh_doitien():
    CO = [(1, 10), (3, 10), (5, 100), (4, 100),
          (20, 1000), (30, 5000), (30, 5000),
          (30, 10**5), (30, 10**5), (30, 99999)]
    for so, (m, S) in enumerate(CO, 1):
        if so == 1:
            c = [3]                   # 10 khong chia het cho 3 -> 0 cach
        elif so == 2:
            c = [1, 2, 5]
        elif so == 3:
            c = [5, 4, 3, 2, 1]
        elif so == 8:                 # menh gia nho -> vong trong dai nhat (test thoi gian)
            c = random.sample(range(1, 61), m)
        elif so == 10:                # khong co to 1 dong, menh gia le -> nhieu tong khong tao duoc
            c = random.sample(range(101, 2000, 2), m)
        else:
            c = random.sample(range(1, min(S, 500) + 1), m)
        ghi('DOITIEN', so, f'{m} {S}\n' + ' '.join(map(str, c)) + '\n',
            str(dap_an_doitien(c, S)) + '\n')

# ---------------- CATGO ----------------
def dap_an_catgo(p):
    n = len(p) - 1
    f = [0] * (n + 1)
    for L in range(1, n + 1):         # xem nhu cai tui khong gioi han: vat "doan dai L" gia p[L]
        pl = p[L]
        for i in range(L, n + 1):
            v = f[i - L] + pl
            if v > f[i]:
                f[i] = v
    return f[n]

def sinh_catgo():
    CO_N = [1, 4, 10, 15, 500, 1000, 1000, 4000, 4000, 4000]
    for so, n in enumerate(CO_N, 1):
        if so == 2:
            p = [1, 5, 8, 9]                                   # vi du kinh dien: dap an 10 (2 + 2)
        elif so in (7, 10):           # gia tang nhanh hon do dai -> khong cat la tot nhat
            p = [i * i * 37 + random.randint(0, 50) for i in range(1, n + 1)]
        elif so == 9:                 # p[i] = 10^9 cho moi i -> cat doan 1 het: n * 10^9 (so lon)
            p = [10**9] * n
        else:                         # gia ngau nhien quanh i * 10^5, co vai do dai "duoc gia"
            p = [i * 100000 + random.randint(-90000, 90000) for i in range(1, n + 1)]
            for _ in range(max(1, n // 50)):
                L = random.randint(1, n)
                p[L - 1] += random.randint(0, 300000)
        ghi('CATGO', so, f'{n}\n' + ' '.join(map(str, p)) + '\n',
            str(dap_an_catgo([0] + p)) + '\n')

# ---------------- DEMXAU ----------------
def dap_an_demxau(n, k):
    # g[i] = so xau hop le do dai i. i < k: 2^i ; i = k: 2^k - 1 ; i > k: 2g[i-1] - g[i-k-1]
    # (tru di cac xau co dung k so 1 o cuoi ma phan truoc hop le va ket thuc bang 0)
    g = [0] * (n + 1)
    g[0] = 1
    for i in range(1, n + 1):
        if i < k:
            g[i] = g[i - 1] * 2 % MOD
        elif i == k:
            g[i] = (g[i - 1] * 2 - 1) % MOD
        else:
            g[i] = (g[i - 1] * 2 - g[i - k - 1]) % MOD
    return g[n]

def sinh_demxau():
    CO = [(1, 1), (5, 2), (20, 3), (20, 20),
          (5000, 1), (5000, 7), (4000, 4000),
          (10**6, 2), (10**6, 1000), (10**6, 10**6)]
    for so, (n, k) in enumerate(CO, 1):
        ghi('DEMXAU', so, f'{n} {k}\n', str(dap_an_demxau(n, k)) + '\n')

# ---------------- VE1 ----------------
def dap_an_ve1(ds):
    # Gom moi so co the gap: n // (2^a 3^b), roi tinh tu nho den lon (bottom-up tren tap thua)
    tap = set()
    hang = list(ds)
    while hang:
        x = hang.pop()
        if x >= 1 and x not in tap:
            tap.add(x)
            hang.append(x // 2)
            hang.append(x // 3)
    f = {}
    for x in sorted(tap):
        if x <= 3:
            f[x] = 0 if x == 1 else 1
        else:
            f[x] = 1 + min(x % 2 + f[x // 2], x % 3 + f[x // 3])
    return '\n'.join(str(f[x]) for x in ds) + '\n'

def dap_an_ve1_bang(ds):              # QHD bang day du: kiem cheo cong thuc cho cac test n <= 10^6
    m = max(ds)
    f = [0] * (m + 1)
    for i in range(2, m + 1):
        b = f[i - 1]
        if i % 2 == 0: b = min(b, f[i // 2])
        if i % 3 == 0: b = min(b, f[i // 3])
        f[i] = b + 1
    return '\n'.join(str(f[x]) for x in ds) + '\n'

def sinh_ve1():
    for so in range(1, 11):
        if so <= 4:
            hi, t = 100, 10
        elif so <= 7:
            hi, t = 10**6, 200
        else:
            hi, t = 10**18, 200
        ds = [random.randint(1, hi) for _ in range(t)]
        if so == 1:
            ds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        elif so == 4:
            ds[:3] = [100, 99, 97]
        elif so == 7:
            ds[:3] = [10**6, 999999, 3**12]
        elif so == 8:
            ds[:4] = [10**18, 10**18 - 1, 2**59, 3**37]
        elif so == 10:                # so gan luy thua cua 2, 3
            ds = [random.choice([2**random.randint(30, 59), 3**random.randint(20, 37)]) + random.randint(-3, 3)
                  for _ in range(t)]
        out = dap_an_ve1(ds)
        if hi <= 10**6:
            assert out == dap_an_ve1_bang(ds), 'cong thuc VE1 lech QHD bang!'
        ghi('VE1', so, f'{t}\n' + '\n'.join(map(str, ds)) + '\n', out)

SINH = {'FIBO': sinh_fibo, 'CAUTHANG': sinh_cauthang, 'DOITIEN': sinh_doitien,
        'CATGO': sinh_catgo, 'DEMXAU': sinh_demxau, 'VE1': sinh_ve1}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        SINH[bai]()
        print('Da sinh', bai)

main()
