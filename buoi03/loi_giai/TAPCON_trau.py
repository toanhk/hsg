# TAPCON - vet can bitmask: moi so m tu 1 den 2^n - 1 la mot tap con, cong lai tung phan tu
# O(2^n * n): n = 16 la 10^6 phep (qua), n = 20 la 2*10^7 phep (qua thoi gian)
def main():
    data = open('TAPCON.INP', 'rb').read().split()
    n, S = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + n]))
    dem = 0
    for m in range(1, 1 << n):
        tong = 0
        for i in range(n):
            if m >> i & 1:
                tong += a[i]
        if tong == S:
            dem += 1
    with open('TAPCON.OUT', 'w') as f:
        f.write(str(dem) + '\n')

main()
