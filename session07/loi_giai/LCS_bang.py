# LCS - bang 2 chieu dung nhu cong thuc tren giay: de doc, de truy vet, nhung cham va ton bo nho
# (2001 x 2001 o). Qua subtask 1, 2; subtask 3 sat hoac qua 1 giay tuy may.
# Truy vet: tu (n, m), neu A[i-1] == B[j-1] lay ky tu va di cheo, khong thi di ve o lon hon.
def main():
    data = open('LCS.INP', 'rb').read().split()
    A, B = data[0], data[1]
    n, m = len(A), len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    with open('LCS.OUT', 'w') as out:
        out.write(str(dp[n][m]) + '\n')

main()
