# SINH TEST cho 6 bai buoi 5 (QHD mot chieu)
#   Tren lop : KHONGKE, DOANMAX, TORAO        Ve nha: ECHNHAY, COPHIEU, XOA1
# Cau truc thu muc theo Themis: test/KHONGKE/Test01/KHONGKE.INP + KHONGKE.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau de kiem cheo:
#   KHONGKE 2 mang lay/bo, DOANMAX tien to tru tien to nho nhat, TORAO cong thuc f[i] = (k-1)(f[i-1]+f[i-2]),
#   ECHNHAY QHD "day toi", COPHIEU max hau to, XOA1 Kadane 2 chieu (trai sang, phai sang) ghep quanh o bi xoa.
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py                -> sinh ca 6 bai (~15 giay)
#       python sinh_test.py KHONGKE XOA1   -> chi sinh cac bai ke ten
import os, random, sys

random.seed(2026)
GOC = 'test'
MOD = 10**9 + 7
GT = 10**9                              # |a[i]| <= 10^9

def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

def day(n, lo, hi):
    return [random.randint(lo, hi) for _ in range(n)]

def ghi_day(bai, so, a, dap_an, dau=''):
    ghi(bai, so, f'{len(a)}{dau}\n' + ' '.join(map(str, a)) + '\n', str(dap_an) + '\n')

# Kich thuoc chung cho 3 bai day so: subtask 1 nho, subtask 2 n <= 5000, subtask 3 n <= 10^6
CO_N = [1, 6, 20, 20, 5000, 5000, 4999, 10**6, 10**6, 10**6]

# ---------------- KHONGKE ----------------
def dap_an_khongke(a):
    lay, bo = [0] * len(a), [0] * len(a)    # lay[i]: co chon a[i]; bo[i]: khong chon a[i]
    for i, x in enumerate(a):
        lay[i] = x + (bo[i - 1] if i else 0)
        bo[i] = max(lay[i - 1], bo[i - 1]) if i else 0
    return max(lay[-1], bo[-1], 0)

def sinh_khongke():
    for so, n in enumerate(CO_N, 1):
        if so == 1:
            a = [-5]                         # chon rong -> 0
        elif so == 2:
            a = [3, 2, 7, 10, 1, 5]          # vi du trong giao an: 3 + 10 + 5 = 18
        elif so in (4, 9):
            a = day(n, -GT, -1)              # toan am -> 0
        elif so == 7:
            a = day(n, 0, 10)                # nhieu so 0 va so bang nhau
        elif so == 10:
            a = day(n, GT - 1000, GT)        # toan duong lon -> tong ~ 5*10^14
        else:
            a = day(n, -GT, GT)
        ghi_day('KHONGKE', so, a, dap_an_khongke(a))

# ---------------- DOANMAX ----------------
def dap_an_doanmax(a):
    s, thap, tot = 0, 0, -10**30            # tong(l..r) = S[r] - S[l-1]; giu min S[0..r-1]
    for x in a:
        s += x
        if s - thap > tot:
            tot = s - thap
        if s < thap:
            thap = s
    return tot

def sinh_doanmax():
    for so, n in enumerate(CO_N, 1):
        if so == 1:
            a = [-7]
        elif so == 2:
            a = [2, -3, 4, -1, 2, -5]        # doan [4, -1, 2] = 5
        elif so in (4, 9):
            a = day(n, -GT, -1)              # toan am -> so lon nhat (bay khoi tao tot = 0)
        elif so == 7:
            a = day(n, -100, 101)            # doan dai, tong lech duong nhe
        elif so == 10:
            a = day(n, 1, GT)                # toan duong -> tong ca day ~ 5*10^14
        else:
            a = day(n, -GT, GT)
        ghi_day('DOANMAX', so, a, dap_an_doanmax(a))

# ---------------- TORAO ----------------
def dap_an_torao(n, k):
    # f[i] = so cach to i cot. Cot i khac mau cot i-1: f[i-1]*(k-1);
    # cot i giong cot i-1 (thi cot i-1 khac cot i-2): f[i-2]*(k-1)
    f = [0] * (n + 1)
    f[1] = k % MOD
    if n >= 2:
        f[2] = k * k % MOD
    for i in range(3, n + 1):
        f[i] = (k - 1) * (f[i - 1] + f[i - 2]) % MOD
    return f[n]

def sinh_torao():
    CO = [(1, 1), (3, 2), (8, 1), (8, 4),
          (5000, 2), (5000, 10**9), (4000, 3),
          (10**6, 10**9), (10**6, 2), (1, MOD + 1)]   # n = 1, k = MOD + 1: in k chua mod -> sai
    for so, (n, k) in enumerate(CO, 1):
        ghi('TORAO', so, f'{n} {k}\n', str(dap_an_torao(n, k)) + '\n')

# ---------------- ECHNHAY ----------------
def dap_an_echnhay(h, k):
    n = len(h)
    f = [float('inf')] * n
    f[0] = 0
    for i in range(n):                       # "day toi": tu hon i cap nhat cac hon i+1..i+k
        fi, hi = f[i], h[i]
        for j in range(i + 1, min(n, i + k + 1)):
            v = fi + abs(hi - h[j])
            if v < f[j]:
                f[j] = v
    return f[-1]

def sinh_echnhay():
    CO = [(2, 1), (6, 2), (20, 3), (20, 20),
          (10**5, 2), (10**5, 1), (99999, 2),
          (10**5, 20), (10**5, 20), (10**5, 15)]
    for so, (n, k) in enumerate(CO, 1):
        if so == 2:
            h = [10, 30, 40, 50, 20, 60]
        elif so == 9:                        # rang cua: nhay xa co loi
            h = [10**4 if i % 3 else 1 for i in range(n)]
        elif so == 10:
            h = sorted(day(n, 1, 10**4))     # tang dan -> dap an h[n] - h[1] voi moi cach
        else:
            h = day(n, 1, 10**4)
        ghi('ECHNHAY', so, f'{n} {k}\n' + ' '.join(map(str, h)) + '\n',
            str(dap_an_echnhay(h, k)) + '\n')

# ---------------- COPHIEU ----------------
def dap_an_cophieu(p):
    cao, tot = 0, 0                          # duyet tu phai sang: cao = max p[i+1..n]
    for x in reversed(p):
        tot = max(tot, cao - x)
        cao = max(cao, x)
    return tot

def sinh_cophieu():
    CO = [1, 6, 1000, 1000, 5000, 5000, 5000, 10**6, 10**6, 10**6]
    for so, n in enumerate(CO, 1):
        if so == 2:
            p = [7, 1, 5, 3, 6, 4]           # mua 1 ban 6 -> 5
        elif so in (4, 9):
            p = sorted(day(n, 1, GT), reverse=True)   # giam dan -> 0
        elif so == 7:                        # thap nhat o cuoi, cao nhat o dau: bay "max - min"
            p = day(n, 10**8, 9 * 10**8)
            p[0], p[-1] = GT, 1
        elif so == 10:
            p = sorted(day(n, 1, GT))        # tang dan
        else:
            p = day(n, 1, GT)
        ghi_day('COPHIEU', so, p, dap_an_cophieu(p))

# ---------------- XOA1 ----------------
def dap_an_xoa1(a):
    n = len(a)
    L, R = a[:], a[:]                        # L[i]: doan tot nhat ket thuc tai i; R[i]: bat dau tai i
    for i in range(1, n):
        L[i] = a[i] + max(L[i - 1], 0)
    for i in range(n - 2, -1, -1):
        R[i] = a[i] + max(R[i + 1], 0)
    tot = max(L)
    for i in range(1, n - 1):                # xoa a[i], ghep doan ket thuc i-1 voi doan bat dau i+1
        tot = max(tot, L[i - 1] + R[i + 1])
    if n >= 2:                               # xoa a[0] hoac a[n-1] (dau doan): doan con lai mot phia
        tot = max(tot, R[1], L[n - 2])
    return tot

def sinh_xoa1():
    CO = [1, 5, 100, 100, 5000, 5000, 5000, 10**6, 10**6, 10**6]
    for so, n in enumerate(CO, 1):
        if so == 1:
            a = [-3]                         # khong duoc xoa het -> -3
        elif so == 2:
            a = [1, -2, 0, 3, -1]            # xoa -2: 1 + 0 + 3 = 4
        elif so in (4, 9):
            a = day(n, -GT, -1)              # toan am -> so lon nhat
        elif so == 7:                        # moi doan duong bi chan boi mot so am rat lon
            a = [-GT if i % 50 == 49 else random.randint(-1000, 3000) for i in range(n)]
        elif so == 10:
            a = [-GT if i % 1000 == 999 else random.randint(-GT // 10, GT // 5) for i in range(n)]
        else:
            a = day(n, -GT, GT)
        ghi_day('XOA1', so, a, dap_an_xoa1(a))

SINH = {'KHONGKE': sinh_khongke, 'DOANMAX': sinh_doanmax, 'TORAO': sinh_torao,
        'ECHNHAY': sinh_echnhay, 'COPHIEU': sinh_cophieu, 'XOA1': sinh_xoa1}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        SINH[bai]()
        print('Da sinh', bai)

main()
