# PHANCUM - vet can (n <= 10): duyet moi cach chia n diem thanh dung k nhom (day "tang truong han che":
# nhom[i] <= max(nhom[0..i-1]) + 1, Bell(10) = 115975 cach), tinh khoang cach nho nhat giua hai nhom.
def main():
    data = open('PHANCUM.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    P = [(int(data[2 + 2 * i]), int(data[3 + 2 * i])) for i in range(n)]
    d = [[abs(P[i][0] - P[j][0]) + abs(P[i][1] - P[j][1]) for j in range(n)] for i in range(n)]
    best = [-1]
    nhom = [0] * n

    def thu(i, so_nhom):
        if n - i < k - so_nhom:
            return                             # khong du diem de tao du k nhom
        if i == n:
            mn = min(d[a][b] for a in range(n) for b in range(a + 1, n) if nhom[a] != nhom[b])
            best[0] = max(best[0], mn)
            return
        for g in range(min(so_nhom + 1, k)):
            nhom[i] = g
            thu(i + 1, max(so_nhom, g + 1))

    thu(0, 0)
    with open('PHANCUM.OUT', 'w') as f:
        f.write(str(best[0]) + '\n')

main()
