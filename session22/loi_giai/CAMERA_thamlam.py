# CAMERA - THAM LAM (dung khi moi c[v] = 1, SAI khi c khac nhau): duyet tu la len, nut nao chua duoc
# giam sat thi dat camera o CHA no (cha giam sat duoc nhieu nut nhat). Goc chua duoc giam sat thi dat o goc.
# Dung cho subtask 2; doi_chieu.py voi c ngau nhien tim ra phan vi du ngay (cha dat qua).
def main():
    data = open('CAMERA.INP', 'rb').read().split()
    n = int(data[0])
    c = [0] + list(map(int, data[1:1 + n]))
    adj = [[] for _ in range(n + 1)]
    pos = 1 + n
    for _ in range(n - 1):
        u, v = int(data[pos]), int(data[pos + 1]); pos += 2
        adj[u].append(v); adj[v].append(u)
    par = [0] * (n + 1); par[1] = 0
    order = []; st = [1]; seen = [False] * (n + 1); seen[1] = True
    while st:
        u = st.pop(); order.append(u)
        for v in adj[u]:
            if not seen[v]:
                seen[v] = True; par[v] = u; st.append(v)
    cam = [False] * (n + 1); gs = [False] * (n + 1)
    for v in reversed(order):
        if not gs[v]:
            p = par[v] if par[v] else v
            cam[p] = True
            gs[p] = True
            if par[p]:
                gs[par[p]] = True
            for u in adj[p]:
                gs[u] = True
    ans = sum(c[v] for v in range(1, n + 1) if cam[v])
    with open('CAMERA.OUT', 'w') as f:
        f.write(str(ans) + '\n')

main()
