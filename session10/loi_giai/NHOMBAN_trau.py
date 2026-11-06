# NHOMBAN - vet can: lan nhan nhu LIENTHONG_trau (O(n*m)), roi xet moi cap (u, v) O(n^2).
# Chi dung cho n, m <= 1000 (subtask 1).

def main():
    data = open('NHOMBAN.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    canh = [(int(data[2 + 2 * i]), int(data[3 + 2 * i])) for i in range(m)]
    nhan = list(range(n + 1))
    doi = True
    while doi:
        doi = False
        for u, v in canh:
            if nhan[u] != nhan[v]:
                nhan[u] = nhan[v] = min(nhan[u], nhan[v])
                doi = True
    so_nhom = len(set(nhan[1:]))
    khac = 0
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            if nhan[u] != nhan[v]:
                khac += 1
    with open('NHOMBAN.OUT', 'w') as out:
        out.write(f'{so_nhom}\n{khac}\n')

main()
