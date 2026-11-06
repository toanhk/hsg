# VANG - vet can: quay lui moi duong, thu D truoc R nen gap duong theo dung thu tu tu dien;
# chi cap nhat khi tong LON HON HAN -> giu duong tu dien nho nhat. Chi subtask 1 (m, n <= 10).
import sys

def main():
    data = open('VANG.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    a = [list(map(int, data[2 + i * n:2 + (i + 1) * n])) for i in range(m)]
    sys.setrecursionlimit(10000)
    best = [-1, '']
    duong = []

    def thu(i, j, tong):
        if a[i][j] < 0:
            return
        tong += a[i][j]
        if i == m - 1 and j == n - 1:
            if tong > best[0]:
                best[0], best[1] = tong, ''.join(duong)
            return
        if i + 1 < m:
            duong.append('D'); thu(i + 1, j, tong); duong.pop()
        if j + 1 < n:
            duong.append('R'); thu(i, j + 1, tong); duong.pop()

    thu(0, 0, 0)
    out = [str(best[0])] if best[0] < 0 else [str(best[0]), best[1]]
    with open('VANG.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
