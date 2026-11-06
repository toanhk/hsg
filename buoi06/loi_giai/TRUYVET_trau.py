# TRUYVET - vet can: bitmask moi tap con, giu tap tot nhat. Chi qua subtask 1 (n <= 15)
def main():
    data = open('TRUYVET.INP', 'rb').read().split()
    n, W = int(data[0]), int(data[1])
    w = [int(data[2 + 2 * i]) for i in range(n)]
    v = [int(data[3 + 2 * i]) for i in range(n)]
    best, bm = 0, 0
    for mask in range(1 << n):
        tw = tv = 0
        for i in range(n):
            if mask >> i & 1:
                tw += w[i]
                tv += v[i]
        if tw <= W and tv > best:
            best, bm = tv, mask
    chon = [i + 1 for i in range(n) if bm >> i & 1]
    with open('TRUYVET.OUT', 'w') as out:
        out.write(f'{best}\n{len(chon)}\n' + ' '.join(map(str, chon)) + '\n')

main()
