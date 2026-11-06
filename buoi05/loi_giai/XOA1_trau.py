# XOA1 - vet can O(n^3): thu "khong xoa" va xoa tung vi tri, voi moi day con lai tim doan tong lon nhat
# bang cach thu moi (l, r). n = 100 -> ~5*10^5 doan. Chi cho subtask 1.
def main():
    data = open('XOA1.INP', 'rb').read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    tot = a[0]
    for xoa in range(-1, n):            # -1: khong xoa
        b = a if xoa < 0 else a[:xoa] + a[xoa + 1:]
        for l in range(len(b)):
            s = 0
            for r in range(l, len(b)):
                s += b[r]
                if s > tot:
                    tot = s
    with open('XOA1.OUT', 'w') as out:
        out.write(str(tot) + '\n')

main()
