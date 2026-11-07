# KHOANGCACH - vet can bang Bellman-Ford: lap noi long MOI canh n - 1 vong. O(n*m), chi cho n, m nho.
def main():
    data = list(map(int, open('KHOANGCACH.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    canh = [(data[2 + 3 * i], data[3 + 3 * i], data[4 + 3 * i]) for i in range(m)]
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[1] = 0
    for _ in range(n - 1):
        for u, v, w in canh:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
            if dist[v] + w < dist[u]:
                dist[u] = dist[v] + w
    with open('KHOANGCACH.OUT', 'w') as f:
        f.write(' '.join(str(x) if x < INF else '-1' for x in dist[1:]) + '\n')

main()
