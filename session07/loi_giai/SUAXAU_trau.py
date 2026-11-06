# SUAXAU - vet can: de quy KHONG nho, xet ky tu cuoi; giong nhau thi bo ca hai (luon toi uu),
# khac nhau thi thu ca 3 phep. Toi da ~3^(n+m) loi goi: chi qua subtask 1 (n, m <= 6).
def main():
    data = open('SUAXAU.INP', 'rb').read().split()
    A, B = data[0], data[1]

    def g(i, j):                            # so phep bien A[:i] thanh B[:j]
        if i == 0:
            return j
        if j == 0:
            return i
        if A[i - 1] == B[j - 1]:
            return g(i - 1, j - 1)
        return 1 + min(g(i - 1, j - 1), g(i - 1, j), g(i, j - 1))

    with open('SUAXAU.OUT', 'w') as out:
        out.write(str(g(len(A), len(B))) + '\n')

main()
