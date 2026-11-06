# DO CAI TUI: chi phi mot o QHD cai tui trong Python va cac meo tang toc
# Chay: python do_tui.py   (~5 giay). Chay tren may phong thi de biet moc that su.
import random, time
from itertools import repeat
from operator import add

random.seed(6)

def do(ten, ham, lan=3):
    tot = float('inf')
    for _ in range(lan):
        t = time.perf_counter(); ham(); tot = min(tot, time.perf_counter() - t)
    print(f'{ten:62s} {tot:.3f} s')

n, W = 100, 50000
w = [random.randint(1, 1000) for _ in range(n)]
v = [random.randint(1, 10**9) for _ in range(n)]

def tui01_1mang():                     # chuan: 1 mang, s giam
    f = [0] * (W + 1)
    for i in range(n):
        wi, vi = w[i], v[i]
        for s in range(W, wi - 1, -1):
            x = f[s - wi] + vi
            if x > f[s]:
                f[s] = x
    return f[W]

def tui01_max():                       # viet bang max(): goi ham moi o -> cham hon if
    f = [0] * (W + 1)
    for i in range(n):
        wi, vi = w[i], v[i]
        for s in range(W, wi - 1, -1):
            f[s] = max(f[s], f[s - wi] + vi)
    return f[W]

def tui01_2chieu():                    # bang 2 chieu: them chi phi chep hang + bo nho
    f = [[0] * (W + 1)]
    for i in range(n):
        wi, vi = w[i], v[i]
        tr = f[-1]; hang = tr[:]
        for s in range(wi, W + 1):
            x = tr[s - wi] + vi
            if x > hang[s]:
                hang[s] = x
        f.append(hang)
    return f[n][W]

def tui01_lat():                       # gan ca lat cat: vong trong chay trong C (0/1 tu nhien dung vi ve phai dung f CU)
    f = [0] * (W + 1)
    for i in range(n):
        wi, vi = w[i], v[i]
        f[wi:] = map(max, f[wi:], map(add, f[:W + 1 - wi], repeat(vi)))
    return f[W]

def truyvet_bytearray():               # them mang danh dau lay[i][s] (bytearray) de truy vet
    f = [0] * (W + 1); lay = []
    for i in range(n):
        wi, vi = w[i], v[i]; c = bytearray(W + 1)
        for s in range(W, wi - 1, -1):
            x = f[s - wi] + vi
            if x > f[s]:
                f[s] = x; c[s] = 1
        lay.append(c)
    return f[W]

def tuivohan():
    f = [0] * (W + 1)
    for i in range(n):
        wi, vi = w[i], v[i]
        for s in range(wi, W + 1):
            x = f[s - wi] + vi
            if x > f[s]:
                f[s] = x
    return f[W]

a = [random.randint(1, 2000) for _ in range(500)]
NUA = sum(a) // 2

def chiakeo_bytearray():               # tap tong: vong lap bytearray, chi lam 50 goi (500 goi ~ 10 lan lau hon)
    d = bytearray(NUA + 1); d[0] = 1
    for x in a[:50]:
        for s in range(NUA, x - 1, -1):
            if d[s - x]:
                d[s] = 1

def chiakeo_bitset():                  # tap tong: so nguyen lon lam bitset, du 500 goi
    mn = (1 << (NUA + 1)) - 1; b = 1
    for x in a:
        b = (b | (b << x)) & mn
    return b.bit_length() - 1

print(f'Cai tui n = {n}, W = {W}  (n * W = {n * W:,} o)')
do('0/1, 1 mang, s giam, if (TUI01.py)', tui01_1mang)
do('0/1, 1 mang, f[s] = max(f[s], ...)', tui01_max)
do('0/1, bang 2 chieu (TUI01_2chieu.py)', tui01_2chieu, lan=1)
do('0/1, gan lat cat map(max, ...) (vong trong trong C)', tui01_lat)
do('0/1 + mang lay[] bytearray de truy vet (TRUYVET.py)', truyvet_bytearray)
do('khong gioi han, s tang (TUIVOHAN.py)', tuivohan)
print(f'Tap tong: 500 goi, tong/2 = {NUA:,}')
do('bytearray, 50 goi dau (= 1/10 bai)', chiakeo_bytearray, lan=1)
do('so nguyen lon bits |= bits << a, du 500 goi (CHIAKEO.py)', chiakeo_bitset)
