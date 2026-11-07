# DUTIEC - ban SAI de chua: tin rang sep luon co so hieu nho hon (p[i] < i) nen duyet i = n, n-1, ..., 2
# va cong d0/d1 cua i vao p[i]. De KHONG hua dieu do: khi p[i] > i, luc cong d[i] vao p[i]
# thi d[i] chua nhan du cac con cua i -> sai. Dung o subtask 2 (p[i] < i), sai o subtask 3.
# Bai hoc: dung tu y gia thiet thu tu dinh; lay thu tu bang BFS tu goc.
def main():
    data = open('DUTIEC.INP', 'rb').read().split()
    n = int(data[0])
    a = [0] + list(map(int, data[1:n + 1]))
    p = [0, 0] + list(map(int, data[n + 1:2 * n]))
    d0 = [0] * (n + 1)
    d1 = a[:]
    for u in range(n, 1, -1):
        c = p[u]
        d0[c] += max(d0[u], d1[u])
        d1[c] += d0[u]
    with open('DUTIEC.OUT', 'w') as f:
        f.write(str(max(d0[1], d1[1])) + '\n')

main()
