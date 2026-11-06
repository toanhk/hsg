# TUILON - vet can: duyet moi tap con bang bitmask, O(2^n * n). Chi qua subtask 1 (n <= 20), W lon khong anh huong
def main():
    data = open('TUILON.INP', 'rb').read().split()
    n, W = int(data[0]), int(data[1])
    w = [int(data[2 + 2 * i]) for i in range(n)]
    v = [int(data[3 + 2 * i]) for i in range(n)]
    best = 0
    for mask in range(1 << n):
        tw = tv = 0
        for i in range(n):
            if mask >> i & 1:
                tw += w[i]
                tv += v[i]
        if tw <= W and tv > best:
            best = tv
    with open('TUILON.OUT', 'w') as out:
        out.write(str(best) + '\n')

main()
