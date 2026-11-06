# COPHIEU - vet can O(n^2): thu moi cap (ngay mua i, ngay ban j > i). Qua subtask 1 (n <= 1000).
def main():
    data = open('COPHIEU.INP', 'rb').read().split()
    n = int(data[0])
    p = list(map(int, data[1:1 + n]))
    tot = 0
    for i in range(n):
        for j in range(i + 1, n):
            if p[j] - p[i] > tot:
                tot = p[j] - p[i]
    with open('COPHIEU.OUT', 'w') as out:
        out.write(str(tot) + '\n')

main()
