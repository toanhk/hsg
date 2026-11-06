# HINHVUONG - vet can: voi moi goc tren-trai, noi rong canh k khi hang moi va cot moi deu toan 1.
# O(m * n * k^2) ~ n^4: chay kip m, n <= 30 (subtask 1), cham voi bang lon nhieu so 1.
def main():
    data = open('HINHVUONG.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    a = [x.decode() for x in data[2:2 + m]]
    best = 0
    for i in range(m):
        for j in range(n):
            k = 0
            while i + k < m and j + k < n:
                # them hang i+k (cot j..j+k) va cot j+k (hang i..i+k)
                if all(a[i + k][c] == '1' for c in range(j, j + k + 1)) and \
                   all(a[r][j + k] == '1' for r in range(i, i + k + 1)):
                    k += 1
                else:
                    break
            best = max(best, k)
    with open('HINHVUONG.OUT', 'w') as out:
        out.write(str(best) + '\n')

main()
