# DONGHANG - vet can (n <= 15): moi cach cat day <=> mot tap "vi tri cat" trong n-1 khe (2^(n-1) cach).
def main():
    data = open('DONGHANG.INP', 'rb').read().split()
    n, K, W = int(data[0]), int(data[1]), int(data[2])
    a = list(map(int, data[3:3 + n]))
    best = -1
    for mask in range(1 << (n - 1)):
        tong = 0; dau = 0; ok = True
        for i in range(n):
            if i == n - 1 or mask >> i & 1:          # cat sau kien i
                doan = a[dau:i + 1]
                if len(doan) > K or sum(doan) > W:
                    ok = False; break
                tong += max(doan); dau = i + 1
        if ok and (best < 0 or tong < best):
            best = tong
    with open('DONGHANG.OUT', 'w') as f:
        f.write(str(best) + '\n')

main()
