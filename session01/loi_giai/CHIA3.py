# CHIA3: in cac so chia het cho 3 theo thu tu nguoc, moi so mot dong; khong co thi in -1
def main():
    data = open('CHIA3.INP', 'rb').read().split()
    n = int(data[0])
    a = list(map(int, data[1:n + 1]))
    out = [str(x) for x in reversed(a) if x % 3 == 0]
    if not out:
        out = ['-1']
    with open('CHIA3.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')       # ghi mot lan

main()
