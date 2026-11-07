# SEQ - vet can O(n * Q): moi truy van quet day, dem doan lien tiep <= K.
def main():
    data = open('SEQ.INP', 'rb').read().split()
    n, q = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + n]))
    out = []
    for t in range(q):
        k = int(data[2 + n + t])
        best = cur = 0
        for x in a:
            if x <= k:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        out.append(best)
    with open('SEQ.OUT', 'w') as f:
        f.write('\n'.join(map(str, out)) + '\n')

main()
