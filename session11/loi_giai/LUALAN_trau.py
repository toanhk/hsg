# LUALAN - vet can: MO PHONG tung phut. Moi phut quet ca bang, o cay nao ke o dang chay thi
# chay o phut sau. O(m * n * so phut) -> chi dung cho subtask 1 (m, n <= 30).
def main():
    data = open('LUALAN.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    g = [list(r.decode()) for r in data[2:2 + m]]
    phut = 0
    while True:
        moi = []
        for i in range(m):
            for j in range(n):
                if g[i][j] != 'T':
                    continue
                for u, v in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= u < m and 0 <= v < n and g[u][v] == 'F':
                        moi.append((i, j))
                        break
        if not moi:
            break
        for i, j in moi:                     # doi sau khi quet xong: lua chi lan 1 o moi phut
            g[i][j] = 'F'
        phut += 1
    con = sum(r.count('T') for r in g)
    with open('LUALAN.OUT', 'w') as f:
        f.write(f'{phut} {con}\n')

main()
