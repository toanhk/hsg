# SINH TEST cho de kiem tra cuoi giai doan 2 (QHD co ban): MUAVE, BALO, NUI
# Cau truc thu muc theo Themis: test/MUAVE/Test01/MUAVE.INP + MUAVE.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau de kiem cheo:
#   MUAVE QHD "day toi" tu dau hang, BALO bang theo khoi luong (khi W nho) hoac bang tu dien
#   {gia tri: khoi luong nho nhat} (khi W lon), NUI LIS O(n^2) cho n nho va Fenwick (cay chi so nhi
#   phan) theo chieu cao da nen cho n lon.
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py              -> sinh ca 3 bai (~15 giay)
#       python sinh_test.py NUI          -> chi sinh bai ke ten
import os, random, sys

random.seed(2026)
GOC = 'test'

def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

# ---------------- MUAVE ----------------
def dap_an_muave(t, r, s):
    n = len(t)
    INF = 10**18
    f = [INF] * (n + 1)
    f[0] = 0
    for i in range(n):                 # "day toi": tu f[i] (i nguoi dau xong) cho nhom tiep theo
        x = f[i]
        if x + t[i] < f[i + 1]: f[i + 1] = x + t[i]
        if i + 2 <= n and x + r[i] < f[i + 2]: f[i + 2] = x + r[i]
        if i + 3 <= n and x + s[i] < f[i + 3]: f[i + 3] = x + s[i]
    return f[n]

def sinh_muave():
    CO = [3, 1, 15, 20, 10**5, 10**5, 99999, 5 * 10**5, 5 * 10**5, 5 * 10**5]
    for so, n in enumerate(CO, 1):
        if so == 1:
            t, r, s = [5, 4, 6], [7, 9], [16]          # vi du trong de
        elif so == 7:                                  # mua chung luon loi -> dung nhom 3 gan het
            t = [random.randint(20000, 30000) for _ in range(n)]
            r = [random.randint(15000, 20000) for _ in range(n - 1)]
            s = [random.randint(10000, 15000) for _ in range(n - 2)]
        elif so == 10:                                 # mua chung dat hon -> dap an = tong t
            t = [random.randint(1, 10000) for _ in range(n)]
            r = [random.randint(20001, 30000) for _ in range(n - 1)]
            s = [random.randint(20001, 30000) for _ in range(n - 2)]
        else:                                          # r, s quanh tong cua t de lua chon kho
            t = [random.randint(1, 10000) for _ in range(n)]
            r = [min(30000, max(1, t[i] + t[i + 1] + random.randint(-3000, 3000))) for i in range(n - 1)]
            s = [min(30000, max(1, t[i] + t[i + 1] + t[i + 2] + random.randint(-5000, 5000)))
                 for i in range(n - 2)]
        inp = f'{n}\n' + ' '.join(map(str, t)) + '\n' + ' '.join(map(str, r)) + '\n' + ' '.join(map(str, s)) + '\n'
        ghi('MUAVE', so, inp, str(dap_an_muave(t, r, s)) + '\n')

# ---------------- BALO ----------------
def dap_an_balo(W, ds):
    if W <= 2 * 10**5:                 # bang theo khoi luong, 2 hang
        f = [0] * (W + 1)
        for w, v in ds:
            g = f[:]
            for c in range(w, W + 1):
                if f[c - w] + v > g[c]:
                    g[c] = f[c - w] + v
            f = g
        return f[W]
    best = {0: 0}                      # gia tri -> khoi luong nho nhat
    for w, v in ds:
        moi = dict(best)
        for x, kl in best.items():
            if kl + w <= W and (x + v not in moi or moi[x + v] > kl + w):
                moi[x + v] = kl + w
        best = moi
    return max(best)

def sinh_balo():
    for so in range(1, 11):
        if so == 1:
            W, ds = 10, [(5, 10), (4, 40), (6, 30), (3, 50)]          # vi du trong de: 90
        elif so == 2:
            W, ds = 3, [(4, 100), (5, 200)]                           # khong lay duoc gi
        elif so <= 4:
            n = 20
            W = random.randint(100, 5000)
            ds = [(random.randint(1, W // 4), random.randint(1, 500)) for _ in range(n)]
        elif so <= 7:
            n = 100
            W = [50000, 50000, 31415][so - 5]
            ds = [(random.randint(1, 2000), random.randint(1, 500)) for _ in range(n)]
            if so == 6:                                               # vat nhe, lay gan het
                ds = [(random.randint(1, 600), random.randint(1, 500)) for _ in range(n)]
        else:
            n = 100
            if so == 8:
                ds = [(random.randint(1, 10**9), random.randint(1, 500)) for _ in range(n)]
                W = sum(w for w, _ in ds) // 2
            elif so == 9:                                             # gia tri lon dong deu
                ds = [(random.randint(10**7, 10**9), 500 - random.randint(0, 3)) for _ in range(n)]
                W = 10**9
            else:
                ds = [(random.randint(10**8, 10**9), random.randint(1, 500)) for _ in range(n)]
                W = 10**9
        inp = f'{len(ds)} {W}\n' + '\n'.join(f'{w} {v}' for w, v in ds) + '\n'
        ghi('BALO', so, inp, str(dap_an_balo(W, ds)) + '\n')

# ---------------- NUI ----------------
def nui_n2(h):
    n = len(h)
    L = [1] * n
    for i in range(n):
        for j in range(i):
            if h[j] < h[i] and L[j] + 1 > L[i]:
                L[i] = L[j] + 1
    R = [1] * n
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if h[j] < h[i] and R[j] + 1 > R[i]:
                R[i] = R[j] + 1
    return n - max(L[i] + R[i] - 1 for i in range(n))

def lis_fenwick(h):                    # L[i] = 1 + max L[j] (h[j] < h[i]) bang Fenwick max theo hang
    vals = sorted(set(h))
    hang = {v: i + 1 for i, v in enumerate(vals)}
    m = len(vals)
    bit = [0] * (m + 1)
    L = []
    for x in h:
        k = hang[x] - 1                # max tren cac chieu cao nho hon NGAT
        b = 0
        while k > 0:
            if bit[k] > b: b = bit[k]
            k -= k & -k
        v = b + 1
        L.append(v)
        k = hang[x]
        while k <= m:
            if bit[k] < v: bit[k] = v
            k += k & -k
    return L

def nui_fenwick(h):
    L = lis_fenwick(h)
    R = lis_fenwick(h[::-1])[::-1]
    return len(h) - max(a + b - 1 for a, b in zip(L, R))

def sinh_nui():
    CO = [8, 1, 15, 15, 2000, 2000, 2000, 2 * 10**5, 2 * 10**5, 2 * 10**5]
    for so, n in enumerate(CO, 1):
        if so == 1:
            h = [1, 5, 2, 4, 7, 3, 6, 2]                 # vi du trong de
        elif so == 2:
            h = [42]
        elif so == 4:
            h = [7] * 15                                 # bang nhau: chi giu 1 cay
        elif so == 6:
            h = [random.randint(1, 5) for _ in range(n)] # nhieu cay bang nhau
        elif so == 7:                                    # gan nhu da la nui, xao tron vai cho
            k = random.randint(n // 3, 2 * n // 3)
            h = sorted(random.sample(range(1, 10**9), k)) + sorted(random.sample(range(1, 10**9), n - k), reverse=True)
            for _ in range(50):
                i, j = random.randrange(n), random.randrange(n)
                h[i], h[j] = h[j], h[i]
        elif so == 9:
            h = list(range(1, n + 1))                    # tang het: chat 0
        elif so == 10:                                   # hai nui chong len nhau
            h = [random.randint(1, 10**9) for _ in range(n)]
            for i in range(0, n, 2):
                h[i] = i if i < n // 2 else 2 * n - i
        else:
            h = [random.randint(1, 10**9) for _ in range(n)]
        if n <= 2000:
            kq = nui_n2(h)
            assert kq == nui_fenwick(h), 'Fenwick lech O(n^2)!'
        else:
            kq = nui_fenwick(h)
        ghi('NUI', so, f'{n}\n' + ' '.join(map(str, h)) + '\n', str(kq) + '\n')

SINH = {'MUAVE': sinh_muave, 'BALO': sinh_balo, 'NUI': sinh_nui}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        SINH[bai]()
        print('Da sinh', bai)

main()
