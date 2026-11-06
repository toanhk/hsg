# SINH TEST cho 6 bai buoi 7 (Day con: LIS, LCS, sua xau)
#   Tren lop : LIS, LCS, SUAXAU        Ve nha: DOIXUNG, TENLUA, THAPHOP
# Cau truc thu muc theo Themis: test/LIS/Test01/LIS.INP + LIS.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau de kiem cheo:
#   LIS, TENLUA, THAPHOP: cay Fenwick lay max (nen gia tri) thay cho bisect;
#   LCS: QHD bit song song tren so nguyen lon; SUAXAU: bang 2 chieu day du;
#   DOIXUNG: QHD tren doan f[l][r] thay cho LCS(S, dao S).
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py              -> sinh ca 6 bai (~15 giay)
#       python sinh_test.py LIS LCS      -> chi sinh cac bai ke ten
import os, random, sys

random.seed(2026)
GOC = 'test'
CHU = 'abcdefghijklmnopqrstuvwxyz'

def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

# ---------- Fenwick lay max tren chi so 1..m (dung chung cho LIS, TENLUA, THAPHOP) ----------
def lis_fenwick(a, chat=True):
    # do dai day con tang (chat=True) hoac khong giam (chat=False) dai nhat
    gt = sorted(set(a))
    hang = {v: i + 1 for i, v in enumerate(gt)}
    m = len(gt)
    bit = [0] * (m + 1)
    tot = 0
    for x in a:
        r = hang[x] - 1 if chat else hang[x]      # lay max tren cac gia tri < x (hoac <= x)
        b = 0
        while r > 0:
            if bit[r] > b: b = bit[r]
            r -= r & -r
        b += 1
        if b > tot: tot = b
        i = hang[x]
        while i <= m:
            if bit[i] < b: bit[i] = b
            i += i & -i
    return tot

# ---------------- LIS ----------------
def sinh_lis():
    CO = [(1, 'ngau'), (8, 'ngau'), (20, 'tang'), (20, 'lap'),
          (3000, 'ngau'), (3000, 'bang'), (2999, 'nho'),
          (5 * 10**5, 'ngau'), (5 * 10**5, 'nho'), (5 * 10**5, 'tang')]
    for so, (n, kieu) in enumerate(CO, 1):
        if kieu == 'tang':                        # tang chat -> dap an n (trau 2^20 nhanh: test thoi gian)
            a = sorted(random.sample(range(-10**9, 10**9), n))
            if so == 10:                          # tang nhung chen nhieu gia tri bang nhau / nhieu
                for i in range(0, n, 3):
                    a[i] = a[i - 1] if i else a[i]
        elif kieu == 'lap':                       # nhieu so bang nhau: bay "tang chat"
            a = [random.choice([5, 5, 5, 7, 3]) for _ in range(n)]
        elif kieu == 'bang':                      # moi phan tu bang nhau -> dap an 1
            a = [-7] * n
        elif kieu == 'nho':                       # gia tri nho, nhieu trung lap
            a = [random.randint(-50, 50) for _ in range(n)]
        else:
            a = [random.randint(-10**9, 10**9) for _ in range(n)]
        if so == 2:
            a = [3, 1, 4, 1, 5, 9, 2, 6]          # vi du trong de: 3 4 5 9 hoac 1 4 5 6 -> 4
        ghi('LIS', so, f'{n}\n' + ' '.join(map(str, a)) + '\n', f'{lis_fenwick(a)}\n')

# ---------------- LCS ----------------
def lcs_bit(A, B):
    M = {}
    for j, y in enumerate(B):
        M[y] = M.get(y, 0) | (1 << j)
    row = 0
    for x in A:
        X = M.get(x, 0) | row
        row = X & ((X - ((row << 1) | 1)) ^ X)
    return bin(row).count('1')

def xau(n, k):
    return ''.join(random.choice(CHU[:k]) for _ in range(n))

def sinh_lcs():
    CO = [(1, 1, 2), (7, 6, 4), (15, 15, 2), (15, 14, 26),
          (500, 500, 4), (500, 300, 26), (499, 500, 2),
          (2000, 2000, 4), (2000, 2000, 26), (2000, 2000, 2)]
    for so, (n, m, k) in enumerate(CO, 1):
        A, B = xau(n, k), xau(m, k)
        if so == 1:
            A, B = 'a', 'b'                       # khong co ky tu chung -> 0
        elif so == 2:
            A, B = 'abcbdab', 'bdcaba'            # vi du kinh dien -> 4
        elif so == 7:
            B = A[1:] + 'a'                       # gan giong nhau
        elif so == 10:                            # B la A bi xoa/thay rai rac -> LCS lon
            B = list(A)
            for _ in range(300):
                B[random.randrange(m)] = random.choice('ab')
            B = ''.join(B)
        ghi('LCS', so, f'{A}\n{B}\n', f'{lcs_bit(A, B)}\n')

# ---------------- SUAXAU ----------------
def sua_bang(A, B):
    n, m = len(A), len(B)
    f = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): f[i][0] = i
    for j in range(m + 1): f[0][j] = j
    for i in range(1, n + 1):
        fi, fp, x = f[i], f[i - 1], A[i - 1]
        for j in range(1, m + 1):
            if x == B[j - 1]:
                fi[j] = fp[j - 1]
            else:
                fi[j] = 1 + min(fp[j - 1], fp[j], fi[j - 1])
    return f[n][m]

def sinh_suaxau():
    CO = [(1, 1, 2), (5, 3, 26), (6, 6, 3), (6, 1, 2),
          (300, 300, 4), (300, 100, 26), (1, 300, 2),
          (1500, 1500, 4), (1500, 1500, 26), (1500, 1400, 2)]
    for so, (n, m, k) in enumerate(CO, 1):
        A, B = xau(n, k), xau(m, k)
        if so == 2:
            A, B = 'sunday', 'saturday'           # vi du trong de -> 3
        elif so == 9:                             # B = A sau ~200 phep ngau nhien -> dap an nho
            B = list(A)
            for _ in range(200):
                p = random.randrange(len(B))
                r = random.randrange(3)
                if r == 0: B[p] = random.choice(CHU)
                elif r == 1: B.pop(p)
                else: B.insert(p, random.choice(CHU))
            B = ''.join(B)
        ghi('SUAXAU', so, f'{A}\n{B}\n', f'{sua_bang(A, B)}\n')

# ---------------- DOIXUNG ----------------
def lps_doan(S):
    n = len(S)
    f = [[0] * n for _ in range(n)]
    for l in range(n - 1, -1, -1):
        fl, fs = f[l], f[l + 1] if l + 1 < n else None
        fl[l] = 1
        for r in range(l + 1, n):
            if S[l] == S[r]:
                fl[r] = (fs[r - 1] if r - 1 > l else 0) + 2
            else:
                fl[r] = max(fs[r], fl[r - 1])
    return f[0][n - 1]

def sinh_doixung():
    CO = [(1, 2), (7, 26), (15, 2), (15, 26),
          (500, 3), (500, 26), (500, 1),
          (2000, 4), (2000, 26), (2000, 2)]
    for so, (n, k) in enumerate(CO, 1):
        S = xau(n, k)
        if so == 2:
            S = 'abcbcda'                         # vi du: xoa thanh 'abcba' hoac 'acbca' -> 5
        elif so == 4:
            S = 'abcdefghijklmno'                 # moi ky tu khac nhau -> 1
        elif so == 6:                             # da doi xung san -> n
            h = xau(250, 26); S = h + h[::-1]
        elif so == 9:                             # doi xung bi chen nhieu ky tu rac
            h = xau(800, 26); S = list(h + h[::-1])
            for _ in range(400):
                S.insert(random.randrange(len(S)), random.choice(CHU))
            S = ''.join(S)
        ghi('DOIXUNG', so, S + '\n', f'{lps_doan(S)}\n')

# ---------------- TENLUA ----------------
def sinh_tenlua():
    CO = [(1, 'ngau'), (8, 'ngau'), (12, 'bang'), (12, 'nho'),
          (3000, 'ngau'), (3000, 'giam'), (3000, 'nho'),
          (2 * 10**5, 'ngau'), (2 * 10**5, 'nho'), (2 * 10**5, 'tang')]
    for so, (n, kieu) in enumerate(CO, 1):
        if kieu == 'bang':
            h = [100] * n                         # mot he thong chan het -> n, 1
        elif kieu == 'nho':
            h = [random.randint(1, 20) for _ in range(n)]
        elif kieu == 'giam':                      # khong tang (co lap) -> n, 1
            h = sorted((random.randint(1, 500) for _ in range(n)), reverse=True)
        elif kieu == 'tang':                      # tang chat -> 1, n
            h = sorted(random.sample(range(1, 10**9 + 1), n))
        else:
            h = [random.randint(1, 10**9) for _ in range(n)]
        if so == 2:
            h = [389, 207, 155, 300, 299, 170, 158, 65]   # vi du trong de -> 6, 2
        neg = [-x for x in h]
        ghi('TENLUA', so, f'{n}\n' + ' '.join(map(str, h)) + '\n',
            f'{lis_fenwick(neg, chat=False)}\n{lis_fenwick(h)}\n')

# ---------------- THAPHOP ----------------
def thap_fenwick(hop):
    # xu ly theo x tang, nhom cung x tinh xong HET roi moi cap nhat cay (de khong noi 2 hop cung x)
    hop = sorted((min(p, q), max(p, q)) for p, q in hop)
    gt = sorted(set(y for _, y in hop))
    hang = {v: i + 1 for i, v in enumerate(gt)}
    m = len(gt)
    bit = [0] * (m + 1)
    tot, i, n = 0, 0, len(hop)
    while i < n:
        j = i
        while j < n and hop[j][0] == hop[i][0]:
            j += 1
        kq = []
        for t in range(i, j):
            r, b = hang[hop[t][1]] - 1, 0
            while r > 0:
                if bit[r] > b: b = bit[r]
                r -= r & -r
            kq.append(b + 1)
        for t in range(i, j):
            v, p = kq[t - i], hang[hop[t][1]]
            if v > tot: tot = v
            while p <= m:
                if bit[p] < v: bit[p] = v
                p += p & -p
        i = j
    return tot

def sinh_thaphop():
    CO = [(1, 10), (4, 10), (10, 6), (10, 10**9),
          (3000, 100), (3000, 10**9), (3000, 30),
          (2 * 10**5, 10**9), (2 * 10**5, 1000), (2 * 10**5, 10**9)]
    for so, (n, hi) in enumerate(CO, 1):
        hop = [(random.randint(1, hi), random.randint(1, hi)) for _ in range(n)]
        if so == 2:
            hop = [(4, 3), (2, 5), (5, 6), (1, 2)]   # vi du trong de: (1,2) (3,4) (5,6) -> 3
        elif so == 3:                                # nhieu hop cung canh nho 2: sap y tang se ra 9 thay vi 4
            hop = [(1, 1)] + [(2, k) if k % 2 else (k, 2) for k in range(3, 10)] + [(3, 10), (11, 4)]
        elif so == 10:                               # moi x co 2 hop (x, 2x), (x, 2x+1): dung n/2, sap sai ra n
            hop = []
            for x in range(1, n // 2 + 1):
                for y in (2 * x, 2 * x + 1):
                    hop.append((x, y) if random.random() < 0.5 else (y, x))
            random.shuffle(hop)
        ghi('THAPHOP', so, f'{len(hop)}\n' + '\n'.join(f'{p} {q}' for p, q in hop) + '\n',
            f'{thap_fenwick(hop)}\n')

SINH = {'LIS': sinh_lis, 'LCS': sinh_lcs, 'SUAXAU': sinh_suaxau,
        'DOIXUNG': sinh_doixung, 'TENLUA': sinh_tenlua, 'THAPHOP': sinh_thaphop}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        SINH[bai]()
        print('Da sinh', bai)

main()
