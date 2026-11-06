# HAIPHE: n hoc sinh, m cap (u, v) "khong hop nhau". Chia lop thanh 2 phe A, B (mot phe co the rong)
# sao cho moi cap khong hop nhau o KHAC phe. Dem so cach chia, in mod 10^9+7 (0 neu khong the).
# n <= 10^5, m <= 2*10^5
# Mo hinh: do thi vo huong, chia 2 phe = to 2 mau = kiem tra DO THI HAI PHIA.
#   - Moi thanh phan lien thong: chon mau cho 1 dinh thi ca thanh phan bi ep (BFS to xen ke).
#     Thanh phan co canh noi 2 dinh cung mau (chu trinh le) -> khong the -> 0.
#   - Cac thanh phan doc lap, moi thanh phan 2 cach (doi cho A <-> B) -> dap an 2^c mod p,
#     c = so thanh phan lien thong (dinh co lap cung la 1 thanh phan: dung phe nao cung duoc).
# BFS bang list theo kieu "for u in q" (khong de quy).  O(n + m)
MOD = 10**9 + 7

def main():
    data = open('HAIPHE.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    adj = [[] for _ in range(n + 1)]
    for i in range(2, 2 + 2 * m, 2):
        u = int(data[i]); v = int(data[i + 1])
        adj[u].append(v); adj[v].append(u)
    mau = [-1] * (n + 1)
    c = 0
    ok = True
    for s in range(1, n + 1):
        if mau[s] >= 0:
            continue
        c += 1
        mau[s] = 0
        q = [s]
        for u in q:
            mv = 1 - mau[u]
            for v in adj[u]:
                if mau[v] < 0:
                    mau[v] = mv; q.append(v)
                elif mau[v] != mv:          # hai dau canh cung mau: chu trinh le
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            break
    with open('HAIPHE.OUT', 'w') as f:
        f.write(str(pow(2, c, MOD) if ok else 0) + '\n')

main()
