# MONHOC - vet can: thu moi hoan vi (n <= 8: 40320 hoan vi), gap hoan vi thoa moi canh thi in.
from itertools import permutations

def main():
    data = open('MONHOC.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    canh = [(int(data[2 + 2 * i]), int(data[3 + 2 * i])) for i in range(m)]
    kq = '-1'
    for p in permutations(range(1, n + 1)):
        vt = [0] * (n + 1)
        for i, x in enumerate(p):
            vt[x] = i                  # vi tri cua mon x trong thu tu
        if all(vt[u] < vt[v] for u, v in canh):
            kq = ' '.join(map(str, p))
            break
    with open('MONHOC.OUT', 'w') as f:
        f.write(kq + '\n')

main()
