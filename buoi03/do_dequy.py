# DO DE QUY: chay tren may phong thi de biet gioi han that su
# Chay: python do_dequy.py   (~5 giay)
import sys, time, threading

def do(ten, ham, lan=3):
    tot = min(_do1(ham) for _ in range(lan))
    print(f'{ten:48s} {tot:.3f} s')

def _do1(ham):
    t = time.perf_counter(); ham(); return time.perf_counter() - t

# 1) Gioi han mac dinh
print('Gioi han de quy mac dinh:', sys.getrecursionlimit())

def sau(k):                      # de quy sau k tang
    return 0 if k == 0 else sau(k - 1) + 1

try:
    sau(5000)
    print('sau(5000): chay duoc')
except RecursionError:
    print('sau(5000): RecursionError (vuot gioi han mac dinh)')

# 2) Tang gioi han: du cho vai chuc nghin tang, nhung ngan xep C co the tran -> chuong trinh chet khong bao loi
sys.setrecursionlimit(10**6)
try:
    sau(50000)
    print('sau(50000) sau khi setrecursionlimit: chay duoc')
except RecursionError:
    print('sau(50000): van RecursionError')

# 3) Cach chay de quy rat sau an toan hon: luong moi voi ngan xep lon
def trong_luong():
    print('sau(500000) trong luong ngan xep 512 MB:', sau(500000))
threading.stack_size(512 * 1024 * 1024)
t = threading.Thread(target=trong_luong); t.start(); t.join()

# 4) Chi phi goi ham: dem 2^20 la cua cay "chon / khong chon" bang de quy vs vong lap
def la_de_quy():
    dem = 0
    def thu(i):
        nonlocal dem
        if i == 20:
            dem += 1; return
        thu(i + 1); thu(i + 1)
    thu(0)

def la_vong_lap():
    dem = 0
    for m in range(1 << 20):
        dem += 1

do('Cay nhi phan 20 tang bang de quy (2^21 loi goi)', la_de_quy)
do('Vong lap 2^20 lan', la_vong_lap)

# 5) Quay lui "chua nho" vs co nho: Fibonacci (mo dau buoi 4)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

from functools import lru_cache
@lru_cache(maxsize=None)
def fib_nho(n):
    return n if n < 2 else fib_nho(n - 1) + fib_nho(n - 2)

do('fib(32) de quy thuan (~7*10^6 loi goi)', lambda: fib(32), lan=1)
do('fib_nho(32) co lru_cache (33 loi goi moi)', lambda: (fib_nho.cache_clear(), fib_nho(32)))
