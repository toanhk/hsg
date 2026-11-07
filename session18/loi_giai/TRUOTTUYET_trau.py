# TRUOTTUYET - vet can (subtask 1, r, c <= 4): tu moi o, DFS ngan xep liet ke moi duong truot.
def main():
    data = list(map(int, open('TRUOTTUYET.INP', 'rb').read().split()))
    r, c = data[0], data[1]
    h = [data[2 + i * c: 2 + (i + 1) * c] for i in range(r)]
    best = 0
    for si in range(r):
        for sj in range(c):
            st = [(si, sj, 1)]
            while st:
                i, j, k = st.pop()
                best = max(best, k)
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < r and 0 <= y < c and h[x][y] < h[i][j]:
                        st.append((x, y, k + 1))
    with open('TRUOTTUYET.OUT', 'w') as fo:
        fo.write(str(best) + '\n')

main()
