# THANGTHUA - ban SAI: duyet THEO thu tu to-po (xuoi) thay vi nguoc. Khi xet u, cac dinh v sau u chua
# duoc tinh (con mac dinh False = "thua") -> u bi coi la thang chi vi co cung ra. Thuc chat ban nay chi
# in 'A' cho moi dinh co cung ra: sai ngay o chuoi 1 -> 2 -> 3 (dung la BAB, ban nay in AAB).
# Bai hoc: thu tu tinh QHD phai bao dam moi trang thai phu thuoc DA XONG.
def main():
    data = list(map(int, open('THANGTHUA.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    it = iter(data[2:2 + 2 * m])
    for u, v in zip(it, it):
        adj[u].append(v); deg[v] += 1
    q = [u for u in range(1, n + 1) if deg[u] == 0]
    for u in q:
        for v in adj[u]:
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    thang = [False] * (n + 1)
    for u in q:                                # SAI: phai la reversed(q)
        for v in adj[u]:
            if not thang[v]:
                thang[u] = True
                break
    with open('THANGTHUA.OUT', 'w') as fo:
        fo.write(''.join('A' if thang[u] else 'B' for u in range(1, n + 1)) + '\n')

main()
