# CHIADOI - vet can: thu moi cach chia 2^n, bo cach co cap khong hop cung doi, lay chenh lech nho nhat.
# O(2^n * m): n <= 15 (subtask 1).

def main():
    data = open('CHIADOI.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    canh = [(int(data[2 + 2 * i]) - 1, int(data[3 + 2 * i]) - 1) for i in range(m)]
    best = -1
    for mask in range(1 << n):                 # bit u = 1: u o doi 1
        if all((mask >> u & 1) != (mask >> v & 1) for u, v in canh):
            c = bin(mask).count('1')
            chenh = abs(c - (n - c))
            if best == -1 or chenh < best:
                best = chenh
    with open('CHIADOI.OUT', 'w') as out:
        out.write(str(best) + '\n')

main()
