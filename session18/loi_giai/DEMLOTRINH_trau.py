# DEMLOTRINH - vet can (subtask 1, n <= 10): DFS ngan xep liet ke moi duong tu 1, dem duong toi n.
def main():
    data = list(map(int, open('DEMLOTRINH.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        adj[data[2 + 2 * i]].append(data[3 + 2 * i])
    dem = 0
    st = [1]
    while st:
        u = st.pop()
        if u == n:
            dem += 1
        st.extend(adj[u])
    with open('DEMLOTRINH.OUT', 'w') as fo:
        fo.write(str(dem % (10**9 + 7)) + '\n')

main()
