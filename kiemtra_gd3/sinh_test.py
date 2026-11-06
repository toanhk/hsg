# SINH TEST cho de kiem tra cuoi giai doan 3 (Do thi co ban): HAIPHE, CUUHOA, DEMNGAN
# Cau truc thu muc theo Themis: test/HAIPHE/Test01/HAIPHE.INP + HAIPHE.OUT
# Dap an tinh bang ham "dap_an_..." viet theo cach KHAC loi giai mau de kiem cheo:
#   HAIPHE bang DSU co chan le, CUUHOA BFS nhieu nguon voi toa do (i, j) + deque + mang khoang cach
#   2 chieu (cach "ngay tho", cham nhung dung), DEMNGAN BFS lay d[] roi duyet dinh theo d tang dan va
#   "keo" cnt tu cac cung VAO (loi giai mau "day" cnt theo cung RA ngay trong luc BFS).
# Moi bai 10 test: Test01-04 subtask 1 (40%), Test05-07 subtask 2 (30%), Test08-10 subtask 3 (30%)
# Chay: python sinh_test.py              -> sinh ca 3 bai (~25 giay)
#       python sinh_test.py CUUHOA       -> chi sinh bai ke ten
# Moi bai co seed rieng (random.seed('HAIPHE-2026'), ...) nen sinh rieng mot bai hay ca bo deu ra CUNG test.
import os, random, sys
from collections import deque

GOC = 'test'
MOD = 10**9 + 7

def ghi(bai, so, inp, out):
    d = os.path.join(GOC, bai, f'Test{so:02d}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, bai + '.INP'), 'w') as f:
        f.write(inp)
    with open(os.path.join(d, bai + '.OUT'), 'w') as f:
        f.write(out)

def de_canh(n, canh):
    return f'{n} {len(canh)}\n' + ''.join(f'{u} {v}\n' for u, v in canh)

# ---------------- HAIPHE ----------------
def dap_an_haiphe(n, canh):
    cha = list(range(n + 1)); le = [0] * (n + 1); co = [1] * (n + 1)
    def find(x):                               # tra ve (goc, chan le cua x so voi goc); hop theo kich thuoc
        p = 0                                  # nen do sau O(log n) nen khong can nen duong
        while cha[x] != x:
            p ^= le[x]; x = cha[x]
        return x, p
    c = n
    for u, v in canh:
        (ru, pu), (rv, pv) = find(u), find(v)
        if ru == rv:
            if pu == pv:
                return '0\n'
        else:
            if co[ru] > co[rv]: ru, rv, pu, pv = rv, ru, pv, pu
            cha[ru] = rv; le[ru] = pu ^ pv ^ 1; co[rv] += co[ru]; c -= 1
    return str(pow(2, c, MOD)) + '\n'

def hai_phia(n, m):
    """Do thi hai phia ngau nhien: to mau bi mat, canh chi noi hai mau khac nhau."""
    mau = [random.randint(0, 1) for _ in range(n + 1)]
    A = [v for v in range(1, n + 1) if mau[v] == 0]; B = [v for v in range(1, n + 1) if mau[v] == 1]
    canh = []
    while len(canh) < m and A and B:
        canh.append((random.choice(A), random.choice(B)) if random.random() < 0.5 else (random.choice(B), random.choice(A)))
    return canh, mau

def sinh_haiphe():
    for so in range(1, 11):
        if so == 1:
            n, canh = 5, [(1, 2), (2, 3), (4, 5)]                     # vi du: {1,3}|{2} va {4}|{5} -> 4
        elif so == 2:
            n, canh = 4, [(1, 2), (2, 3), (3, 1)]                     # tam giac -> 0
        elif so == 3:
            n, canh = 15, []                                          # 2^15
        elif so == 4:
            n = 15; canh, _ = hai_phia(n, 10)
        elif so == 5:
            n = 2000; canh, _ = hai_phia(n, 1500)
        elif so == 6:                                                 # chu trinh le 1999 dinh -> 0
            n = 2000; canh = [(i, i + 1) for i in range(1, 1999)] + [(1999, 1)]; random.shuffle(canh)
        elif so == 7:
            n, canh = 2000, []                                        # 2^2000 mod p: quen mod la sai
        elif so == 8:
            n = 10**5; canh, _ = hai_phia(n, 2 * 10**5)
        elif so == 9:                                                 # chu trinh chan 2*10^5 + day cung
            n = 10**5; hv = list(range(1, n + 1)); random.shuffle(hv)
            canh = [(hv[i], hv[(i + 1) % n]) for i in range(n)]
            canh += [(hv[i], hv[(i + 2 * random.randint(1, 50) + 1) % n]) for i in random.sample(range(n), 5 * 10**4 - 1)]
            canh = canh[:2 * 10**5]; random.shuffle(canh)
        else:                                                         # hai phia lon + 1 canh pha o cuoi
            n = 10**5; canh, mau = hai_phia(n, 2 * 10**5 - 1)
            A = [v for v in range(1, n + 1) if mau[v] == 0]
            canh.append(tuple(random.sample(A, 2)))
        ghi('HAIPHE', so, de_canh(n, canh), dap_an_haiphe(n, canh))

# ---------------- CUUHOA ----------------
def dap_an_cuuhoa(g):
    m, n = len(g), len(g[0])
    d = [[-1] * n for _ in range(m)]
    q = deque()
    for i in range(m):
        for j in range(n):
            if g[i][j] == 'T':
                d[i][j] = 0; q.append((i, j))
    while q:
        i, j = q.popleft()
        for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= x < m and 0 <= y < n and g[x][y] != '#' and d[x][y] < 0:
                d[x][y] = d[i][j] + 1; q.append((x, y))
    khong = tong = 0
    for i in range(m):
        for j in range(n):
            if g[i][j] == 'H':
                if d[i][j] < 0: khong += 1
                else: tong += d[i][j]
    return f'{khong} {tong}\n'

def ngau_nhien(m, n, p_tuong, p_nha, so_tram):
    g = [[('#' if random.random() < p_tuong else ('H' if random.random() < p_nha else '.'))
          for _ in range(n)] for _ in range(m)]
    for _ in range(so_tram):
        g[random.randrange(m)][random.randrange(n)] = 'T'
    return g

def ran(m, n, p_nha):
    """Me cung ran: hang le la tuong, chua khe xen ke dau/cuoi -> duong di dai ~ m*n/2."""
    g = [['H' if random.random() < p_nha else '.' for _ in range(n)] for _ in range(m)]
    for i in range(1, m, 2):
        g[i] = ['#'] * n
        g[i][n - 1 if i % 4 == 1 else 0] = '.'
    return g

def sinh_cuuhoa():
    for so in range(1, 11):
        if so == 1:
            g = [list('T..#H'), list('.#.#.'), list('H...H'), list('##.#T')]   # vi du
        elif so == 2:
            g = ngau_nhien(20, 30, 0.2, 0.3, 0)                       # khong co tram nao
        elif so == 3:                                                 # nha bi tuong vay kin
            g = ngau_nhien(30, 30, 0.1, 0.1, 3)
            for x, y in ((5, 5), (5, 7), (4, 6), (6, 6)):
                g[x][y] = '#'
            g[5][6] = 'H'
        elif so == 4:
            g = ngau_nhien(30, 30, 0.3, 0.2, 4)
        elif so == 5:
            g = ngau_nhien(1000, 1000, 0.2, 0.1, 1)
        elif so == 6:
            g = ran(1000, 1000, 0.05); g[0][0] = 'T'                  # 1 tram, duong dai 5*10^5
        elif so == 7:
            g = ngau_nhien(1000, 1, 0.0, 0.5, 0); g[0][0] = 'T'       # bang 1 cot
        elif so == 8:
            g = ngau_nhien(1000, 1000, 0.25, 0.2, 1000)
        elif so == 9:
            g = ran(1000, 1000, 0.1)
            for _ in range(50):
                i = 2 * random.randrange(500); g[i][random.randrange(1000)] = 'T'
        else:                                                         # khong tuong, 10^5 tram, nhieu nha
            g = ngau_nhien(1000, 1000, 0.0, 0.5, 10**5)
        g = [''.join(r) for r in g]
        inp = f'{len(g)} {len(g[0])}\n' + '\n'.join(g) + '\n'
        ghi('CUUHOA', so, inp, dap_an_cuuhoa(g))

# ---------------- DEMNGAN ----------------
def dap_an_demngan(n, canh):
    adj = [[] for _ in range(n + 1)]; vao = [[] for _ in range(n + 1)]
    for u, v in canh:
        adj[u].append(v); vao[v].append(u)
    d = [-1] * (n + 1); d[1] = 0; q = deque([1])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if d[v] < 0:
                d[v] = d[u] + 1; q.append(v)
    if d[n] < 0:
        return '-1\n'
    thu_tu = sorted((v for v in range(1, n + 1) if d[v] >= 0), key=d.__getitem__)
    cnt = [0] * (n + 1); cnt[1] = 1
    for v in thu_tu:
        if v != 1:
            cnt[v] = sum(cnt[u] for u in vao[v] if d[u] == d[v] - 1) % MOD
    return f'{d[n]} {cnt[n]}\n'

def phan_lop(n, rong, m, ngau=0):
    """Dinh 1, cac lop do rong 'rong', dinh n; cung giua hai lop ke nhau (+ 'ngau' cung ngau nhien)."""
    giua = list(range(2, n)); random.shuffle(giua)
    lop = [[1]] + [giua[i:i + rong] for i in range(0, len(giua), rong)] + [[n]]
    canh = []
    for a, b in zip(lop, lop[1:]):
        for v in b:
            canh.append((random.choice(a), v))                        # moi dinh deu toi duoc
    while len(canh) < m - ngau:
        k = random.randrange(len(lop) - 1)
        canh.append((random.choice(lop[k]), random.choice(lop[k + 1])))
    while len(canh) < m:
        canh.append((random.randint(1, n), random.randint(1, n)))
    random.shuffle(canh)
    return canh

def sinh_demngan():
    for so in range(1, 11):
        if so == 1:
            n, canh = 6, [(1, 2), (1, 3), (2, 4), (3, 4), (4, 6), (2, 5), (5, 6)]   # vi du: 3 3
        elif so == 2:
            n, canh = 5, [(1, 2), (2, 3), (4, 5), (5, 1)]                   # khong toi n -> -1
        elif so == 3:
            n, canh = 1, []                                                # n = 1: 0 1
        elif so == 4:
            n = 10; canh = [(random.randint(1, n), random.randint(1, n)) for _ in range(25)]
        elif so == 5:
            n = 2000; canh = [(random.randint(1, n), random.randint(1, n)) for _ in range(3000)]
            canh += [(i, i + 1) for i in range(1, n)]; random.shuffle(canh)      # xich bao dam toi duoc n
        elif so == 6:
            n = 2000; canh = phan_lop(n, 20, 5000)                         # so duong lon -> phai mod
        elif so == 7:                                                      # cung lap: dem nhieu lan
            n = 1000; canh = phan_lop(n, 3, 800); canh += canh; random.shuffle(canh)
        elif so == 8:                                                      # lop rong 2, d ~ 10^5
            n = 10**5; canh = phan_lop(n, 2, 2 * 10**5)
        elif so == 9:
            n = 10**5; canh = [(random.randint(1, n), random.randint(1, n)) for _ in range(10**5 + 1)]
            canh += [(i, i + 1) for i in range(1, n)]; random.shuffle(canh)
        else:
            n = 10**5; canh = phan_lop(n, 300, 2 * 10**5, ngau=30000)
        ghi('DEMNGAN', so, de_canh(n, canh), dap_an_demngan(n, canh))

SINH = {'HAIPHE': sinh_haiphe, 'CUUHOA': sinh_cuuhoa, 'DEMNGAN': sinh_demngan}

def main():
    ds = sys.argv[1:] or list(SINH)
    for bai in ds:
        random.seed(bai + '-2026')
        SINH[bai]()
        print('Da sinh', bai)

main()
