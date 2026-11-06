# SUAXAU - bang 2 chieu theo dung cong thuc, kem truy vet day phep bien doi (in ra man hinh khi n nho)
# Qua subtask 1, 2; subtask 3 cham hon SUAXAU.py ~2 lan.
import sys

def main():
    data = open('SUAXAU.INP', 'rb').read().split()
    A, B = data[0].decode(), data[1].decode()
    n, m = len(A), len(B)
    f = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        f[i][0] = i
    for j in range(m + 1):
        f[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                f[i][j] = f[i - 1][j - 1]
            else:
                f[i][j] = 1 + min(f[i - 1][j - 1], f[i - 1][j], f[i][j - 1])
    with open('SUAXAU.OUT', 'w') as out:
        out.write(str(f[n][m]) + '\n')
    if n + m <= 30:                          # truy vet tu (n, m) ve (0, 0), in ra stderr
        i, j, buoc = n, m, []
        while i or j:
            if i and j and A[i - 1] == B[j - 1] and f[i][j] == f[i - 1][j - 1]:
                i, j = i - 1, j - 1
            elif i and j and f[i][j] == f[i - 1][j - 1] + 1:
                buoc.append(f'thay {A[i - 1]} -> {B[j - 1]} (vi tri {i})'); i, j = i - 1, j - 1
            elif i and f[i][j] == f[i - 1][j] + 1:
                buoc.append(f'xoa {A[i - 1]} (vi tri {i})'); i -= 1
            else:
                buoc.append(f'chen {B[j - 1]} (sau vi tri {i})'); j -= 1
        sys.stderr.write('\n'.join(reversed(buoc)) + '\n')

main()
