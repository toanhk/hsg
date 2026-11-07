# GIAMSAT: mang luoi n tram noi bang n-1 day (la mot CAY). Lap camera o tram i ton c[i]. Camera o tram i giam sat
# chinh tram i va moi tram NOI TRUC TIEP voi i. Chon cac tram lap camera de moi tram deu duoc giam sat, tong chi phi
# nho nhat.   n <= 10^5, c[i] <= 10^9.
# QHD tren cay (buoi 19) - goc tai 1, duyet KHONG de quy: BFS lay thu tu, roi duyet NGUOC (con truoc cha).
# Ba trang thai cho moi dinh v (chi xet cay con goc v):
#   A[v] = v CO camera.                               A[v] = c[v] + tong min(A, B, C)[con]
#   B[v] = v khong camera, da duoc MOT con giam sat.  B[v] = tong min(A, B)[con] + phat, voi
#          phat = min(A[con] - min(A, B)[con]) >= 0 (bat buoc it nhat mot con co camera). La: B = vo cuc.
#   C[v] = v khong camera, CHUA duoc giam sat (cha v bat buoc co camera).   C[v] = tong B[con]
#          (con khong duoc o trang thai C vi v khong co camera; con o A thi v da duoc giam sat -> thuoc B).
# Khoi tao: la v co A = c[v], B = vo cuc, C = 0.   Thu tu: nguoc thu tu BFS.   Dap an: min(A[1], B[1]).
# O(n). Do: ~0,25 s voi n = 10^5.
def main():
    data = open('GIAMSAT.INP', 'rb').read().split()
    n = int(data[0])
    c = [0] + list(map(int, data[1:1 + n]))
    adj = [[] for _ in range(n + 1)]
    p = 1 + n
    for _ in range(n - 1):
        u, v = int(data[p]), int(data[p + 1]); p += 2
        adj[u].append(v); adj[v].append(u)
    cha = [0] * (n + 1)
    cha[1] = -1
    thu_tu = [1]                                # BFS: dinh nao cung dung sau cha cua no
    for u in thu_tu:
        for v in adj[u]:
            if v != cha[u]:
                cha[v] = u
                thu_tu.append(v)
    INF = 10**18
    sA = [0] * (n + 1)                          # tong min(A,B,C) cac con da xu ly
    sB = [0] * (n + 1)                          # tong min(A,B)
    sC = [0] * (n + 1)                          # tong B (chan tren INF)
    phat = [INF] * (n + 1)                      # min (A - min(A,B)) cua cac con
    for v in reversed(thu_tu):
        a = c[v] + sA[v]
        b = sB[v] + phat[v] if phat[v] < INF else INF
        cc = sC[v]
        if v == 1:
            break
        u = cha[v]
        ab = a if a < b else b
        sA[u] += ab if ab < cc else cc
        sB[u] += ab
        sC[u] = sC[u] + b if sC[u] + b < INF else INF
        if a - ab < phat[u]:
            phat[u] = a - ab
    with open('GIAMSAT.OUT', 'w') as f:
        f.write(str(min(a, b)) + '\n')

main()
