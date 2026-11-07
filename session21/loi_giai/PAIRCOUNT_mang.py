# PAIRCOUNT - cach cho subtask 2 (0 <= a[i] <= 10^6): mang dem do dai 10^6 + 1 thay cho dict.
# Gap a[i] am hoac > 10^6 (subtask 3) se IndexError hoac sai -> chi lay 40% + 30%.
def main():
    data = open('PAIRCOUNT.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + n]))
    M = 10**6
    dem = [0] * (M + 1)
    ans = 0
    for x in a:
        y = x - k
        if y >= 0:
            ans += dem[y]
        dem[x] += 1
    with open('PAIRCOUNT.OUT', 'w') as f:
        f.write(str(ans) + '\n')

main()
