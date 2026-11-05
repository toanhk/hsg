# QUANHAU: dem so cach dat n quan hau tren ban n x n (moi hang dung 1 quan), khong quan nao
# an nhau va khong dat vao o cam '#'. n <= 11
# Quay lui theo hang; danh dau cot, duong cheo chinh (r - c + n - 1), duong cheo phu (r + c)
def main():
    data = open('QUANHAU.INP', 'rb').read().split()
    n = int(data[0])
    ban = [data[1 + r].decode() for r in range(n)]
    # o_duoc[r] = danh sach cot dat duoc o hang r (bo o cam ngay tu dau)
    o_duoc = [[c for c in range(n) if ban[r][c] == '.'] for r in range(n)]
    cot = [False] * n
    cheo1 = [False] * (2 * n)
    cheo2 = [False] * (2 * n)
    dem = 0

    def thu(r):
        nonlocal dem
        if r == n:
            dem += 1
            return
        for c in o_duoc[r]:
            d1 = r - c + n - 1; d2 = r + c
            if not cot[c] and not cheo1[d1] and not cheo2[d2]:
                cot[c] = cheo1[d1] = cheo2[d2] = True
                thu(r + 1)
                cot[c] = cheo1[d1] = cheo2[d2] = False

    thu(0)
    with open('QUANHAU.OUT', 'w') as f:
        f.write(str(dem) + '\n')

main()
