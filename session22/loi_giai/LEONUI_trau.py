# LEONUI - vet can cho luoi nho: thu tung nguong D trong tap cac chenh lech co the (tang dan), BFS kiem tra.
def main():
    data = open('LEONUI.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    h = [list(map(int, data[2 + i * n:2 + (i + 1) * n])) for i in range(m)]
    ds = {0}
    for i in range(m):
        for j in range(n):
            if i + 1 < m: ds.add(abs(h[i][j] - h[i + 1][j]))
            if j + 1 < n: ds.add(abs(h[i][j] - h[i][j + 1]))
    for D in sorted(ds):
        seen = {(0, 0)}; st = [(0, 0)]
        while st:
            i, j = st.pop()
            for a, b in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= a < m and 0 <= b < n and (a, b) not in seen and abs(h[i][j] - h[a][b]) <= D:
                    seen.add((a, b)); st.append((a, b))
        if (m - 1, n - 1) in seen:
            break
    with open('LEONUI.OUT', 'w') as f:
        f.write(str(D) + '\n')

main()
