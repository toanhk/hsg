# KHOANGCACH - Dijkstra O(n^2) KHONG heap (subtask 1-2, n <= 2000): moi buoc quet tim dinh chua chot
# co dist nho nhat, chot no, roi noi long cac canh ra. Ma tran ke giu canh nho nhat giua moi cap.
# n = 10^5 -> n^2 = 10^10: qua gio va ma tran khong vua bo nho.
def main():
    data = list(map(int, open('KHOANGCACH.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    INF = float('inf')
    a = [[INF] * (n + 1) for _ in range(n + 1)]
    it = iter(data[2:2 + 3 * m])
    for u, v, w in zip(it, it, it):
        if w < a[u][v]:
            a[u][v] = a[v][u] = w
    dist = [INF] * (n + 1)
    dist[1] = 0
    xong = [False] * (n + 1)
    for _ in range(n):
        u, best = -1, INF
        for x in range(1, n + 1):
            if not xong[x] and dist[x] < best:
                u, best = x, dist[x]
        if u == -1:                      # cac dinh con lai khong toi duoc
            break
        xong[u] = True
        hang = a[u]
        for v in range(1, n + 1):
            if best + hang[v] < dist[v]:
                dist[v] = best + hang[v]
    with open('KHOANGCACH.OUT', 'w') as f:
        f.write(' '.join(str(x) if x < INF else '-1' for x in dist[1:]) + '\n')

main()
