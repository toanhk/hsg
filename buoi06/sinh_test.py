# SINH TEST cho 6 bai buoi 6 (Cai tui)
#   Tren lop : TUI01, TUIVOHAN, TRUYVET        Ve nha: CHIAKEO, DOITIEN2, TUILON
# Cau truc thu muc theo Themis: test/TUI01/Test01/TUI01.INP + TUI01.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau de kiem cheo:
#   TUI01 "day toi" tren 2 hang voi khoi luong DUNG s, TUIVOHAN vong ngoai la s,
#   TRUYVET bang 2 chieu + truy vet, CHIAKEO so nguyen lon tren CA tong (khong cat mat na),
#   DOITIEN2 BFS tren cac so tien (moi to = 1 canh), TUILON "day toi" bang dict gia tri -> khoi luong.
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py               -> sinh ca 6 bai (~15 giay)
#       python sinh_test.py TUI01 CHIAKEO -> chi sinh cac bai ke ten
# Moi bai co seed rieng (random.seed('TUI01-2026'), ...) nen sinh rieng mot bai hay ca bo deu ra CUNG test.
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

def de_vat(W, vat):
    return f'{len(vat)} {W}\n' + ''.join(f'{w} {v}\n' for w, v in vat)

def vat_ngau_nhien(n, wmax, vmax):
    return [(random.randint(1, wmax), random.randint(1, vmax)) for _ in range(n)]

# ---------------- TUI01 ----------------
def dap_an_tui01(W, vat):
    AM = -1
    g = [AM] * (W + 1)                # g[s] = gia tri lon nhat voi khoi luong DUNG bang s
    g[0] = 0
    for w, v in vat:
        moi = g[:]
        for s in range(W - w + 1):    # "day toi": tu trang thai s sang s + w (dung hang cu g)
            if g[s] >= 0 and g[s] + v > moi[s + w]:
                moi[s + w] = g[s] + v
        g = moi
    return max(g)

def sinh_tui01():
    CO = [(1, 10, 10), (4, 10, 20), (12, 100, 60), (15, 1000, 1000),      # (n, W, w lon nhat)
          (50, 1000, 100), (100, 1000, 1000), (100, 1000, 30),
          (100, 50000, 1000), (100, 50000, 100), (100, 50000, 50000)]
    for so, (n, W, wm) in enumerate(CO, 1):
        vat = vat_ngau_nhien(n, wm, 10**9)
        if so == 1:
            vat = [(3, 5)]            # mot vat: ban duyet xuoi se lay 3 lan -> 15, dung la 5
        elif so == 2:
            vat = [(5, 10), (4, 40), (6, 30), (3, 50)]   # vi du trong de: 90
        elif so == 3:                 # tong khoi luong <= W: lay het
            vat = vat_ngau_nhien(n, 8, 10**9)
        elif so == 7:                 # vat nang hon W lan vao
            for i in range(0, n, 7):
                vat[i] = (W + random.randint(1, 50), 10**9)
        elif so == 10:                # moi vat deu nang hon nua W -> chi lay duoc 1 vat; gia tri ~ ti le khoi luong
            vat = [(w, w * 20000 + random.randint(0, 10**6)) for w in
                   (random.randint(W // 2 + 1, W) for _ in range(n))]
        ghi('TUI01', so, de_vat(W, vat), str(dap_an_tui01(W, vat)) + '\n')

# ---------------- TUIVOHAN ----------------
def dap_an_tuivohan(W, vat):
    f = [0] * (W + 1)
    for s in range(1, W + 1):         # vong NGOAI la s: f[s] = max(f[s-1], f[s-w] + v)
        b = f[s - 1]
        for w, v in vat:
            if w <= s and f[s - w] + v > b:
                b = f[s - w] + v
        f[s] = b
    return f[W]

def sinh_tuivohan():
    CO = [(1, 10, 10), (3, 20, 10), (5, 50, 20), (5, 50, 50),
          (30, 1000, 200), (100, 1000, 1000), (100, 999, 50),
          (100, 50000, 1000), (100, 50000, 50), (100, 49999, 50000)]
    for so, (n, W, wm) in enumerate(CO, 1):
        vat = vat_ngau_nhien(n, wm, 10**6)
        if so == 1:
            vat = [(3, 5)]            # 3 cai -> 15
        elif so == 2:
            vat = [(5, 10), (4, 40), (6, 30)]
        elif so == 4:                 # vat nho gia thap, vat to gia cao: phai tron
            vat = [(7, 100), (11, 160), (13, 190), (50, 1000), (49, 960)]
        elif so == 10:                # khong co vat nao khoi luong < 100: f[s] = 0 voi s nho
            vat = [(random.randint(100, W), random.randint(1, 10**9)) for _ in range(n)]
        ghi('TUIVOHAN', so, de_vat(W, vat), str(dap_an_tuivohan(W, vat)) + '\n')

# ---------------- TRUYVET ----------------
def dap_an_truyvet(W, vat):
    n = len(vat)
    f = [[0] * (W + 1)]
    for i in range(1, n + 1):
        w, v = vat[i - 1]
        tr = f[-1]
        hang = tr[:]
        for s in range(w, W + 1):
            if tr[s - w] + v > hang[s]:
                hang[s] = tr[s - w] + v
        f.append(hang)
    chon, s = [], W
    for i in range(n, 0, -1):         # f[i][s] != f[i-1][s] -> bat buoc lay vat i
        if f[i][s] != f[i - 1][s]:
            chon.append(i)
            s -= vat[i - 1][0]
    chon.reverse()
    return f'{f[n][W]}\n{len(chon)}\n' + ' '.join(map(str, chon)) + '\n'

def sinh_truyvet():
    CO = [(1, 10, 10), (4, 10, 6), (10, 100, 40), (15, 1000, 300),
          (50, 1000, 100), (100, 1000, 500), (100, 1000, 20),
          (100, 30000, 1000), (100, 30000, 100), (100, 30000, 30000)]
    for so, (n, W, wm) in enumerate(CO, 1):
        vat = vat_ngau_nhien(n, wm, 10**6)
        if so == 1:
            vat = [(11, 5)]           # khong lay duoc gi: 0, k = 0, dong 3 rong
        elif so == 2:
            vat = [(5, 10), (4, 40), (6, 30), (3, 50)]
        elif so == 7:                 # nhieu vat giong nhau -> rat nhieu cach toi uu
            vat = [(random.choice([4, 6, 10]), 0) for _ in range(n)]
            vat = [(w, w * 3) for w, _ in vat]
        ghi('TRUYVET', so, de_vat(W, vat), dap_an_truyvet(W, vat))

# ---------------- CHIAKEO ----------------
def dap_an_chiakeo(a):
    tong = sum(a)
    bits = 1
    for x in a:                       # khong cat mat na: giu ca cac tong > tong/2
        bits |= bits << x
    s = bin(bits)[:1:-1]              # s[t] = '1' neu tao duoc tong t
    t = tong // 2
    while s[t] != '1':
        t -= 1
    return tong - 2 * t

def sinh_chiakeo():
    CO = [(1, 2000), (4, 10), (12, 2000), (15, 2000),
          (50, 100), (100, 100), (100, 100),
          (500, 2000), (500, 2000), (500, 2000)]
    for so, (n, am) in enumerate(CO, 1):
        a = [random.randint(1, am) for _ in range(n)]
        if so == 2:
            a = [3, 1, 4, 2]          # vi du: 5 / 5 -> 0
        elif so == 4:                 # mot goi rat to: chenh lech = goi to - phan con lai
            a = [random.randint(1, 50) for _ in range(n - 1)] + [2000]
        elif so == 7:                 # toan so chan + mot so le -> tong le, dap an >= 1
            a = [2 * random.randint(1, 50) for _ in range(n - 1)] + [51]
        elif so == 9:                 # toan so chia het cho 7 -> dap an la boi cua 7
            a = [7 * random.randint(1, 285) for _ in range(n)]
        ghi('CHIAKEO', so, f'{n}\n' + ' '.join(map(str, a)) + '\n', str(dap_an_chiakeo(a)) + '\n')

# ---------------- DOITIEN2 ----------------
def dap_an_doitien2(c, S):
    d = [-1] * (S + 1)                # BFS: dinh = so tien, canh s -> s + c (them 1 to)
    d[0] = 0
    q = deque([0])
    while q:
        s = q.popleft()
        for x in c:
            t = s + x
            if t <= S and d[t] < 0:
                d[t] = d[s] + 1
                q.append(t)
    return d[S]

def sinh_doitien2():
    CO = [(1, 10), (3, 6), (3, 100), (3, 97),
          (10, 10000), (10, 9999), (8, 10000),
          (50, 10**5), (50, 10**5), (50, 99991)]
    for so, (m, S) in enumerate(CO, 1):
        if so == 1:
            c = [3]                   # 10 khong chia het cho 3 -> -1
        elif so == 2:
            c = [1, 3, 4]             # bay tham lam: 3 + 3
        elif so == 4:
            c = [6, 10, 15]           # 97 = 6*2 + 10*7 + 15 ... (khong co to 1)
        elif so == 6:                 # tham lam va -1 nham: khong co to nho
            c = [7, 31, 97, 250, 1001, 1777, 2003, 4096, 5000, 7919]
        elif so == 7:                 # toan menh gia chan, S chan: co to 2 nen luon doi duoc
            c = [2, 6, 8, 14, 26, 38, 50, 62]
        elif so == 8:                 # menh gia nho -> vong trong dai nhat
            c = random.sample(range(1, 200), m)
        elif so == 10:                # toan menh gia chia het cho 3, S khong chia het -> -1
            c = random.sample(range(300, 30000, 3), m)
        else:
            c = random.sample(range(2, min(S, 5000) + 1), m)
        ghi('DOITIEN2', so, f'{m} {S}\n' + ' '.join(map(str, c)) + '\n',
            str(dap_an_doitien2(c, S)) + '\n')

# ---------------- TUILON ----------------
def dap_an_tuilon(W, vat):
    g = {0: 0}                        # gia tri dat duoc -> khoi luong nho nhat
    for w, v in vat:
        moi = dict(g)
        for t, kl in g.items():       # "day toi" tu moi trang thai cu
            if kl + w < moi.get(t + v, float('inf')):
                moi[t + v] = kl + w
        g = moi
    return max(t for t, kl in g.items() if kl <= W)

def sinh_tuilon():
    CO = [(1, 10**9, 10**9), (4, 10, 6), (12, 10**9, 2 * 10**8), (15, 10**9, 10**9),
          (50, 50000, 5000), (100, 50000, 2000), (100, 50000, 50000),
          (100, 10**9, 10**8), (100, 10**9, 10**9), (100, 10**9, 10**7)]
    for so, (n, W, wm) in enumerate(CO, 1):
        vat = vat_ngau_nhien(n, wm, 500)
        if so == 1:
            vat = [(10**9, 500)]      # vua khit
        elif so == 2:
            vat = [(5, 10), (4, 40), (6, 30), (3, 50)]
        elif so == 9:                 # moi vat gia tri 500 -> nhieu trang thai trung
            vat = [(random.randint(1, wm), 500) for _ in range(n)]
        # so == 10: w <= 10^7 nen tong khoi luong <= 10^9 = W -> lay het (dap an = tong gia tri)
        kq = dap_an_tuilon(W, vat)
        if W <= 50000:
            assert kq == dap_an_tui01(W, vat), 'TUILON lech QHD theo khoi luong!'
        ghi('TUILON', so, de_vat(W, vat), str(kq) + '\n')

SINH = {'TUI01': sinh_tui01, 'TUIVOHAN': sinh_tuivohan, 'TRUYVET': sinh_truyvet,
        'CHIAKEO': sinh_chiakeo, 'DOITIEN2': sinh_doitien2, 'TUILON': sinh_tuilon}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        random.seed(bai + '-2026')
        SINH[bai]()
        print('Da sinh', bai)

main()
