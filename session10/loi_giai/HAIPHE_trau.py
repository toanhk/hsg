# HAIPHE - vet can: thu moi cach chia 2^n, dem cach thoa man moi rang buoc. O(2^n * m): n <= 15.

def main():
    data = open('HAIPHE.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    rb = [(int(data[2 + 3 * i]) - 1, int(data[3 + 3 * i]) - 1, int(data[4 + 3 * i])) for i in range(m)]
    dem = 0
    for mask in range(1 << n):
        if all(((mask >> u) ^ (mask >> v)) & 1 == t for u, v, t in rb):
            dem += 1
    with open('HAIPHE.OUT', 'w') as out:
        out.write(str(dem % (10**9 + 7)) + '\n')

main()
