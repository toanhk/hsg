# DAONOI - vet can: sau moi lan, loang (DFS ngan xep) lai toan bo luoi de dem dao. O(k * R * C).

def main():
    data = open('DAONOI.INP', 'rb').read().split()
    R, C, k = int(data[0]), int(data[1]), int(data[2])
    g = [[0] * (C + 2) for _ in range(R + 2)]
    out = []
    for t in range(3, 3 + 2 * k, 2):
        g[int(data[t])][int(data[t + 1])] = 1
        tham = [[False] * (C + 2) for _ in range(R + 2)]
        dao = 0
        for i in range(1, R + 1):
            for j in range(1, C + 1):
                if g[i][j] and not tham[i][j]:
                    dao += 1
                    tham[i][j] = True
                    st = [(i, j)]
                    while st:
                        x, y = st.pop()
                        for u, v in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                            if g[u][v] and not tham[u][v]:
                                tham[u][v] = True; st.append((u, v))
        out.append(str(dao))
    with open('DAONOI.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
