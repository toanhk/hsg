# CATDX - vet can (|S| <= 15): moi cach cat la mot tap con cua n-1 cho cat -> 2^(n-1) cach.
# Voi moi cach, kiem tra tung doan bang so sanh voi xau dao nguoc.
def main():
    data = open('CATDX.INP', 'rb').read().split()
    S = data[0].decode()
    n = len(S)
    best = n
    for mask in range(1 << (n - 1)):           # bit i = 1: cat giua S[i] va S[i+1]
        dau, ok, dem = 0, True, 0
        for i in range(n):
            if i == n - 1 or mask >> i & 1:
                t = S[dau:i + 1]
                if t != t[::-1]:
                    ok = False
                    break
                dem += 1
                dau = i + 1
        if ok and dem < best:
            best = dem
    with open('CATDX.OUT', 'w') as out:
        out.write(str(best) + '\n')

main()
