# DO TOC DO DSU tren n = 2*10^5 phan tu, q = 2*10^5 thao tac (nua hop, nua hoi).
# So sanh: day du (nen duong + kich thuoc) / chi nen duong / chi kich thuoc / ngay tho,
# find ham rieng hay viet thang trong vong lap, nen nua duong (path halving), va find de quy.
# Hai bo du lieu: NGAU NHIEN va CHUOI (hop "i, i+1" lan luot roi hoi tu dau chuoi) - bo CHUOI
# la test xau nhat cho ban khong nen duong.
# Chay: python do_dsu.py   (~10 giay). Chay tren may phong thi de biet moc that su.
import random, sys, time

def do(ten, ham, lan=3):
    tot = float('inf')
    for _ in range(lan):
        t = time.perf_counter(); kq = ham(); tot = min(tot, time.perf_counter() - t)
    print(f'{ten:62s} {tot:.3f} s   (kq = {kq})')

random.seed(1)
N = Q = 2 * 10**5
NGAU = [(random.randint(0, 1), random.randint(1, N), random.randint(1, N)) for _ in range(Q)]
CHUOI = [(1, i, i + 1) for i in range(1, Q // 2 + 1)] + [(0, 1, random.randint(1, N)) for _ in range(Q // 2)]

def day_du(ds):
    cha = list(range(N + 1)); co = [1] * (N + 1)
    def find(x):
        r = x
        while cha[r] != r:
            r = cha[r]
        while cha[x] != r:
            cha[x], x = r, cha[x]
        return r
    dem = 0
    for t, u, v in ds:
        a = find(u); b = find(v)
        if t:
            if a != b:
                if co[a] < co[b]:
                    a, b = b, a
                cha[b] = a; co[a] += co[b]
        elif a == b:
            dem += 1
    return dem

def chi_nen(ds):
    cha = list(range(N + 1))
    def find(x):
        r = x
        while cha[r] != r:
            r = cha[r]
        while cha[x] != r:
            cha[x], x = r, cha[x]
        return r
    dem = 0
    for t, u, v in ds:
        a = find(u); b = find(v)
        if t:
            if a != b:
                cha[a] = b
        elif a == b:
            dem += 1
    return dem

def chi_kich_thuoc(ds):
    cha = list(range(N + 1)); co = [1] * (N + 1)
    def find(x):
        while cha[x] != x:
            x = cha[x]
        return x
    dem = 0
    for t, u, v in ds:
        a = find(u); b = find(v)
        if t:
            if a != b:
                if co[a] < co[b]:
                    a, b = b, a
                cha[b] = a; co[a] += co[b]
        elif a == b:
            dem += 1
    return dem

def ngay_tho(ds):
    cha = list(range(N + 1))
    def find(x):
        while cha[x] != x:
            x = cha[x]
        return x
    dem = 0
    for t, u, v in ds:
        a = find(u); b = find(v)
        if t:
            if a != b:
                cha[a] = b
        elif a == b:
            dem += 1
    return dem

def nua_duong(ds):
    cha = list(range(N + 1)); co = [1] * (N + 1)
    dem = 0
    for t, u, v in ds:
        a = u
        while cha[a] != a:                 # path halving: moi buoc cho a tro len "ong"
            cha[a] = cha[cha[a]]; a = cha[a]
        b = v
        while cha[b] != b:
            cha[b] = cha[cha[b]]; b = cha[b]
        if t:
            if a != b:
                if co[a] < co[b]:
                    a, b = b, a
                cha[b] = a; co[a] += co[b]
        elif a == b:
            dem += 1
    return dem

def de_quy(ds):
    cha = list(range(N + 1))
    def find(x):
        if cha[x] != x:
            cha[x] = find(cha[x])
        return cha[x]
    dem = 0
    for t, u, v in ds:
        a = find(u); b = find(v)
        if t:
            if a != b:
                cha[a] = b
        elif a == b:
            dem += 1
    return dem

for ten, ds in (('NGAU NHIEN', NGAU), ('CHUOI', CHUOI)):
    print(f'--- {ten}: n = q = 2*10^5')
    do('Day du: nen duong + hop theo kich thuoc (find la ham)', lambda: day_du(ds))
    do('Nen nua duong, viet thang trong vong lap (khong goi ham)', lambda: nua_duong(ds))
    do('Chi nen duong', lambda: chi_nen(ds))
    do('Chi hop theo kich thuoc', lambda: chi_kich_thuoc(ds))
    if ten == 'NGAU NHIEN':
        do('Ngay tho (khong nen, khong kich thuoc)', lambda: ngay_tho(ds))
    else:
        nho = CHUOI[:10**4] + CHUOI[Q // 2:Q // 2 + 10**4]         # chuoi 10^4 + 10^4 cau hoi
        do('Ngay tho, chi chuoi 10^4 + 10^4 cau hoi (that: 10^5)', lambda: ngay_tho(nho), lan=1)
    try:
        do('find DE QUY (chi nen duong), gioi han de quy mac dinh', lambda: de_quy(ds), lan=1)
    except RecursionError:
        print(f'{"find DE QUY (chi nen duong), gioi han de quy mac dinh":62s} RecursionError!')
