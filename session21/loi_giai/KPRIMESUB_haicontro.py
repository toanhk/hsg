# KPRIMESUB - hai con tro O(N) moi test: voi moi L tim R nho nhat du K so nguyen to.
# T * N = 10^7 buoc o subtask cuoi -> qua 1 giay trong Python (lay 40% + 30%).
def main():
    data = open('KPRIMESUB.INP', 'rb').read().split()
    t = int(data[0])
    q = [(int(data[1 + 2 * i]), int(data[2 + 2 * i])) for i in range(t)]
    M = max(2, max(N for N, K in q))
    nt = [1] * (M + 1); nt[0] = nt[1] = 0
    for i in range(2, int(M ** 0.5) + 1):
        if nt[i]:
            for j in range(i * i, M + 1, i):
                nt[j] = 0
    out = []
    for N, K in q:
        ans = 0
        R = 1; dem = 0                    # doan hien tai [L..R], dem = so nguyen to trong doan
        for L in range(2, N + 1):
            while R < N and dem < K:
                R += 1; dem += nt[R]
            if dem >= K:
                ans += N - max(R, L) + 1  # K = 0 thi R co the < L
            if R >= L:
                dem -= nt[L]
            else:
                R = L                     # khong xay ra khi K >= 1
        out.append(ans)
    with open('KPRIMESUB.OUT', 'w') as f:
        f.write('\n'.join(map(str, out)) + '\n')

main()
