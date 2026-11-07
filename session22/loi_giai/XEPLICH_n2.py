# XEPLICH - QHD O(n^2): f[i] = max(f[i-1], p[i] + max f[j] voi viec j ket thuc truoc s[i]), duyet j tuyen tinh.
# Kip subtask 1-2 (n <= 5000); n = 2*10^5 qua gio. Bai hoc: mang e da sap -> tim j bang bisect.
def main():
    data = open('XEPLICH.INP', 'rb').read().split()
    n = int(data[0])
    viec = sorted((int(data[2 + 3 * i]), int(data[1 + 3 * i]), int(data[3 + 3 * i])) for i in range(n))
    f = [0] * (n + 1)
    for i in range(1, n + 1):
        ei, si, pi = viec[i - 1]
        j = i - 1
        while j > 0 and viec[j - 1][0] >= si:
            j -= 1
        f[i] = max(f[i - 1], pi + f[j])
    with open('XEPLICH.OUT', 'w') as fo:
        fo.write(str(f[n]) + '\n')

main()
