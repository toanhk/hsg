# DO QHD MOT CHIEU: chi phi cac cach viet vong lap QHD tren day 10^6 phan tu trong Python
# Chay: python do_qhd1chieu.py   (~10 giay). Chay tren may phong thi de biet moc that su.
import random, time
from itertools import accumulate, repeat
from operator import add, sub

def do(ten, ham, lan=3):
    tot = float('inf')
    for _ in range(lan):
        t = time.perf_counter(); ham(); tot = min(tot, time.perf_counter() - t)
    print(f'{ten:60s} {tot:.3f} s')

random.seed(1)
N = 10**6
a = [random.randint(-10**9, 10**9) for _ in range(N)]
du_lieu = ('%d\n' % N + ' '.join(map(str, a)) + '\n').encode()

# 0) Doc input: tach + doi so (phan nay tinh vao moi bai)
do('doc 10^6 so: split + map(int)', lambda: list(map(int, du_lieu.split()[1:])))

# 1) KHONGKE: max() so voi if
def khongke_max(a):
    t2 = t1 = 0
    for x in a:
        t2, t1 = t1, max(t1, t2 + x)
    return t1

def khongke_if(a):
    t2 = t1 = 0
    for x in a:
        c = t2 + x
        t2 = t1
        if c > t1:
            t1 = c
    return t1

def khongke_mang(a):                    # dung mang f day du
    n = len(a)
    f = [0] * (n + 2)
    for i in range(n):
        f[i + 2] = max(f[i + 1], f[i] + a[i])
    return f[n + 1]

do('KHONGKE: mang f + max()', lambda: khongke_mang(a))
do('KHONGKE: 2 bien + max()', lambda: khongke_max(a))
do('KHONGKE: 2 bien + if', lambda: khongke_if(a))

# 2) Kadane: vong lap so voi accumulate (ham C)
def kadane_if(a):
    cur = tot = a[0]
    for x in a[1:]:
        cur = cur + x if cur > 0 else x
        if cur > tot:
            tot = cur
    return tot

def kadane_accumulate(a):               # f[i] = max(f[i-1] + a[i], a[i]) viet thanh ham 2 doi so
    return max(accumulate(a, lambda c, x: c + x if c > 0 else x))

def kadane_tien_to(a):                  # max(S[r] - min S[l]) bang 2 lan accumulate (toan ham C)
    s = list(accumulate(a, initial=0))
    thap = accumulate(s, min)           # thap[r] = min(S[0..r])
    return max(map(sub, s[1:], thap))

do('Kadane: vong lap + if', lambda: kadane_if(a))
do('Kadane: accumulate + lambda', lambda: kadane_accumulate(a))
do('Kadane: tien to + accumulate(min) + map(sub)', lambda: kadane_tien_to(a))

# 3) Dem co modulo voi 2 trang thai (TORAO)
MOD = 10**9 + 7
def torao(n, k):
    khac, giong = k, 0
    for _ in range(n - 1):
        khac, giong = (khac + giong) * (k - 1) % MOD, khac
    return khac + giong

do('TORAO: 10^6 buoc, 2 trang thai, % MOD', lambda: torao(N, 10**9))

# 4) ECHNHAY: f[i] = min(f[j] + |h[i] - h[j]|), j = i-k..i-1. Vong trong Python so voi map
h = [random.randint(1, 10**4) for _ in range(10**5)]

def ech_vong(h, k):
    n = len(h)
    f = [0] * n
    for i in range(1, n):
        hi = h[i]
        b = 1 << 60
        for j in range(max(0, i - k), i):
            v = f[j] + abs(hi - h[j])
            if v < b:
                b = v
        f[i] = b
    return f[-1]

def ech_map(h, k):
    n = len(h)
    f = [0] * n
    for i in range(1, n):
        j = max(0, i - k)
        f[i] = min(map(add, f[j:i], map(abs, map(sub, h[j:i], repeat(h[i])))))
    return f[-1]

do('ECHNHAY n=10^5, k=20: vong trong Python', lambda: ech_vong(h, 20), lan=1)
do('ECHNHAY n=10^5, k=20: min(map(...))', lambda: ech_map(h, 20), lan=1)
do('ECHNHAY n=10^5, k=100: vong trong Python', lambda: ech_vong(h, 100), lan=1)
do('ECHNHAY n=10^5, k=100: min(map(...))', lambda: ech_map(h, 100), lan=1)
