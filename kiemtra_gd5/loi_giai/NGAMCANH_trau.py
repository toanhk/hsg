# NGAMCANH - vet can (n <= 10): liet ke moi duong DON 1 -> n bang ngan xep, chon (thoi gian nho nhat, diem lon nhat).
def main():
    data = open('NGAMCANH.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    b = [0] + list(map(int, data[2:2 + n]))
    p = 2 + n
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v, w = int(data[p + 3 * i]), int(data[p + 3 * i + 1]), int(data[p + 3 * i + 2])
        adj[u].append((v, w)); adj[v].append((u, w))
    best = None                                 # (thoi gian, -diem)
    st = [(1, 1 << 1, 0, b[1])]                 # (dinh, tap da qua, thoi gian, diem)
    while st:
        u, da, t, s = st.pop()
        if u == n:
            if best is None or (t, -s) < best:
                best = (t, -s)
            continue
        for v, w in adj[u]:
            if not da >> v & 1:
                st.append((v, da | 1 << v, t + w, s + b[v]))
    with open('NGAMCANH.OUT', 'w') as f:
        f.write('-1\n' if best is None else f'{best[0]} {-best[1]}\n')

main()
