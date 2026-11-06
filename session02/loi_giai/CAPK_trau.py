# CAPK - vet can O(n^2): xet moi cap. Chi qua subtask n <= 1000 (5*10^5 cap)
def main():
    data = open('CAPK.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + n]))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] + a[j] == k:
                ans += 1
    with open('CAPK.OUT', 'w') as f:
        f.write(str(ans) + '\n')

main()
