# XEPLICH - vet can (n <= 15): thu moi tap viec, kiem tra tung cap khong trung ngay.
def main():
    data = open('XEPLICH.INP', 'rb').read().split()
    n = int(data[0])
    v = [(int(data[1 + 3 * i]), int(data[2 + 3 * i]), int(data[3 + 3 * i])) for i in range(n)]
    best = 0
    for mask in range(1 << n):
        chon = [v[i] for i in range(n) if mask >> i & 1]
        ok = all(a[1] < b[0] or b[1] < a[0] for i, a in enumerate(chon) for b in chon[i + 1:])
        if ok:
            best = max(best, sum(x[2] for x in chon))
    with open('XEPLICH.OUT', 'w') as fo:
        fo.write(str(best) + '\n')

main()
