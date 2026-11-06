# TOHOP - vet can: duyet moi tap con bang bitmask, giu tap co dung k phan tu, sap xep lai
# O(2^n * n): chi qua n <= 20. n = 50 thi 2^50 tap -> khong bao gio xong
def main():
    data = open('TOHOP.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    ds = []
    for m in range(1 << n):
        if bin(m).count('1') == k:
            ds.append([i + 1 for i in range(n) if m >> i & 1])
    ds.sort()                            # bitmask khong cho san thu tu tu dien
    with open('TOHOP.OUT', 'w') as f:
        f.write(str(len(ds)) + '\n' + '\n'.join(' '.join(map(str, t)) for t in ds) + '\n')

main()
