# PAIRCOUNT - vet can O(n^2), dung cho subtask 1 (n <= 10^3).
def main():
    data = open('PAIRCOUNT.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + n]))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] + k == a[j]:
                ans += 1
    with open('PAIRCOUNT.OUT', 'w') as f:
        f.write(str(ans) + '\n')

main()
