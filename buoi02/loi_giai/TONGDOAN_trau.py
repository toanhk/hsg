# TONGDOAN - vet can O(n*q): moi truy van cong lai tu dau. Chi qua subtask n, q <= 1000
def main():
    data = open('TONGDOAN.INP', 'rb').read().split()
    n, q = int(data[0]), int(data[1])
    a = [0] + list(map(int, data[2:2 + n]))      # danh so tu 1
    pos = 2 + n
    out = []
    for _ in range(q):
        l = int(data[pos]); r = int(data[pos + 1]); pos += 2
        tong = 0
        for i in range(l, r + 1):
            tong += a[i]
        out.append(str(tong))
    with open('TONGDOAN.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
