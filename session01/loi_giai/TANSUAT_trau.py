# TANSUAT - vet can O(n*q): chi qua subtask n, q <= 1000
def main():
    data = open('TANSUAT.INP', 'rb').read().split()
    n, q = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + n]))
    out = []
    for x in map(int, data[2 + n:2 + n + q]):
        out.append(str(a.count(x)))
    with open('TANSUAT.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
