# TIMVONG - cach 2: DFS 3 mau KHONG de quy. 0 = trang (chua tham), 1 = xam (dang nam tren ngan
# xep, tuc la tren duong DFS hien tai), 2 = den (da xong). Gap cung u -> v voi v xam: co chu trinh,
# chinh la doan ngan xep tu v den u. Ngan xep luu (dinh, chi so cung ke tiep) de "quay lai dung cho".
def main():
    data = open('TIMVONG.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    adj = [[] for _ in range(n + 1)]
    for i in range(2, 2 + 2 * m, 2):
        adj[int(data[i])].append(int(data[i + 1]))
    mau = [0] * (n + 1)
    ct = None
    for s in range(1, n + 1):
        if mau[s] or ct:
            continue
        st = [s]; chiso = [0]; mau[s] = 1
        while st:
            u = st[-1]; i = chiso[-1]
            if i < len(adj[u]):
                chiso[-1] = i + 1
                v = adj[u][i]
                if mau[v] == 0:
                    mau[v] = 1; st.append(v); chiso.append(0)
                elif mau[v] == 1:              # cung quay ve dinh xam
                    ct = st[st.index(v):]
                    break
            else:
                mau[u] = 2; st.pop(); chiso.pop()
    with open('TIMVONG.OUT', 'w') as f:
        if ct is None:
            f.write('-1\n')
        else:
            f.write(f'{len(ct)}\n' + ' '.join(map(str, ct)) + '\n')

main()
