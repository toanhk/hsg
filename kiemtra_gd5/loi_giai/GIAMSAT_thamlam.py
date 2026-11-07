# GIAMSAT - THAM LAM (dung khi moi c[i] bang nhau - subtask 2, SAI khi chi phi khac nhau):
# duyet nguoc thu tu BFS (la truoc); gap tram v chua duoc giam sat thi lap camera o CHA cua v (goc thi lap o v):
# camera o cha phu duoc v, ca cha va ong - khong kem hon lap o v. Phan vi du: cha rat dat, la re.
def main():
    data = open('GIAMSAT.INP', 'rb').read().split()
    n = int(data[0])
    c = [0] + list(map(int, data[1:1 + n]))
    adj = [[] for _ in range(n + 1)]
    p = 1 + n
    for _ in range(n - 1):
        u, v = int(data[p]), int(data[p + 1]); p += 2
        adj[u].append(v); adj[v].append(u)
    cha = [0] * (n + 1)
    thu_tu = [1]
    for u in thu_tu:
        for v in adj[u]:
            if v != cha[u]:
                cha[v] = u
                thu_tu.append(v)
    cam = [False] * (n + 1)
    phu = [False] * (n + 1)
    tong = 0
    for v in reversed(thu_tu):
        if phu[v] or cam[cha[v]]:
            continue
        u = cha[v] if v != 1 else 1
        cam[u] = True; tong += c[u]
        phu[u] = phu[cha[u]] = phu[v] = True
    with open('GIAMSAT.OUT', 'w') as f:
        f.write(str(tong) + '\n')

main()
