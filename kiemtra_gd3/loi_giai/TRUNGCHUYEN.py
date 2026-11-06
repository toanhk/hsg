# TRUNGCHUYEN: n nut, m duong HAI CHIEU (moi duong 1 phut). Xet cac duong di NGAN NHAT tu nut 1 den nut n.
# In 3 so: D = do dai duong ngan nhat; A = so nut nam tren IT NHAT MOT duong ngan nhat; B = so nut nam tren
# MOI duong ngan nhat (A, B tinh ca nut 1 va nut n). Khong di duoc thi in -1.  n <= 10^5, m <= 1.5*10^5
# Hai lan BFS: d1[] tu nut 1, dn[] tu nut n. D = d1[n].
#   - v nam tren mot duong ngan nhat  <=>  d1[v] + dn[v] == D  (ghep duong 1->v va v->n ngan nhat).
#   - Moi duong ngan nhat di qua DUNG MOT nut o moi "tang" d1 = 0, 1, ..., D. Nut v (tren duong ngan nhat)
#     nam tren MOI duong  <=>  tang d1[v] chi co DUY NHAT mot nut tren duong ngan nhat.
#     (Neu tang k co 2 nut x, y thi co duong qua x va duong qua y, nen x khong nam tren moi duong.)
# O(n + m). BFS kieu "for u in q" (list vua la hang doi vua la thu tu tham).
def bfs(adj, n, s):
    d = [-1] * (n + 1)
    d[s] = 0
    q = [s]
    for u in q:
        du = d[u] + 1
        for v in adj[u]:
            if d[v] < 0:
                d[v] = du
                q.append(v)
    return d

def main():
    data = open('TRUNGCHUYEN.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    adj = [[] for _ in range(n + 1)]
    for i in range(2, 2 + 2 * m, 2):
        u = int(data[i]); v = int(data[i + 1])
        adj[u].append(v); adj[v].append(u)
    d1 = bfs(adj, n, 1)
    D = d1[n]
    if D < 0:
        out = '-1'
    else:
        dn = bfs(adj, n, n)
        tang = [0] * (D + 1)                  # tang[k] = so nut tren duong ngan nhat co d1 = k
        A = 0
        for v in range(1, n + 1):
            if d1[v] >= 0 and d1[v] + dn[v] == D:
                tang[d1[v]] += 1
                A += 1
        B = tang.count(1)
        out = f'{D} {A} {B}'
    with open('TRUNGCHUYEN.OUT', 'w') as f:
        f.write(out + '\n')

main()
