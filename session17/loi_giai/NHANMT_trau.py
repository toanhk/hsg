# NHANMT - vet can (n <= 10): de quy thu MOI cach dat ngoac, KHONG nho.
# So cach dat ngoac la so Catalan: n = 10 -> 4862 cach, n = 20 -> 1,7*10^9 (khong kip).
def main():
    data = open('NHANMT.INP', 'rb').read().split()
    n = int(data[0])
    p = list(map(int, data[1:n + 2]))
    def thu(l, r):
        if l == r:
            return 0
        return min(thu(l, k) + thu(k + 1, r) + p[l] * p[k + 1] * p[r + 1] for k in range(l, r))
    with open('NHANMT.OUT', 'w') as out:
        out.write(str(thu(0, n - 1)) + '\n')

main()
