# TORAO - vet can: sinh het k^n cach to bang itertools.product, dem cach hop le.
# n = 8, k = 4 -> 65536 cach. Chi cho subtask 1 (n <= 8, k <= 4).
from itertools import product

def main():
    data = open('TORAO.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    dem = 0
    for c in product(range(k), repeat=n):
        if all(not (c[i] == c[i - 1] == c[i - 2]) for i in range(2, n)):
            dem += 1
    with open('TORAO.OUT', 'w') as out:
        out.write(str(dem % (10**9 + 7)) + '\n')

main()
