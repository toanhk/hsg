# THUONGPHAT - vet can (subtask 1-2, n <= 100): Floyd chap nhan canh am.
#   d[i][i] < 0 sau Floyd  <=>  i nam tren mot chu trinh am.
#   VOCUC  <=>  ton tai i: d[1][i] < INF, d[i][n] < INF va d[i][i] < 0.
def main():
    data = open('THUONGPHAT.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    INF = float('inf')
    d = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        d[i][i] = 0
    for i in range(m):
        u, v, w = (int(x) for x in data[2 + 3 * i: 5 + 3 * i])
        d[u][v] = min(d[u][v], w)
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if d[i][k] == INF:
                continue
            for j in range(1, n + 1):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    if any(d[1][i] < INF and d[i][n] < INF and d[i][i] < 0 for i in range(1, n + 1)):
        kq = 'VOCUC'
    elif d[1][n] == INF:
        kq = 'KHONG'
    else:
        kq = str(d[1][n])
    with open('THUONGPHAT.OUT', 'w') as f:
        f.write(kq + '\n')

main()
