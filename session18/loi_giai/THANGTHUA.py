# THANGTHUA: DAG n dinh, m cung. Dat mot quan co o dinh s. An va Binh lan luot di (An di truoc), moi luot
# day quan co theo mot cung u -> v. Ai den luot ma KHONG DI DUOC thi THUA. Ca hai choi toi uu.
# Voi moi s = 1..n, in 'A' neu An thang, 'B' neu Binh thang (mot xau n ky tu). n, m <= 2*10^5.
# QHD tren DAG (trang thai tro choi):
#   Trang thai : thang[u] = nguoi SAP DI tai u co thang khong
#   Truy hoi   : thang[u] = True  <=>  co cung u -> v voi thang[v] = False (day doi thu vao the thua)
#   Khoi tao   : dinh khong co cung ra: thang = False (khong di duoc -> thua)
#   Thu tu     : NGUOC thu tu to-po (moi v sau u da tinh xong truoc u)
#   Dap an     : thang[s] cho tung s
# Chi can mot nuoc di toi the thua la du thang; khong co nuoc nao nhu vay -> thua.  O(n + m)
def main():
    data = list(map(int, open('THANGTHUA.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    it = iter(data[2:2 + 2 * m])
    for u, v in zip(it, it):
        adj[u].append(v); deg[v] += 1
    q = [u for u in range(1, n + 1) if deg[u] == 0]
    for u in q:                                # Kahn lay thu tu to-po
        for v in adj[u]:
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    thang = [False] * (n + 1)
    for u in reversed(q):                      # duyet NGUOC: cac dinh sau u da co ket qua
        for v in adj[u]:
            if not thang[v]:
                thang[u] = True
                break
    with open('THANGTHUA.OUT', 'w') as fo:
        fo.write(''.join('A' if thang[u] else 'B' for u in range(1, n + 1)) + '\n')

main()
