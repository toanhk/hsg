# CHIADOI - ban trung gian (subtask 2, n <= 2000): buoc 1 giong CHIADOI.py, buoc 2 la QHD tap tong
# bang mang True/False va duyet s GIAM DAN (moi thanh phan dung mot lan, nhu tui 0-1 buoi 6).
# O(c * D) voi c = so thanh phan, D <= n: n = 2000 -> <= 4*10^6 o, ~0.3 s. n = 10^5 -> 10^10: qua cham.

def main():
    data = open('CHIADOI.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + 2 * m]))
    ke = [[] for _ in range(n + 1)]
    for u, v in zip(a[0::2], a[1::2]):
        ke[u].append(v)
        ke[v].append(u)
    mau = [-1] * (n + 1)
    ds = []
    for s in range(1, n + 1):
        if mau[s] != -1:
            continue
        mau[s] = 0
        st = [s]
        dem = [1, 0]
        while st:
            u = st.pop()
            for v in ke[u]:
                if mau[v] == -1:
                    mau[v] = 1 - mau[u]
                    dem[mau[v]] += 1
                    st.append(v)
                elif mau[v] == mau[u]:
                    open('CHIADOI.OUT', 'w').write('-1\n')
                    return
        ds.append(abs(dem[0] - dem[1]))
    D = sum(ds)
    f = [False] * (D + 1)
    f[0] = True
    for d in ds:
        if d == 0:
            continue
        for s in range(D, d - 1, -1):          # GIAM DAN: f[s - d] con la gia tri cu
            if f[s - d]:
                f[s] = True
    s = max(x for x in range(D // 2 + 1) if f[x])
    with open('CHIADOI.OUT', 'w') as out:
        out.write(str(D - 2 * s) + '\n')

main()
