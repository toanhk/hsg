# SINH TEST cho 3 bai tren lop: TONG, CHIA3, BACDINH
# Cau truc thu muc theo Themis: test/TONG/Test01/TONG.INP + TONG.OUT
# Dap an duoc tinh bang ham "trau" (vet can, de kiem chung) ngay trong file nay.
# Chay: python sinh_test.py
import os, random

random.seed(2026)
GOC = 'test'

def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

# Subtask: 4 test n <= 1000 (40%), 3 test n <= 10^5 (30%), 3 test n <= 10^6 (30%)
CO_N = [5, 100, 1000, 1000, 10**5, 10**5, 10**5, 10**6, 10**6, 10**6]

def trau_tong(a):
    tong = 0; chan = 0
    for x in a:
        tong += x
        if x % 2 == 0:
            chan += 1
    return f'{tong}\n{chan}\n'

def trau_chia3(a):
    kq = []
    for i in range(len(a) - 1, -1, -1):
        if a[i] % 3 == 0:
            kq.append(str(a[i]))
    return '\n'.join(kq) + '\n' if kq else '-1\n'

def trau_bac(n, canh):
    deg = [0] * (n + 1)
    for u, v in canh:
        deg[u] += 1; deg[v] += 1
    best = 1
    for v in range(1, n + 1):
        if deg[v] > deg[best]:
            best = v
    return ' '.join(map(str, deg[1:])) + '\n' + str(best) + '\n'

for so, n in enumerate(CO_N, 1):
    # TONG: test 3 toan so am, test 4 toan so le (bien)
    if so == 3:
        a = [random.randint(-10**9, -1) for _ in range(n)]
    elif so == 4:
        a = [random.randrange(-10**9 + 1, 10**9, 2) for _ in range(n)]
    else:
        a = [random.randint(-10**9, 10**9) for _ in range(n)]
    ghi('TONG', so, f'{n}\n' + '\n'.join(map(str, a)) + '\n', trau_tong(a))   # moi so mot dong

    # CHIA3: test 2 khong co so nao chia het cho 3 -> -1
    if so == 2:
        a = [random.choice([1, 2]) + 3 * random.randint(0, 10**8) for _ in range(n)]
    else:
        a = [random.randint(-10**9, 10**9) for _ in range(n)]
    ghi('CHIA3', so, f'{n}\n' + ' '.join(map(str, a)) + '\n', trau_chia3(a))

    # BACDINH: so dinh = n // 10 (toi thieu 2), m = 2 * so dinh, co the co canh lap
    nd = max(2, min(10**5, n // 10))
    m = min(2 * 10**5, 2 * nd)
    if so == 1:
        canh = [(1, 2)] * m                       # bien: moi canh trung nhau
    elif so == 8:
        canh = [(1, random.randint(2, nd)) for _ in range(m)]   # hinh sao
    else:
        canh = [(random.randint(1, nd), random.randint(1, nd)) for _ in range(m)]
        canh = [(u, v) if u != v else (u, u % nd + 1) for u, v in canh]
    inp = f'{nd} {m}\n' + '\n'.join(f'{u} {v}' for u, v in canh) + '\n'
    ghi('BACDINH', so, inp, trau_bac(nd, canh))

print('Da sinh xong thu muc', GOC)
