# GIOHANG - bang 2 chieu dp[k][b] theo tung nhom (dung nhung cham + ton bo nho): truy cap dp[k][b] long nhau
# cham hon nhieu so voi mot mang. Kip subtask nho; test lon ~1,5 s.
def main():
    data = open('GIOHANG.INP', 'rb').read().split()
    n, B = int(data[0]), int(data[1])
    nhom = {}
    pos = 2
    for _ in range(n):
        g, w, v = int(data[pos]), int(data[pos + 1]), int(data[pos + 2]); pos += 3
        nhom.setdefault(g, []).append((w, v))
    ds_nhom = list(nhom.values())
    G = len(ds_nhom)
    dp = [[0] * (B + 1) for _ in range(G + 1)]
    for k in range(1, G + 1):
        for b in range(B + 1):
            dp[k][b] = dp[k - 1][b]
            for w, v in ds_nhom[k - 1]:
                if w <= b and dp[k - 1][b - w] + v > dp[k][b]:
                    dp[k][b] = dp[k - 1][b - w] + v
    with open('GIOHANG.OUT', 'w') as fo:
        fo.write(str(dp[G][B]) + '\n')

main()
