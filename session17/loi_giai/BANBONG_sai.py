# BANBONG - SAI MO HINH: chon qua k bi ban DAU TIEN trong doan [l..r]; luc do hang xom cua k la k-1 va k+1
# (hoac qua ngoai doan l-1 / r+1), roi coi hai nua [l..k-1] va [k+1..r] la hai bai DOC LAP:
#   f[l][r] = max_k b[k-1] * b[k] * b[k+1] + f[l][k-1] + f[k+1][r]
# Sai vi sau khi ban k, qua k-1 va k+1 tro thanh KE NHAU: diem cua cac qua ban sau phu thuoc ca hai nua,
# ma f[l][k-1] lai tinh nhu the qua k van con o ben phai. Sua: chon qua bi ban CUOI CUNG (BANBONG.py).
def main():
    data = open('BANBONG.INP', 'rb').read().split()
    n = int(data[0])
    b = [1] + list(map(int, data[1:1 + n])) + [1]
    f = [[0] * (n + 2) for _ in range(n + 2)]
    for l in range(n, 0, -1):
        for r in range(l, n + 1):
            f[l][r] = max(b[k - 1] * b[k] * b[k + 1] + f[l][k - 1] + f[k + 1][r] for k in range(l, r + 1))
    with open('BANBONG.OUT', 'w') as out:
        out.write(str(f[1][n]) + '\n')

main()
