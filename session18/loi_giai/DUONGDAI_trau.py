# DUONGDAI - vet can (subtask 1, n <= 10): liet ke MOI duong di tu 1 bang DFS ngan xep (DAG nen khong can
# danh dau da tham - moi duong deu huu han), lay tong lon nhat trong cac duong ket thuc o n.
def main():
    data = list(map(int, open('DUONGDAI.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v, w = data[2 + 3 * i], data[3 + 3 * i], data[4 + 3 * i]
        adj[u].append((v, w))
    best = None
    st = [(1, 0)]
    while st:
        u, s = st.pop()
        if u == n and (best is None or s > best):
            best = s
        for v, w in adj[u]:
            st.append((v, s + w))
    with open('DUONGDAI.OUT', 'w') as fo:
        fo.write(('KHONG' if best is None else str(best)) + '\n')

main()
