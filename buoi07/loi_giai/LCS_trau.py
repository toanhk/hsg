# LCS - vet can: thu moi tap con cua A (2^n), kiem tra co la day con cua B khong
# Chi qua subtask 1 (|A| <= 15)
def la_day_con(s, B):
    it = iter(B)
    return all(ch in it for ch in s)        # 'ch in it' tieu thu iterator -> giu dung thu tu

def main():
    data = open('LCS.INP', 'rb').read().split()
    A, B = data[0].decode(), data[1].decode()
    n = len(A)
    tot = 0
    for mask in range(1 << n):
        s = [A[i] for i in range(n) if mask >> i & 1]
        if len(s) > tot and la_day_con(s, B):
            tot = len(s)
    with open('LCS.OUT', 'w') as out:
        out.write(str(tot) + '\n')

main()
