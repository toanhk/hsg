# SONHANG - son XUOI bang gan lat cat: mau[l:r+1] = [c] * (r - l + 1). Gan lat cat chay bang C nen
# nhanh, nhung tong do dai cac doan co the toi q * n = 10^11 -> chi qua subtask 1-2.

def main():
    data = open('SONHANG.INP', 'rb').read().split()
    n, q = int(data[0]), int(data[1])
    mau = [0] * (n + 1)
    for t in range(2, 2 + 3 * q, 3):
        l, r = int(data[t]), int(data[t + 1])
        mau[l:r + 1] = [int(data[t + 2])] * (r - l + 1)
    with open('SONHANG.OUT', 'w') as f:
        f.write(' '.join(map(str, mau[1:])) + '\n')

main()
