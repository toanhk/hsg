# PHANCONG - ban QHD co chieu THUA: luu them chi so nguoi i, dp[i][mask]. DUNG va van chay kip (~0,46 s, vi bo qua
# mask khong toi duoc) nhung ton (n+1) * 2^n o: n = 18 -> 5*10^6 o, ~57 MB (ban chinh ~23 MB), cham gan gap doi.
# Bai hoc: so nguoi da giao viec = so bit 1 cua mask, nen chieu i la THUA. Bo chieu thua -> nhe hon va nhanh hon.
# (Neu quen dong "if x == INF: continue" thi phai duyet du n * 2^n * n = 8,5*10^7 buoc -> qua gio.)
def main():
    data = open('PHANCONG.INP', 'rb').read().split()
    n = int(data[0])
    c = [list(map(int, data[1 + i * n:1 + (i + 1) * n])) for i in range(n)]
    N = 1 << n
    INF = 10**18
    dp = [[INF] * N for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        cur, nxt, row = dp[i], dp[i + 1], c[i]
        for mask in range(N):
            x = cur[mask]
            if x == INF:
                continue
            for j in range(n):
                if not mask >> j & 1:
                    nm = mask | 1 << j
                    if x + row[j] < nxt[nm]:
                        nxt[nm] = x + row[j]
    with open('PHANCONG.OUT', 'w') as f:
        f.write(str(dp[n][N - 1]) + '\n')

main()
