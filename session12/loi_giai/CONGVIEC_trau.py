# CONGVIEC - vet can (n <= 10): Bellman-Ford tim duong dai nhat (lap n vong noi long moi canh; vong
# n + 1 van con thay doi -> co vong). Viec v gang <=> tang t[v] them 1 thi T tang (co mot duong dai
# nhat di qua v). Cach nghi khac han lam QHD nguoc, dung de kiem cheo.
def tinh_T(n, t, canh):
    f = t[:]                                    # f[v] = xong som nhat cua v
    for _ in range(n + 1):
        doi = False
        for u, v in canh:
            if f[u] + t[v] > f[v]:
                f[v] = f[u] + t[v]; doi = True
        if not doi:
            return max(f[1:])
    return -1

def main():
    data = open('CONGVIEC.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    t = [0] + [int(x) for x in data[2:2 + n]]
    canh = [(int(data[2 + n + 2 * i]), int(data[3 + n + 2 * i])) for i in range(m)]
    T = tinh_T(n, t, canh)
    if T < 0:
        out = '-1'
    else:
        gang = 0
        for v in range(1, n + 1):
            t[v] += 1
            if tinh_T(n, t, canh) > T:
                gang += 1
            t[v] -= 1
        out = f'{T} {gang}'
    with open('CONGVIEC.OUT', 'w') as f:
        f.write(out + '\n')

main()
