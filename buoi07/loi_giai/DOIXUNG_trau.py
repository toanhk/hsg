# DOIXUNG - vet can: thu moi tap con ky tu (2^n), giu cac xau doi xung. Subtask 1 (n <= 15).
def main():
    data = open('DOIXUNG.INP', 'rb').read().split()
    S = data[0].decode()
    n = len(S)
    tot = 0
    for mask in range(1, 1 << n):
        t = [S[i] for i in range(n) if mask >> i & 1]
        if len(t) > tot and t == t[::-1]:
            tot = len(t)
    with open('DOIXUNG.OUT', 'w') as out:
        out.write(str(tot) + '\n')

main()
