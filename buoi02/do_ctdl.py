# DO THOI GIAN CAC THAO TAC CTDL SAN CO TREN MAY PHONG THI
# Chay: python do_ctdl.py   (khoang 10-20 giay)
# Moi phep do chay 3 lan, lay thoi gian nho nhat.
import time, random, heapq, bisect
from collections import deque

N = 10**5           # so thao tac cho cac phep "cham" (O(n) moi lan)
M = 10**6           # so thao tac cho cac phep "nhanh" (O(1) hoac O(log n))

def list_pop0():                    # list.pop(0): moi lan dich ca mang -> O(n)
    a = list(range(N))
    for _ in range(N):
        a.pop(0)

def deque_popleft():                # deque.popleft(): O(1)
    q = deque(range(N))
    for _ in range(N):
        q.popleft()

def list_insert0():                 # list.insert(0, x): O(n)
    a = []
    for i in range(N):
        a.insert(0, i)

def tim_trong_list():               # x in list: duyet tuan tu O(n); chi 10^3 truy van!
    a = list(range(N))
    for x in range(N - 1000, N):
        x in a

def tim_trong_set():                # x in set: bang bam, trung binh O(1); 10^6 truy van
    s = set(range(M))
    for x in range(M):
        x in s

def dict_dem():                     # dem tan suat bang dict.get: 10^6 phan tu
    random.seed(1)
    a = [random.randint(1, 10**5) for _ in range(M)]
    t = time.perf_counter()
    d = {}
    for x in a:
        d[x] = d.get(x, 0) + 1
    return time.perf_counter() - t

def heap_push_pop():                # 10^6 heappush roi 10^6 heappop: O(log n) moi lan
    random.seed(2)
    a = [random.randint(1, 10**9) for _ in range(M)]
    t = time.perf_counter()
    h = []
    for x in a:
        heapq.heappush(h, x)
    for _ in range(M):
        heapq.heappop(h)
    return time.perf_counter() - t

def sap_xep():                      # list.sort() 10^6 so: O(n log n), viet bang C
    random.seed(3)
    a = [random.randint(1, 10**9) for _ in range(M)]
    t = time.perf_counter()
    a.sort()
    return time.perf_counter() - t

def bisect_tim():                   # 10^6 lan bisect tren mang 10^6 phan tu da sap
    a = list(range(0, 2 * M, 2))
    t = time.perf_counter()
    bl = bisect.bisect_left
    for x in range(M):
        bl(a, x)
    return time.perf_counter() - t

def vong_lap_doi():                 # 10^7 phep: vong lap long 3163 x 3163
    k = 3163
    s = 0
    for i in range(k):
        for j in range(k):
            s += j
    return s

def do(ham):
    tot = 1e9
    for _ in range(3):
        t = time.perf_counter()
        r = ham()
        tg = time.perf_counter() - t
        if isinstance(r, float):    # ham tu do phan loi (khong tinh tao du lieu)
            tg = r
        tot = min(tot, tg)
    return tot

def main():
    ds = [('list.pop(0)       x 10^5', list_pop0),
          ('deque.popleft()   x 10^5', deque_popleft),
          ('list.insert(0,x)  x 10^5', list_insert0),
          ('x in list(10^5)   x 10^3', tim_trong_list),
          ('x in set(10^6)    x 10^6', tim_trong_set),
          ('dict dem          x 10^6', dict_dem),
          ('heappush+heappop  x 10^6', heap_push_pop),
          ('list.sort()   10^6 so   ', sap_xep),
          ('bisect_left       x 10^6', bisect_tim),
          ('vong lap long  ~10^7 phep', vong_lap_doi)]
    for ten, ham in ds:
        print(f'{ten}  {do(ham):6.3f} s')

main()
