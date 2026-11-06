# SINH TEST cho 6 bai buoi 8 (QHD tren luoi)
#   Tren lop : DUONGDI, DEMDUONG, HINHVUONG        Ve nha: VANG, HVCON, HAIROBOT
# Cau truc thu muc theo Themis: test/DUONGDI/Test01/DUONGDI.INP + DUONGDI.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau de kiem cheo:
#   DUONGDI QHD tu dich ve, DEMDUONG QHD "day toi", HINHVUONG dung so o 1 lien tiep tren/trai,
#   VANG bang xuoi + bang nguoc (o nam tren duong toi uu), HVCON chat nhi phan canh,
#   HAIROBOT bang day du theo hang tuyet doi (khong dung doi xung r1 <= r2).
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py                 -> sinh ca 6 bai (~30 giay)
#       python sinh_test.py VANG HVCON      -> chi sinh cac bai ke ten
import os, random, sys
from itertools import accumulate
from operator import add

random.seed(2026)
GOC = 'test'
MOD = 10**9 + 7

def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

def bang_so(a):
    return '\n'.join(' '.join(map(str, r)) for r in a) + '\n'

def bang_ngau_nhien(m, n, lo, hi):
    return [[random.randint(lo, hi) for _ in range(n)] for _ in range(m)]

# ---------------- DUONGDI ----------------
def dap_an_duongdi(a):
    m, n = len(a), len(a[0])
    NEG = -10**30
    g = [NEG] * (n + 1)                   # g[j] = tong lon nhat tu (i,j) den dich, hang duoi
    for i in range(m - 1, -1, -1):
        moi = [NEG] * (n + 1)
        for j in range(n - 1, -1, -1):
            b = max(g[j], moi[j + 1])
            if i == m - 1 and j == n - 1:
                b = 0
            moi[j] = b + a[i][j]
        g = moi
    return g[0]

def sinh_duongdi():
    for so in range(1, 11):
        if so == 1:
            a = [[1, -2, 3], [4, 5, -6], [-7, 8, 9]]
        elif so == 2:
            a = [[-5]]
        elif so == 3:
            a = bang_ngau_nhien(1, 10, -100, 100)
        elif so == 4:
            a = bang_ngau_nhien(10, 10, -100, 100)
        elif so == 5:
            a = bang_ngau_nhien(300, 300, -10**9, 10**9)
        elif so == 6:
            a = bang_ngau_nhien(200, 300, -10**9, -1)      # toan so am
        elif so == 7:
            a = bang_ngau_nhien(300, 1, -10**9, 10**9)
        elif so == 8:
            a = bang_ngau_nhien(1000, 1000, -10**9, 10**9)
        elif so == 9:
            a = bang_ngau_nhien(1000, 1000, -10**9, -10**9 + 10)
        else:
            a = bang_ngau_nhien(1000, 1000, 10**9 - 1000, 10**9)
        ghi('DUONGDI', so, f'{len(a)} {len(a[0])}\n' + bang_so(a), str(dap_an_duongdi(a)) + '\n')

# ---------------- DEMDUONG ----------------
def dap_an_demduong(g):
    m, n = len(g), len(g[0])
    f = [[0] * (n + 1) for _ in range(m + 1)]
    if g[0][0] == '.':
        f[0][0] = 1
    for i in range(m):                    # "day toi": o (i,j) cong so cach sang o duoi va o phai
        for j in range(n):
            x = f[i][j]
            if x == 0 or g[i][j] == '#':
                continue
            if i + 1 < m and g[i + 1][j] == '.':
                f[i + 1][j] = (f[i + 1][j] + x) % MOD
            if j + 1 < n and g[i][j + 1] == '.':
                f[i][j + 1] = (f[i][j + 1] + x) % MOD
    return f[m - 1][n - 1] if g[m - 1][n - 1] == '.' else 0

def luoi_cam(m, n, p):
    g = [['#' if random.random() < p else '.' for _ in range(n)] for _ in range(m)]
    g[0][0] = g[m - 1][n - 1] = '.'
    return g

def sinh_demduong():
    for so in range(1, 11):
        if so == 1:
            g = [list('...'), list('.#.'), list('...')]
        elif so == 2:
            g = [list('#..'), list('...')]           # o xuat phat bi cam -> 0
        elif so == 3:
            g = luoi_cam(10, 10, 0.0)
        elif so == 4:
            g = luoi_cam(10, 10, 0.2)
        elif so == 5:
            g = luoi_cam(1000, 1000, 0.0)
        elif so == 6:
            g = luoi_cam(1, 1000, 0.0)
        elif so == 7:
            g = luoi_cam(500, 800, 0.0)
        elif so == 8:
            g = luoi_cam(1000, 1000, 0.1)
        elif so == 9:
            g = luoi_cam(1000, 1000, 0.05)
            g[999][999] = '#'                          # o dich cam -> 0
        else:                                          # tuong chan giua bang, chi mot khe
            g = luoi_cam(1000, 1000, 0.02)
            for j in range(1000):
                g[500][j] = '#'
            g[500][random.randint(0, 999)] = '.'
        ghi('DEMDUONG', so, f'{len(g)} {len(g[0])}\n' + '\n'.join(''.join(r) for r in g) + '\n',
            str(dap_an_demduong(g)) + '\n')

# ---------------- HINHVUONG ----------------
def dap_an_hinhvuong(b):
    # f[i][j] = min(f[i-1][j-1] + 1, so so 1 lien tiep di len tu (i,j), so so 1 lien tiep sang trai)
    m, n = len(b), len(b[0])
    len_tren = [0] * n
    cheo_cu = [0] * (n + 1)
    best = 0
    for i in range(m):
        trai = 0
        cheo = [0] * (n + 1)
        for j in range(n):
            if b[i][j] == '1':
                len_tren[j] += 1
                trai += 1
                v = min(cheo_cu[j] + 1, len_tren[j], trai)
            else:
                len_tren[j] = 0
                trai = 0
                v = 0
            cheo[j + 1] = v
            best = max(best, v)
        cheo_cu = cheo
    return best

def bang01(m, n, p):
    return [['1' if random.random() < p else '0' for _ in range(n)] for _ in range(m)]

def trong_vuong(b, k):                    # cay mot hinh vuong toan 1 canh k vao vi tri ngau nhien
    m, n = len(b), len(b[0])
    i0, j0 = random.randint(0, m - k), random.randint(0, n - k)
    for i in range(i0, i0 + k):
        for j in range(j0, j0 + k):
            b[i][j] = '1'

def sinh_hinhvuong():
    for so in range(1, 11):
        if so == 1:
            b = [list(x) for x in ('10100', '10111', '11111', '10010')]
        elif so == 2:
            b = bang01(30, 30, 0.0)
        elif so == 3:
            b = bang01(30, 30, 1.0)
        elif so == 4:
            b = bang01(30, 25, 0.8)
        elif so == 5:
            b = bang01(300, 300, 0.9)
        elif so == 6:
            b = bang01(300, 300, 0.9995)                 # gan nhu toan 1 -> vet can rat cham
        elif so == 7:
            b = bang01(300, 1, 0.9)
        elif so == 8:
            b = bang01(1000, 1000, 0.95)
            trong_vuong(b, 200)
        elif so == 9:
            b = bang01(1000, 1000, 0.7)
            trong_vuong(b, 377)
        else:
            b = bang01(1000, 1000, 1.0)
        ghi('HINHVUONG', so, f'{len(b)} {len(b[0])}\n' + '\n'.join(''.join(r) for r in b) + '\n',
            str(dap_an_hinhvuong(b)) + '\n')

# ---------------- VANG ----------------
def dap_an_vang(a):
    m, n = len(a), len(a[0])
    AM = -1
    f = [[AM] * n for _ in range(m)]      # xuoi: tu (0,0) den (i,j)
    for i in range(m):
        for j in range(n):
            if a[i][j] < 0:
                continue
            if i == 0 and j == 0:
                f[i][j] = a[i][j]; continue
            b = max(f[i - 1][j] if i else AM, f[i][j - 1] if j else AM)
            if b >= 0:
                f[i][j] = b + a[i][j]
    if f[m - 1][n - 1] < 0:
        return '-1\n'
    best = f[m - 1][n - 1]
    g = [[AM] * n for _ in range(m)]      # nguoc: tu (i,j) den dich
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if a[i][j] < 0:
                continue
            if i == m - 1 and j == n - 1:
                g[i][j] = a[i][j]; continue
            b = max(g[i + 1][j] if i + 1 < m else AM, g[i][j + 1] if j + 1 < n else AM)
            if b >= 0:
                g[i][j] = b + a[i][j]
    tot = lambda i, j: f[i][j] >= 0 and g[i][j] >= 0 and f[i][j] + g[i][j] - a[i][j] == best
    i = j = 0
    s = []
    while i < m - 1 or j < n - 1:         # o tiep theo phai nam tren mot duong toi uu
        if i + 1 < m and tot(i + 1, j) and f[i + 1][j] == f[i][j] + a[i + 1][j]:
            s.append('D'); i += 1
        else:
            s.append('R'); j += 1
    return f'{best}\n' + ''.join(s) + '\n'

def bang_vang(m, n, hi, p_da):
    a = [[-1 if random.random() < p_da else random.randint(0, hi) for _ in range(n)] for _ in range(m)]
    a[0][0] = random.randint(0, hi)
    a[m - 1][n - 1] = random.randint(0, hi)
    return a

def sinh_vang():
    for so in range(1, 11):
        if so == 1:
            a = [[1, 0, 2, 3], [0, -1, 1, 0], [5, 0, 0, 1]]
        elif so == 2:
            a = [[3, -1], [-1, 4]]                     # khong co duong -> -1
        elif so == 3:
            a = [[7]]
        elif so == 4:
            a = bang_vang(10, 10, 2, 0.15)             # gia tri nho -> rat nhieu duong hoa
        elif so == 5:
            a = bang_vang(300, 300, 3, 0.2)
        elif so == 6:
            a = bang_vang(300, 250, 10**6, 0.1)
        elif so == 7:
            a = bang_vang(300, 300, 0, 0.0)            # toan 0: dap an 0, duong D...DR...R
        elif so == 8:
            a = bang_vang(1000, 1000, 1, 0.2)
        elif so == 9:
            a = bang_vang(1000, 1000, 10**6, 0.05)
        else:
            a = bang_vang(1000, 1000, 2, 0.3)
        ghi('VANG', so, f'{len(a)} {len(a[0])}\n' + bang_so(a), dap_an_vang(a))

# ---------------- HVCON ----------------
def cong_don(a):
    n = len(a[0])
    P = [[0] * (n + 1)]
    for r in a:
        P.append(list(map(add, P[-1], accumulate(r, initial=0))))
    return P

def dap_an_hvcon(a, S):
    m, n = len(a), len(a[0])
    P = cong_don(a)
    def co(k):
        for i in range(k, m + 1):
            Pi, Pk = P[i], P[i - k]
            for j in range(k, n + 1):
                if Pi[j] - Pk[j] - Pi[j - k] + Pk[j - k] <= S:
                    return True
        return False
    lo, hi = 0, min(m, n)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if co(mid): lo = mid
        else: hi = mid - 1
    return lo

def S_cho_canh(a, k):                     # lay tong mot hinh vuong canh k ngau nhien lam S
    m, n = len(a), len(a[0])
    P = cong_don(a)
    i, j = random.randint(k, m), random.randint(k, n)
    return P[i][j] - P[i - k][j] - P[i][j - k] + P[i - k][j - k]

def sinh_hvcon():
    for so in range(1, 11):
        if so == 1:
            a, S = [[1, 2, 3, 4], [5, 1, 1, 6], [2, 1, 1, 9]], 10
        elif so == 2:
            a = bang_ngau_nhien(20, 30, 5, 100); S = 4            # moi o > S -> 0
        elif so == 3:
            a = bang_ngau_nhien(50, 40, 0, 10**6); S = 10**15     # lay ca bang vuong lon nhat
        elif so == 4:
            a = bang_ngau_nhien(50, 50, 0, 1000); S = S_cho_canh(a, 13)
        elif so == 5:
            a = bang_ngau_nhien(300, 300, 0, 10**6); S = S_cho_canh(a, 70)
        elif so == 6:
            a = [[7] * 300 for _ in range(250)]; S = 7 * 123 * 123 + 6
        elif so == 7:
            a = bang_ngau_nhien(300, 300, 0, 10); S = S_cho_canh(a, 200)
        elif so == 8:
            a = bang_ngau_nhien(1000, 1000, 0, 10**6); S = S_cho_canh(a, 300)
        elif so == 9:
            a = bang_ngau_nhien(1000, 1000, 0, 10**6); S = 10**15
        else:                                                    # vung toan 0 an trong bang
            a = bang_ngau_nhien(1000, 1000, 1, 10**6)
            i0, j0 = random.randint(0, 500), random.randint(0, 500)
            for i in range(i0, i0 + 451):
                for j in range(j0, j0 + 451):
                    a[i][j] = 0
            S = 5
        m, n = len(a), len(a[0])
        ghi('HVCON', so, f'{m} {n} {S}\n' + bang_so(a), str(dap_an_hvcon(a, S)) + '\n')

# ---------------- HAIROBOT ----------------
def dap_an_hairobot(a):
    n = len(a)
    AM = -1
    f = [[AM] * n for _ in range(n)]       # f[r1][r2] theo hang tuyet doi, du ca r1 > r2
    if a[0][0] >= 0:
        f[0][0] = a[0][0]
    for s in range(1, 2 * n - 1):
        g = [[AM] * n for _ in range(n)]
        for r1 in range(max(0, s - n + 1), min(s, n - 1) + 1):
            c1 = s - r1
            if a[r1][c1] < 0:
                continue
            for r2 in range(max(0, s - n + 1), min(s, n - 1) + 1):
                c2 = s - r2
                if a[r2][c2] < 0:
                    continue
                b = AM
                for p1 in (r1, r1 - 1):
                    for p2 in (r2, r2 - 1):
                        if 0 <= p1 and 0 <= p2 and f[p1][p2] > b:
                            b = f[p1][p2]
                if b >= 0:
                    g[r1][r2] = b + a[r1][c1] + (a[r2][c2] if r1 != r2 else 0)
        f = g
    return f[n - 1][n - 1]

def sinh_hairobot():
    for so in range(1, 11):
        if so == 1:
            a = [[1, 1, 1], [3, 2, 3], [2, 0, 0]]      # tham lam 2 lan ra 11, dung la 12
        elif so == 2:
            a = [[9]]
        elif so == 3:
            a = [[1, -1, 5], [-1, 2, 3], [4, -1, 1]]   # (1,1) bi da vay -> -1
        elif so == 4:
            a = bang_vang(6, 6, 9, 0.15)
        elif so == 5:
            a = bang_vang(30, 30, 1000, 0.1)
        elif so == 6:
            a = bang_vang(30, 30, 1, 0.25)
        elif so == 7:
            a = bang_vang(25, 25, 1000, 0.0)
        elif so == 8:
            a = bang_vang(100, 100, 1000, 0.1)
        elif so == 9:
            a = bang_vang(100, 100, 1000, 0.0)
        else:                                  # vang chi o hai "hanh lang" xa nhau -> 2 robot tach ra
            a = bang_vang(100, 100, 3, 0.15)
            for i in range(100):
                a[i][5] = 1000 if a[i][5] >= 0 else -1
                a[94][i] = 1000 if a[94][i] >= 0 else -1
        n = len(a)
        ghi('HAIROBOT', so, f'{n}\n' + bang_so(a), str(dap_an_hairobot(a)) + '\n')

SINH = {'DUONGDI': sinh_duongdi, 'DEMDUONG': sinh_demduong, 'HINHVUONG': sinh_hinhvuong,
        'VANG': sinh_vang, 'HVCON': sinh_hvcon, 'HAIROBOT': sinh_hairobot}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        SINH[bai]()
        print('Da sinh', bai)

main()
