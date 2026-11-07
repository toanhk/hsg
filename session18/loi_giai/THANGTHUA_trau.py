# THANGTHUA - vet can (subtask 1, n <= 10): voi moi s, thu het moi van dau bang de quy minimax KHONG nho
# (so van dau co the luy thua, nhung n <= 10 thi du nhanh). Do sau de quy <= n nen dung de quy o day duoc.
def main():
    data = list(map(int, open('THANGTHUA.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        adj[data[2 + 2 * i]].append(data[3 + 2 * i])

    def thang(u):                              # nguoi sap di tai u co thang khong
        for v in adj[u]:
            if not thang(v):
                return True
        return False

    with open('THANGTHUA.OUT', 'w') as fo:
        fo.write(''.join('A' if thang(s) else 'B' for s in range(1, n + 1)) + '\n')

main()
