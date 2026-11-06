# DEMDUONG - vet can: quay lui dem moi duong khong qua o cam. Chi cho subtask 1 (m, n <= 10).
import sys

def main():
    data = open('DEMDUONG.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    luoi = [x.decode() for x in data[2:2 + m]]
    sys.setrecursionlimit(10000)
    dem = 0

    def thu(i, j):
        nonlocal dem
        if luoi[i][j] == '#':
            return
        if i == m - 1 and j == n - 1:
            dem += 1
            return
        if i + 1 < m: thu(i + 1, j)
        if j + 1 < n: thu(i, j + 1)

    thu(0, 0)
    with open('DEMDUONG.OUT', 'w') as out:
        out.write(str(dem % (10**9 + 7)) + '\n')

main()
