# SOHOCKY: n mon, m quan he "u truoc v". Moi hoc ky hoc bao nhieu mon cung duoc, nhung mon v chi hoc
# khi MOI mon tien quyet da hoc o cac ky TRUOC. Hoi it nhat bao nhieu ky (-1 neu khong the). n, m <= 2*10^5
# QHD tren DAG theo thu tu to-po:
#   Trang thai : f[v] = ky som nhat co the hoc mon v
#   Truy hoi   : f[v] = 1 + max f[u] voi moi cung u -> v   (khong co mon tien quyet: f[v] = 1)
#   Khoi tao   : f[v] = 1 voi moi v
#   Thu tu     : thu tu to-po (Kahn) - khi lay u ra thi f[u] da xong, "day" sang cac v
#   Dap an     : max f[v]  (= so dinh tren duong di dai nhat); Kahn khong lay du n dinh -> -1
def main():
    data = open('SOHOCKY.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    for i in range(2, 2 + 2 * m, 2):
        u = int(data[i]); v = int(data[i + 1])
        adj[u].append(v); deg[v] += 1
    f = [1] * (n + 1)
    q = [u for u in range(1, n + 1) if deg[u] == 0]
    for u in q:
        fu = f[u] + 1
        for v in adj[u]:
            if fu > f[v]:
                f[v] = fu              # "day toi": u hoc ky f[u] thi v som nhat ky f[u] + 1
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    with open('SOHOCKY.OUT', 'w') as f_out:
        f_out.write(str(max(f[1:]) if len(q) == n else -1) + '\n')

main()
