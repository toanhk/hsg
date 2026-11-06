# HANHTRINH - vet can: Bellman-Ford co truy vet (n, m nho). O(n*m).
def main():
    data = list(map(int, open('HANHTRINH.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    canh = [(data[2 + 3 * i], data[3 + 3 * i], data[4 + 3 * i]) for i in range(m)]
    canh += [(v, u, w) for u, v, w in canh]
    INF = float('inf')
    dist = [INF] * (n + 1)
    tr = [0] * (n + 1)
    dist[1] = 0
    for _ in range(n - 1):
        for u, v, w in canh:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                tr[v] = u
    with open('HANHTRINH.OUT', 'w') as f:
        if dist[n] == INF:
            f.write('-1\n')
            return
        duong = [n]
        while duong[-1] != 1:
            duong.append(tr[duong[-1]])
        duong.reverse()
        f.write(f'{dist[n]}\n{len(duong)}\n' + ' '.join(map(str, duong)) + '\n')

main()
