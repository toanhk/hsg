# DO DAY CON: chi phi LIS O(n^2) va O(n log n), cac cach cai dat bang LCS / sua xau trong Python
# Chay: python do_daycon.py   (~10 giay). Chay tren may phong thi de biet moc that su.
import random, time
from bisect import bisect_left

random.seed(7)

def do(ten, ham, lan=3):
    tot = float('inf')
    for _ in range(lan):
        t = time.perf_counter(); ham(); tot = min(tot, time.perf_counter() - t)
    print(f'{ten:58s} {tot:.3f} s')

# ---------- LIS ----------
def lis_n2(a):
    n = len(a); f = [1] * n
    for i in range(n):
        ai = a[i]; tot = 0
        for j in range(i):
            if a[j] < ai and f[j] > tot:
                tot = f[j]
        f[i] = tot + 1
    return max(f)

def lis_bisect(a):
    d = []
    for x in a:
        k = bisect_left(d, x)
        if k == len(d): d.append(x)
        else: d[k] = x
    return len(d)

for n in (1000, 3000, 5000):
    a = [random.randint(1, 10**9) for _ in range(n)]
    do(f'LIS O(n^2), n = {n}', lambda: lis_n2(a), lan=1)
for n in (10**5, 5 * 10**5, 10**6):
    a = [random.randint(1, 10**9) for _ in range(n)]
    do(f'LIS bisect, n = {n}', lambda: lis_bisect(a))

# ---------- LCS: 4 cach cai dat cho cung cong thuc ----------
def lcs_bang(A, B):                       # bang 2 chieu dp[i][j], dung nguyen cong thuc
    n, m = len(A), len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]

def lcs_2hang_max(A, B):                  # 2 hang, nhung van goi max() va chi so B[j-1]
    m = len(B); truoc = [0] * (m + 1)
    for x in A:
        hang = [0] * (m + 1)
        for j in range(1, m + 1):
            if x == B[j - 1]:
                hang[j] = truoc[j - 1] + 1
            else:
                hang[j] = max(truoc[j], hang[j - 1])
        truoc = hang
    return truoc[m]

def lcs_2hang_if(A, B):                   # 2 hang + enumerate + bien c + if thay max (LCS.py)
    m = len(B); truoc = [0] * (m + 1)
    for x in A:
        hang = [0]; c = 0
        for j, y in enumerate(B):
            if x == y:
                c = truoc[j] + 1
            else:
                t = truoc[j + 1]
                if t > c: c = t
            hang.append(c)
        truoc = hang
    return truoc[m]

def lcs_bit(A, B):                        # bit song song tren so nguyen lon (LCS_bit.py)
    M = {}
    for j, y in enumerate(B):
        M[y] = M.get(y, 0) | (1 << j)
    row = 0
    for x in A:
        X = M.get(x, 0) | row
        row = X & ((X - ((row << 1) | 1)) ^ X)
    return bin(row).count('1')

A = bytes(random.choice(b'abcd') for _ in range(2000))
B = bytes(random.choice(b'abcd') for _ in range(2000))
kq = {f(A, B) for f in (lcs_bang, lcs_2hang_max, lcs_2hang_if, lcs_bit)}
assert len(kq) == 1, 'cac cach LCS lech nhau!'
do('LCS 2000x2000: bang 2 chieu dp[i][j]', lambda: lcs_bang(A, B), lan=1)
do('LCS 2000x2000: 2 hang, max(), B[j-1]', lambda: lcs_2hang_max(A, B), lan=1)
do('LCS 2000x2000: 2 hang, enumerate, if (LCS.py)', lambda: lcs_2hang_if(A, B))
do('LCS 2000x2000: bit song song (LCS_bit.py)', lambda: lcs_bit(A, B))
A3 = bytes(random.choice(b'abcd') for _ in range(3000))
B3 = bytes(random.choice(b'abcd') for _ in range(3000))
do('LCS 3000x3000: 2 hang, enumerate, if', lambda: lcs_2hang_if(A3, B3), lan=1)
A5 = bytes(random.choice(b'abcd') for _ in range(50000))
B5 = bytes(random.choice(b'abcd') for _ in range(50000))
do('LCS 50000x50000: bit song song', lambda: lcs_bit(A5, B5), lan=1)

# ---------- Sua xau ----------
def sua(A, B):
    m = len(B); truoc = list(range(m + 1))
    for i, x in enumerate(A, 1):
        hang = [i]; c = i
        for j, y in enumerate(B):
            if x == y:
                c = truoc[j]
            else:
                t = truoc[j]; u = truoc[j + 1]
                if u < t: t = u
                if c < t: t = c
                c = t + 1
            hang.append(c)
        truoc = hang
    return truoc[m]

for n in (1500, 2000):
    A = bytes(random.choice(b'abcd') for _ in range(n))
    B = bytes(random.choice(b'abcd') for _ in range(n))
    do(f'Sua xau {n}x{n}: 2 hang (SUAXAU.py)', lambda: sua(A, B), lan=1)
