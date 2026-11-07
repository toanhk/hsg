# SINH TEST buoi 22 - de thi thu so 2 (150 phut): TRAMSAC, LEONUI, XEPLICH
# Cau truc thu muc theo Themis: test/TRAMSAC/Test01/TRAMSAC.INP + TRAMSAC.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau de kiem cheo:
#   TRAMSAC hang doi don dieu (deque) lay min cua so (loi giai mau: heapq bo phan tu het han),
#   LEONUI Dijkstra "minimax" (khoang cach = canh lon nhat tren duong) (loi giai mau: Kruskal + DSU),
#   XEPLICH QHD tu phai sang theo ngay bat dau (loi giai mau: tu trai sang theo ngay ket thuc).
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py              -> sinh ca 3 bai (~20 giay)
#       python sinh_test.py XEPLICH       -> chi sinh bai ke ten
import os, random, sys, heapq, bisect
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

# ---------------- XEPLICH ----------------
def dap_an_xeplich(viec):
    # QHD "tu phai sang": sap theo ngay BAT DAU, g[i] = tot nhat voi cac viec i..n-1
    v = sorted(viec)                                   # (s, e, p)
    starts = [x[0] for x in v]
    n = len(v)
    g = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        s, e, p = v[i]
        j = bisect.bisect_right(starts, e)             # viec dau tien bat dau sau ngay e
        g[i] = max(g[i + 1], p + g[j])
    return f'{g[0]}\n'

def viec_ngau_nhien(n, D, dai, pmax):
    res = []
    for _ in range(n):
        s = random.randint(1, D); e = min(D, s + random.randint(0, dai))
        res.append((s, e, random.randint(1, pmax)))
    return res

def sinh_xeplich():
    for so in range(1, 11):
        if so == 1:                                   # vi du: 10
            viec = [(1, 3, 5), (2, 5, 6), (4, 6, 5), (6, 7, 4)]
        elif so == 2:                                 # bay "e <= s": cac viec noi duoi chung mot ngay
            viec = [(1, 5, 10), (5, 9, 10), (9, 12, 10), (2, 4, 1)]
        elif so == 3:
            viec = viec_ngau_nhien(15, 50, 10, 100)
        elif so == 4:                                 # bay tham lam: viec ngan re, viec dai dat
            viec = [(i, i + 1, 1) for i in range(1, 14, 2)] + [(1, 14, 50)]
        elif so == 5:
            viec = viec_ngau_nhien(5000, 10**9, 10**7, 10**9)
        elif so == 6:
            viec = viec_ngau_nhien(5000, 10**5, 10**5, 10**9)   # viec rat dai, trung nhau nhieu
        elif so == 7:
            viec = viec_ngau_nhien(5000, 20000, 5, 10)
        elif so == 8:
            viec = viec_ngau_nhien(2 * 10**5, 10**9, 10**6, 10**9)
        elif so == 9:
            viec = viec_ngau_nhien(2 * 10**5, 10**9, 10**9, 10**9) # gan nhu moi viec trung nhau
        else:
            viec = [(5, 5, random.randint(1, 10**9)) for _ in range(10**5)] + viec_ngau_nhien(10**5, 10**6, 3, 10**9)
            random.shuffle(viec)
        inp = f'{len(viec)}\n' + ''.join(f'{s} {e} {p}\n' for s, e, p in viec)
        ghi('XEPLICH', so, inp, dap_an_xeplich(viec))

SINH = {'TRAMSAC': sinh_tramsac, 'LEONUI': sinh_leonui, 'XEPLICH': sinh_xeplich}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        random.seed(bai + '-2026')
        SINH[bai]()
        print('Da sinh', bai)

main()
