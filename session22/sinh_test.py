# SINH TEST buoi 22 - de thi thu so 2 (180 phut): TRAMSAC, LEONUI, CAMERA
# Cau truc thu muc theo Themis: test/TRAMSAC/Test01/TRAMSAC.INP + TRAMSAC.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau de kiem cheo:
#   TRAMSAC hang doi don dieu (deque) lay min cua so (loi giai mau: heapq bo phan tu het han),
#   LEONUI Dijkstra "minimax" (khoang cach = canh lon nhat tren duong) (loi giai mau: Kruskal + DSU),
#   CAMERA QHD cay voi bo trang thai khac: "co camera / duoc cha giam sat / phai nho con".
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py              -> sinh ca 3 bai (~20 giay)
#       python sinh_test.py CAMERA       -> chi sinh bai ke ten
import os, random, sys, heapq
from collections import deque

GOC = 'test'

def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

# ---------------- TRAMSAC ----------------
def dap_an_tramsac(L, P, tram):
    xs = [0] + [x for x, c in tram]
    f = [0] * len(xs)
    dq = deque([0])                                  # chi so j, f[j] tang dan tu dau den cuoi
    INF = float('inf')
    for i in range(1, len(xs)):
        while dq and xs[dq[0]] < xs[i] - L:
            dq.popleft()
        if not dq:
            f[i] = INF
            continue
        f[i] = f[dq[0]] + tram[i - 1][1]
        while dq and f[dq[-1]] >= f[i]:
            dq.pop()
        dq.append(i)
    best = min((f[j] for j in range(len(xs)) if P - xs[j] <= L), default=INF)
    return f'{best if best < INF else -1}\n'

def tram_ngau_nhien(n, P, cmax):
    xs = sorted(random.sample(range(1, P), n))
    return [(x, random.randint(1, cmax)) for x in xs]

def sinh_tramsac():
    for so in range(1, 11):
        if so == 1:                                   # vi du: 16
            L, P = 10, 30; tram = [(5, 3), (8, 10), (12, 4), (18, 7), (24, 2)]
        elif so == 2:                                 # co khoang trong > L: -1
            L, P = 5, 40; tram = [(4, 1), (8, 1), (20, 1), (24, 1), (30, 1)]
        elif so == 3:
            L, P = 30, 200; tram = tram_ngau_nhien(15, P, 100)
        elif so == 4:                                 # L >= P: khong can sac, 0
            L, P = 100, 100; tram = tram_ngau_nhien(15, P, 10**9)
        elif so == 5:
            L, P = 10**6, 10**8; tram = tram_ngau_nhien(5000, P, 10**9)
        elif so == 6:                                 # cua so chua gan het day: O(n^2) vua kip n = 5000
            L, P = 10**9 - 1, 10**9; tram = tram_ngau_nhien(5000, P, 10**9)
        elif so == 7:                                 # bay tham lam: tram xa re thi it, tram gan re nhieu
            P = 5000 * 10; L = 25
            tram = [(10 * i, 1 if i % 2 else 50) for i in range(1, 5000)]
        elif so == 8:
            L, P = 10**9 - 1, 10**9; tram = tram_ngau_nhien(2 * 10**5, P, 10**9)
        elif so == 9:
            L, P = 5 * 10**6, 10**9; tram = tram_ngau_nhien(2 * 10**5, P, 10**9)   # ~1000 tram / cua so
        else:                                         # di duoc gan het roi tac o cuoi: -1
            P = 10**9; L = 10**7
            tram = tram_ngau_nhien(2 * 10**5, P - 2 * 10**7, 10**9)
        inp = f'{len(tram)} {L} {P}\n' + ''.join(f'{x} {c}\n' for x, c in tram)
        ghi('TRAMSAC', so, inp, dap_an_tramsac(L, P, tram))

# ---------------- LEONUI ----------------
def dap_an_leonui(m, n, h):
    N = m * n
    d = [1 << 40] * N; d[0] = 0
    pq = [(0, 0)]
    while pq:
        du, p = heapq.heappop(pq)
        if du > d[p]:
            continue
        if p == N - 1:
            break
        i, j = divmod(p, n)
        for ok, r in ((i > 0, p - n), (i < m - 1, p + n), (j > 0, p - 1), (j < n - 1, p + 1)):
            if ok:
                nd = max(du, abs(h[p] - h[r]))
                if nd < d[r]:
                    d[r] = nd; heapq.heappush(pq, (nd, r))
    return f'{d[N - 1]}\n'

def luoi_con_ran(m, n):
    """Hanh lang hinh con ran do cao thay doi it (+-3), xung quanh la tuong rat cao/rat thap xen ke."""
    h = [random.choice((0, 10**6)) for _ in range(m * n)]
    cur = 500000
    for i in range(m):
        if i % 2 == 0:                               # hang chan: ca hang la hanh lang, chieu doi luan phien
            cols = range(n) if i % 4 == 0 else range(n - 1, -1, -1)
            for j in cols:
                cur += random.randint(-3, 3); h[i * n + j] = cur
        else:                                        # hang le: chi mot o noi xuong, luan phien hai dau
            j = n - 1 if i % 4 == 1 else 0
            cur += random.randint(-3, 3); h[i * n + j] = cur
    return h

def sinh_leonui():
    for so in range(1, 11):
        if so == 1:                                   # vi du: 2
            m, n = 3, 3; h = [1, 2, 9, 9, 4, 9, 5, 6, 7]
        elif so == 2:
            m, n = 1, 1; h = [7]
        elif so == 3:
            m, n = 30, 30; h = [random.randint(0, 10**6) for _ in range(m * n)]
        elif so == 4:
            m, n = 30, 30; h = [random.randint(0, 3) for _ in range(m * n)]
        elif so == 5:
            m, n = 100, 100; h = [random.randint(0, 10**6) for _ in range(m * n)]
        elif so == 6:
            m, n = 1, 100; h = [random.randint(0, 10**6) for _ in range(m * n)]
        elif so == 7:
            m, n = 99, 100; h = luoi_con_ran(m, n)
        elif so == 8:
            m, n = 300, 300; h = [random.randint(0, 10**6) for _ in range(m * n)]
        elif so == 9:                                 # suon doi tron: chenh lech nho, nhieu canh bang nhau
            m, n = 300, 300; h = [min(10**6, i * 1000 + j * 997 + random.randint(0, 50)) for i in range(m) for j in range(n)]
        else:
            m, n = 299, 300; h = luoi_con_ran(m, n)
        inp = f'{m} {n}\n' + ''.join(' '.join(map(str, h[i * n:(i + 1) * n])) + '\n' for i in range(m))
        ghi('LEONUI', so, inp, dap_an_leonui(m, n, h))

# ---------------- CAMERA ----------------
def dap_an_camera(n, c, canh):
    adj = [[] for _ in range(n + 1)]
    for u, v in canh:
        adj[u].append(v); adj[v].append(u)
    par = [0] * (n + 1); seen = [False] * (n + 1); seen[1] = True
    q = deque([1]); order = []
    while q:                                          # thu tu BFS (khac loi giai mau dung ngan xep)
        u = q.popleft(); order.append(u)
        for v in adj[u]:
            if not seen[v]:
                seen[v] = True; par[v] = u; q.append(v)
    INF = 1 << 60
    X = [0] * (n + 1)   # v co camera
    Y = [0] * (n + 1)   # v khong camera, CHA co camera (v da duoc giam sat)
    Z = [0] * (n + 1)   # v khong camera, can it nhat mot con co camera
    for v in reversed(order):
        ch = [u for u in adj[v] if u != par[v]]
        X[v] = c[v - 1] + sum(min(X[u], Y[u]) for u in ch)
        Y[v] = sum(min(X[u], Z[u]) for u in ch)
        if ch:
            s = sum(min(X[u], Z[u]) for u in ch)
            Z[v] = s + max(0, min(X[u] - Z[u] for u in ch))
        else:
            Z[v] = INF
    return f'{min(X[1], Z[1])}\n'

def cay_ngau_nhien(n, kieu='ngau_nhien'):
    p = list(range(1, n + 1)); random.shuffle(p)
    canh = []
    for i in range(1, n):
        if kieu == 'chuoi':
            j = i - 1
        elif kieu == 'sao':
            j = 0
        elif kieu == 'sau_bu':                         # "sau bu": xuong song dai + la treo
            j = i - 1 if i % 3 else i - 2 if i >= 2 else 0
        else:
            j = random.randrange(max(0, i - 5), i) if random.random() < 0.5 else random.randrange(i)
        canh.append((p[i], p[j]))
    random.shuffle(canh)
    return canh

def sinh_camera():
    for so in range(1, 11):
        if so == 1:                                   # vi du: 5
            n = 6; c = [3, 2, 4, 1, 5, 2]; canh = [(1, 2), (1, 3), (3, 4), (3, 5), (5, 6)]
        elif so == 2:
            n = 1; c = [7]; canh = []
        elif so == 3:
            n = 15; c = [random.randint(1, 10**4) for _ in range(n)]; canh = cay_ngau_nhien(n)
        elif so == 4:                                 # sao: tam dat dat
            n = 15; c = [random.randint(1, 20) for _ in range(n)]; canh = cay_ngau_nhien(n, 'sao')
        elif so <= 7:
            n = 10**5; c = [1] * n; canh = cay_ngau_nhien(n, ['ngau_nhien', 'chuoi', 'sau_bu'][so - 5])
        else:
            n = 10**5; c = [random.randint(1, 10**4) for _ in range(n)]
            canh = cay_ngau_nhien(n, ['ngau_nhien', 'chuoi', 'sao'][so - 8])
        inp = f'{n}\n' + ' '.join(map(str, c)) + '\n' + ''.join(f'{u} {v}\n' for u, v in canh)
        ghi('CAMERA', so, inp, dap_an_camera(n, c, canh))

SINH = {'TRAMSAC': sinh_tramsac, 'LEONUI': sinh_leonui, 'CAMERA': sinh_camera}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        random.seed(bai + '-2026')
        SINH[bai]()
        print('Da sinh', bai)

main()
