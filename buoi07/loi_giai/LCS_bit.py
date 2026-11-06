# LCS - MO RONG cho hoc sinh gioi (ngoai chuong trinh): QHD bit song song (Allison-Dix / Hyyro)
# Moi hang QHD duoc nen thanh MOT so nguyen lon cua Python; phep tru/and/xor tren so lon chay bang C
# nen nhanh gap hang tram lan: |A| = |B| = 2000 ~ 0.002 s, |A| = |B| = 50000 van < 1 s.
#   M[c]  = bitmask cac vi tri j trong B co B[j] == c
#   row   : bit j bat <=> hang QHD hien tai "tang 1" tai cot j (f[i][j+1] - f[i][j] = 1)
#   moi ky tu x cua A: X = M[x] | row ; row = X & ((X - ((row << 1) | 1)) ^ X)
#   Dap an: so bit 1 cua row
# Chi dung de doi chieu / tham khao; tren lop day ban LCS.py.
def main():
    data = open('LCS.INP', 'rb').read().split()
    A, B = data[0], data[1]
    M = {}
    for j, y in enumerate(B):
        M[y] = M.get(y, 0) | (1 << j)
    row = 0
    for x in A:
        X = M.get(x, 0) | row
        row = X & ((X - ((row << 1) | 1)) ^ X)
    with open('LCS.OUT', 'w') as out:
        out.write(str(bin(row).count('1')) + '\n')

main()
