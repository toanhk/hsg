# TRUOTTUYET: luoi r x c, o (i, j) co do cao h. Tu mot o duoc truot sang o KE CANH co do cao NHO HON HAN.
# Hoi duong truot dai nhat di qua bao nhieu o (bat dau o dau cung duoc). r, c <= 500, h <= 10^9.
# Do thi AN: dinh = o, cung = "truot tu o cao sang o thap ke canh". Do cao giam ngat nen khong co chu trinh
# -> DAG. Thu tu to-po co san: SAP XEP CAC O THEO DO CAO TANG DAN (khong can Kahn).
#   Trang thai : f[p] = so o cua duong truot dai nhat BAT DAU tu o p
#   Truy hoi   : f[p] = 1 + max f[q] voi q ke p va h[q] < h[p]   (khong co q: f[p] = 1)
#   Khoi tao   : f[p] = 1
#   Thu tu     : h tang dan -> moi o thap hon p da tinh xong truoc p
#   Dap an     : max f[p]
# Ma hoa o p = (i + 1) * W + (j + 1) voi vien do cao "vo cung" (khong bao gio truot vao) - nhu buoi 11.
# O(rc log(rc)) do sap xep; 2.5*10^5 o x 4 huong ~ 10^6 phep: an toan.
def main():
    data = open('TRUOTTUYET.INP', 'rb').read().split()
    r, c = int(data[0]), int(data[1])
    W = c + 2
    CAO = 1 << 40                              # vien: cao hon moi o that -> khong truot vao
    h = [CAO] * (W * (r + 2))
    p = 2
    for i in range(1, r + 1):
        base = i * W + 1
        h[base:base + c] = map(int, data[p:p + c])
        p += c
    o = [i * W + j for i in range(1, r + 1) for j in range(1, c + 1)]
    o.sort(key=h.__getitem__)                  # thu tu to-po: do cao tang dan
    f = [1] * len(h)
    for x in o:
        hx = h[x]; best = 1
        for y in (x - W, x + W, x - 1, x + 1):
            if h[y] < hx and f[y] >= best:
                best = f[y] + 1
        f[x] = best
    with open('TRUOTTUYET.OUT', 'w') as fo:
        fo.write(str(max(f[x] for x in o)) + '\n')

main()
