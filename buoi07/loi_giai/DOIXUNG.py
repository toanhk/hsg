# DOIXUNG: xoa mot so ky tu (giu nguyen thu tu) cua xau S de duoc xau doi xung dai nhat. In do dai.
# |S| <= 2000, chu thuong.
# Nhan xet: xau doi xung T la day con cua S <=> T cung la day con cua S dao nguoc.
#   Moi xau doi xung xoa duoc la day con chung cua S va S[::-1]; nguoc lai LCS(S, S[::-1]) luon
#   dat duoc bang do dai mot xau doi xung (cung cong thuc voi QHD tren doan, xem DOIXUNG_doan.py), nen
#   Dap an = LCS(S, S[::-1]) -> dung lai nguyen code LCS.py, 4*10^6 o ~ 0.4 s
# (Buoi 17 se giai lai bang QHD tren doan f[l][r]: xem DOIXUNG_doan.py)
def main():
    data = open('DOIXUNG.INP', 'rb').read().split()
    A = data[0]
    B = A[::-1]
    m = len(B)
    truoc = [0] * (m + 1)
    for x in A:
        hang = [0]
        c = 0
        for j, y in enumerate(B):
            if x == y:
                c = truoc[j] + 1
            else:
                t = truoc[j + 1]
                if t > c:
                    c = t
            hang.append(c)
        truoc = hang
    with open('DOIXUNG.OUT', 'w') as out:
        out.write(str(truoc[m]) + '\n')

main()
