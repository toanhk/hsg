# DO QHD: so sanh 3 cach tinh Fibonacci va chi phi mot vong lap QHD trong Python
# Chay: python do_qhd.py   (~5 giay). Chay tren may phong thi de biet moc that su.
import sys, time
from functools import lru_cache

MOD = 10**9 + 7

def do(ten, ham, lan=3):
    tot = float('inf')
    for _ in range(lan):
        t = time.perf_counter(); ham(); tot = min(tot, time.perf_counter() - t)
    print(f'{ten:55s} {tot:.3f} s')

# 1) De quy thuan: so loi goi ~ 1.6^n
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

# 2) Co nho (memo): moi n chi tinh 1 lan, nhung van la de quy -> sau n tang
def fib_nho_dict(n):                 # memo bang dict, ham Python thuong
    nho = {0: 0, 1: 1}
    def f(k):
        if k in nho:
            return nho[k]
        r = (f(k - 1) + f(k - 2)) % MOD
        nho[k] = r
        return r
    return f(n)

def fib_nho_lru(n):                  # memo bang lru_cache: goi qua ham C -> gioi han sau rieng
    @lru_cache(maxsize=None)
    def f(k):
        return k if k < 2 else (f(k - 1) + f(k - 2)) % MOD
    return f(n)

# 3) Bang (bottom-up): vong lap tu nho den lon
def fib_bang(n):
    f = [0] * (n + 1)
    if n: f[1] = 1
    for i in range(2, n + 1):
        f[i] = (f[i - 1] + f[i - 2]) % MOD
    return f[n]

# 4) Chi giu 2 so cuoi
def fib_2bien(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % MOD
    return a

do('fib(30) de quy thuan (~2.7*10^6 loi goi)', lambda: fib(30), lan=1)
do('fib(32) de quy thuan (~7*10^6 loi goi)', lambda: fib(32), lan=1)

try:
    fib_nho_dict(5000)
    print('memo de quy n=5000, gioi han mac dinh: chay duoc')
except RecursionError:
    print('memo de quy n=5000, gioi han mac dinh: RecursionError')
sys.setrecursionlimit(10**6)
do('memo dict n=10^5 (sau 10^5 tang, sau setrecursionlimit)', lambda: fib_nho_dict(10**5))
for n in (2000, 5000, 20000):
    try:
        fib_nho_lru(n)
        print(f'lru_cache n={n} sau setrecursionlimit: chay duoc')
    except RecursionError:
        print(f'lru_cache n={n} sau setrecursionlimit: RecursionError (gioi han ngan xep C)')
do('fib_bang(10^6) bang', lambda: fib_bang(10**6))
do('fib_2bien(10^6) hai bien', lambda: fib_2bien(10**6))

# 5) Chi phi 1 "o" QHD dem co modulo: f[s] = (f[s] + f[s - c]) % MOD
def doi_tien(m, S):
    f = [0] * (S + 1); f[0] = 1
    for c in range(1, m + 1):
        for s in range(c, S + 1):
            f[s] = (f[s] + f[s - c]) % MOD
    return f[S]

do('doi tien: 10^6 o (m=10, S=10^5), co % MOD', lambda: doi_tien(10, 10**5))

def doi_tien_tru(m, S):           # thay % bang phep tru co dieu kien
    f = [0] * (S + 1); f[0] = 1
    for c in range(1, m + 1):
        for s in range(c, S + 1):
            v = f[s] + f[s - c]
            f[s] = v - MOD if v >= MOD else v
    return f[S]

do('doi tien: 10^6 o, tru co dieu kien thay %', lambda: doi_tien_tru(10, 10**5))
