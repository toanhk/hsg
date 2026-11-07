# SONHANG: hang rao n coc, ban dau chua son (mau 0). Lan luot q lan: son cac coc l..r bang mau c
# (lan sau de len lan truoc). In mau cuoi cung cua n coc.   n <= 3*10^5, q <= 2*10^5, c <= 10^9
# Son XUOI thi moi coc co the bi son lai nhieu lan -> O(n * q). Lam NGUOC: lan son CUOI cung phu
#   len coc nao thi do la mau cuoi -> di tu lan q ve lan 1, moi coc chi son MOT lan (khi gap lan
#   dau tien tu cuoi), cac lan som hon bo qua coc da son.
# Can nhay nhanh qua cac coc da son: DSU "con tro sang phai".
#   nxt[i] = i neu coc i chua son; son xong thi nxt[i] = r + 1 (gop i vao nhom ben phai; tro
#   thang toi r + 1 vi ca doan l..r deu se son xong, nhay xa hon i + 1 ma van dung).
#   find(i) = coc CHUA SON dau tien >= i. Coc n + 1 la linh canh, khong bao gio bi son.
# Moi coc bi gop dung 1 lan, nen duong giu cho find nhanh: tong O((n + q) * log) thuc te rat nhanh.
# (Day la DSU khong hop theo kich thuoc vi huong gop co dinh: luon trai -> phai.)

def main():
    data = open('SONHANG.INP', 'rb').read().split()
    n, q = int(data[0]), int(data[1])
    nxt = list(range(n + 2))
    mau = [0] * (n + 1)

    def find(x):
        r = x
        while nxt[r] != r:
            r = nxt[r]
        while nxt[x] != r:
            nxt[x], x = r, nxt[x]
        return r

    for t in range(2 + 3 * (q - 1), 1, -3):    # tu lan son cuoi ve lan dau
        l, r = int(data[t]), int(data[t + 1])
        c = int(data[t + 2])
        i = find(l)
        while i <= r:
            mau[i] = c
            nxt[i] = r + 1             # ca doan l..r se duoc son het -> tro thang qua r
            i += 1
            if nxt[i] != i:            # coc ke da son tu truoc -> nhay
                i = find(i)
    with open('SONHANG.OUT', 'w') as f:
        f.write(' '.join(map(str, mau[1:])) + '\n')

main()
