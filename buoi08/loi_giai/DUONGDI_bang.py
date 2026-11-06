# DUONGDI - ban bang 2 chieu day du, viet dp[i][j] va max() (cach hoc sinh hay viet dau tien).
# Dung, de truy vet; cham hon ban 1 hang ~3 lan (0.13 s / 10^6 o tren may cloud) nhung van kip.
def main():
    data = open('DUONGDI.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    a = [list(map(int, data[2 + i * n:2 + (i + 1) * n])) for i in range(m)]
    NEG = -10**18
    dp = [[NEG] * n for _ in range(m)]
    dp[0][0] = a[0][0]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            tren = dp[i - 1][j] if i > 0 else NEG      # chu y: dp[-1][j] KHONG bao loi -> phai if
            trai = dp[i][j - 1] if j > 0 else NEG
            dp[i][j] = max(tren, trai) + a[i][j]
    with open('DUONGDI.OUT', 'w') as out:
        out.write(str(dp[m - 1][n - 1]) + '\n')

main()
