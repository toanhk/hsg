# DEMKHOANG - vet can O(n*q). Chi qua subtask n, q <= 1000
def main():
    data = open('DEMKHOANG.INP', 'rb').read().split()
    n, q = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + n]))
    pos = 2 + n
    out = []
    for _ in range(q):
        L = int(data[pos]); R = int(data[pos + 1]); pos += 2
        dem = 0
        for x in a:
            if L <= x <= R:
                dem += 1
        out.append(str(dem))
    with open('DEMKHOANG.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
