# DO LOANG TREN LUOI: cung mot bai "BFS tu o (0,0) tren bang 1000 x 1000 (10^6 o), 25% o cam"
# viet theo nhieu cach de thay cach nao Python chay kip 1 giay.
# Chay: python do_loang.py   (~15 giay). Chay tren may phong thi de biet moc that su.
import random, time
from collections import deque

def do(ten, ham, lan=3):
    tot = float('inf')
    for _ in range(lan):
        t = time.perf_counter(); kq = ham(); tot = min(tot, time.perf_counter() - t)
    print(f'{ten:64s} {tot:.3f} s   (kq = {kq})')

random.seed(1)
M = N = 1000
luoi = [bytes(random.choice(b'....#') if random.random() < 0.95 else 35 for _ in range(N))
        for _ in range(M)]                       # 46 '.', 35 '#'  (~24% o cam)
luoi[0] = b'.' + luoi[0][1:]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 1) Kieu "sach giao khoa": deque cac tuple (i, j), mang dist 2 chieu, kiem tra bien 4 lan
def b1():
    dist = [[-1] * N for _ in range(M)]
    dist[0][0] = 0
    q = deque([(0, 0)])
    while q:
        i, j = q.popleft()
        for k in range(4):
            u, v = i + dx[k], j + dy[k]
            if 0 <= u < M and 0 <= v < N and luoi[u][v] == 46 and dist[u][v] == -1:
                dist[u][v] = dist[i][j] + 1
                q.append((u, v))
    return max(max(r) for r in dist)

# 2) Ma hoa o thanh so p = i*N + j (khong vien), van kiem tra bien bang i, j = divmod
def b2():
    o = b''.join(luoi)
    dist = [-1] * (M * N)
    dist[0] = 0
    q = deque([0])
    while q:
        p = q.popleft()
        i, j = divmod(p, N)
        d = dist[p] + 1
        if i > 0 and o[p - N] == 46 and dist[p - N] < 0: dist[p - N] = d; q.append(p - N)
        if i < M - 1 and o[p + N] == 46 and dist[p + N] < 0: dist[p + N] = d; q.append(p + N)
        if j > 0 and o[p - 1] == 46 and dist[p - 1] < 0: dist[p - 1] = d; q.append(p - 1)
        if j < N - 1 and o[p + 1] == 46 and dist[p + 1] < 0: dist[p + 1] = d; q.append(p + 1)
    return max(dist)

# Luoi co VIEN: them 1 hang/cot '#' quanh bang, W = N + 2. O vien coi nhu "da tham" -> khong
# can kiem tra bien nua. dist o cam/vien dat san = -2 (khac -1) de chi 1 phep so sanh.
W = N + 2
def lam_vien():
    dist = [-2] * ((M + 2) * W)
    for i in range(M):
        r = luoi[i]; goc = (i + 1) * W + 1
        for j in range(N):
            if r[j] == 46:
                dist[goc + j] = -1
    return dist

def lam_vien_nhanh():                             # cung viec tren nhung chay trong C
    s = b'#' * W + b''.join(b'#' + r + b'#' for r in luoi) + b'#' * W
    return [-1 if c == 46 else -2 for c in s]

# 3) Co vien + deque + vong for qua 4 huong
def b3():
    dist = lam_vien_nhanh()
    s = W + 1
    dist[s] = 0
    q = deque([s])
    huong = (-W, W, -1, 1)
    while q:
        p = q.popleft()
        d = dist[p] + 1
        for h in huong:
            v = p + h
            if dist[v] == -1:
                dist[v] = d
                q.append(v)
    return max(dist)

# 4) Co vien + BFS THEO TANG (list "tang hien tai" -> "tang ke tiep"), khong can luu dist moi o
#    rieng: biet so tang la biet khoang cach
def b4():
    dist = lam_vien_nhanh()
    s = W + 1
    dist[s] = 0
    tang = [s]; d = 0
    while tang:
        d += 1
        ke = []
        for p in tang:
            for v in (p - W, p + W, p - 1, p + 1):
                if dist[v] == -1:
                    dist[v] = d
                    ke.append(v)
        tang = ke
    return d - 1

# 5) Co vien + list lam hang doi, "for p in q" trong luc q.append (Python cho phep, list dai dan)
def b5():
    dist = lam_vien_nhanh()
    s = W + 1
    dist[s] = 0
    q = [s]
    for p in q:
        d = dist[p] + 1
        for v in (p - W, p + W, p - 1, p + 1):
            if dist[v] == -1:
                dist[v] = d
                q.append(v)
    return max(dist)

# 6) Dem thanh phan lien thong (dem dao): DFS bang ngan xep, co vien, danh dau tham ngay khi day vao
def c1():
    s = bytearray(b'#' * W + b''.join(b'#' + r + b'#' for r in luoi) + b'#' * W)
    dem = 0
    for goc in range(len(s)):
        if s[goc] != 46:
            continue
        dem += 1
        s[goc] = 35
        st = [goc]
        while st:
            p = st.pop()
            for v in (p - W, p + W, p - 1, p + 1):
                if s[v] == 46:
                    s[v] = 35
                    st.append(v)
    return dem

# 7) Dem thanh phan, nhung DUYET GOC bang s.find(b'.', vi tri) (chay trong C) thay vi for qua 10^6 o
def c2():
    s = bytearray(b'#' * W + b''.join(b'#' + r + b'#' for r in luoi) + b'#' * W)
    dem = 0
    goc = s.find(b'.')
    while goc >= 0:
        dem += 1
        s[goc] = 35
        st = [goc]
        while st:
            p = st.pop()
            for v in (p - W, p + W, p - 1, p + 1):
                if s[v] == 46:
                    s[v] = 35
                    st.append(v)
        goc = s.find(b'.', goc)
    return dem

# 8) Quan ma 8 huong tren ban 1000 x 1000 khong o cam, vien day 2
def m1():
    K = N + 4
    dist = [-2] * (K * 2) + ([-2, -2] + [-1] * N + [-2, -2]) * M + [-2] * (K * 2)
    s = 2 * K + 2
    dist[s] = 0
    huong = (-2 * K - 1, -2 * K + 1, -K - 2, -K + 2, K - 2, K + 2, 2 * K - 1, 2 * K + 1)
    q = [s]
    for p in q:
        d = dist[p] + 1
        for h in huong:
            v = p + h
            if dist[v] == -1:
                dist[v] = d
                q.append(v)
    return max(dist)

do('tao vien: 2 vong for Python', lambda: len(lam_vien()))
do('tao vien: bytes join + list comprehension', lambda: len(lam_vien_nhanh()))
do('BFS 1: deque tuple (i,j), dist 2 chieu, kiem tra bien', b1, lan=1)
do('BFS 2: ma hoa p = i*N+j, divmod kiem tra bien', b2, lan=1)
do('BFS 3: co vien, deque, for qua 4 huong', b3)
do('BFS 4: co vien, BFS theo tang', b4)
do('BFS 5: co vien, list lam hang doi (for p in q)', b5)
do('Dem dao 1: DFS ngan xep, co vien, for qua moi o', c1)
do('Dem dao 2: nhu tren, tim goc bang bytearray.find', c2)
do('Quan ma 8 huong, 10^6 o, vien 2, list lam hang doi', m1)
