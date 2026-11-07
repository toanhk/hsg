# LATGACH - vet can (n <= 12): quay lui dat gach vao o trong dau tien (theo cot, tren truoc duoi).
import sys

def dem(n):
    o = [[False] * n for _ in range(2)]

    def quay_lui():
        for j in range(n):                    # tim o trong dau tien
            for i in range(2):
                if not o[i][j]:
                    tong = 0
                    if i == 0 and not o[1][j]:                      # gach doc
                        o[0][j] = o[1][j] = True; tong += quay_lui(); o[0][j] = o[1][j] = False
                    if j + 1 < n and not o[i][j + 1]:               # gach ngang
                        o[i][j] = o[i][j + 1] = True; tong += quay_lui(); o[i][j] = o[i][j + 1] = False
                    if i == 0 and j + 1 < n and not o[1][j] and not o[0][j + 1] and not o[1][j + 1]:   # 2x2
                        for a in range(2):
                            o[a][j] = o[a][j + 1] = True
                        tong += quay_lui()
                        for a in range(2):
                            o[a][j] = o[a][j + 1] = False
                    return tong
        return 1                              # da kin

    return quay_lui()

def main():
    data = open('LATGACH.INP', 'rb').read().split()
    t = int(data[0])
    out = [dem(int(x)) % (10**9 + 7) for x in data[1:1 + t]]
    with open('LATGACH.OUT', 'w') as f:
        f.write('\n'.join(map(str, out)) + '\n')

main()
