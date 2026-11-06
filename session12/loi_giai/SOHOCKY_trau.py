# SOHOCKY - vet can (n <= 8): thu so ky K = 1, 2, ..., n; voi moi K quay lui gan ky 1..K cho tung mon,
# cat nhanh ngay khi mot canh u -> v (ca hai da gan) vi pham ky[u] < ky[v]. K dau tien gan duoc la dap an.
def main():
    data = open('SOHOCKY.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    canh = [(int(data[2 + 2 * i]), int(data[3 + 2 * i])) for i in range(m)]
    ky = [0] * (n + 1)

    def thu(i, K):                     # gan ky cho mon i..n (de quy sau toi da n <= 8)
        if i > n:
            return True
        for k in range(1, K + 1):
            ky[i] = k
            if all(ky[v] == 0 or ky[u] == 0 or ky[u] < ky[v] for u, v in canh) and thu(i + 1, K):
                return True
        ky[i] = 0
        return False

    kq = -1
    for K in range(1, n + 1):
        if thu(1, K):
            kq = K
            break
    with open('SOHOCKY.OUT', 'w') as f:
        f.write(str(kq) + '\n')

main()
