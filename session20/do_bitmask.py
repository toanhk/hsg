# DO TOC DO QHD BITMASK trong Python: n toi da bao nhieu thi chay kip 1 giay?
#   1) Phan cong n nguoi n viec: dp[mask], O(2^n * n)        -> so sanh 3 cach duyet bit
#   2) Nguoi giao hang (TSP): dp[mask][v], O(2^n * n^2)      -> so sanh bang 2 chieu va mang phang
#   3) Phu tap bang goi (set cover): O(2^n * m)
#   4) Dem thu tu hoc (dem sap xep to-po): O(2^n * n)
# Chay: python do_bitmask.py   (~40 giay). Chay tren may phong thi de biet moc that su.
import random, time

def do(ten, ham, *ts):
    tot = float('inf')
    for _ in range(2):
        t = time.perf_counter(); kq = ham(*ts); tot = min(tot, time.perf_counter() - t)
    print(f'{ten:62s} {tot:.3f} s   (kq = {kq})')
    return tot

def moc():
    s = 0
    for i in range(10**7):
        s += i
    return s

random.seed(1)

# ---------- 1) PHAN CONG ----------
def pc_ngaytho(n, c):
    """Duyet moi j, hoi bit bang if; dem so bit bang bin().count('1')."""
    INF = float('inf')
    dp = [INF] * (1 << n); dp[0] = 0
    for mask in range(1 << n):
        v = dp[mask]
        i = bin(mask).count('1')                  # nguoi thu i (dem tu 0) nhan viec tiep
        row = c[i] if i < n else None
        for j in range(n):
            if not mask >> j & 1:
                nm = mask | 1 << j
                if v + row[j] < dp[nm]:
                    dp[nm] = v + row[j]
    return dp[-1]

def pc_keo(n, c):
    """Keo ve: dp[mask] = min dp[mask bo j] + c[k-1][j] voi j thuoc mask, k = so bit; lay bit thap nhat."""
    INF = float('inf')
    N = 1 << n
    pc = [0] * N
    for m in range(1, N):
        pc[m] = pc[m >> 1] + (m & 1)
    vt = {1 << j: j for j in range(n)}            # luy thua 2 -> chi so bit
    dp = [0] * N
    for mask in range(1, N):
        row = c[pc[mask] - 1]
        best = INF; m = mask
        while m:
            b = m & -m                            # bit thap nhat
            v = dp[mask ^ b] + row[vt[b]]
            if v < best:
                best = v
            m ^= b
        dp[mask] = best
    return dp[-1]

def pc_keo_ds(n, c):
    """Nhu pc_keo nhung duyet j bang danh sach bit (for j in range(n) + if) - de so sanh."""
    INF = float('inf')
    N = 1 << n
    dp = [0] * N
    pc = [0] * N
    for m in range(1, N):
        pc[m] = pc[m >> 1] + (m & 1)
    for mask in range(1, N):
        row = c[pc[mask] - 1]
        best = INF
        for j in range(n):
            if mask >> j & 1:
                v = dp[mask ^ (1 << j)] + row[j]
                if v < best:
                    best = v
        dp[mask] = best
    return dp[-1]

# ---------- 2) TSP ----------
def tsp_2chieu(n, d):
    """dp[mask][v]: xuat phat 0, da tham mask (luon chua 0), dang o v. Day toi."""
    INF = float('inf')
    N = 1 << n
    dp = [[INF] * n for _ in range(N)]
    dp[1][0] = 0
    for mask in range(1, N, 2):                   # mask le = co dinh 0
        row = dp[mask]
        for v in range(n):
            x = row[v]
            if x == INF:
                continue
            dv = d[v]
            for u in range(n):
                if not mask >> u & 1:
                    y = x + dv[u]
                    r = dp[mask | 1 << u]
                    if y < r[u]:
                        r[u] = y
    full = dp[N - 1]
    return min(full[v] + d[v][0] for v in range(1, n))

def tsp_keo(n, d):
    """Keo ve: f[mask][v] = min f[mask bo v][u] + d[u][v], u thuoc mask bo v. Duyet bit bang danh sach."""
    INF = float('inf')
    N = 1 << n
    dt = [list(col) for col in zip(*d)]           # dt[v][u] = d[u][v]
    f = [None] * N
    f[1] = [0] + [INF] * (n - 1)
    bits = [[u for u in range(n) if m >> u & 1] for m in range(N)] if n <= 16 else None
    for mask in range(3, N, 2):
        cur = [INF] * n
        bm = bits[mask]
        for v in bm:
            if v == 0:
                continue
            p = f[mask ^ (1 << v)]
            dv = dt[v]
            best = INF
            for u in bits[mask ^ (1 << v)]:
                y = p[u] + dv[u]
                if y < best:
                    best = y
            cur[v] = best
        f[mask] = cur
    full = f[N - 1]
    return min(full[v] + d[v][0] for v in range(1, n))

def tsp_keo_map(n, d):
    """Keo ve, vong trong thay bang min(map(add, ...)) tren cac u thuoc mask (khong dung dinh vo cuc)."""
    from operator import add
    INF = float('inf')
    N = 1 << n
    dt = [list(col) for col in zip(*d)]
    f = [None] * N
    f[1] = [0] + [INF] * (n - 1)
    for mask in range(3, N, 2):
        cur = [INF] * n
        for v in range(1, n):
            if mask >> v & 1:
                p = f[mask ^ (1 << v)]
                cur[v] = min(map(add, p, dt[v]))  # u ngoai mask co p[u] = INF -> tu loai
        f[mask] = cur
    full = f[N - 1]
    return min(full[v] + d[v][0] for v in range(1, n))

# ---------- 3) SET COVER ----------
def phu(n, goi):
    INF = float('inf')
    N = 1 << n
    dp = [INF] * N; dp[0] = 0
    for mask in range(N):
        x = dp[mask]
        if x == INF:
            continue
        for s, g in goi:
            nm = mask | s
            if x + g < dp[nm]:
                dp[nm] = x + g
    return dp[-1]

# ---------- 4) DEM THU TU HOC ----------
def dem_topo(n, truoc):
    MOD = 10**9 + 7
    N = 1 << n
    vt = {1 << j: j for j in range(n)}
    f = [0] * N; f[0] = 1
    for mask in range(1, N):
        s = 0; m = mask
        while m:
            b = m & -m; m ^= b
            r = mask ^ b                          # hoc mon b CUOI CUNG: moi mon tien quyet cua b phai o r
            if truoc[vt[b]] & r == truoc[vt[b]]:
                s += f[r]
        f[mask] = s % MOD
    return f[-1]

def main():
    print('Moc: 10^7 phep cong trong ham:', end=' ')
    t = time.perf_counter(); moc(); print(f'{time.perf_counter() - t:.3f} s\n')

    for n in (16, 18, 20):
        c = [[random.randint(1, 10**6) for _ in range(n)] for _ in range(n)]
        if n <= 16:
            do(f'PHANCONG n={n}: day toi, bin().count, for j + if', pc_ngaytho, n, c)
        if n <= 18:
            do(f'PHANCONG n={n}: keo ve, for j in range(n) + if', pc_keo_ds, n, c)
        do(f'PHANCONG n={n}: keo ve, tach bit thap nhat m & -m', pc_keo, n, c)
    print()
    for n in (13, 15, 16, 17):
        d = [[0 if i == j else random.randint(1, 10**6) for j in range(n)] for i in range(n)]
        if n <= 15:
            do(f'TSP n={n}: bang 2 chieu, day toi', tsp_2chieu, n, d)
        if n <= 16:
            do(f'TSP n={n}: keo ve, danh sach bit', tsp_keo, n, d)
        do(f'TSP n={n}: keo ve, min(map(add, ...))', tsp_keo_map, n, d)
    print()
    for n, m in ((15, 100), (16, 100), (18, 30)):
        goi = [(random.randint(1, (1 << n) - 1), random.randint(1, 10**6)) for _ in range(m)]
        do(f'COMBO n={n}, m={m}: 2^n * m', phu, n, goi)
    print()
    for n in (16, 18, 20):
        truoc = [0] * n
        for v in range(n):
            for u in range(v):
                if random.random() < 0.15:
                    truoc[v] |= 1 << u
        do(f'LICHHOC n={n}: dem thu tu, tach bit thap nhat', dem_topo, n, truoc)

main()
