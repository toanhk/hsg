# SINH TEST cho de kiem tra cuoi giai doan 4 (thi thu nua chang, 150 phut): DONGHANG, MOTUYEN, PHANCUM
# Cau truc thu muc theo Themis: test/DONGHANG/Test01/DONGHANG.INP + DONGHANG.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau de kiem cheo:
#   DONGHANG QHD "day toi" (tu f[j] cap nhat cac f[i] phia sau) thay vi "keo ve",
#   MOTUYEN Dijkstra MOT lan tren do thi trang thai (nut, da dung tuyen moi chua) de lay thoi gian tot nhat,
#     roi tim so hieu nho nhat dat thoi gian do,
#   PHANCUM Kruskal tren do thi day du, dung khi con k thanh phan (loi giai mau dung Prim O(n^2)).
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py              -> sinh ca 3 bai (~30 giay)
#       python sinh_test.py PHANCUM      -> chi sinh bai ke ten
# Moi bai co seed rieng (random.seed('DONGHANG-2026'), ...) nen sinh rieng mot bai hay ca bo deu ra CUNG test.
import os, random, sys, heapq

GOC = 'test'

def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

# ---------------- DONGHANG ----------------
def dap_an_donghang(n, K, W, a):
    INF = float('inf')
    f = [INF] * (n + 1); f[0] = 0
    for j in range(n):                       # xe moi bat dau tu kien j+1
        if f[j] == INF:
            continue
        s = 0; mx = 0
        for i in range(j + 1, min(n, j + K) + 1):
            s += a[i - 1]
            if s > W:
                break
            mx = max(mx, a[i - 1])
            if f[j] + mx < f[i]:
                f[i] = f[j] + mx
    return f'{f[n]}\n'

def sinh_donghang():
    for so in range(1, 11):
        if so == 1:
            n, K, W, a = 6, 3, 10, [2, 5, 3, 7, 1, 1]                  # vi du: 12
        elif so == 2:
            n, K, W, a = 4, 2, 100, [1, 9, 9, 1]                        # tham lam sai: 11
        elif so == 3:
            n = 15; K = random.randint(2, 6); W = 30; a = [random.randint(1, 15) for _ in range(n)]
        elif so == 4:
            n = 15; K = 15; W = 10**9; a = [random.randint(1, 10**9 // 15) for _ in range(n)]
        elif so == 5:
            n = 2000; K = 2000; W = 10**9; a = [random.randint(1, 10**6) for _ in range(n)]
        elif so == 6:
            n = 2000; K = 50; W = 300; a = [random.randint(1, 100) for _ in range(n)]
        elif so == 7:
            n = 2000; K = 1; W = 10; a = [random.randint(1, 10) for _ in range(n)]    # moi kien mot xe
        elif so == 8:
            n = 10**5; K = 20; W = 10**9; a = [random.randint(1, 10**9 // 20) for _ in range(n)]
        elif so == 9:
            n = 10**5; K = 20; W = 10**6; a = [random.randint(1, 10**6) for _ in range(n)]
        else:                                                           # lon nho xen ke
            n = 10**5; K = 20; W = 5 * 10**9 // 10
            a = [random.randint(10**8, W) if random.random() < 0.1 else random.randint(1, 1000) for _ in range(n)]
        inp = f'{n} {K} {W}\n' + ' '.join(map(str, a)) + '\n'
        ghi('DONGHANG', so, inp, dap_an_donghang(n, K, W, a))

# ---------------- MOTUYEN ----------------
def dap_an_motuyen(n, canh, de_xuat):
    INF = 1 << 62
    adj = [[] for _ in range(2 * (n + 1))]   # dinh v (chua dung tuyen moi) va v + n + 1 (da dung)
    for u, v, w in canh:
        for t in (0, n + 1):
            adj[u + t].append((v + t, w)); adj[v + t].append((u + t, w))
    for u, v, c in de_xuat:
        adj[u].append((v + n + 1, c)); adj[v].append((u + n + 1, c))
    d = [INF] * (2 * (n + 1)); d[1] = 0; pq = [(0, 1)]
    while pq:
        du, u = heapq.heappop(pq)
        if du > d[u]:
            continue
        for v, w in adj[u]:
            if du + w < d[v]:
                d[v] = du + w; heapq.heappush(pq, (d[v], v))
    best = min(d[n], d[2 * n + 1])
    if best >= INF:
        return '-1\n'
    if d[n] == best:
        return f'{best} 0\n'
    # tim so hieu nho nhat dat best: can khoang cach toi n tren lop "da dung" -> Dijkstra nguoc tu n
    dn = [INF] * (n + 1); dn[n] = 0; pq = [(0, n)]
    while pq:
        du, u = heapq.heappop(pq)
        if du > dn[u]:
            continue
        for v, w in adj[u]:
            if v <= n and du + w < dn[v]:
                dn[v] = du + w; heapq.heappush(pq, (dn[v], v))
    for i, (u, v, c) in enumerate(de_xuat, 1):
        if min(d[u] + dn[v], d[v] + dn[u]) + c == best:
            return f'{best} {i}\n'

def ngau_nhien(n, m, wmax, lien_thong=True):
    canh = []
    if lien_thong:
        hv = list(range(1, n + 1)); random.shuffle(hv)
        for i in range(1, n):
            canh.append((hv[i], hv[random.randrange(i)], random.randint(1, wmax)))
    while len(canh) < m:
        u, v = random.sample(range(1, n + 1), 2)
        canh.append((u, v, random.randint(1, wmax)))
    random.shuffle(canh)
    return canh

def sinh_motuyen():
    for so in range(1, 11):
        if so == 1:
            n = 5; canh = [(1, 2, 4), (2, 3, 4), (3, 5, 4), (1, 4, 3), (4, 5, 10)]
            dx = [(2, 5, 5), (1, 3, 3), (4, 3, 1)]                    # vi du: 7 2
        elif so == 2:                                                 # 1 va n khong noi, de xuat noi duoc
            n = 6; canh = [(1, 2, 1), (2, 3, 1), (4, 5, 1), (5, 6, 1)]
            dx = [(1, 4, 9), (3, 4, 2), (2, 5, 3)]
        elif so == 3:                                                 # khong de xuat nao tot hon -> 0
            n = 50; canh = ngau_nhien(n, 200, 10)
            dx = [(u, v, 10**9) for u, v in (random.sample(range(1, n + 1), 2) for _ in range(200))]
        elif so == 4:
            n = 100; canh = ngau_nhien(n, 200, 1000)
            dx = [tuple(random.sample(range(1, n + 1), 2)) + (random.randint(1, 1000),) for _ in range(200)]
        elif so <= 7:                                                 # subtask 2: moi thoi gian = 1
            n = 10**5; m = 10**5
            canh = [(u, v, 1) for u, v, w in ngau_nhien(n, m, 1, lien_thong=(so != 6))]
            dx = [tuple(random.sample(range(1, n + 1), 2)) + (1,) for _ in range(10**5)]
            if so == 7:                                               # do thi duong thang, k de xuat
                canh = [(i, i + 1, 1) for i in range(1, n)]
        else:
            n = 10**5; m = 10**5
            wmax = 10**9 if so != 9 else 3
            canh = ngau_nhien(n, m, wmax)
            dx = [tuple(random.sample(range(1, n + 1), 2)) + (random.randint(1, wmax),) for _ in range(10**5)]
            if so == 10:                                              # duong 1 -> n rat dai, nhieu tuyen tat
                canh = [(i, i + 1, random.randint(10**8, 10**9)) for i in range(1, n)] + canh[:1]
        inp = f'{n} {len(canh)} {len(dx)}\n' + ''.join(f'{u} {v} {w}\n' for u, v, w in canh) \
              + ''.join(f'{u} {v} {c}\n' for u, v, c in dx)
        ghi('MOTUYEN', so, inp, dap_an_motuyen(n, canh, dx))

# ---------------- PHANCUM ----------------
def dap_an_phancum(n, k, P):
    e = sorted((abs(P[i][0] - P[j][0]) + abs(P[i][1] - P[j][1]), i, j) for i in range(n) for j in range(i + 1, n))
    par = list(range(n)); nhom = n
    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    for w, i, j in e:
        a, b = f(i), f(j)
        if a != b:
            if nhom == k:
                return f'{w}\n'
            par[a] = b; nhom -= 1

def sinh_phancum():
    for so in range(1, 11):
        if so == 1:
            n, k = 6, 3; P = [(0, 0), (1, 1), (9, 0), (10, 2), (0, 7), (2, 8)]   # vi du: 7
        elif so == 2:
            n, k = 10, 10; P = [(random.randint(0, 50), random.randint(0, 50)) for _ in range(n)]
        elif so == 3:
            n, k = 10, 2; P = [(random.randint(0, 10**9), random.randint(0, 10**9)) for _ in range(n)]
        elif so == 4:                                                    # co diem trung nhau
            n, k = 10, 4; P = [(random.randint(0, 3), random.randint(0, 3)) for _ in range(n)]
        elif so == 5:
            n, k = 500, 7; P = [(random.randint(0, 10**9), random.randint(0, 10**9)) for _ in range(n)]
        elif so == 6:                                                    # 5 cum ro ret, k = 5
            n, k = 500, 5
            tam = [(random.randint(0, 10**9), random.randint(0, 10**9)) for _ in range(5)]
            P = [(x + random.randint(0, 10**5), y + random.randint(0, 10**5)) for x, y in (random.choice(tam) for _ in range(n))]
            P = [(min(x, 10**9), min(y, 10**9)) for x, y in P]
        elif so == 7:
            n, k = 500, 500; P = [(random.randint(0, 10**6), random.randint(0, 10**6)) for _ in range(n)]
        elif so == 8:
            n, k = 1500, 2; P = [(random.randint(0, 10**9), random.randint(0, 10**9)) for _ in range(n)]
        elif so == 9:
            n, k = 1500, 100; P = [(random.randint(0, 10**9), random.randint(0, 10**9)) for _ in range(n)]
        else:                                                            # tren mot duong thang
            n, k = 1500, 750; P = [(random.randint(0, 10**9), 0) for _ in range(n)]
        inp = f'{n} {k}\n' + ''.join(f'{x} {y}\n' for x, y in P)
        ghi('PHANCUM', so, inp, dap_an_phancum(n, k, P))

SINH = {'DONGHANG': sinh_donghang, 'MOTUYEN': sinh_motuyen, 'PHANCUM': sinh_phancum}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        random.seed(bai + '-2026')
        SINH[bai]()
        print('Da sinh', bai)

main()
