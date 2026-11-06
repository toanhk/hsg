# XEPHANG - vet can (n <= 8): dem so hoan vi hop le (dung o hoan vi thu 2).
from itertools import permutations

def main():
    data = open('XEPHANG.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    canh = [(int(data[2 + 2 * i]), int(data[3 + 2 * i])) for i in range(m)]
    tim = []
    for p in permutations(range(1, n + 1)):
        vt = [0] * (n + 1)
        for i, x in enumerate(p):
            vt[x] = i
        if all(vt[u] < vt[v] for u, v in canh):
            tim.append(p)
            if len(tim) == 2:
                break
    kq = '-1' if not tim else ('0' if len(tim) == 2 else ' '.join(map(str, tim[0])))
    with open('XEPHANG.OUT', 'w') as f:
        f.write(kq + '\n')

main()
