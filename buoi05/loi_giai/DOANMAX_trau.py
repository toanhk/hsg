# DOANMAX - vet can O(n^2): thu moi dau l, keo dai r va cong dan.
# n = 5000 -> 1.25*10^7 phep cong: sat hoac qua 1 giay trong Python. Chac chan qua subtask 1.
def main():
    data = open('DOANMAX.INP', 'rb').read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    tot = a[0]
    for l in range(n):
        s = 0
        for r in range(l, n):
            s += a[r]
            if s > tot:
                tot = s
    with open('DOANMAX.OUT', 'w') as out:
        out.write(str(tot) + '\n')

main()
