# DUONGRE - vet can (subtask 1, n <= 8): liet ke moi duong DON tu 1 den n (w >= 1 nen duong ngan nhat luon
# la duong don), giu tong nho nhat va so duong dat tong do.
def main():
    data = list(map(int, open('DUONGRE.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v, w = data[2 + 3 * i], data[3 + 3 * i], data[4 + 3 * i]
        adj[u].append((v, w))
    best, dem = None, 0
    st = [(1, 0, 1 << 1)]                 # (dinh, tong, tap dinh da di dang bit)
    while st:
        u, s, da = st.pop()
        if u == n:
            if best is None or s < best:
                best, dem = s, 1
            elif s == best:
                dem += 1
            continue
        for v, w in adj[u]:
            if not da >> v & 1:
                st.append((v, s + w, da | 1 << v))
    with open('DUONGRE.OUT', 'w') as fo:
        fo.write('-1 0\n' if best is None else f'{best} {dem % (10**9 + 7)}\n')

main()
