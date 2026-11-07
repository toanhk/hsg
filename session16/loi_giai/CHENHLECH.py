# CHENHLECH: do thi n dinh, m canh co trong so. Tim cay khung co (canh LON nhat - canh NHO nhat) nho nhat.
# In hieu do; khong co cay khung thi in -1. n <= 100, m <= 1000, w <= 10^9.
# Sap canh tang dan. Co dinh canh nho nhat la canh thu i (trong thu tu da sap). Trong cac cay chi dung
# canh i, i+1, ..., cay co canh lon nhat NHO NHAT chinh la Kruskal bat dau tu i (tinh chat "cay khung nho
# nhat cung la cay co canh lon nhat nho nhat"). Kruskal tu i dung lai khi du n-1 canh: hieu = w[j] - w[i].
# Kruskal tu i co the KHONG dung canh i, khi do hieu thuc te con nho hon - van dung vi lan thu i' > i se gap.
# Cat nhanh: neu tu i khong noi duoc moi dinh thi tu i+1 tro di cung khong -> dung han.
# O(m^2 * alpha): m = 1000 -> toi da ~5*10^5 lan hop (do: ~0,15 s).
def main():
    data = open('CHENHLECH.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    canh = sorted((int(data[i + 2]), int(data[i]), int(data[i + 1])) for i in range(2, 2 + 3 * m, 3))
    best = -1
    for i in range(m):
        parent = list(range(n + 1))            # DSU moi cho moi diem bat dau (n nho nen reset re)
        chon = 0
        wi = canh[i][0]
        for j in range(i, m):
            w, a, b = canh[j]
            while parent[a] != a:
                parent[a] = parent[parent[a]]; a = parent[a]
            while parent[b] != b:
                parent[b] = parent[parent[b]]; b = parent[b]
            if a != b:
                parent[a] = b
                chon += 1
                if chon == n - 1:
                    break
            if best >= 0 and w - wi >= best:   # da khong the tot hon dap an hien co
                break
        if chon == n - 1:
            if best < 0 or w - wi < best:
                best = w - wi
        elif best < 0 or w - wi < best:
            break                              # het canh ma chua noi xong -> cac i sau cung vay
    with open('CHENHLECH.OUT', 'w') as f:
        f.write(str(best if n > 1 else 0) + '\n')

main()
