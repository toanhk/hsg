# DO TOC DO QHD TREN DOAN (buoi 17)
#   1) Gop soi: O(n^3/6) - vong lap thuan vs min(map(add, ...)) tren 2 bang (theo hang va theo cot)
#   2) Tro choi lay so: O(n^2/2) o - bang 2 chieu vs giu 1 hang
#   3) Bang "doan con doi xung" n^2/2 o (dung cho CATDX)
# Chay: python do_doan.py   (~20 giay). Chay tren may phong thi de biet moc that su.
import random, time
from operator import add

def do(ten, ham, lan=2):
    tot = float('inf')
    for _ in range(lan):
        t = time.perf_counter(); kq = ham(); tot = min(tot, time.perf_counter() - t)
    print(f'{ten:58s} {tot:.3f} s   (kq = {kq})')

def cong_10_7():
    s = 0
    for i in range(10**7):
        s += i
    return s

def gop_thuan(a):
    n = len(a)
    P = [0]
    for x in a:
        P.append(P[-1] + x)
    INF = float('inf')
    f = [[0] * n for _ in range(n)]
    for d in range(1, n):
        for l in range(n - d):
            r = l + d
            best = INF
            fl = f[l]
            for k in range(l, r):
                t = fl[k] + f[k + 1][r]
                if t < best:
                    best = t
            f[l][r] = best + P[r + 1] - P[l]
    return f[0][n - 1]

def gop_map(a):
    # f[l][k] theo hang, g[r][k] = f[k][r] theo cot -> min(map(add, f[l][l:r], g[r][l+1:r+1]))
    n = len(a)
    P = [0]
    for x in a:
        P.append(P[-1] + x)
    f = [[0] * n for _ in range(n)]
    g = [[0] * n for _ in range(n)]
    for d in range(1, n):
        for l in range(n - d):
            r = l + d
            v = min(map(add, f[l][l:r], g[r][l + 1:r + 1])) + P[r + 1] - P[l]
            f[l][r] = v
            g[r][l] = v
    return f[0][n - 1]

def layso_bang(a):
    n = len(a)
    f = [[0] * n for _ in range(n)]
    for i in range(n):
        f[i][i] = a[i]
    for l in range(n - 2, -1, -1):
        fl = f[l]; fs = f[l + 1]; x = a[l]
        for r in range(l + 1, n):
            u = x - fs[r]; v = a[r] - fl[r - 1]
            fl[r] = u if u > v else v
    return f[0][n - 1]

def layso_hang(a):
    n = len(a)
    sau = [0] * n
    for l in range(n - 1, -1, -1):
        x = a[l]
        hang = [0] * n
        c = x; hang[l] = x                 # c = f[l][r-1]
        for r in range(l + 1, n):
            u = x - sau[r]; v = a[r] - c
            c = u if u > v else v
            hang[r] = c
        sau = hang
    return sau[n - 1]

def bang_dx(s):
    n = len(s)
    dx = [[False] * n for _ in range(n)]
    for l in range(n - 1, -1, -1):
        dl = dx[l]; ds = dx[l + 1] if l + 1 < n else None; x = s[l]
        dl[l] = True
        for r in range(l + 1, n):
            if s[r] == x and (r - l < 2 or ds[r - 1]):
                dl[r] = True
    return sum(map(sum, dx))

def main():
    random.seed(17)
    do('10^7 phep cong (moc may)', cong_10_7, 1)
    for n in (100, 200, 300):
        a = [random.randint(1, 10**9) for _ in range(n)]
        do(f'gop soi vong lap thuan n={n}', lambda: gop_thuan(a), 1)
    for n in (200, 300, 400, 500):
        a = [random.randint(1, 10**9) for _ in range(n)]
        do(f'gop soi min(map(add)) n={n}', lambda: gop_map(a), 1)
    for n in (2000, 3000):
        a = [random.randint(1, 10**9) for _ in range(n)]
        do(f'lay so bang 2 chieu n={n}', lambda: layso_bang(a))
        do(f'lay so giu 1 hang n={n}', lambda: layso_hang(a))
    for n in (2000, 3000):
        s = ''.join(random.choice('ab') for _ in range(n))
        do(f'bang doan doi xung n={n}', lambda: bang_dx(s))

main()
