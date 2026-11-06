# DOANK - vet can O(n^2): co dinh dau l, cong dan sang phai. Chi qua n <= 1000
def main():
    data = open('DOANK.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + n]))
    ans = 0
    for l in range(n):
        tong = 0
        for r in range(l, n):
            tong += a[r]
            if tong == k:
                ans += 1
    with open('DOANK.OUT', 'w') as f:
        f.write(str(ans) + '\n')

main()
