# DO DFS TREN DO THI LON: n = 10^5 dinh, m = 2*10^5 canh (gioi han chuan cua de cap tinh),
# viet theo nhieu cach de thay cach nao Python chay kip 1 giay, va vi sao KHONG dung de quy.
# Chay: python do_dfs.py   (~10 giay). Chay tren may phong thi de biet moc that su.
import random, subprocess, sys, time
from collections import deque

def do(ten, ham, lan=3):
    tot = float('inf')
    for _ in range(lan):
        t = time.perf_counter(); kq = ham(); tot = min(tot, time.perf_counter() - t)
    print(f'{ten:62s} {tot:.3f} s   (kq = {kq})')

random.seed(1)
N, M = 10**5, 2 * 10**5
canh = [(random.randint(1, N), random.randint(1, N)) for _ in range(M)]
data = (f'{N} {M}\n' + '\n'.join(f'{u} {v}' for u, v in canh) + '\n').encode().split()

# ---------- 1) Doc input + dung danh sach ke ----------
def doc_va_dung_ke():                      # cach chuan: list cua list, append 2 chieu
    n, m = int(data[0]), int(data[1])
    ke = [[] for _ in range(n + 1)]
    for i in range(2, 2 + 2 * m, 2):
        u = int(data[i]); v = int(data[i + 1])
        ke[u].append(v); ke[v].append(u)
    return len(ke)

def doc_map_int_zip():                     # doi tat ca sang int truoc, roi ghep cap bang zip
    n, m = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + 2 * m]))
    ke = [[] for _ in range(n + 1)]
    for u, v in zip(a[0::2], a[1::2]):
        ke[u].append(v); ke[v].append(u)
    return len(ke)

n = N
a = list(map(int, data[2:2 + 2 * M]))
ke = [[] for _ in range(n + 1)]
for u, v in zip(a[0::2], a[1::2]):
    ke[u].append(v); ke[v].append(u)

# ---------- 2) Dem thanh phan lien thong ----------
def dfs_ngan_xep():                        # danh dau KHI DAY vao ngan xep (moi dinh vao 1 lan)
    tham = [False] * (n + 1); dem = 0
    for s in range(1, n + 1):
        if tham[s]: continue
        dem += 1; tham[s] = True; st = [s]
        while st:
            u = st.pop()
            for v in ke[u]:
                if not tham[v]:
                    tham[v] = True; st.append(v)
    return dem

def dfs_ngan_xep_lay_ra():                 # danh dau KHI LAY RA: mot dinh co the bi day nhieu lan
    tham = [False] * (n + 1); dem = 0
    for s in range(1, n + 1):
        if tham[s]: continue
        dem += 1; st = [s]
        while st:
            u = st.pop()
            if tham[u]: continue
            tham[u] = True
            st.extend(ke[u])
    return dem

def dfs_dung_thu_tu():                     # DFS "that": nho chi so canh dang xet cua tung dinh
    tham = [False] * (n + 1); dem = 0
    it = [0] * (n + 1)
    for s in range(1, n + 1):
        if tham[s]: continue
        dem += 1; tham[s] = True; st = [s]
        while st:
            u = st[-1]; ku = ke[u]
            if it[u] < len(ku):
                v = ku[it[u]]; it[u] += 1
                if not tham[v]:
                    tham[v] = True; st.append(v)
            else:
                st.pop()
    return dem

def bfs_deque():
    tham = [False] * (n + 1); dem = 0
    for s in range(1, n + 1):
        if tham[s]: continue
        dem += 1; tham[s] = True; q = deque([s])
        while q:
            u = q.popleft()
            for v in ke[u]:
                if not tham[v]:
                    tham[v] = True; q.append(v)
    return dem

def de_quy():                              # de quy tren do thi ngau nhien (do sau nho) van chay
    sys.setrecursionlimit(10**6)
    tham = [False] * (n + 1)
    def dfs(u):
        tham[u] = True
        for v in ke[u]:
            if not tham[v]: dfs(v)
    dem = 0
    for s in range(1, n + 1):
        if not tham[s]:
            dem += 1; dfs(s)
    return dem

# ---------- 3) De quy tren DUONG THANG 1-2-...-n: do sau = n ----------
DEQUY_DUONG = r'''
import sys
sys.setrecursionlimit(%s)
n = %d
ke = [[] for _ in range(n + 1)]
for i in range(1, n):
    ke[i].append(i + 1); ke[i + 1].append(i)
tham = [False] * (n + 1)
def dfs(u):
    tham[u] = True
    for v in ke[u]:
        if not tham[v]: dfs(v)
dfs(1)
print('chay xong, tham', sum(tham), 'dinh')
'''

def thu_de_quy(gioi_han, so_dinh):
    r = subprocess.run([sys.executable, '-c', DEQUY_DUONG % (gioi_han, so_dinh)],
                       capture_output=True, text=True)
    if r.returncode == 0:
        kq = r.stdout.strip()
    else:
        dong = (r.stderr.strip().splitlines() or ['(khong co thong bao)'])[-1]
        kq = f'LOI, ma thoat {r.returncode}: {dong[:60]}'
    print(f'  de quy, gioi han {gioi_han:>8}, duong {so_dinh:>6} dinh: {kq}')

def main():
    print(f'Do thi ngau nhien n = {N}, m = {M}')
    do('1a) doc + danh sach ke (int() tung so)', doc_va_dung_ke)
    do('1b) doc + danh sach ke (map int + zip)', doc_map_int_zip)
    do('2a) DFS ngan xep, danh dau khi day vao', dfs_ngan_xep)
    do('2b) DFS ngan xep, danh dau khi lay ra (extend)', dfs_ngan_xep_lay_ra)
    do('2c) DFS dung thu tu (chi so canh it[u])', dfs_dung_thu_tu)
    do('2d) BFS voi deque', bfs_deque)
    do('2e) DFS de quy (do thi ngau nhien, do sau nho)', de_quy)
    print('De quy tren do thi duong thang (do sau = so dinh), chay trong tien trinh rieng:')
    thu_de_quy(1000, 10**5)                # gioi han mac dinh -> RecursionError
    thu_de_quy(10**6, 10**4)
    thu_de_quy(10**6, 10**5)               # co the vo ngan xep C (Segmentation fault)
    thu_de_quy(10**6, 5 * 10**5)

main()
