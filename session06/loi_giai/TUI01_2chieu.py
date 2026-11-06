# TUI01 - ban bang 2 chieu (de giang truoc khi rut gon con 1 mang)
#   f[i][s] = gia tri lon nhat khi chi dung i vat dau, tong khoi luong <= s
#   f[i][s] = max(f[i-1][s], f[i-1][s - w_i] + v_i)  (khong lay / lay vat i)
# Bo nho (n+1)*(W+1) so: 5*10^6 so Python ~ 40 MB -> sat gioi han bo nho, va cham hon ban 1 mang.
def main():
    data = open('TUI01.INP', 'rb').read().split()
    n, W = int(data[0]), int(data[1])
    f = [[0] * (W + 1)]
    for i in range(1, n + 1):
        w, v = int(data[2 * i]), int(data[2 * i + 1])
        tr = f[i - 1]
        hang = tr[:]                           # khong lay vat i
        for s in range(w, W + 1):
            x = tr[s - w] + v                  # lay vat i: dung hang i-1 nen duyet chieu nao cung dung
            if x > hang[s]:
                hang[s] = x
        f.append(hang)
    with open('TUI01.OUT', 'w') as out:
        out.write(str(f[n][W]) + '\n')

main()
