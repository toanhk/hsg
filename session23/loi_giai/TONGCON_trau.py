# TONGCON - vet can O(n^2): co dinh l, cong dan r (subtask 1: n <= 3000).
def main():
    data = open('TONGCON.INP', 'rb').read().split()
    n, L, R = int(data[0]), int(data[1]), int(data[2])
    a = list(map(int, data[3:3 + n]))
    ans = 0
    for l in range(n):
        s = 0
        for r in range(l, n):
            s += a[r]
            if L <= s <= R:
                ans += 1
    with open('TONGCON.OUT', 'w') as f:
        f.write(str(ans) + '\n')

main()
