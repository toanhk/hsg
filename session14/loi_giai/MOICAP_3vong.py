# MOICAP - Floyd viet thang 3 vong lap voi chi so d[i][j] (cach "giao khoa"): DUNG nhung cham
# hon MOICAP.py khoang 1,5 lan vi moi lan d[i][k], d[k][j], d[i][j] deu phai tra 2 lan chi so.
def main():
    data = open('MOICAP.INP', 'rb').read().split()
    n, m, q = int(data[0]), int(data[1]), int(data[2])
    INF = 10**18
    d = [[INF] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    p = 3
    for _ in range(m):
        u = int(data[p]) - 1; v = int(data[p + 1]) - 1; w = int(data[p + 2]); p += 3
        if w < d[u][v]:
            d[u][v] = d[v][u] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    out = []
    for _ in range(q):
        u = int(data[p]) - 1; v = int(data[p + 1]) - 1; p += 2
        out.append(str(d[u][v]) if d[u][v] < INF else '-1')
    with open('MOICAP.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
