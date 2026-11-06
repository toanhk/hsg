# CHENHLECH - vet can (n <= 6, m <= 12): thu moi tap n-1 canh, tap nao noi duoc moi dinh thi lay max - min.
from itertools import combinations

def main():
    data = open('CHENHLECH.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    canh = [(int(data[i]), int(data[i + 1]), int(data[i + 2])) for i in range(2, 2 + 3 * m, 3)]
    best = -1 if n > 1 else 0
    for tap in combinations(canh, n - 1):
        if n == 1:
            break
        nhom = list(range(n + 1))
        for u, v, w in tap:
            a, b = nhom[u], nhom[v]
            nhom = [a if x == b else x for x in nhom]
        if len(set(nhom[1:])) == 1:
            ws = [w for u, v, w in tap]
            if best < 0 or max(ws) - min(ws) < best:
                best = max(ws) - min(ws)
    with open('CHENHLECH.OUT', 'w') as f:
        f.write(str(best) + '\n')

main()
