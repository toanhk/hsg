# MAXMIN: nhieu bo test, moi bo in max - min. Tong n <= 10^6
def main():
    data = open('MAXMIN.INP', 'rb').read().split()
    t = int(data[0]); pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos]); pos += 1
        a = list(map(int, data[pos:pos + n])); pos += n
        out.append(str(max(a) - min(a)))
    with open('MAXMIN.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
