# DAYNGOAC - SAI: chi xet ghep S[l] voi S[r] (hai dau doan), KHONG tach doan:
#   f[l][r] = f[l+1][r-1] neu S[l], S[r] la mot cap; nguoc lai 1 + min(f[l+1][r], f[l][r-1])
# Cong thuc nay dung cho "xau doi xung" nhung sai voi ngoac: "()()" ghep S[0] voi S[3] khong duoc,
# tra ve 2 thay vi 0. Phai them truong hop TACH: S[l] ghep voi S[k] o giua.
def main():
    data = open('DAYNGOAC.INP', 'rb').read().split()
    S = data[0].decode()
    n = len(S)
    f = [[0] * (n + 1) for _ in range(n + 1)]
    for l in range(n - 1, -1, -1):
        f[l][l] = 1
        for r in range(l + 1, n):
            if S[l] + S[r] in ('()', '[]'):
                f[l][r] = f[l + 1][r - 1] if r - l > 1 else 0
            else:
                f[l][r] = 1 + min(f[l + 1][r], f[l][r - 1])
    with open('DAYNGOAC.OUT', 'w') as out:
        out.write(str(f[0][n - 1]) + '\n')

main()
