# DEMNHOM - DSU dung, nhung sau moi cay cau QUET lai moi dinh de dem goc va tim nhom lon nhat.
# O(n * m): n = m = 3000 -> 9*10^6 (kip); n = m = 2*10^5 -> 4*10^10 (khong kip). Qua subtask 1-2.

def main():
    data = open('DEMNHOM.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    cha = list(range(n + 1))
    co = [1] * (n + 1)

    def find(x):
        r = x
        while cha[r] != r:
            r = cha[r]
        while cha[x] != r:
            cha[x], x = r, cha[x]
        return r

    out = []
    for i in range(2, 2 + 2 * m, 2):
        a = find(int(data[i])); b = find(int(data[i + 1]))
        if a != b:
            if co[a] < co[b]:
                a, b = b, a
            cha[b] = a
            co[a] += co[b]
        nhom = lon = 0
        for x in range(1, n + 1):          # quet lai: day la cho lam cham
            if cha[x] == x:
                nhom += 1
                if co[x] > lon:
                    lon = co[x]
        out.append(f'{nhom} {lon}')
    with open('DEMNHOM.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
