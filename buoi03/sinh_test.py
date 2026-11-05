# SINH TEST cho 6 bai buoi 3 (De quy & quay lui)
#   Tren lop : XAUNP, TOHOP, TAPCON        Ve nha: HOANVI, QUANHAU, DIENDAU
# Cau truc thu muc theo Themis: test/XAUNP/Test01/XAUNP.INP + XAUNP.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau (vong lap, itertools,
# bitmask, QHD bang dict) de kiem cheo - khong ham nao dung de quy.
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py              -> sinh ca 6 bai (~15 giay)
#       python sinh_test.py TOHOP DIENDAU -> chi sinh cac bai ke ten
import os, random, sys
from itertools import combinations
from collections import defaultdict

random.seed(2026)
GOC = 'test'

def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

def liet_ke(ds):                      # dinh dang chung: dong 1 la so luong, sau do moi dong 1 ket qua
    return str(len(ds)) + '\n' + ''.join(s + '\n' for s in ds)

# ---------------- XAUNP ----------------
def dap_an_xaunp(n):
    ds = ['']                         # sinh theo tung do dai, giu thu tu tu dien
    for _ in range(n):
        moi = []
        for s in ds:
            moi.append(s + '0')
            if not s.endswith('1'):
                moi.append(s + '1')
        ds = moi
    return liet_ke(ds)

def sinh_xaunp():
    CO_N = [1, 2, 5, 10, 13, 15, 16, 20, 23, 24]
    for so, n in enumerate(CO_N, 1):
        ghi('XAUNP', so, f'{n}\n', dap_an_xaunp(n))

# ---------------- TOHOP ----------------
def dap_an_tohop(n, k):
    return liet_ke([' '.join(map(str, t)) for t in combinations(range(1, n + 1), k)])

def sinh_tohop():
    CO = [(4, 1), (5, 3), (10, 5), (10, 10),
          (15, 7), (17, 8), (20, 6),
          (50, 3), (40, 4), (50, 49)]
    for so, (n, k) in enumerate(CO, 1):
        ghi('TOHOP', so, f'{n} {k}\n', dap_an_tohop(n, k))

# ---------------- TAPCON ----------------
def dap_an_tapcon(a, S):
    dem = defaultdict(int)            # dem[t] = so tap con co tong t (chi giu t <= S)
    dem[0] = 1
    for x in a:
        for t, c in list(dem.items()):
            if t + x <= S:
                dem[t + x] += c
    return str(dem[S]) + '\n'

def sinh_tapcon():
    CO_N = [1, 5, 10, 10, 14, 16, 16, 20, 20, 20]
    for so, n in enumerate(CO_N, 1):
        if so in (4, 8):                                  # moi so bang nhau -> C(n, n/2) tap
            a = [10] * n; S = 10 * (n // 2)
        elif so == 7:                                     # S lon hon tong -> 0, khong cat duoc nhanh "vuot S"
            a = [random.randint(1, 10**9) for _ in range(n)]; S = sum(a) + 1
        elif so == 9:                                     # so lon gan bang nhau: tong cac tap phan biet,
            a = [10**8 + (1 << i) for i in range(n)]      # cat nhanh it tac dung (test xau cho vet can)
            random.shuffle(a); S = 10 * 10**8 + (1 << 19) - 1 + 5
        elif so in (2, 5, 10):                            # gia tri nho -> rat nhieu tap trung tong
            a = [random.randint(1, 20) for _ in range(n)]; S = sum(a) // 2
        else:                                             # S la tong mot tap ngau nhien (dap an >= 1)
            a = [random.randint(1, 10**9) for _ in range(n)]
            S = sum(x for x in a if random.random() < 0.5) or a[0]
        ghi('TAPCON', so, f'{n} {S}\n' + ' '.join(map(str, a)) + '\n', dap_an_tapcon(a, S))

# ---------------- HOANVI ----------------
def dap_an_hoanvi(s):
    p = sorted(s); n = len(p); ds = []
    while True:                       # thuat toan "hoan vi ke tiep", tu xu ly ky tu lap
        ds.append(''.join(p))
        i = n - 2
        while i >= 0 and p[i] >= p[i + 1]:
            i -= 1
        if i < 0:
            break
        j = n - 1
        while p[j] <= p[i]:
            j -= 1
        p[i], p[j] = p[j], p[i]
        p[i + 1:] = reversed(p[i + 1:])
    return liet_ke(ds)

def sinh_hoanvi():
    CO = ['a', 'cab', 'abba', 'hgfedcba',
          'aaabbbccde', 'aaaaabbbbb', 'edcbaaabbc',
          'aaaabbbbcccc', 'zzzzzyyyyyxw', 'aaaaaaaaaaaa']
    for so, s in enumerate(CO, 1):
        s = list(s); random.shuffle(s); s = ''.join(s)   # dau vao khong sap xep san
        ghi('HOANVI', so, s + '\n', dap_an_hoanvi(s))

# ---------------- QUANHAU ----------------
def dap_an_quanhau(ban):
    n = len(ban); full = (1 << n) - 1
    cam = [sum(1 << c for c in range(n) if ban[r][c] == '#') for r in range(n)]
    dem = 0
    st = [(0, 0, 0, 0)]               # ngan xep tuong minh: (hang, cot da dung, cheo trai, cheo phai) dang bitmask
    while st:
        r, cot, d1, d2 = st.pop()
        if r == n:
            dem += 1; continue
        trong = full & ~(cot | d1 | d2 | cam[r])
        while trong:
            b = trong & -trong; trong ^= b
            st.append((r + 1, cot | b, ((d1 | b) << 1) & full, (d2 | b) >> 1))
    return str(dem) + '\n'

def sinh_quanhau():
    CO = [(1, 0), (4, 0), (6, 0.15), (8, 0),
          (9, 0.1), (10, 0), (10, 0.12),
          (11, 0), (11, 0.05), (11, 0.15)]
    for so, (n, p) in enumerate(CO, 1):
        ban = [''.join('#' if random.random() < p else '.' for _ in range(n)) for _ in range(n)]
        ghi('QUANHAU', so, f'{n}\n' + '\n'.join(ban) + '\n', dap_an_quanhau(ban))

# ---------------- DIENDAU ----------------
def dap_an_diendau(s, S):
    d = [int(c) for c in s]
    trang_thai = {(0, d[0]): 1}       # (tong cac so hang da xong, so hang dang viet CO DAU) -> so cach
    for x in d[1:]:
        moi = defaultdict(int)
        for (tong, so), c in trang_thai.items():
            moi[(tong, so * 10 + (x if so >= 0 else -x))] += c   # noi chu so
            moi[(tong + so, x)] += c                              # dien '+'
            moi[(tong + so, -x)] += c                             # dien '-'
        trang_thai = moi
    return str(sum(c for (tong, so), c in trang_thai.items() if tong + so == S)) + '\n'

def sinh_diendau():
    CO_N = [1, 4, 8, 8, 9, 11, 11, 12, 13, 13]
    for so, n in enumerate(CO_N, 1):
        if so == 3:
            s = '12345678'; S = 100
        elif so == 10:
            s = '1' * n; S = 1                            # nhieu cach (so 1 lap lai)
        else:
            s = ''.join(random.choice('123456789') for _ in range(n))
            if so in (4, 8):
                S = 0
            elif so == 6:
                S = 10**13                                # khong dat duoc -> 0
            else:                                         # S = gia tri mot cach dien ngau nhien
                bt = s[0] + ''.join(random.choice(['', '+', '-']) + c for c in s[1:])
                S = eval(bt)
        ghi('DIENDAU', so, f'{s} {S}\n', dap_an_diendau(s, S))

SINH = {'XAUNP': sinh_xaunp, 'TOHOP': sinh_tohop, 'TAPCON': sinh_tapcon,
        'HOANVI': sinh_hoanvi, 'QUANHAU': sinh_quanhau, 'DIENDAU': sinh_diendau}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        SINH[bai]()
        print('Da sinh', bai)

main()
