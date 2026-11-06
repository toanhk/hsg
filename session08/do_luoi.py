# DO QHD TREN LUOI: cung mot bai "duong di tong lon nhat" tren bang 1000 x 1000 (10^6 o),
# viet theo nhieu cach de thay cach nao Python chay kip 1 giay.
# Chay: python do_luoi.py   (~10 giay). Chay tren may phong thi de biet moc that su.
import random, time
from itertools import accumulate
from operator import add

MOD = 10**9 + 7

def do(ten, ham, lan=3):
    tot = float('inf')
    for _ in range(lan):
        t = time.perf_counter(); kq = ham(); tot = min(tot, time.perf_counter() - t)
    print(f'{ten:62s} {tot:.3f} s   (kq = {kq})')

random.seed(1)
M = N = 1000
a = [[random.randint(-1000, 1000) for _ in range(N)] for _ in range(M)]
cam = [[random.random() < 0.1 for _ in range(N)] for _ in range(M)]
cam[0][0] = cam[M - 1][N - 1] = False
nhiphan = [[1 if random.random() < 0.9 else 0 for _ in range(N)] for _ in range(M)]

# 1) Bang 2 chieu, viet dp[i][j] day du, dung max()
def c1():
    NEG = -10**18
    dp = [[NEG] * N for _ in range(M)]
    dp[0][0] = a[0][0]
    for i in range(M):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            tren = dp[i - 1][j] if i > 0 else NEG
            trai = dp[i][j - 1] if j > 0 else NEG
            dp[i][j] = max(tren, trai) + a[i][j]
    return dp[M - 1][N - 1]

# 2) Bang 2 chieu, gan bi danh hang: tren = dp[i-1], hang = dp[i], so sanh bang if
def c2():
    dp = [[0] * N for _ in range(M)]
    hang = dp[0]; ai = a[0]
    hang[0] = ai[0]
    for j in range(1, N):
        hang[j] = hang[j - 1] + ai[j]
    for i in range(1, M):
        tren = dp[i - 1]; hang = dp[i]; ai = a[i]
        hang[0] = tren[0] + ai[0]
        for j in range(1, N):
            x = tren[j]; y = hang[j - 1]
            hang[j] = (x if x > y else y) + ai[j]
    return dp[M - 1][N - 1]

# 3) Chi giu 1 hang, bien "trai" giu o ben trai, duyet zip(hang cu, hang a)
def c3():
    f = list(accumulate(a[0]))            # hang dau: tong cong don
    for i in range(1, M):
        moi = []; trai = -10**18
        for x, v in zip(f, a[i]):          # x = o ben tren, trai = o ben trai vua tinh
            trai = (x if x > trai else trai) + v
            moi.append(trai)
        f = moi
    return f[-1]

# 4) Dem duong di co o cam: % MOD moi o
def d1():
    f = [0] * N; f[0] = 1
    for i in range(M):
        ci = cam[i]
        for j in range(N):
            if ci[j]:
                f[j] = 0
            elif j:
                f[j] = (f[j] + f[j - 1]) % MOD
    return f[-1]

# 5) Dem duong di co o cam: tru co dieu kien, bien trai, zip
def d2():
    f = [0] * N; f[0] = 1
    for i in range(M):
        moi = []; trai = 0
        for x, c in zip(f, cam[i]):
            if c:
                trai = 0
            else:
                trai += x
                if trai >= MOD: trai -= MOD
            moi.append(trai)
        f = moi
    return f[-1]

# 6) Hinh vuong toan 1: min(3 so) bang ham min()
def h1():
    tren = [0] * (N + 1); best = 0
    for i in range(M):
        hang = [0] * (N + 1); r = nhiphan[i]
        for j in range(1, N + 1):
            if r[j - 1]:
                v = min(tren[j], hang[j - 1], tren[j - 1]) + 1
                hang[j] = v
                if v > best: best = v
        tren = hang
    return best

# 7) Hinh vuong toan 1: min bang if, bien trai / cheo, zip
def h2():
    tren = [0] * (N + 1); best = 0
    for i in range(M):
        hang = [0]; trai = 0; cheo = 0
        for t, b in zip(tren[1:], nhiphan[i]):    # t = o tren, cheo = o tren-trai
            if b:
                v = t if t < trai else trai
                if cheo < v: v = cheo
                v += 1
                if v > best: best = v
            else:
                v = 0
            hang.append(v); trai = v; cheo = t
        tren = hang
    return best

# 8) Mang cong don 2 chieu bang accumulate + map(add) (moi hang chay trong C)
def p1():
    P = [0] * (N + 1)
    for r in a:
        P = list(map(add, P, accumulate(r, initial=0)))
    return P[-1]

# 9) Doc 10^6 so tu bytes
s = ('\n'.join(' '.join(map(str, r)) for r in a)).encode()
def r1():
    return len(s.split())

do('doc + tach 10^6 so (bytes.split)', r1)
do('duong di max: dp[i][j] day du + max()', c1, lan=1)
do('duong di max: bi danh hang, so sanh bang if', c2)
do('duong di max: 1 hang, zip, bien trai', c3)
do('dem duong o cam: % MOD moi o', d1)
do('dem duong o cam: tru co dieu kien, zip, bien trai', d2)
do('hinh vuong toan 1: min() 3 so', h1)
do('hinh vuong toan 1: if, zip, bien trai/cheo', h2)
do('mang cong don 2 chieu: accumulate + map(add)', p1)
