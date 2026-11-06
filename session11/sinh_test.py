# SINH TEST cho 6 bai buoi 11 (Loang tren luoi)
#   Tren lop : DEMDAO, MECUNG, LUALAN        Ve nha: HONUOC, QUANMA, CHAYTHOAT
# Cau truc thu muc theo Themis: test/DEMDAO/Test01/DEMDAO.INP + DEMDAO.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau de kiem cheo:
#   DEMDAO dung DSU, cac bai con lai dung BFS "sach giao khoa" (deque tuple (i, j), mang 2 chieu,
#   kiem tra bien) thay cho mang 1 chieu co vien cua loi giai; HONUOC dem vung nuoc roi xet cham mep.
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py                  -> sinh ca 6 bai (~1 phut)
#       python sinh_test.py MECUNG QUANMA    -> chi sinh cac bai ke ten
import os, random, sys
from collections import deque

random.seed(2026)
GOC = 'test'
HUONG4 = ((-1, 0), (1, 0), (0, -1), (0, 1))

def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

def luoi_str(g):
    return '\n'.join(''.join(r) for r in g) + '\n'

def ngau_nhien(m, n, p, co, khong):          # o = co voi xac suat p, nguoc lai = khong
    return [[co if random.random() < p else khong for _ in range(n)] for _ in range(m)]

def con_ran(m, n, duong, tuong):
    # hanh lang ziczac: hang chan toan "duong", hang le toan "tuong" tru 1 khe xen ke dau/cuoi
    g = [[duong] * n if i % 2 == 0 else [tuong] * n for i in range(m)]
    for i in range(1, m, 2):
        g[i][n - 1 if i % 4 == 1 else 0] = duong
    return g

def dat_ngau_nhien(g, ky_tu, cam=('#',)):    # dat ky_tu vao mot o ngau nhien khong thuoc 'cam'
    m, n = len(g), len(g[0])
    while True:
        i, j = random.randrange(m), random.randrange(n)
        if g[i][j] not in cam:
            g[i][j] = ky_tu
            return i, j

def bfs2(g, nguon, di_duoc):                 # BFS sach giao khoa, tra ve mang dist 2 chieu
    m, n = len(g), len(g[0])
    d = [[-1] * n for _ in range(m)]
    q = deque()
    for i, j in nguon:
        d[i][j] = 0
        q.append((i, j))
    while q:
        i, j = q.popleft()
        for a, b in HUONG4:
            u, v = i + a, j + b
            if 0 <= u < m and 0 <= v < n and d[u][v] < 0 and di_duoc(g[u][v]):
                d[u][v] = d[i][j] + 1
                q.append((u, v))
    return d

# ---------------- DEMDAO ----------------
def dap_an_demdao(g):
    m, n = len(g), len(g[0])
    cha = list(range(m * n))
    def tim(x):
        while cha[x] != x:
            cha[x] = cha[cha[x]]
            x = cha[x]
        return x
    for i in range(m):
        for j in range(n):
            if g[i][j] != '#':
                continue
            if i + 1 < m and g[i + 1][j] == '#':
                cha[tim(i * n + j)] = tim((i + 1) * n + j)
            if j + 1 < n and g[i][j + 1] == '#':
                cha[tim(i * n + j)] = tim(i * n + j + 1)
    dem = {}
    for i in range(m):
        for j in range(n):
            if g[i][j] == '#':
                r = tim(i * n + j)
                dem[r] = dem.get(r, 0) + 1
    return f'{len(dem)} {max(dem.values(), default=0)}\n'

def sinh_demdao():
    for so in range(1, 11):
        if so == 1:
            g = [list(x) for x in ('##..#', '#...#', '..#..', '##.##')]
        elif so == 2:
            g = ngau_nhien(5, 7, 0.0, '#', '.')                 # khong co dao
        elif so == 3:
            g = ngau_nhien(50, 50, 1.0, '#', '.')               # ca bang la 1 dao
        elif so == 4:
            g = ngau_nhien(50, 50, 0.45, '#', '.')
        elif so == 5:
            g = ngau_nhien(300, 300, 0.5, '#', '.')             # nhieu dao nho (gan nguong tham thau)
        elif so == 6:
            g = [['#' if (i + j) % 2 == 0 else '.' for j in range(300)] for i in range(300)]  # ban co
        elif so == 7:
            g = con_ran(299, 300, '#', '.')                     # 1 dao dai -> de quy sau ~45000
        elif so == 8:
            g = ngau_nhien(1000, 1000, 0.55, '#', '.')
        elif so == 9:
            g = con_ran(999, 1000, '#', '.')                    # dao con ran 5*10^5 o
        else:
            g = ngau_nhien(1000, 1000, 0.3, '#', '.')           # rat nhieu dao nho
        ghi('DEMDAO', so, f'{len(g)} {len(g[0])}\n' + luoi_str(g), dap_an_demdao(g))

# ---------------- MECUNG ----------------
def dap_an_mecung(g):
    for i, r in enumerate(g):
        for j, c in enumerate(r):
            if c == 'S': s = (i, j)
            if c == 'E': e = (i, j)
    d = bfs2(g, [s], lambda c: c != '#')
    return str(d[e[0]][e[1]]) + '\n'

def me_cung_dfs(m, n):
    # me cung "hoan hao" sinh bang DFS ngau nhien tren cac o (le, le): duong di rat dai, ngoan ngoeo
    g = [['#'] * n for _ in range(m)]
    g[0][0] = '.'
    st = [(0, 0)]
    while st:
        i, j = st[-1]
        ke = [(i + a, j + b, i + a // 2, j + b // 2) for a, b in ((-2, 0), (2, 0), (0, -2), (0, 2))
              if 0 <= i + a < m and 0 <= j + b < n and g[i + a][j + b] == '#']
        if not ke:
            st.pop()
            continue
        u, v, x, y = random.choice(ke)
        g[x][y] = g[u][v] = '.'
        st.append((u, v))
    return g

def sinh_mecung():
    for so in range(1, 11):
        if so == 1:
            g = [list(x) for x in ('S.#.', '.##.', '...E')]
        elif so == 2:
            g = [list(x) for x in ('S#.', '#..', '..E')]        # S bi vay -> -1
        elif so == 3:
            g = me_cung_dfs(21, 21); g[0][0] = 'S'; g[20][20] = 'E'
        elif so == 4:
            g = ngau_nhien(30, 30, 0.3, '#', '.'); dat_ngau_nhien(g, 'S'); dat_ngau_nhien(g, 'E', ('#', 'S'))
        elif so == 5:
            g = me_cung_dfs(299, 299); g[0][0] = 'S'; g[298][298] = 'E'
        elif so == 6:
            g = ngau_nhien(300, 300, 0.0, '#', '.'); g[0][0] = 'S'; g[299][299] = 'E'
        elif so == 7:
            g = con_ran(299, 300, '.', '#'); g[0][0] = 'S'; g[298][0] = 'E'   # hanh lang ziczac dai
        elif so == 8:
            g = me_cung_dfs(999, 1000); g[0][0] = 'S'; g[998][998] = 'E'
        elif so == 9:
            g = ngau_nhien(1000, 1000, 0.3, '#', '.')
            for i in range(3):                              # mo goc de S, E khong bi vay
                for j in range(3):
                    g[i][j] = g[999 - i][999 - j] = '.'
            g[0][0] = 'S'; g[999][999] = 'E'
        else:
            g = ngau_nhien(1000, 1000, 0.2, '#', '.')
            for j in range(1000):                           # tuong ngang chi chua 1 khe o sat mep
                g[500][j] = '#'
            g[500][997] = g[499][997] = g[501][997] = '.'
            g[0][0] = 'S'; g[999][0] = 'E'
        ghi('MECUNG', so, f'{len(g)} {len(g[0])}\n' + luoi_str(g), dap_an_mecung(g))

# ---------------- LUALAN ----------------
def dap_an_lualan(g):
    m, n = len(g), len(g[0])
    nguon = [(i, j) for i in range(m) for j in range(n) if g[i][j] == 'F']
    d = bfs2(g, nguon, lambda c: c == 'T')
    phut = con = 0
    for i in range(m):
        for j in range(n):
            if g[i][j] == 'T':
                if d[i][j] < 0: con += 1
                else: phut = max(phut, d[i][j])
    return f'{phut} {con}\n'

def rung(m, n, p_cay, so_lua):
    g = ngau_nhien(m, n, p_cay, 'T', '.')
    for _ in range(so_lua):
        dat_ngau_nhien(g, 'F', ())
    return g

def sinh_lualan():
    for so in range(1, 11):
        if so == 1:
            g = [list(x) for x in ('TTT.T', 'TFT.T', 'TT.TT', 'F.TTT')]
        elif so == 2:
            g = rung(10, 10, 0.8, 0)                           # khong co lua -> 0 va moi cay
        elif so == 3:
            g = rung(30, 30, 1.0, 1)
        elif so == 4:
            g = rung(30, 30, 0.7, 5)
        elif so == 5:
            g = rung(300, 300, 0.75, 20)
        elif so == 6:
            g = con_ran(300, 300, 'T', '.'); g[0][0] = 'F'      # lua chay theo hanh lang dai
        elif so == 7:
            g = rung(300, 300, 0.9, 3000)                      # rat nhieu dam chay
        elif so == 8:
            g = rung(1000, 1000, 0.8, 1000)                    # BFS tung nguon se qua cham
        elif so == 9:
            g = con_ran(1000, 1000, 'T', '.'); g[0][0] = 'F'
        else:
            g = rung(1000, 1000, 1.0, 1)
        ghi('LUALAN', so, f'{len(g)} {len(g[0])}\n' + luoi_str(g), dap_an_lualan(g))

# ---------------- HONUOC ----------------
def dap_an_honuoc(g):
    m, n = len(g), len(g[0])
    tham = [[False] * n for _ in range(m)]
    so_ho = tong = 0
    for i in range(m):
        for j in range(n):
            if g[i][j] != '.' or tham[i][j]:
                continue
            tham[i][j] = True
            q = deque([(i, j)]); dt = 0; mep = False
            while q:
                x, y = q.popleft(); dt += 1
                if x == 0 or y == 0 or x == m - 1 or y == n - 1:
                    mep = True
                for a, b in HUONG4:
                    u, v = x + a, y + b
                    if 0 <= u < m and 0 <= v < n and not tham[u][v] and g[u][v] == '.':
                        tham[u][v] = True; q.append((u, v))
            if not mep:
                so_ho += 1; tong += dt
    return f'{so_ho} {tong}\n'

def ao_ho(m, n, so_vong):                    # dat cac "vong dat" hinh chu nhat quanh vung nuoc
    g = ngau_nhien(m, n, 0.1, '#', '.')
    for _ in range(so_vong):
        h, w = random.randint(3, max(3, m // 4)), random.randint(3, max(3, n // 4))
        i0, j0 = random.randint(0, m - h), random.randint(0, n - w)
        for i in range(i0, i0 + h):
            for j in range(j0, j0 + w):
                if i in (i0, i0 + h - 1) or j in (j0, j0 + w - 1):
                    g[i][j] = '#'
    return g

def sinh_honuoc():
    for so in range(1, 11):
        if so == 1:
            g = [list(x) for x in ('######.', '#..#..#', '####.##', '#.#..#.', '######.')]
        elif so == 2:
            g = ngau_nhien(20, 20, 0.0, '#', '.')               # toan nuoc bien -> 0 0
        elif so == 3:
            g = ngau_nhien(30, 30, 0.5, '#', '.')
        elif so == 4:
            g = ao_ho(40, 40, 15)
        elif so == 5:
            g = ngau_nhien(300, 300, 0.55, '#', '.')
        elif so == 6:
            g = ao_ho(300, 300, 200)
        elif so == 7:                                           # 1 ho con ran bi bao kin
            g = con_ran(298, 300, '.', '#')
            g = [['#'] * 302] + [['#'] + r + ['#'] for r in g] + [['#'] * 302]
        elif so == 8:
            g = ngau_nhien(1000, 1000, 0.6, '#', '.')
        elif so == 9:
            g = ao_ho(1000, 1000, 2000)
        else:
            g = con_ran(998, 998, '.', '#')
            g = [['#'] * 1000] + [['#'] + r + ['#'] for r in g] + [['#'] * 1000]
            g[0][500] = '.'                                     # mo 1 khe ra bien -> khong con ho
        ghi('HONUOC', so, f'{len(g)} {len(g[0])}\n' + luoi_str(g), dap_an_honuoc(g))

# ---------------- QUANMA ----------------
def dap_an_quanma(n, x1, y1, x2, y2, g):
    d = [[-1] * n for _ in range(n)]
    d[x1][y1] = 0
    q = deque([(x1, y1)])
    while q:
        i, j = q.popleft()
        for a, b in ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)):
            u, v = i + a, j + b
            if 0 <= u < n and 0 <= v < n and d[u][v] < 0 and g[u][v] == '.':
                d[u][v] = d[i][j] + 1
                q.append((u, v))
    return str(d[x2][y2]) + '\n'

def sinh_quanma():
    for so in range(1, 11):
        if so == 1:
            n, g, a = 5, ngau_nhien(5, 5, 0.0, '#', '.'), (0, 0, 4, 4)
        elif so == 2:
            n, g, a = 3, ngau_nhien(3, 3, 0.0, '#', '.'), (0, 0, 1, 1)   # o giua ban 3x3 -> -1
            g[1][1] = '.'
        elif so == 3:
            n, g, a = 8, ngau_nhien(8, 8, 0.0, '#', '.'), (0, 0, 0, 0)   # trung o -> 0
        elif so == 4:
            n = 20; g = ngau_nhien(n, n, 0.3, '#', '.'); a = (0, 0, 19, 19)
        elif so == 5:
            n = 300; g = ngau_nhien(n, n, 0.0, '#', '.'); a = (0, 0, 299, 299)
        elif so == 6:
            n = 300; g = ngau_nhien(n, n, 0.35, '#', '.'); a = (0, 0, 299, 299)
        elif so == 7:
            n = 300; g = ngau_nhien(n, n, 0.2, '#', '.'); a = (150, 150, 0, 299)
        elif so == 8:
            n = 800; g = ngau_nhien(n, n, 0.0, '#', '.'); a = (0, 0, 799, 798)
        elif so == 9:
            n = 800; g = ngau_nhien(n, n, 0.3, '#', '.'); a = (0, 0, 799, 799)
        else:                                                    # 1 hang vat can kin: ma van nhay qua duoc
            n = 800; g = ngau_nhien(n, n, 0.15, '#', '.'); a = (0, 0, 799, 799)
            g[400] = ['#'] * n
        x1, y1, x2, y2 = a
        g[x1][y1] = g[x2][y2] = '.'
        inp = f'{n}\n{x1 + 1} {y1 + 1} {x2 + 1} {y2 + 1}\n' + luoi_str(g)
        ghi('QUANMA', so, inp, dap_an_quanma(n, x1, y1, x2, y2, g))

# ---------------- CHAYTHOAT ----------------
def dap_an_chaythoat(g):
    m, n = len(g), len(g[0])
    nguon = [(i, j) for i in range(m) for j in range(n) if g[i][j] == 'F']
    lua = bfs2(g, nguon, lambda c: c != '#')
    VC = 10**9
    for i in range(m):
        for j in range(n):
            if lua[i][j] < 0: lua[i][j] = VC
    for i in range(m):
        for j in range(n):
            if g[i][j] == 'J': s = (i, j)
    d = [[-1] * n for _ in range(m)]
    d[s[0]][s[1]] = 0
    q = deque([s])
    while q:
        i, j = q.popleft()
        if i == 0 or j == 0 or i == m - 1 or j == n - 1:
            return str(d[i][j] + 1) + '\n'                       # BFS: o mep dau tien lay ra la gan nhat
        for a, b in HUONG4:
            u, v = i + a, j + b
            if 0 <= u < m and 0 <= v < n and d[u][v] < 0 and g[u][v] != '#' and lua[u][v] > d[i][j] + 1:
                d[u][v] = d[i][j] + 1
                q.append((u, v))
    return '-1\n'

def toa_nha(m, n, p_tuong, so_lua, j_giua=False):
    g = ngau_nhien(m, n, p_tuong, '#', '.')
    if j_giua:
        g[m // 2][n // 2] = 'J'
    else:
        dat_ngau_nhien(g, 'J', ())
    for _ in range(so_lua):
        dat_ngau_nhien(g, 'F', ('J',))
    return g

def sinh_chaythoat():
    for so in range(1, 11):
        if so == 1:
            g = [list(x) for x in ('####', '#JF#', '#..#', '#..#')]
        elif so == 2:
            g = [list(x) for x in ('##.##', '#J.F#', '#.###', '#...#', '###.#')]  # lua toi (2,3) dung luc
            # Binh toi -> khong duoc di loi tat len tren (3 phut), phai vong xuong duoi: 6 phut
        elif so == 3:
            g = toa_nha(15, 20, 0.25, 0, True)
        elif so == 4:
            g = toa_nha(20, 20, 0.2, 3, True)
        elif so == 5:
            g = toa_nha(300, 300, 0.25, 5, True)
        elif so == 6:
            g = me_cung_dfs(299, 299); g[149][149] = 'J'
            dat_ngau_nhien(g, 'F', ('#', 'J'))
        elif so == 7:
            g = toa_nha(300, 300, 0.1, 100, True)
        elif so == 8:
            g = toa_nha(1000, 1000, 0.25, 10, True)
        elif so == 9:
            g = me_cung_dfs(999, 999); g[499][499] = 'J'
            for i in range(999):                            # duc 10% tuong -> me cung co nhieu vong
                for j in range(999):
                    if g[i][j] == '#' and random.random() < 0.1:
                        g[i][j] = '.'
            for _ in range(2): dat_ngau_nhien(g, 'F', ('#', 'J'))
        else:
            g = toa_nha(1000, 1000, 0.05, 2, True)
            g[0][0] = 'F'
        ghi('CHAYTHOAT', so, f'{len(g)} {len(g[0])}\n' + luoi_str(g), dap_an_chaythoat(g))

SINH = {'DEMDAO': sinh_demdao, 'MECUNG': sinh_mecung, 'LUALAN': sinh_lualan,
        'HONUOC': sinh_honuoc, 'QUANMA': sinh_quanma, 'CHAYTHOAT': sinh_chaythoat}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        SINH[bai]()
        print('Da sinh', bai)

main()
