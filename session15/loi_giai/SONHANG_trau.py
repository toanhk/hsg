# SONHANG - vet can: voi moi coc, tim lan son CUOI CUNG co doan chua no. O(n * q).

def main():
    data = open('SONHANG.INP', 'rb').read().split()
    n, q = int(data[0]), int(data[1])
    ds = [(int(data[t]), int(data[t + 1]), data[t + 2].decode()) for t in range(2, 2 + 3 * q, 3)]
    kq = []
    for i in range(1, n + 1):
        c = '0'
        for l, r, x in ds:
            if l <= i <= r:
                c = x
        kq.append(c)
    with open('SONHANG.OUT', 'w') as f:
        f.write(' '.join(kq) + '\n')

main()
