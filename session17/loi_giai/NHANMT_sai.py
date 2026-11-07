# NHANMT - SAI THU TU TINH: duyet l TANG dan (giong mang 1 chieu quen tay).
# Khi tinh f[l][r] can f[k+1][r] voi k+1 > l -> hang do CHUA tinh (van bang 0) -> dap an qua nho.
# Sua: l giam dan, hoac duyet theo do dai doan d = r - l tang dan (xem GOPSOI.py).
# Vi du trong de (10 30 5 60) VAN RA DUNG 4500 do may man -> qua vi du chua chac dung!
# Test bat loi: n = 3, p = 3 2 6 8: dung 144, ban sai in 48.
def main():
    data = open('NHANMT.INP', 'rb').read().split()
    n = int(data[0])
    p = list(map(int, data[1:n + 2]))
    f = [[0] * n for _ in range(n)]
    for l in range(n):                          # <-- SAI: phai la range(n - 2, -1, -1)
        for r in range(l + 1, n):
            f[l][r] = min(f[l][k] + f[k + 1][r] + p[l] * p[k + 1] * p[r + 1] for k in range(l, r))
    with open('NHANMT.OUT', 'w') as out:
        out.write(str(f[0][n - 1]) + '\n')

main()
