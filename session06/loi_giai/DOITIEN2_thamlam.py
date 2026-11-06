# DOITIEN2 - ban THAM LAM (SAI) de chua bai: luon lay to lon nhat con lay duoc.
# Dung voi he tien "dep" (1, 2, 5, 10, ...) nhung sai voi {1, 3, 4}, S = 6, va co the bao -1 nham.
def main():
    data = open('DOITIEN2.INP', 'rb').read().split()
    m, S = int(data[0]), int(data[1])
    c = sorted(map(int, data[2:2 + m]), reverse=True)
    dem, con = 0, S
    for x in c:
        dem += con // x
        con %= x
    with open('DOITIEN2.OUT', 'w') as out:
        out.write(str(dem if con == 0 else -1) + '\n')

main()
