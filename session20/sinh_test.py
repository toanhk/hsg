# SINH TEST cho 6 bai buoi 20 (QHD bitmask)
#   Tren lop : PHANCONG, COMBO, GIAOHANG        Ve nha: GHEPCAP, KHOBAU, LICHHOC
# Cau truc thu muc theo Themis: test/PHANCONG/Test01/PHANCONG.INP + PHANCONG.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau de kiem cheo:
#   PHANCONG day toi (tu dp[mask] giao viec cho nguoi tiep theo) thay vi keo ve,
#   COMBO QHD "theo tung goi" (giong cai tui: voi moi goi, duyet moi mask) thay vi theo mask,
#   GIAOHANG bang 2 chieu day toi thay vi keo ve,
#   GHEPCAP keo ve tren MOI mask (khong dung meo chi xet mask toi duoc),
#   KHOBAU BFS bang deque + toa do (i, j), TSP day toi,
#   LICHHOC day toi: tu f[mask] hoc them mon v co du tien quyet trong mask.
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py                  -> sinh ca 6 bai (~30 giay)
#       python sinh_test.py GIAOHANG KHOBAU  -> chi sinh cac bai ke ten
# Moi bai co seed rieng (random.seed('PHANCONG-2026'), ...) nen sinh rieng mot bai hay ca bo deu ra CUNG test.
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

def ma_tran(a):
    return ''.join(' '.join(map(str, r)) + '\n' for r in a)

# ---------------- PHANCONG ----------------
def dap_an_phancong(n, c):
    INF = float('inf')
    N = 1 << n
    dp = [INF] * N; dp[0] = 0
    for mask in range(N - 1):
        i = bin(mask).count('1')              # nguoi tiep theo
        x = dp[mask]
        for j in range(n):
            if not mask >> j & 1 and x + c[i][j] < dp[mask | 1 << j]:
                dp[mask | 1 << j] = x + c[i][j]
    return f'{dp[N - 1]}\n'

def sinh_phancong():
    for so in range(1, 11):
        if so == 1:
            n, c = 3, [[4, 2, 8], [6, 4, 3], [5, 7, 6]]                         # vi du: 10
        elif so == 2:
            n, c = 1, [[7]]
        else:
            n = {3: 6, 4: 8, 5: 11, 6: 12, 7: 13, 8: 17, 9: 18, 10: 18}[so]
            vmax = 10**6 if so != 6 else 3                                      # so 6: nhieu chi phi bang nhau
            c = [[random.randint(1, vmax) for _ in range(n)] for _ in range(n)]
            if so == 10:                                                        # nguoi i gioi dung viec p[i]
                p = list(range(n)); random.shuffle(p)                           # (bay tham lam theo hang)
                c = [[random.randint(5 * 10**5, 10**6) for _ in range(n)] for _ in range(n)]
                for i in range(n):
                    c[i][p[i]] = random.randint(1, 10**5)
                    c[i][p[(i + 1) % n]] = 1                                    # re hon nhung khong tao hoan vi tot
        ghi('PHANCONG', so, f'{n}\n' + ma_tran(c), dap_an_phancong(n, c))

# ---------------- COMBO ----------------
def dap_an_combo(n, goi):
    INF = float('inf')
    N = 1 << n
    dp = [INF] * N; dp[0] = 0
    for g, mon in goi:                        # moi goi mua toi da 1 lan (mua 2 lan khong co loi)
        s = 0
        for t in mon:
            s |= 1 << (t - 1)
        for mask in range(N - 1, -1, -1):     # duyet nguoc: dp[mask] cu chua dung goi nay
            if dp[mask] + g < dp[mask | s]:
                dp[mask | s] = dp[mask] + g
    return f'{dp[N - 1] if dp[N - 1] < INF else -1}\n'

def goi_ngau_nhien(n, m, kmax, gmax, bo=()):
    ds = []
    con = [t for t in range(1, n + 1) if t not in bo]
    for _ in range(m):
        k = random.randint(1, min(kmax, len(con)))
        ds.append((random.randint(1, gmax), sorted(random.sample(con, k))))
    return ds

def sinh_combo():
    for so in range(1, 11):
        if so == 1:
            n = 4; goi = [(5, [1, 2]), (4, [3]), (7, [2, 3, 4]), (6, [4])]       # vi du: 12
        elif so == 2:
            n = 5; goi = [(3, [1, 2]), (4, [2, 3]), (9, [1, 4])]                # mon 5 khong co -> -1
        elif so == 3:
            n = 8; goi = goi_ngau_nhien(n, 12, 4, 100)
        elif so == 4:
            n = 15; goi = goi_ngau_nhien(n, 15, 6, 10**6)
        elif so == 5:
            n = 10; goi = goi_ngau_nhien(n, 100, 3, 1000)
        elif so == 6:
            n = 10; goi = goi_ngau_nhien(n, 100, 10, 10**6, bo=(7,))            # thieu mon 7 -> -1
        elif so == 7:
            n = 10; goi = goi_ngau_nhien(n, 99, 2, 10**6) + [(10**6, list(range(1, 11)))]
        elif so == 8:                                                           # moi mask deu toi duoc: test cham nhat
            n = 15; goi = [(random.randint(1, 1000), [t]) for t in range(1, n + 1)]
            goi += goi_ngau_nhien(n, 100 - n, 2, 1500)
        elif so == 9:
            n = 15; goi = goi_ngau_nhien(n, 100, 8, 10**6)
        else:                                                                   # goi trung tap, gia khac nhau
            n = 15; goi = goi_ngau_nhien(n, 50, 4, 10**6)
            goi += [(random.randint(1, 10**6), mon) for g, mon in goi]
        random.shuffle(goi)
        inp = f'{n} {len(goi)}\n' + ''.join(f'{g} {len(mon)} ' + ' '.join(map(str, mon)) + '\n' for g, mon in goi)
        ghi('COMBO', so, inp, dap_an_combo(n, goi))

# ---------------- GIAOHANG ----------------
def dap_an_giaohang(n, d):
    if n == 1:
        return '0\n'
    INF = float('inf')
    N = 1 << n
    f = [[INF] * n for _ in range(N)]
    f[1][0] = 0
    for mask in range(1, N, 2):
        for v in range(n):
            x = f[mask][v]
            if x == INF:
                continue
            for u in range(n):
                if not mask >> u & 1 and x + d[v][u] < f[mask | 1 << u][u]:
                    f[mask | 1 << u][u] = x + d[v][u]
    return f'{min(f[N - 1][v] + d[v][0] for v in range(1, n))}\n'

def khoang_cach(n, vmax, doi_xung=False):
    d = [[0 if i == j else random.randint(1, vmax) for j in range(n)] for i in range(n)]
    if doi_xung:
        for i in range(n):
            for j in range(i):
                d[i][j] = d[j][i]
    return d

def mat_phang(n):
    """Diem tren mat phang, khoang cach Manhattan (doi xung, thoa bat dang thuc tam giac)."""
    p = [(random.randint(0, 10**5), random.randint(0, 10**5)) for _ in range(n)]
    return [[abs(a[0] - b[0]) + abs(a[1] - b[1]) for b in p] for a in p]

def sinh_giaohang():
    for so in range(1, 11):
        if so == 1:
            n = 4; d = [[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]   # vi du: 35
        elif so == 2:
            n = 2; d = [[0, 7], [3, 0]]                                         # 10 (bat ban quen duong ve)
        elif so == 3:
            n = 1; d = [[0]]
        elif so == 4:
            n = 9; d = khoang_cach(n, 100)
        elif so == 5:
            n = 12; d = mat_phang(n)
        elif so == 6:
            n = 13; d = khoang_cach(n, 10**6)
        elif so == 7:
            n = 13; d = khoang_cach(n, 5, doi_xung=True)
        elif so == 8:
            n = 16; d = mat_phang(n)
        elif so == 9:                                                           # vong mot chieu re: i -> i+1 gia 1
            n = 16; d = khoang_cach(n, 10**6)
            hv = list(range(1, n)); random.shuffle(hv); hv = [0] + hv
            for i in range(n):
                d[hv[i]][hv[(i + 1) % n]] = 1
        else:
            n = 16; d = khoang_cach(n, 10**6)
        ghi('GIAOHANG', so, f'{n}\n' + ma_tran(d), dap_an_giaohang(n, d))

# ---------------- GHEPCAP ----------------
def dap_an_ghepcap(n, a):
    N = 1 << n
    dp = [0] * N
    for mask in range(3, N):
        if bin(mask).count('1') % 2:
            continue
        i = (mask & -mask).bit_length() - 1
        r = mask ^ (1 << i)
        dp[mask] = max(dp[r ^ (1 << j)] + a[i][j] for j in range(n) if r >> j & 1)
    return f'{dp[N - 1]}\n'

def an_y(n, vmax):
    a = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            a[i][j] = a[j][i] = random.randint(0, vmax)
    return a

def sinh_ghepcap():
    for so in range(1, 11):
        if so == 1:
            n = 4; a = [[0, 5, 3, 4], [5, 0, 6, 2], [3, 6, 0, 7], [4, 2, 7, 0]]  # vi du: 12
        elif so == 2:
            n = 2; a = [[0, 9], [9, 0]]
        elif so == 3:
            n = 10; a = an_y(n, 100)
        elif so == 4:
            n = 12; a = an_y(n, 10**6)
        elif so == 5:
            n = 18; a = an_y(n, 1000)
        elif so == 6:
            n = 18; a = an_y(n, 3)                                              # nhieu cach bang nhau
        elif so == 7:
            n = 18; a = an_y(n, 10**6)
        elif so == 8:
            n = 20; a = an_y(n, 3)
        elif so == 9:                                                           # bay tham lam: nhom 4 ban x,y,z,w
            n = 20; a = an_y(n, 1000)                                           # a[x][y] lon nhat nhung x-z + y-w
            p = list(range(n)); random.shuffle(p)                               # moi la cach tot
            for t in range(0, n, 4):
                x, y, z, w = p[t:t + 4]
                a[x][y] = a[y][x] = 10**6
                a[x][z] = a[z][x] = a[y][w] = a[w][y] = 7 * 10**5
        else:
            n = 20; a = an_y(n, 10**6)
        ghi('GHEPCAP', so, f'{n}\n' + ma_tran(a), dap_an_ghepcap(n, a))

# ---------------- KHOBAU ----------------
def dap_an_khobau(g):
    R, C = len(g), len(g[0])
    diem = [None]
    for i in range(R):
        for j in range(C):
            if g[i][j] == 'S':
                diem[0] = (i, j)
            elif g[i][j] == '*':
                diem.append((i, j))
    D = []
    for si, sj in diem:
        dist = [[-1] * C for _ in range(R)]
        dist[si][sj] = 0
        q = deque([(si, sj)])
        while q:
            i, j = q.popleft()
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < R and 0 <= y < C and g[x][y] != '#' and dist[x][y] < 0:
                    dist[x][y] = dist[i][j] + 1
                    q.append((x, y))
        D.append([dist[x][y] for x, y in diem])
    k = len(diem) - 1
    if k == 0:
        return '0\n'
    if min(D[0]) < 0:
        return '-1\n'
    INF = float('inf')
    K = 1 << k
    f = [[INF] * k for _ in range(K)]
    for v in range(k):
        f[1 << v][v] = D[0][v + 1]
    for mask in range(1, K):
        for v in range(k):
            x = f[mask][v]
            if x == INF:
                continue
            for u in range(k):
                if not mask >> u & 1 and x + D[v + 1][u + 1] < f[mask | 1 << u][u]:
                    f[mask | 1 << u][u] = x + D[v + 1][u + 1]
    return f'{min(f[K - 1])}\n'

def ban_do(R, C, p_da, k):
    g = [['#' if random.random() < p_da else '.' for _ in range(C)] for _ in range(R)]
    o = random.sample([(i, j) for i in range(R) for j in range(C)], k + 1)
    i, j = o[0]; g[i][j] = 'S'
    for i, j in o[1:]:
        g[i][j] = '*'
    return [''.join(r) for r in g]

def me_cung(R, C, k):
    """Me cung tren cac o (le, le) - duong di dai, quanh co (sinh bang DFS ngan xep)."""
    g = [['#'] * C for _ in range(R)]
    st = [(1, 1)]; g[1][1] = '.'
    while st:
        i, j = st[-1]
        ke = [(i + di, j + dj, di, dj) for di, dj in ((2, 0), (-2, 0), (0, 2), (0, -2))
              if 0 < i + di < R - 1 and 0 < j + dj < C - 1 and g[i + di][j + dj] == '#']
        if not ke:
            st.pop(); continue
        x, y, di, dj = random.choice(ke)
        g[i + di // 2][j + dj // 2] = '.'; g[x][y] = '.'
        st.append((x, y))
    trong = [(i, j) for i in range(R) for j in range(C) if g[i][j] == '.']
    o = random.sample(trong, k + 1)
    i, j = o[0]; g[i][j] = 'S'
    for i, j in o[1:]:
        g[i][j] = '*'
    return [''.join(r) for r in g]

def sinh_khobau():
    for so in range(1, 11):
        if so == 1:
            g = ['S..#*.', '.#...#', '.#*#..', '*.....']                       # vi du: 10
        elif so == 2:
            g = ['S.#*', '..#.', '###.', '*...']                                # kho bau goc phai bi nhot -> -1
        elif so == 3:
            g = ban_do(15, 20, 0.2, 6)
        elif so == 4:
            g = ban_do(1, 20, 0.0, 5)                                           # mot hang: S o giua, di hai phia
        elif so == 5:
            g = ban_do(100, 100, 0.25, 10)
        elif so == 6:
            g = me_cung(99, 99, 10)
        elif so == 7:
            g = ban_do(100, 100, 0.0, 0)                                        # k = 0 -> 0
        elif so == 8:
            g = ban_do(200, 200, 0.0, 15)                                       # dong trong: BFS lan het luoi
        elif so == 9:
            g = me_cung(199, 199, 15)
        else:
            g = ban_do(200, 200, 0.3, 15)
            # dam bao co the toi duoc: neu khong thi doi ban do khac (giu test co dap an duong)
            while dap_an_khobau(g) == '-1\n':
                g = ban_do(200, 200, 0.3, 15)
        inp = f'{len(g)} {len(g[0])}\n' + '\n'.join(g) + '\n'
        ghi('KHOBAU', so, inp, dap_an_khobau(g))

# ---------------- LICHHOC ----------------
def dap_an_lichhoc(n, dk):
    MOD = 10**9 + 7
    truoc = [0] * n
    for u, v in dk:
        truoc[v - 1] |= 1 << (u - 1)
    N = 1 << n
    f = [0] * N; f[0] = 1
    for mask in range(N - 1):
        x = f[mask]
        if x == 0:
            continue
        for v in range(n):
            if not mask >> v & 1 and truoc[v] & mask == truoc[v]:
                f[mask | 1 << v] = (f[mask | 1 << v] + x) % MOD
    return f'{f[N - 1]}\n'

def dag(n, p):
    """DAG ngau nhien: tron so hieu, chi noi tu truoc ra sau trong thu tu an."""
    hv = list(range(1, n + 1)); random.shuffle(hv)
    return [(hv[i], hv[j]) for i in range(n) for j in range(i + 1, n) if random.random() < p]

def sinh_lichhoc():
    for so in range(1, 11):
        if so == 1:
            n = 4; dk = [(1, 2), (1, 3), (3, 4)]                                 # vi du: 3
        elif so == 2:
            n = 3; dk = [(1, 2), (2, 3), (3, 1)]                                 # vong -> 0
        elif so == 3:
            n = 8; dk = dag(n, 0.2)
        elif so == 4:
            n = 8; dk = []                                                     # 8! = 40320
        elif so == 5:
            n = 14; dk = dag(n, 0.1)
        elif so == 6:
            n = 14; dk = dag(n, 0.3)
            dk += dk[:5]                                                       # dieu kien lap lai
        elif so == 7:
            n = 14; dk = dag(n, 0.2)
            u, v = dk[0]; dk.append((v, u))                                    # them mot vong -> 0
        elif so == 8:
            n = 18; dk = []                                                    # 18! mod p
        elif so == 9:
            n = 18; dk = dag(n, 0.08)
        else:
            n = 18; dk = dag(n, 0.15)
        random.shuffle(dk)
        inp = f'{n} {len(dk)}\n' + ''.join(f'{u} {v}\n' for u, v in dk)
        ghi('LICHHOC', so, inp, dap_an_lichhoc(n, dk))

SINH = {'PHANCONG': sinh_phancong, 'COMBO': sinh_combo, 'GIAOHANG': sinh_giaohang,
        'GHEPCAP': sinh_ghepcap, 'KHOBAU': sinh_khobau, 'LICHHOC': sinh_lichhoc}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        random.seed(bai + '-2026')
        SINH[bai]()
        print('Da sinh', bai)

main()
