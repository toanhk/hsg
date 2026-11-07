# PHANCUM - Kruskal tren do thi day du: sinh n(n-1)/2 canh (gop w, i, j vao mot so nguyen), sap, hop den khi
# con k thanh phan. Dung, nhung voi n = 1500 co 1,1*10^6 canh: do tren may Python 3.13 mat ~0,6 s (gap doi Prim),
# may phong thi cham hon co the sat/qua 1 s. Chac chan qua subtask 1 + 2; subtask 3 tuy may.
def main():
    data = open('PHANCUM.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    X = list(map(int, data[2:2 + 2 * n:2]))
    Y = list(map(int, data[3:3 + 2 * n:2]))
    e = []
    for i in range(n):
        xi = X[i]; yi = Y[i]
        for j in range(i + 1, n):
            e.append((abs(xi - X[j]) + abs(yi - Y[j])) << 22 | i << 11 | j)
    e.sort()
    parent = list(range(n))
    nhom = n
    kq = 0
    for x in e:
        a = x >> 11 & 2047; b = x & 2047
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        while parent[b] != b:
            parent[b] = parent[parent[b]]; b = parent[b]
        if a != b:
            if nhom == k:                      # canh dau tien noi hai nhom khi da con dung k nhom
                kq = x >> 22
                break
            parent[a] = b; nhom -= 1
    with open('PHANCUM.OUT', 'w') as f:
        f.write(str(kq) + '\n')

main()
