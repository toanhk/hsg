# QUYNHOM - BAN SAI de chua bai: quen kiem tra "a != b" khi hop.
# Neu u, v da cung nhom (a == b): cha[a] = a khong sao, nhung tong[a] += tong[a] -> quy NHAN DOI.
# Ket qua dung tren test khong bao gio gop lai hai ban da cung nhom, sai o cac test con lai.

def main():
    data = open('QUYNHOM.INP', 'rb').read().split()
    n, q = int(data[0]), int(data[1])
    cha = list(range(n + 1))
    co = [1] * (n + 1)
    tong = [0] + list(map(int, data[2:2 + n]))
    pos = 2 + n

    def find(x):
        r = x
        while cha[r] != r:
            r = cha[r]
        while cha[x] != r:
            cha[x], x = r, cha[x]
        return r

    out = []
    for _ in range(q):
        t = data[pos]
        if t == b'1':
            a = find(int(data[pos + 1])); b = find(int(data[pos + 2])); pos += 3
            if co[a] < co[b]:
                a, b = b, a
            cha[b] = a                     # thieu: if a != b
            co[a] += co[b]
            tong[a] += tong[b]
        elif t == b'2':
            tong[find(int(data[pos + 1]))] += int(data[pos + 2]); pos += 3
        else:
            out.append(str(tong[find(int(data[pos + 1]))])); pos += 2
    with open('QUYNHOM.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
