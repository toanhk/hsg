# TUI01: cai tui 0/1. n do vat, vat i nang w[i], gia tri v[i]; tui chiu toi da W.
# Moi vat lay hoac khong (0/1). Tong gia tri lon nhat? n <= 100, W <= 5*10^4
#   Trang thai : f[s] = gia tri lon nhat voi tong khoi luong <= s, chi dung cac vat DA XET
#   Truy hoi   : xet them vat (w, v): f[s] = max(f[s], f[s - w] + v)
#   Khoi tao   : f[s] = 0 voi moi s (chua lay gi)
#   Thu tu     : vong NGOAI la vat, vong TRONG la s GIAM dan tu W ve w
#   Dap an     : f[W]
# Vi sao s GIAM: khi tinh f[s] ta can f[s - w] CU (chua co vat nay). Duyet giam thi f[s - w]
# chua bi ghi de trong luot nay. Duyet tang -> f[s - w] da co vat nay -> vat bi lay nhieu lan (= TUIVOHAN).
# O(n * W) = 5*10^6 o ~ 0.25 s
def main():
    data = open('TUI01.INP', 'rb').read().split()
    n, W = int(data[0]), int(data[1])
    f = [0] * (W + 1)
    for i in range(n):
        w, v = int(data[2 + 2 * i]), int(data[3 + 2 * i])
        for s in range(W, w - 1, -1):          # s giam dan
            x = f[s - w] + v
            if x > f[s]:
                f[s] = x
    with open('TUI01.OUT', 'w') as out:
        out.write(str(f[W]) + '\n')

main()
