# CATDIEN - lam XUOI: sau moi lan dut, dung lai DSU tu dau voi cac day con lai. O(q * (n + m)).
# n = m = q = 2000 -> ~8*10^6 (kip); 10^5 -> khong kip. Qua subtask 1-2.

def main():
    data = open('CATDIEN.INP', 'rb').read().split()
    n, m, q = int(data[0]), int(data[1]), int(data[2])
    U = list(map(int, data[3:3 + 2 * m:2]))
    V = list(map(int, data[4:4 + 2 * m:2]))
    cat = [int(x) - 1 for x in data[3 + 2 * m:3 + 2 * m + q]]
    con = bytearray([1]) * m
    out = []
    for e in cat:
        con[e] = 0
        cha = list(range(n + 1))
        vung = n
        for i in range(m):
            if con[i]:
                a = U[i]
                while cha[a] != a:
                    cha[a] = cha[cha[a]]; a = cha[a]     # nen nua duong (path halving)
                b = V[i]
                while cha[b] != b:
                    cha[b] = cha[cha[b]]; b = cha[b]
                if a != b:
                    cha[a] = b; vung -= 1
        out.append(str(vung))
    with open('CATDIEN.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
