# SUADUONG - vet can: liet ke MOI duong di don tu 1 den n (n <= 8) bang DFS ngan xep, giu cac duong
# co tong nho nhat, hop tat ca canh tren cac duong do. (Trong so >= 1 nen duong ngan nhat luon la duong don.)
def main():
    data = list(map(int, open('SUADUONG.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v, w = data[2 + 3 * i], data[3 + 3 * i], data[4 + 3 * i]
        adj[u].append((v, w, i + 1))
        adj[v].append((u, w, i + 1))
    best, tap = float('inf'), set()
    st = [(1, 0, (1,), ())]              # (dinh, tong, cac dinh da di, cac canh da di)
    while st:
        u, s, dinh, cd = st.pop()
        if u == n:
            if s < best:
                best, tap = s, set(cd)
            elif s == best:
                tap |= set(cd)
            continue
        for v, w, i in adj[u]:
            if v not in dinh:
                st.append((v, s + w, dinh + (v,), cd + (i,)))
    kq = sorted(tap)
    with open('SUADUONG.OUT', 'w') as f:
        f.write(f'{len(kq)}\n' + (' '.join(map(str, kq)) + '\n' if kq else ''))

main()
