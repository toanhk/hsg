# GOPSOI - vet can (n <= 8): thu MOI cach chon cap ke nhau de gop o tung buoc (de quy + nho theo trang thai day).
# So trang thai nho, nhung KHONG mo rong duoc: so day khac nhau tang theo cap so nhan.
def main():
    data = open('GOPSOI.INP', 'rb').read().split()
    n = int(data[0])
    a = tuple(map(int, data[1:1 + n]))
    nho = {}
    def thu(d):
        if len(d) == 1:
            return 0
        if d in nho:
            return nho[d]
        best = None
        for i in range(len(d) - 1):
            s = d[i] + d[i + 1]
            t = s + thu(d[:i] + (s,) + d[i + 2:])
            if best is None or t < best:
                best = t
        nho[d] = best
        return best
    with open('GOPSOI.OUT', 'w') as out:
        out.write(str(thu(a)) + '\n')

main()
