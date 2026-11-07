# CHUYENBAY - vet can (subtask 1, n <= 8): liet ke moi duong don 1 -> n, ghi (tong, so canh).
def main():
    data = list(map(int, open('CHUYENBAY.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v, w = data[2 + 3 * i], data[3 + 3 * i], data[4 + 3 * i]
        adj[u].append((v, w))
    duong = []                            # (tong, so chuyen) cua moi duong toi n
    st = [(1, 0, 0, 1 << 1)]
    while st:
        u, s, k, da = st.pop()
        if u == n:
            duong.append((s, k)); continue
        for v, w in adj[u]:
            if not da >> v & 1:
                st.append((v, s + w, k + 1, da | 1 << v))
    C = min(s for s, k in duong)
    ks = [k for s, k in duong if s == C]
    with open('CHUYENBAY.OUT', 'w') as fo:
        fo.write(f'{C} {len(ks) % (10**9 + 7)} {min(ks)} {max(ks)}\n')

main()
