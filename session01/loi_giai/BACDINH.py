# BACDINH: bac cua moi dinh va dinh co bac lon nhat (chi so nho nhat neu bang nhau)
def main():
    data = open('BACDINH.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    e = list(map(int, data[2:2 + 2 * m]))
    deg = [0] * (n + 1)
    for x in e:                 # moi dau mut cua canh cong 1 bac
        deg[x] += 1
    best = 1
    for v in range(2, n + 1):
        if deg[v] > deg[best]:
            best = v
    with open('BACDINH.OUT', 'w') as f:
        f.write(' '.join(map(str, deg[1:])) + '\n' + str(best) + '\n')

main()
