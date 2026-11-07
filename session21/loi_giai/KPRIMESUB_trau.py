# KPRIMESUB - vet can O(N^2) moi test bang mang cong don so nguyen to (subtask 1: N <= 100).
def la_nt(x):
    if x < 2:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

def main():
    data = open('KPRIMESUB.INP', 'rb').read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        N, K = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        s = [0] * (N + 1)
        for x in range(1, N + 1):
            s[x] = s[x - 1] + la_nt(x)
        ans = 0
        for L in range(2, N + 1):
            for R in range(L, N + 1):
                if s[R] - s[L - 1] >= K:
                    ans += 1
        out.append(ans)
    with open('KPRIMESUB.OUT', 'w') as f:
        f.write('\n'.join(map(str, out)) + '\n')

main()
