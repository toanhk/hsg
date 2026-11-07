# SINH TEST buoi 23 - de thi thu so 3 (180 phut): TONGCON, MUASAM, PHATUONG
# Bo test nay CO Y cai bay cho cac loi hay gap: sai bien (TONGCON: nhieu so 0, doan tong dung bang L),
# cap nhat tai cho (MUASAM: nhieu mon cung nhom), quen reset (PHATUONG: nhieu bo test), qua gio (test lon).
# Cau truc thu muc theo Themis: test/TONGCON/Test01/TONGCON.INP + TONGCON.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau de kiem cheo:
#   TONGCON mang cong don + bisect (loi giai mau: hai con tro),
#   MUASAM QHD hai hang "keo ve" theo tung nhom (loi giai mau: map tren lat cat),
#   PHATUONG BFS tren do thi trang thai (o, da pha) ma hoa so nguyen (loi giai mau: 2 BFS tu S va T).
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py              -> sinh ca 3 bai (~40 giay)
#       python sinh_test.py PHATUONG     -> chi sinh bai ke ten
import os, random, sys, bisect
from itertools import accumulate

GOC = 'test'

def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

# ---------------- TONGCON ----------------
def dap_an_tongcon(L, R, a):
    P = list(accumulate(a, initial=0))
    ans = 0
    for r in range(1, len(P)):              # dem l < r voi P[r] - R <= P[l] <= P[r] - L
        ans += bisect.bisect_right(P, P[r] - L, 0, r) - bisect.bisect_left(P, P[r] - R, 0, r)
    return f'{ans}\n'

def sinh_tongcon():
    for so in range(1, 11):
        if so == 1:
            L, R, a = 3, 5, [1, 2, 0, 3, 1, 2]                                  # vi du: 8
        elif so == 2:
            L, R, a = 0, 0, [0, 0, 5, 0, 0, 0, 7, 0]                            # chi doan toan so 0
        elif so == 3:
            n = 3000; a = [random.randint(0, 10**6) for _ in range(n)]; L = 10**7; R = 3 * 10**7
        elif so == 4:
            n = 3000; a = [random.randint(0, 2) for _ in range(n)]; L = R = 10
        elif so == 5:
            n = 5 * 10**5; a = [random.randint(1, 10**9) for _ in range(n)]; L = 10**11; R = 3 * 10**11
        elif so == 6:
            n = 5 * 10**5; a = [1] * n; L = R = 1000                           # dap an n - 999
        elif so == 7:
            n = 5 * 10**5; a = [random.randint(1, 10**9) for _ in range(n)]; L = 1; R = 10**15   # moi doan
        elif so == 8:
            n = 5 * 10**5; a = [random.randint(0, 10) for _ in range(n)]; L = R = 20
        elif so == 9:
            n = 5 * 10**5; a = [0 if random.random() < 0.5 else random.randint(1, 10**9) for _ in range(n)]
            L = 10**9; R = 2 * 10**9
        else:
            n = 5 * 10**5; a = [0] * n; L = 0; R = 10**15                      # dap an ~1,25*10^11
        inp = f'{len(a)} {L} {R}\n' + ' '.join(map(str, a)) + '\n'
        ghi('TONGCON', so, inp, dap_an_tongcon(L, R, a))

# ---------------- MUASAM ----------------
def dap_an_muasam(B, mon):
    nhom = {}
    for g, w, v in mon:
        nhom.setdefault(g, []).append((w, v))
    cu = [0] * (B + 1)
    for ds in nhom.values():
        moi = cu[:]
        for b in range(B + 1):              # keo ve: o b lay tu mon nao trong nhom
            best = moi[b]
            for w, v in ds:
                if w <= b and cu[b - w] + v > best:
                    best = cu[b - w] + v
            moi[b] = best
        cu = moi
    return f'{cu[B]}\n'

def mon_ngau_nhien(n, B, so_nhom, wmax=None):
    wmax = wmax or B
    return [(random.randint(1, so_nhom), random.randint(1, wmax), random.randint(1, 10**6)) for _ in range(n)]

def sinh_muasam():
    for so in range(1, 11):
        if so == 1:                                                             # vi du: 14
            B = 10; mon = [(1, 4, 5), (1, 5, 6), (2, 3, 4), (2, 6, 9), (3, 2, 3)]
        elif so == 2:
            B = 10; mon = [(1, 4, 5), (1, 5, 6)]                                # bay cap nhat tai cho: 6
        elif so == 3:
            B = 50; mon = mon_ngau_nhien(10, B, 4, 25)
        elif so == 4:
            B = 100; mon = mon_ngau_nhien(10, B, 1)                             # mot nhom: lay 1 mon tot nhat
        elif so == 5:
            B = 5000; mon = mon_ngau_nhien(200, B, 40, 500)
        elif so == 6:
            B = 1000; mon = [(i + 1, random.randint(1, 100), random.randint(1, 10**6)) for i in range(1000)]
        elif so == 7:
            B = 2000; mon = mon_ngau_nhien(500, B, 100, 200)
        elif so == 8:
            B = 5000; mon = mon_ngau_nhien(1000, B, 100, 300)
        elif so == 9:
            B = 5000; mon = mon_ngau_nhien(1000, B, 3, 5000)                    # 3 nhom rat dong
        else:
            B = 5000; mon = [(i + 1, random.randint(1, 50), random.randint(1, 10**6)) for i in range(1000)]
        inp = f'{len(mon)} {B}\n' + ''.join(f'{g} {w} {v}\n' for g, w, v in mon)
        ghi('MUASAM', so, inp, dap_an_muasam(B, mon))

# ---------------- PHATUONG ----------------
def dap_an_phatuong(bo):
    out = []
    for r, c, g in bo:
        N = r * c
        s = next(i * c + j for i in range(r) for j in range(c) if g[i][j] == 'S')
        e = next(i * c + j for i in range(r) for j in range(c) if g[i][j] == 'T')
        tuong = [g[i][j] == '#' for i in range(r) for j in range(c)]
        d = [-1] * (2 * N)                      # trang thai k * N + o
        d[s] = 0; tang = [s]; k = 0; ans = -1
        while tang and ans < 0:
            k += 1; moi = []
            for st in tang:
                da, p = divmod(st, N)
                i, j = divmod(p, c)
                for ok, q in ((i > 0, p - c), (i < r - 1, p + c), (j > 0, p - 1), (j < c - 1, p + 1)):
                    if not ok:
                        continue
                    nk = da + tuong[q]
                    if nk <= 1 and d[nk * N + q] < 0:
                        d[nk * N + q] = k; moi.append(nk * N + q)
                        if q == e:
                            ans = k
            tang = moi
        out.append(ans)
    return '\n'.join(map(str, out)) + '\n'

def luoi(r, c, ti_le):
    g = [['#' if random.random() < ti_le else '.' for _ in range(c)] for _ in range(r)]
    a, b = random.sample(range(r * c), 2)
    g[a // c][a % c] = 'S'; g[b // c][b % c] = 'T'
    return (r, c, [''.join(x) for x in g])

def luoi_hanh_lang(r, c):
    """Cac hang tuong ngang co mot khe, khe lech nhau -> duong rat dai; pha dung cho tiet kiem nhieu."""
    g = [['.'] * c for _ in range(r)]
    for i in range(1, r - 1, 2):
        for j in range(c):
            g[i][j] = '#'
        g[i][c - 1 if i % 4 == 1 else 0] = '.'
    g[0][0] = 'S'; g[r - 1][c - 1] = 'T'
    return (r, c, [''.join(x) for x in g])

def sinh_phatuong():
    for so in range(1, 11):
        if so == 1:                                                             # vi du: 6 va 4
            bo = [(4, 5, ['S.#..', '##.#.', '...#T', '.#...']),
                  (3, 3, ['S#.', '##.', '.#T'])]
        elif so == 2:
            bo = [(1, 2, ['ST']), (2, 3, ['S##', '##T']), (1, 5, ['S#.#T'])]     # 1, -1, -1
        elif so == 3:
            bo = [luoi(50, 50, 0.35)]
        elif so == 4:
            bo = [luoi_hanh_lang(49, 50)]
        elif so == 5:
            bo = [luoi(700, 700, 0.3)]
        elif so == 6:                                                           # hanh lang 1 x 500000, mot tuong
            c = 5 * 10**5; row = ['.'] * c; row[0] = 'S'; row[-1] = 'T'; row[c // 2] = '#'
            bo = [(1, c, [''.join(row)])]
        elif so == 7:
            bo = [luoi_hanh_lang(699, 700)]
        elif so == 8:                                                           # 10^4 luoi nho 5 x 10
            bo = [luoi(5, 10, 0.4) for _ in range(10**4)]
        elif so == 9:
            bo = [luoi(70, 70, 0.3) for _ in range(100)]
        else:
            bo = [luoi(300, 300, 0.25), luoi_hanh_lang(299, 300), luoi(1, 50000, 0.05), luoi(500, 200, 0.4)]
        inp = f'{len(bo)}\n' + ''.join(f'{r} {c}\n' + '\n'.join(g) + '\n' for r, c, g in bo)
        ghi('PHATUONG', so, inp, dap_an_phatuong(bo))

SINH = {'TONGCON': sinh_tongcon, 'MUASAM': sinh_muasam, 'PHATUONG': sinh_phatuong}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        random.seed(bai + '-2026')
        SINH[bai]()
        print('Da sinh', bai)

main()
