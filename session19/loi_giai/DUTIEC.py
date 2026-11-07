# DUTIEC: cong ty n nhan vien, giam doc la 1, nhan vien i (i >= 2) co sep truc tiep p[i].
# Moi nguoi co do vui a[i] (co the AM). Chon mot nhom moi du tiec sao cho KHONG co ai di cung sep truc tiep
# cua minh, tong do vui lon nhat (duoc phep khong moi ai -> 0). n <= 2*10^5, |a[i]| <= 10^4.
# QHD tren cay (tap doc lap lon nhat co trong so):
#   trang thai : d0[u] = tong lon nhat trong cay con u khi KHONG moi u, d1[u] = khi MOI u
#   truy hoi   : d0[u] = tong_{v con u} max(d0[v], d1[v]);   d1[u] = a[u] + tong_{v con u} d0[v]
#   khoi tao   : d0[u] = 0, d1[u] = a[u] (la: dung luon)
#   thu tu     : con truoc cha -> duyet NGUOC thu tu BFS tu goc 1
#   dap an     : max(d0[1], d1[1])
# CHU Y: de KHONG hua p[i] < i, nen phai lay thu tu bang BFS chu khong duyet i = n..2. O(n).
def main():
    data = open('DUTIEC.INP', 'rb').read().split()
    n = int(data[0])
    a = [0] + list(map(int, data[1:n + 1]))
    p = [0, 0] + list(map(int, data[n + 1:2 * n]))
    con = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        con[p[i]].append(i)
    order = [1]
    for u in order:
        order.extend(con[u])                   # cay co huong cha -> con: khong can kiem tra cha
    d0 = [0] * (n + 1)
    d1 = a[:]
    for u in reversed(order):
        if u == 1:
            break                              # goc la phan tu dau, khong co cha
        c = p[u]
        x, y = d0[u], d1[u]
        d0[c] += x if x > y else y
        d1[c] += x
    with open('DUTIEC.OUT', 'w') as f:
        f.write(str(max(d0[1], d1[1])) + '\n')

main()
