# BALO - vet can: thu moi tap con bang quay lui (2^n). Subtask 1 (n <= 20).
import sys

def main():
    data = open('BALO.INP', 'rb').read().split()
    n, W = int(data[0]), int(data[1])
    w = [int(data[2 + 2 * i]) for i in range(n)]
    v = [int(data[3 + 2 * i]) for i in range(n)]
    sys.setrecursionlimit(1000)
    best = 0

    def thu(i, kl, gt):
        nonlocal best
        if kl > W:
            return
        if i == n:
            if gt > best: best = gt
            return
        thu(i + 1, kl + w[i], gt + v[i])
        thu(i + 1, kl, gt)

    thu(0, 0, 0)
    with open('BALO.OUT', 'w') as f:
        f.write(str(best) + '\n')

main()
