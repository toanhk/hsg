# HAIPHE - vet can (n <= 15): thu moi 2^n cach gan phe, dem cach thoa moi cap.
def main():
    data = open('HAIPHE.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    canh = [(int(data[2 + 2 * i]) - 1, int(data[3 + 2 * i]) - 1) for i in range(m)]
    dem = 0
    for mask in range(1 << n):
        if all((mask >> u & 1) != (mask >> v & 1) for u, v in canh):
            dem += 1
    with open('HAIPHE.OUT', 'w') as f:
        f.write(str(dem % (10**9 + 7)) + '\n')

main()
