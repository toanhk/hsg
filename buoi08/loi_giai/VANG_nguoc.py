# VANG - ban SAI de chua bai: bang XUOI f[i][j] (tu (1,1) den (i,j)) roi truy vet NGUOC tu dich,
# o moi buoc uu tien "den tu tren" (tuc buoc cuoi la D). Tong dung, nhung duong di khong phai
# luon la tu dien nho nhat: truy vet nguoc chi uu tien D o CUOI duong, con tu dien can D o DAU.
def main():
    data = open('VANG.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    a = [list(map(int, data[2 + i * n:2 + (i + 1) * n])) for i in range(m)]
    AM = -1
    f = [[AM] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if a[i][j] < 0:
                continue
            if i == 0 and j == 0:
                f[i][j] = a[i][j]
                continue
            b = max(f[i - 1][j] if i else AM, f[i][j - 1] if j else AM)
            if b >= 0:
                f[i][j] = b + a[i][j]
    out = []
    if f[m - 1][n - 1] < 0:
        out.append('-1')
    else:
        out.append(str(f[m - 1][n - 1]))
        buoc = []
        i, j = m - 1, n - 1
        while i or j:
            can = f[i][j] - a[i][j]
            if i and f[i - 1][j] == can:
                buoc.append('D'); i -= 1
            else:
                buoc.append('R'); j -= 1
        out.append(''.join(reversed(buoc)))
    with open('VANG.OUT', 'w') as fo:
        fo.write('\n'.join(out) + '\n')

main()
