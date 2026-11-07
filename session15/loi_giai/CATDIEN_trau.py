# CATDIEN - vet can: sau moi lan dut, dung lai danh sach ke cac day con lai va DFS dem vung.

def main():
    data = open('CATDIEN.INP', 'rb').read().split()
    n, m, q = int(data[0]), int(data[1]), int(data[2])
    canh = [(int(data[3 + 2 * i]), int(data[4 + 2 * i])) for i in range(m)]
    cat = [int(x) - 1 for x in data[3 + 2 * m:3 + 2 * m + q]]
    con = [True] * m
    out = []
    for e in cat:
        con[e] = False
        ke = [[] for _ in range(n + 1)]
        for i in range(m):
            if con[i]:
                u, v = canh[i]; ke[u].append(v); ke[v].append(u)
        tham = [False] * (n + 1)
        vung = 0
        for s in range(1, n + 1):
            if not tham[s]:
                vung += 1; tham[s] = True; st = [s]
                while st:
                    x = st.pop()
                    for y in ke[x]:
                        if not tham[y]:
                            tham[y] = True; st.append(y)
        out.append(str(vung))
    with open('CATDIEN.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
