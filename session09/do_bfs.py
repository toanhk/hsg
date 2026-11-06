# DO BFS: cung mot do thi 2*10^5 dinh, 4*10^5 canh (vo huong), viet theo nhieu cach
# de thay cach nao Python chay kip 1 giay. Them BFS tren "do thi an" 10^6 dinh (bai BIENSO).
# Chay: python do_bfs.py   (~10 giay). Chay tren may phong thi de biet moc that su.
import random, time
from collections import deque

def do(ten, ham, lan=3):
    tot = float('inf')
    for _ in range(lan):
        t = time.perf_counter(); kq = ham(); tot = min(tot, time.perf_counter() - t)
    print(f'{ten:62s} {tot:.3f} s   (kq = {kq})')

random.seed(1)
N, M = 2 * 10**5, 4 * 10**5
canh = [(random.randint(1, N), random.randint(1, N)) for _ in range(M)]
for i in range(1, N):                      # them mot duong noi 1..N de do thi lien thong
    canh[i - 1] = (i, i + 1)
s = (f'{N} {M}\n' + '\n'.join(f'{u} {v}' for u, v in canh) + '\n').encode()
data = s.split()

# 1) Doc + dung danh sach ke: list cua list, append tung canh
def doc_ke():
    n, m = int(data[0]), int(data[1])
    ke = [[] for _ in range(n + 1)]
    for i in range(2, 2 + 2 * m, 2):
        u = int(data[i]); v = int(data[i + 1])
        ke[u].append(v); ke[v].append(u)
    return ke

# 2) Nhu tren nhung doi int ca mang mot lan bang map, roi duyet zip(it, it)
def doc_ke_map():
    a = list(map(int, data))
    n, m = a[0], a[1]
    ke = [[] for _ in range(n + 1)]
    it = iter(a[2:2 + 2 * m])
    for u, v in zip(it, it):
        ke[u].append(v); ke[v].append(u)
    return ke

# 3) Sai lam hay gap: ke = [[]] * (n+1) -> moi dinh dung CHUNG mot list
def ke_nhan_ban():
    ke = [[]] * 4
    ke[1].append(2)
    return ke                              # [[2], [2], [2], [2]] !

KE = doc_ke_map()

# 4) BFS chuan: deque, danh dau dist khi DAY vao hang doi
def bfs_deque():
    dist = [-1] * (N + 1); dist[1] = 0
    q = deque([1])
    while q:
        u = q.popleft(); du = dist[u] + 1
        for v in KE[u]:
            if dist[v] < 0:
                dist[v] = du; q.append(v)
    return max(dist)

# 5) BFS bang list + con tro dau (khong xoa phan tu nao) - nhanh tuong duong deque
def bfs_contro():
    dist = [-1] * (N + 1); dist[1] = 0
    q = [1]; dau = 0
    while dau < len(q):
        u = q[dau]; dau += 1; du = dist[u] + 1
        for v in KE[u]:
            if dist[v] < 0:
                dist[v] = du; q.append(v)
    return max(dist)

# 6) BFS theo tang: duyet ca tang hien tai, sinh tang moi (khong can hang doi)
def bfs_tang():
    dist = [-1] * (N + 1); dist[1] = 0
    tang = [1]; d = 0
    while tang:
        d += 1; moi = []
        for u in tang:
            for v in KE[u]:
                if dist[v] < 0:
                    dist[v] = d; moi.append(v)
        tang = moi
    return max(dist)

# 7) Danh dau khi LAY RA (sai lam pho bien): mot dinh bi day vao hang doi nhieu lan
def bfs_danh_dau_muon():
    dist = [-1] * (N + 1)
    q = deque([(1, 0)]); so_lan_day = 1
    while q:
        u, d = q.popleft()
        if dist[u] >= 0:
            continue
        dist[u] = d
        for v in KE[u]:
            if dist[v] < 0:
                q.append((v, d + 1)); so_lan_day += 1
    return f'{max(dist)}, day {so_lan_day} lan cho {N} dinh'

# 8) BFS bang list.pop(0): moi lan pop dich ca mang -> O(n^2)
def bfs_pop0():
    dist = [-1] * (N + 1); dist[1] = 0
    q = [1]
    while q:
        u = q.pop(0); du = dist[u] + 1
        for v in KE[u]:
            if dist[v] < 0:
                dist[v] = du; q.append(v)
    return max(dist)

# 9) Do thi an (bai BIENSO): dinh 0..10^6, canh x -> x+1, x-1, 2x; BFS tu 1 toi het
L = 10**6
def bfs_an():
    dist = [-1] * (L + 1); dist[1] = 0
    q = deque([1])
    while q:
        x = q.popleft(); d = dist[x] + 1
        for y in (x + 1, x - 1, 2 * x):
            if 0 <= y <= L and dist[y] < 0:
                dist[y] = d; q.append(y)
    return max(dist)

# 10) Nhu tren nhung viet tung nhanh bang if (khong tao tuple moi lan)
def bfs_an_if():
    dist = [-1] * (L + 1); dist[1] = 0
    q = deque([1]); push = q.append; pop = q.popleft
    while q:
        x = pop(); d = dist[x] + 1
        y = x + 1
        if y <= L and dist[y] < 0: dist[y] = d; push(y)
        y = x - 1
        if y >= 0 and dist[y] < 0: dist[y] = d; push(y)
        y = 2 * x
        if y <= L and dist[y] < 0: dist[y] = d; push(y)
    return max(dist)

print('ke = [[]] * 4 roi ke[1].append(2) ->', ke_nhan_ban())
do('doc 4*10^5 canh: int() tung so, append', lambda: len(doc_ke()), lan=1)
do('doc 4*10^5 canh: map(int) ca mang, zip(it, it)', lambda: len(doc_ke_map()), lan=1)
do('BFS deque, danh dau khi day vao', bfs_deque)
do('BFS list + con tro dau', bfs_contro)
do('BFS theo tang (list tang hien tai / tang moi)', bfs_tang)
do('BFS danh dau khi lay ra (sai lam)', bfs_danh_dau_muon, lan=1)
do('BFS list.pop(0)', bfs_pop0, lan=1)
do('BFS do thi an 10^6 dinh: for y in (x+1, x-1, 2x)', bfs_an, lan=1)
do('BFS do thi an 10^6 dinh: 3 lenh if, push/pop gan san', bfs_an_if, lan=1)
