# DAOCHIEU - vet can (subtask 1, n <= 100, m <= 1000): Bellman-Ford tren do thi 0/1.
# Lap lai "duyet moi canh, noi long" cho den khi khong doi; toi da n - 1 vong -> O(n*m).
def main():
    data = open('DAOCHIEU.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    canh = []
    for i in range(m):
        u = int(data[2 + 2 * i]); v = int(data[3 + 2 * i])
        canh.append((u, v, 0)); canh.append((v, u, 1))
    INF = float('inf')
    d = [INF] * (n + 1); d[1] = 0
    for _ in range(n - 1):
        doi = False
        for u, v, w in canh:
            if d[u] + w < d[v]:
                d[v] = d[u] + w; doi = True
        if not doi:
            break
    with open('DAOCHIEU.OUT', 'w') as f:
        f.write(str(d[n] if d[n] < INF else -1) + '\n')

main()
