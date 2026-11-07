# LAYSO - THAM LAM (SAI): moi luot lay dau nao LON HON.
# Phan vi du: 3 9 1 2 -> tham lam: An lay 3 (3 > 2), Binh lay 9, An lay 2, Binh lay 1 -> An = 5.
# Toi uu: An lay 2 truoc (khong mo duong cho 9) -> Binh lay 3 hoac 1, An lay 9 -> An = 11.
def main():
    data = open('LAYSO.INP', 'rb').read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    l, r = 0, n - 1
    diem = [0, 0]
    luot = 0
    while l <= r:
        if a[l] >= a[r]:
            diem[luot] += a[l]; l += 1
        else:
            diem[luot] += a[r]; r -= 1
        luot ^= 1
    with open('LAYSO.OUT', 'w') as out:
        out.write(str(diem[0]) + '\n')

main()
