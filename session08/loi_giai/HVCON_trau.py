# HVCON - vet can: thu moi canh k, moi vi tri, cong truc tiep k x k o. Chi subtask 1 (m, n <= 50).
def main():
    data = open('HVCON.INP', 'rb').read().split()
    m, n, S = int(data[0]), int(data[1]), int(data[2])
    a = [list(map(int, data[3 + i * n:3 + (i + 1) * n])) for i in range(m)]
    ans = 0
    for k in range(1, min(m, n) + 1):
        if any(sum(sum(a[r][j:j + k]) for r in range(i, i + k)) <= S
               for i in range(m - k + 1) for j in range(n - k + 1)):
            ans = k
    with open('HVCON.OUT', 'w') as f:
        f.write(str(ans) + '\n')

main()
