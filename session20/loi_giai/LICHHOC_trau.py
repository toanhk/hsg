# LICHHOC - vet can (n <= 8): thu moi hoan vi, kiem tra moi dieu kien u truoc v.
from itertools import permutations

def main():
    data = open('LICHHOC.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    dk = [(int(data[2 + 2 * k]) - 1, int(data[3 + 2 * k]) - 1) for k in range(m)]
    dem = 0
    for p in permutations(range(n)):
        vt = [0] * n
        for i, x in enumerate(p):
            vt[x] = i
        if all(vt[u] < vt[v] for u, v in dk):
            dem += 1
    with open('LICHHOC.OUT', 'w') as f:
        f.write(str(dem % (10**9 + 7)) + '\n')

main()
