# SINH TEST cho de kiem tra cuoi giai doan 3 (Do thi co ban): XEPHANG, CUUHOA, TRUNGCHUYEN
# Cau truc thu muc theo Themis: test/XEPHANG/Test01/XEPHANG.INP + XEPHANG.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau de kiem cheo:
#   XEPHANG to-po bang DFS 3 mau + "moi cap ke nhau deu co cung" (loi giai mau dem hang doi Kahn),
#   CUUHOA BFS nhieu nguon voi toa do (i, j) + deque + mang khoang cach 2 chieu (cach "ngay tho"),
#   TRUNGCHUYEN dem so duong ngan nhat theo 2 modulo: v tren moi duong <=> cnt1[v]*cntn[v] == cnt1[n]
#   (loi giai mau dem so nut tren tung tang BFS).
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py              -> sinh ca 3 bai (~25 giay)
#       python sinh_test.py CUUHOA       -> chi sinh bai ke ten
# Moi bai co seed rieng (random.seed('XEPHANG-2026'), ...) nen sinh rieng mot bai hay ca bo deu ra CUNG test.
import os, random, sys
from collections import deque

GOC = 'test'
def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

def de_canh(n, canh):
    return f'{n} {len(canh)}\n' + ''.join(f'{u} {v}\n' for u, v in canh)

# ---------------- XEPHANG ----------------
def dap_an_xephang(n, canh):
    adj = [[] for _ in range(n + 1)]
    for u, v in canh:
        adj[u].append(v)
    mau = [0] * (n + 1); hau = []             # DFS 3 mau khong de quy -> thu tu hau tu
    for s in range(1, n + 1):
        if mau[s]:
            continue
        st = [[s, 0]]; mau[s] = 1
        while st:
            top = st[-1]; u = top[0]
            if top[1] < len(adj[u]):
                v = adj[u][top[1]]; top[1] += 1
                if mau[v] == 1:
                    return '-1\n'                # cung quay ve dinh xam: mau thuan
                if mau[v] == 0:
                    mau[v] = 1; st.append([v, 0])
            else:
                mau[u] = 2; hau.append(u); st.pop()
    tt = hau[::-1]
    co = set(canh)                            # duy nhat <=> moi cap ke nhau trong thu tu deu co cung
    if all((tt[i], tt[i + 1]) in co for i in range(n - 1)):
        return ' '.join(map(str, tt)) + '\n'
    return '0\n'

def bang(n, m, bo=(), vong=None):
    """Xich hv[0] -> hv[1] -> ... (bang that) + cung tien ngau nhien; bo = chi so i bi bo cung hv[i]->hv[i+1];
    vong = (i, j) them cung nguoc hv[j] -> hv[i] (j > i) tao chu trinh."""
    hv = list(range(1, n + 1)); random.shuffle(hv)
    canh = [(hv[i], hv[i + 1]) for i in range(n - 1) if i not in bo]
    da = set(canh); cam = {(hv[i], hv[i + 1]) for i in bo}
    while len(canh) < m - (vong is not None):
        i = random.randrange(n - 1); j = random.randint(i + 1, min(n - 1, i + 50))
        e = (hv[i], hv[j])
        if e not in da and e not in cam:
            da.add(e); canh.append(e)
    if vong:
        canh.append((hv[vong[1]], hv[vong[0]]))
    random.shuffle(canh)
    return canh

def sinh_xephang():
    for so in range(1, 11):
        if so == 1:
            n, canh = 4, [(1, 2), (2, 3), (1, 3), (3, 4)]           # vi du: 1 2 3 4
        elif so == 2:
            n, canh = 3, [(1, 2), (1, 3)]                           # 2 va 3 doi cho duoc -> 0
        elif so == 3:
            n, canh = 5, [(1, 2), (1, 3), (4, 5), (5, 4)]           # vua mo ho vua mau thuan -> -1
        elif so == 4:
            n = 8; canh = bang(n, 14)
        elif so == 5:
            n = 2000; canh = bang(n, 5000)
        elif so == 6:
            n = 2000; canh = bang(n, 4000, bo={1234})               # thieu dung 1 mat xich -> 0
        elif so == 7:
            n = 2000; canh = bang(n, 4000, bo={3}, vong=(1500, 1900))   # mo ho som, vong muon -> -1
        elif so == 8:
            n = 10**5; canh = bang(n, 2 * 10**5)
        elif so == 9:
            n = 10**5; canh = bang(n, 2 * 10**5, bo={n - 3})        # chi mo ho o gan cuoi -> 0
        else:
            n = 10**5; canh = bang(n, 2 * 10**5, bo={0}, vong=(70000, 70040))
        ghi('XEPHANG', so, de_canh(n, canh), dap_an_xephang(n, canh))

# ---------------- CUUHOA ----------------
def dap_an_cuuhoa(g):
    m, n = len(g), len(g[0])
    d = [[-1] * n for _ in range(m)]
    q = deque()
    for i in range(m):
        for j in range(n):
            if g[i][j] == 'T':
                d[i][j] = 0; q.append((i, j))
    while q:
        i, j = q.popleft()
        for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= x < m and 0 <= y < n and g[x][y] != '#' and d[x][y] < 0:
                d[x][y] = d[i][j] + 1; q.append((x, y))
    khong = tong = 0
    for i in range(m):
        for j in range(n):
            if g[i][j] == 'H':
                if d[i][j] < 0: khong += 1
                else: tong += d[i][j]
    return f'{khong} {tong}\n'

def ngau_nhien(m, n, p_tuong, p_nha, so_tram):
    g = [[('#' if random.random() < p_tuong else ('H' if random.random() < p_nha else '.'))
          for _ in range(n)] for _ in range(m)]
    for _ in range(so_tram):
        g[random.randrange(m)][random.randrange(n)] = 'T'
    return g

def ran(m, n, p_nha):
    """Me cung ran: hang le la tuong, chua khe xen ke dau/cuoi -> duong di dai ~ m*n/2."""
    g = [['H' if random.random() < p_nha else '.' for _ in range(n)] for _ in range(m)]
    for i in range(1, m, 2):
        g[i] = ['#'] * n
        g[i][n - 1 if i % 4 == 1 else 0] = '.'
    return g

def sinh_cuuhoa():
    for so in range(1, 11):
        if so == 1:
            g = [list('T..#H'), list('.#.#.'), list('H...H'), list('##.#T')]   # vi du
        elif so == 2:
            g = ngau_nhien(20, 30, 0.2, 0.3, 0)                       # khong co tram nao
        elif so == 3:                                                 # nha bi tuong vay kin
            g = ngau_nhien(30, 30, 0.1, 0.1, 3)
            for x, y in ((5, 5), (5, 7), (4, 6), (6, 6)):
                g[x][y] = '#'
            g[5][6] = 'H'
        elif so == 4:
            g = ngau_nhien(30, 30, 0.3, 0.2, 4)
        elif so == 5:
            g = ngau_nhien(1000, 1000, 0.2, 0.1, 1)
        elif so == 6:
            g = ran(1000, 1000, 0.05); g[0][0] = 'T'                  # 1 tram, duong dai 5*10^5
        elif so == 7:
            g = ngau_nhien(1000, 1, 0.0, 0.5, 0); g[0][0] = 'T'       # bang 1 cot
        elif so == 8:
            g = ngau_nhien(1000, 1000, 0.25, 0.2, 1000)
        elif so == 9:
            g = ran(1000, 1000, 0.1)
            for _ in range(50):
                i = 2 * random.randrange(500); g[i][random.randrange(1000)] = 'T'
        else:                                                         # khong tuong, 10^5 tram, nhieu nha
            g = ngau_nhien(1000, 1000, 0.0, 0.5, 10**5)
        g = [''.join(r) for r in g]
        inp = f'{len(g)} {len(g[0])}\n' + '\n'.join(g) + '\n'
        ghi('CUUHOA', so, inp, dap_an_cuuhoa(g))

# ---------------- TRUNGCHUYEN ----------------
def dap_an_trungchuyen(n, canh):
    adj = [[] for _ in range(n + 1)]
    for u, v in canh:
        adj[u].append(v); adj[v].append(u)
    P = (10**9 + 7, 998244353)
    def bfs_dem(s):                           # khoang cach + so duong ngan nhat theo 2 modulo
        d = [-1] * (n + 1); c = [[0] * (n + 1) for _ in P]
        d[s] = 0; c[0][s] = c[1][s] = 1; q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if d[v] < 0:
                    d[v] = d[u] + 1; q.append(v)
                if d[v] == d[u] + 1:
                    for k in range(2):
                        c[k][v] = (c[k][v] + c[k][u]) % P[k]
        return d, c
    d1, c1 = bfs_dem(1)
    if d1[n] < 0:
        return '-1\n'
    dn, cn = bfs_dem(n)
    D = d1[n]
    tren = [v for v in range(1, n + 1) if d1[v] >= 0 and d1[v] + dn[v] == D]
    # v tren MOI duong <=> (so duong 1->v) * (so duong v->n) == tong so duong 1->n
    moi = [v for v in tren if all(c1[k][v] * cn[k][v] % P[k] == c1[k][n] for k in range(2))]
    return f'{D} {len(tren)} {len(moi)}\n'

def tron_nhan(n, canh):
    """Doi ten ngau nhien cac nut 2..n-1 (giu 1 va n) de khong lo cau truc."""
    p = list(range(2, n)); random.shuffle(p)
    ten = [0, 1] + p + [n]
    canh = [(ten[u], ten[v]) if random.random() < 0.5 else (ten[v], ten[u]) for u, v in canh]
    random.shuffle(canh)
    return canh

def luoi(R, C):
    """Luoi R x C, nut 1 o goc tren-trai, nut R*C o goc duoi-phai."""
    id_ = lambda i, j: i * C + j + 1
    canh = [(id_(i, j), id_(i, j + 1)) for i in range(R) for j in range(C - 1)]
    canh += [(id_(i, j), id_(i + 1, j)) for i in range(R - 1) for j in range(C)]
    return canh

def chuoi_kim_cuong(n, rong_max):
    """1 -> [nhom nut] -> nut co chai -> [nhom nut] -> ... -> n. Nhom rong 1 cung la nut co chai."""
    canh = []; truoc = [1]; v = 2
    while v < n:
        k = min(random.randint(1, rong_max), n - v)
        nhom = list(range(v, v + k)); v += k
        for x in nhom:
            canh.append((random.choice(truoc), x))
        for x in truoc:
            canh.append((x, random.choice(nhom)))
        truoc = nhom
    for x in truoc:
        canh.append((x, n))
    return canh

def sinh_trungchuyen():
    for so in range(1, 11):
        if so == 1:
            n, canh = 6, [(1, 2), (1, 3), (2, 4), (3, 4), (4, 6), (4, 5), (5, 6)]   # vi du: 3 5 3
        elif so == 2:
            n, canh = 5, [(1, 2), (2, 3), (4, 5)]                                   # khong toi n -> -1
        elif so == 3:
            n, canh = 1, []                                                         # n = 1: 0 1 1
        elif so == 4:
            n = 10; canh = tron_nhan(n, [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (4, 6), (5, 10), (6, 10),
                                         (2, 7), (7, 8), (8, 9), (9, 10)])          # 4 7 3
        elif so == 5:
            n = 1000; canh = tron_nhan(n, [e for e in luoi(25, 40) if random.random() < 0.8])
        elif so == 6:
            n = 1000; canh = tron_nhan(n, luoi(25, 40))                              # B = 2
        elif so == 7:
            n = 1000; canh = tron_nhan(n, chuoi_kim_cuong(n, 4))
        elif so == 8:
            n = 200 * 375; canh = tron_nhan(n, luoi(200, 375))                       # 149 425 canh
        elif so == 9:
            n = 7 * 10**4; canh = tron_nhan(n, chuoi_kim_cuong(n, 2))
        else:
            n = 200 * 375; canh = luoi(200, 375)                                     # luoi bi duc lo
            vien = lambda u: u <= 375 or u % 375 == 0                               # hang dau, cot cuoi
            canh = tron_nhan(n, [e for e in canh if random.random() < 0.8 or (vien(e[0]) and vien(e[1]))])
        ghi('TRUNGCHUYEN', so, de_canh(n, canh), dap_an_trungchuyen(n, canh))

SINH = {'XEPHANG': sinh_xephang, 'CUUHOA': sinh_cuuhoa, 'TRUNGCHUYEN': sinh_trungchuyen}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        random.seed(bai + '-2026')
        SINH[bai]()
        print('Da sinh', bai)

main()
