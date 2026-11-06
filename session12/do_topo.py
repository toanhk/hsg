# DO TOC DO DO THI CO HUONG: n = 2*10^5 dinh, m = 2*10^5 canh (DAG ngau nhien + mot duong dai),
# va BFS tren luoi 1000 x 1000 (de chuan bi de kiem tra cuoi giai doan 3).
# Chay: python do_topo.py   (~10 giay). Chay tren may phong thi de biet moc that su.
import random, time, heapq
from collections import deque

def do(ten, ham, lan=3):
    tot = float('inf')
    for _ in range(lan):
        t = time.perf_counter(); kq = ham(); tot = min(tot, time.perf_counter() - t)
    print(f'{ten:62s} {tot:.3f} s   (kq = {kq})')

random.seed(1)
N = M = 2 * 10**5
hv = list(range(1, N + 1)); random.shuffle(hv)          # hv = mot thu tu to-po bi mat
canh = [(hv[i], hv[i + 1]) for i in range(N - 1)]        # mot duong di qua moi dinh (chuoi dai)
while len(canh) < M:
    i, j = sorted(random.sample(range(N), 2))
    canh.append((hv[i], hv[j]))
random.shuffle(canh)
s = (f'{N} {M}\n' + ''.join(f'{u} {v}\n' for u, v in canh)).encode()

# 1) Doc + dung danh sach ke bang list cua list (append)
def doc_ke():
    data = s.split()
    n, m = int(data[0]), int(data[1])
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    for i in range(2, 2 + 2 * m, 2):
        u = int(data[i]); v = int(data[i + 1])
        adj[u].append(v); deg[v] += 1
    return n, adj, deg

def c1():
    return len(doc_ke()[1])

# 2) Doc bang map(int) mot lan roi zip cap (u, v)
def doc_ke2():
    data = list(map(int, s.split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    it = iter(data[2:2 + 2 * m])
    for u, v in zip(it, it):
        adj[u].append(v); deg[v] += 1
    return n, adj, deg

def c2():
    return len(doc_ke2()[1])

n0, ADJ, DEG = doc_ke2()

# 3) Kahn voi deque
def k1():
    deg = DEG[:]
    q = deque(u for u in range(1, n0 + 1) if deg[u] == 0)
    thu_tu = []
    while q:
        u = q.popleft(); thu_tu.append(u)
        for v in ADJ[u]:
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    return len(thu_tu)

# 4) Kahn voi list lam hang doi (con tro dau) - khong can deque
def k2():
    deg = DEG[:]
    q = [u for u in range(1, n0 + 1) if deg[u] == 0]
    for u in q:                       # duyet list trong khi dang append: hop le trong Python
        for v in ADJ[u]:
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    return len(q)

# 5) Kahn voi heapq (thu tu tu dien nho nhat)
def k3():
    deg = DEG[:]
    h = [u for u in range(1, n0 + 1) if deg[u] == 0]
    heapq.heapify(h)
    dem = 0
    while h:
        u = heapq.heappop(h); dem += 1
        for v in ADJ[u]:
            deg[v] -= 1
            if deg[v] == 0:
                heapq.heappush(h, v)
    return dem

# 6) Kahn + QHD duong dai nhat (so hoc ky) trong cung vong
def k4():
    deg = DEG[:]
    f = [1] * (n0 + 1)
    q = [u for u in range(1, n0 + 1) if deg[u] == 0]
    for u in q:
        fu = f[u] + 1
        for v in ADJ[u]:
            if fu > f[v]:
                f[v] = fu
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    return max(f)

# 7) "Mo phong tung hoc ky": moi ky quet lai moi canh -> O(so ky * m)
def k5():
    xong = [False] * (n0 + 1)
    con = n0; ky = 0
    while con and ky < 20:            # chi chay 20 ky de do (that ra can toi 2*10^5 ky!)
        deg = [0] * (n0 + 1)
        for u, v in canh:
            if not xong[u]:
                deg[v] += 1
        moi = [u for u in range(1, n0 + 1) if not xong[u] and deg[u] == 0]
        for u in moi:
            xong[u] = True
        con -= len(moi); ky += 1
    return ky

# 8) DFS 3 mau bang ngan xep tuong minh (tim chu trinh), luu (dinh, chi so canh ke tiep)
def d1():
    mau = [0] * (n0 + 1)              # 0 trang, 1 xam (dang tren ngan xep), 2 den (xong)
    co = False
    for s0 in range(1, n0 + 1):
        if mau[s0]:
            continue
        st = [(s0, 0)]; mau[s0] = 1
        while st:
            u, i = st[-1]
            if i < len(ADJ[u]):
                st[-1] = (u, i + 1)
                v = ADJ[u][i]
                if mau[v] == 0:
                    mau[v] = 1; st.append((v, 0))
                elif mau[v] == 1:
                    co = True
            else:
                mau[u] = 2; st.pop()
    return co

# 9-11) BFS tren luoi 1000 x 1000, 10% o cam, mot nguon o goc
R = C = 1000
luoi = [bytes(random.choice(b'.........#') for _ in range(C)) for _ in range(R)]
W = C + 2                                  # them vien tuong de khoi kiem tra bien
cam = bytearray(b'\x01' * (W * (R + 2)))
for i, r in enumerate(luoi):
    base = (i + 1) * W + 1
    cam[base:base + C] = bytes(1 if ch == 35 else 0 for ch in r)
cam[W + 1] = 0

def g1():                                  # (i, j) + deque + kiem tra bien + dist 2 chieu
    d = [[-1] * C for _ in range(R)]
    d[0][0] = 0; q = deque([(0, 0)]); dem = 0
    while q:
        i, j = q.popleft(); dem += 1
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x, y = i + di, j + dj
            if 0 <= x < R and 0 <= y < C and luoi[x][y] != 35 and d[x][y] < 0:
                d[x][y] = d[i][j] + 1; q.append((x, y))
    return dem

def g2():                                  # ma hoa o = i*W + j, vien tuong, deque
    d = [-1] * len(cam)
    s0 = W + 1; d[s0] = 0; q = deque([s0])
    while q:
        u = q.popleft(); du = d[u] + 1
        for v in (u - W, u + W, u - 1, u + 1):
            if not cam[v] and d[v] < 0:
                d[v] = du; q.append(v)
    return du

def g3():                                  # ma hoa o, vien tuong, BFS theo TUNG LOP bang list
    da = bytearray(cam)                    # da[v] = 1: tuong hoac da tham (gop 2 mang lam 1)
    s0 = W + 1; da[s0] = 1
    lop = [s0]; k = 0; tong = 0
    while lop:
        moi = []
        for u in lop:
            for v in (u - W, u + W, u - 1, u + 1):
                if not da[v]:
                    da[v] = 1; moi.append(v)
        tong += k * len(lop)              # tong khoang cach cua lop k
        lop = moi; k += 1
    return tong

do('doc + danh sach ke: int() tung tu', c1)
do('doc + danh sach ke: map(int) + zip(it, it)', c2)
do('Kahn: deque', k1)
do('Kahn: list lam hang doi (for u in q)', k2)
do('Kahn: heapq (thu tu tu dien nho nhat)', k3)
do('Kahn + QHD so hoc ky trong cung vong', k4)
do('mo phong tung ky: chi 20 ky dau (that can 2*10^5 ky)', k5, lan=1)
do('DFS 3 mau, ngan xep (dinh, chi so)', d1)
do('BFS luoi 10^6: (i,j) + deque + kiem tra bien', g1, lan=1)
do('BFS luoi 10^6: ma hoa i*W+j, vien tuong, deque', g2)
do('BFS luoi 10^6: ma hoa, vien tuong, theo lop, bytearray', g3)
