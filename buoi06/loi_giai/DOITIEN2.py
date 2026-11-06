# DOITIEN2: m loai to tien (moi loai khong gioi han). Doi S dong bang IT TO NHAT; khong doi duoc in -1.
# m <= 50, S <= 10^5
#   Trang thai : f[s] = so to it nhat de tao dung s dong (INF neu khong tao duoc)
#   Truy hoi   : f[s] = min(f[s], f[s - c] + 1)   (cai tui khong gioi han: s tang dan)
#   Khoi tao   : f[0] = 0, f[s > 0] = INF   (khac TUIVOHAN: phai DUNG s, nen khong khoi tao 0 het)
#   Thu tu     : vong ngoai loai tien, vong trong s tang dan
#   Dap an     : f[S] (INF -> -1)
# Tham lam "lay to lon nhat truoc" SAI: to {1, 3, 4}, S = 6 -> 4+1+1 (3 to) trong khi 3+3 (2 to).
# O(m * S) = 5*10^6 o ~ 0.2 s
def main():
    data = open('DOITIEN2.INP', 'rb').read().split()
    m, S = int(data[0]), int(data[1])
    c = list(map(int, data[2:2 + m]))
    INF = S + 1                                # so to khong bao gio vuot S (to nho nhat >= 1)
    f = [INF] * (S + 1)
    f[0] = 0
    for x in c:
        for s in range(x, S + 1):
            y = f[s - x] + 1
            if y < f[s]:
                f[s] = y
    with open('DOITIEN2.OUT', 'w') as out:
        out.write(str(f[S] if f[S] < INF else -1) + '\n')

main()
