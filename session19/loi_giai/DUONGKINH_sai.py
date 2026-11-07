# DUONGKINH - ban SAI de chua: chi lay "duong di xuong dai nhat tu goc 1" (xa[1]),
# tuc la ngam cho rang duong kinh luon xuat phat tu goc. Sai khi duong kinh nam han trong mot cay con,
# hoac di qua goc theo HAI nhanh. Vi du: 1-2 (1), 2-3 (5), 2-4 (5): dap an 10, ban nay ra 6.
def main():
    data = open('DUONGKINH.INP', 'rb').read().split()
    n = int(data[0])
    adj = [[] for _ in range(n + 1)]
    for i in range(1, 3 * n - 2, 3):
        u, v, w = int(data[i]), int(data[i + 1]), int(data[i + 2])
        adj[u].append((v, w)); adj[v].append((u, w))
    d = [-1] * (n + 1); d[1] = 0
    q = [1]
    for u in q:
        for v, w in adj[u]:
            if d[v] < 0:
                d[v] = d[u] + w; q.append(v)
    with open('DUONGKINH.OUT', 'w') as f:
        f.write(str(max(d)) + '\n')

main()
