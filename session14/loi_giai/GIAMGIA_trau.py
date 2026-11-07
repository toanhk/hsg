# GIAMGIA - vet can (subtask 1, n <= 100, m <= 500): Bellman-Ford tren do thi trang thai (v, j):
# lap "duyet moi chuyen bay, moi j, noi long ca 2 kieu" den khi khong doi. O((k+1) * n * m).
def main():
    data = open('GIAMGIA.INP', 'rb').read().split()
    n, m, k = int(data[0]), int(data[1]), int(data[2])
    canh = [tuple(int(x) for x in data[3 + 3 * i: 6 + 3 * i]) for i in range(m)]
    INF = float('inf')
    d = [[INF] * (k + 1) for _ in range(n + 1)]      # d[v][j]
    d[1][0] = 0
    doi = True
    while doi:
        doi = False
        for u, v, w in canh:
            for j in range(k + 1):
                if d[u][j] + w < d[v][j]:
                    d[v][j] = d[u][j] + w; doi = True
                if j < k and d[u][j] + w // 2 < d[v][j + 1]:
                    d[v][j + 1] = d[u][j] + w // 2; doi = True
    kq = min(d[n])
    with open('GIAMGIA.OUT', 'w') as f:
        f.write(str(kq if kq < INF else -1) + '\n')

main()
