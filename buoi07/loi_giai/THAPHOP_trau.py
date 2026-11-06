# THAPHOP - vet can (n <= 10): thu moi tap con, thu xoay tung hop, kiem tra xep thanh thap duoc khong.
# Mot tap xep duoc <=> sap theo dien tich roi moi hop lien tiep long vao nhau (thu ca 2 cach xoay).
def vua(X, Y):                              # X dat len Y duoc khong (thu 2 cach xoay X)
    return (X[0] < Y[0] and X[1] < Y[1]) or (X[1] < Y[0] and X[0] < Y[1])

def main():
    data = open('THAPHOP.INP', 'rb').read().split()
    n = int(data[0])
    hop = [(int(data[1 + 2 * i]), int(data[2 + 2 * i])) for i in range(n)]
    tot = 0
    for mask in range(1, 1 << n):
        t = sorted((hop[i] for i in range(n) if mask >> i & 1), key=lambda h: h[0] * h[1])
        if len(t) > tot and all(vua(t[i], t[i + 1]) for i in range(len(t) - 1)):
            tot = len(t)
    with open('THAPHOP.OUT', 'w') as out:
        out.write(str(tot) + '\n')

main()
