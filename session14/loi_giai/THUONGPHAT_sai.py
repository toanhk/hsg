# THUONGPHAT - BAN SAI de chua bai: thay co dinh van giam o vong thu n la in VOCUC ngay.
# Sai vi chu trinh am co the KHONG dan toi n (lac vao mot nhanh cut) - khi do dap an van huu han.
def main():
    data = open('THUONGPHAT.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    canh = [tuple(int(x) for x in data[2 + 3 * i: 5 + 3 * i]) for i in range(m)]
    INF = float('inf')
    d = [INF] * (n + 1); d[1] = 0
    for _ in range(n - 1):
        doi = False
        for u, v, w in canh:
            if d[u] + w < d[v]:
                d[v] = d[u] + w; doi = True
        if not doi:
            break
    if any(d[u] + w < d[v] for u, v, w in canh):
        kq = 'VOCUC'                       # SAI: chua kiem tra chu trinh am co toi duoc n khong
    elif d[n] == INF:
        kq = 'KHONG'
    else:
        kq = str(d[n])
    with open('THUONGPHAT.OUT', 'w') as f:
        f.write(kq + '\n')

main()
