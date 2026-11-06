# HAIPHE - cach 2: DSU "co chan le" (moi dinh luu chan le so voi goc). Ghep canh (u, v) yeu cau
# u, v khac phe. find khong de quy. Dung de doi chieu; buoi 15 se hoc ky DSU.
MOD = 10**9 + 7

def main():
    data = open('HAIPHE.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    cha = list(range(n + 1)); le = [0] * (n + 1)   # le[x] = phe x khac phe cha[x]?
    def find(x):
        duong = []
        while cha[x] != x:
            duong.append(x); x = cha[x]
        goc = x; p = 0
        for y in reversed(duong):                  # nen duong, cong don chan le ve goc
            p ^= le[y]; le[y] = p; cha[y] = goc
        return goc
    c = n; ok = True
    for i in range(2, 2 + 2 * m, 2):
        u = int(data[i]); v = int(data[i + 1])
        ru, rv = find(u), find(v)
        if ru == rv:
            if le[u] == le[v]:
                ok = False; break
        else:
            cha[ru] = rv; le[ru] = le[u] ^ le[v] ^ 1; c -= 1
    with open('HAIPHE.OUT', 'w') as f:
        f.write(str(pow(2, c, MOD) if ok else 0) + '\n')

main()
