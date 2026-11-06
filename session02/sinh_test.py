# SINH TEST cho 6 bai buoi 2
#   Tren lop : TONGDOAN, CAPK, DEMKHOANG      Ve nha: HANGDOI, NOIDAY, DOANK
# Cau truc thu muc theo Themis: test/TONGDOAN/Test01/TONGDOAN.INP + TONGDOAN.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau (de kiem cheo).
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py            -> sinh ca 6 bai (~1 phut, ~130 MB)
#       python sinh_test.py CAPK NOIDAY -> chi sinh cac bai ke ten
import os, random, sys, heapq
from collections import Counter, deque

random.seed(2026)
GOC = 'test'

def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

def dong(a):
    return ' '.join(map(str, a))

# ---------------- TONGDOAN ----------------
def dap_an_tongdoan(a, qs):
    s = [0] * (len(a) + 1)
    for i, x in enumerate(a):
        s[i + 1] = s[i] + x
    return '\n'.join(str(s[r] - s[l - 1]) for l, r in qs) + '\n'

def sinh_tongdoan():
    CO = [(5, 5), (100, 100), (1000, 1000), (1000, 1000),
          (10**5, 10**5), (10**5, 10**5), (10**5, 10**5),
          (10**6, 2 * 10**5), (10**6, 2 * 10**5), (10**6, 2 * 10**5)]
    for so, (n, q) in enumerate(CO, 1):
        if so == 4:
            a = [random.randint(-10**9, -1) for _ in range(n)]      # toan so am
        else:
            a = [random.randint(-10**9, 10**9) for _ in range(n)]
        qs = []
        for t in range(q):
            if t % 10 == 0:
                qs.append((1, n))                                    # ca day
            elif t % 10 == 1:
                i = random.randint(1, n); qs.append((i, i))          # l = r
            else:
                l = random.randint(1, n); r = random.randint(l, n); qs.append((l, r))
        inp = f'{n} {q}\n{dong(a)}\n' + '\n'.join(f'{l} {r}' for l, r in qs) + '\n'
        ghi('TONGDOAN', so, inp, dap_an_tongdoan(a, qs))

# ---------------- CAPK ----------------
def dap_an_capk(a, k):
    c = Counter(a)
    tong = 0
    for x, cx in c.items():
        y = k - x
        if y == x:
            tong += cx * (cx - 1)            # dem ca 2 chieu, chia 2 o cuoi
        elif y in c:
            tong += cx * c[y]
    return str(tong // 2) + '\n'

def sinh_capk():
    CO_N = [5, 100, 1000, 1000, 10**5, 10**5, 10**5, 5 * 10**5, 5 * 10**5, 5 * 10**5]
    for so, n in enumerate(CO_N, 1):
        if so in (3, 9):                      # moi so bang nhau, 2x = K -> dap an n(n-1)/2
            a = [7] * n; k = 14
        elif so == 2:                         # K khong dat duoc -> 0
            a = [random.randint(1, 10**9) for _ in range(n)]; k = -5
        elif so in (1, 5, 8):                 # gia tri nho -> rat nhieu cap
            a = [random.randint(-50, 50) for _ in range(n)]; k = random.randint(-20, 20)
        else:                                 # gia tri lon co am, K = tong 2 phan tu ngau nhien
            a = [random.randint(-10**9, 10**9) for _ in range(n)]
            k = a[0] + a[-1]
            for _ in range(n // 10):          # cai them nhieu cap cho test co y nghia
                i = random.randrange(n); j = random.randrange(n); a[j] = k - a[i]
                if abs(a[j]) > 10**9: a[j] = a[i]
        ghi('CAPK', so, f'{n} {k}\n{dong(a)}\n', dap_an_capk(a, k))

# ---------------- DEMKHOANG ----------------
def dap_an_demkhoang(a, qs):
    # Quet su kien offline: khong dung bisect, de kiem cheo loi giai mau
    b = sorted(a)
    diem = sorted(set([L for L, R in qs] + [R for L, R in qs]))
    nho_hon, nho_hon_bang = {}, {}
    i = 0
    for v in diem:
        while i < len(b) and b[i] < v:
            i += 1
        nho_hon[v] = i
        j = i
        while j < len(b) and b[j] == v:
            j += 1
        nho_hon_bang[v] = j
    return '\n'.join(str(nho_hon_bang[R] - nho_hon[L]) for L, R in qs) + '\n'

def sinh_demkhoang():
    CO = [5, 100, 1000, 1000] + [2 * 10**5] * 6
    for so, n in enumerate(CO, 1):
        q = n
        V = 10**6 if 5 <= so <= 7 or so <= 2 else 10**9
        lo = 0 if V == 10**6 else -10**9
        if so == 4:
            a = [random.randint(1, 10) for _ in range(n)]           # nhieu gia tri trung
        else:
            a = [random.randint(lo, V) for _ in range(n)]
        qs = []
        for t in range(q):
            if t % 7 == 0:
                x = random.choice(a); qs.append((x, x))              # L = R trung phan tu
            elif t % 7 == 1:
                qs.append((lo, V))                                   # ca mien
            else:
                L = random.randint(lo, V); R = random.randint(L, min(V, L + (V - lo) // 10))
                qs.append((L, R))
        inp = f'{n} {q}\n{dong(a)}\n' + '\n'.join(f'{L} {R}' for L, R in qs) + '\n'
        ghi('DEMKHOANG', so, inp, dap_an_demkhoang(a, qs))

# ---------------- HANGDOI ----------------
def sinh_hangdoi():
    CO = [6, 100, 1000, 1000, 10**5, 10**5, 10**5, 10**6, 10**6, 10**6]
    for so, Q in enumerate(CO, 1):
        lenh, out = [], []
        dq = deque()
        for t in range(Q):
            if so == 2:
                loai = random.choice([3, 4, 3, 1])                   # hay lay khi rong -> -1
            elif so in (6, 9):                                       # nua dau them dau, nua sau lay dau
                loai = 2 if t < Q // 2 else 3
            else:
                loai = random.choice([1, 2, 1, 2, 3, 4])
            if loai <= 2:
                x = random.randint(1, 10**9)
                lenh.append(f'{loai} {x}')
                dq.append(x) if loai == 1 else dq.appendleft(x)
            else:
                lenh.append(str(loai))
                if not dq:
                    out.append('-1')
                else:
                    out.append(str(dq.popleft() if loai == 3 else dq.pop()))
        if not out:                                                  # bao dam co it nhat 1 dong ra
            lenh.append('3'); out.append(str(dq.popleft()) if dq else '-1'); Q += 1
        ghi('HANGDOI', so, f'{Q}\n' + '\n'.join(lenh) + '\n', '\n'.join(out) + '\n')

# ---------------- NOIDAY ----------------
def dap_an_noiday(a):
    h = []
    for x in a:
        heapq.heappush(h, x)
    tong = 0
    while len(h) > 1:
        x = heapq.heappop(h); y = heapq.heappop(h)
        tong += x + y
        heapq.heappush(h, x + y)
    return str(tong) + '\n'

def sinh_noiday():
    CO = [1, 100, 1000, 1000, 10**5, 10**5, 10**5, 2 * 10**5, 2 * 10**5, 2 * 10**5]
    for so, n in enumerate(CO, 1):
        if so in (4, 9):
            a = [10**9] * n                                          # bang nhau, gia tri max
        elif so == 6:
            a = list(range(1, n + 1))                                # da sap xep
        else:
            a = [random.randint(1, 10**9) for _ in range(n)]
        ghi('NOIDAY', so, f'{n}\n{dong(a)}\n', dap_an_noiday(a))

# ---------------- DOANK ----------------
def dap_an_doank(a, k):
    c = Counter([0])
    s = 0; tong = 0
    for x in a:
        s += x
        tong += c[s - k]
        c[s] += 1
    return str(tong) + '\n'

def sinh_doank():
    CO_N = [5, 100, 1000, 1000, 10**5, 10**5, 10**5, 10**6, 10**6, 10**6]
    for so, n in enumerate(CO_N, 1):
        if so in (4, 10):
            a = [0] * n; k = 0                                       # dap an n(n+1)/2
        elif so == 7:
            a = [random.randint(1, 10**4) for _ in range(n)]           # toan duong
            l = random.randrange(n); k = sum(a[l:l + 5000])          # K = tong mot doan that
        else:
            a = [random.randint(-10, 10) for _ in range(n)]; k = random.randint(-15, 15)
        ghi('DOANK', so, f'{n} {k}\n{dong(a)}\n', dap_an_doank(a, k))

BAI = {'TONGDOAN': sinh_tongdoan, 'CAPK': sinh_capk, 'DEMKHOANG': sinh_demkhoang,
       'HANGDOI': sinh_hangdoi, 'NOIDAY': sinh_noiday, 'DOANK': sinh_doank}

def main():
    chon = sys.argv[1:] or list(BAI)
    for ten in chon:
        BAI[ten]()
        print('Da sinh xong', ten)

main()
