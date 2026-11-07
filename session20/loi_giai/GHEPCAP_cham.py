# GHEPCAP - ban DUNG nhung CHAM: keo ve tren MOI mask, khong biet mask nao toi duoc.
# dp[mask] = max dp[mask bo i bo j] + a[i][j] voi i = bit thap nhat cua mask, j thuoc mask.
# Duyet du 2^n mask, moi mask ~n/2 lan thu -> n = 20 mat ~1 s (qua gio). Dung voi n <= 16 (subtask 2).
def main():
    data = open('GHEPCAP.INP', 'rb').read().split()
    n = int(data[0])
    a = [list(map(int, data[1 + i * n:1 + (i + 1) * n])) for i in range(n)]
    N = 1 << n
    vt = {1 << j: j for j in range(n)}
    dp = [0] * N
    for mask in range(3, N):
        b = mask & -mask
        r = mask ^ b
        if r == 0:
            continue
        row = a[vt[b]]
        best = -1
        m = r
        while m:
            c = m & -m
            m ^= c
            y = dp[r ^ c] + row[vt[c]]
            if y > best:
                best = y
        dp[mask] = best
    with open('GHEPCAP.OUT', 'w') as f:
        f.write(str(dp[N - 1]) + '\n')

main()
