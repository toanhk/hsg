# DEMXAU - QHD hai chieu O(n*k): trang thai (do dai, so so 1 lien tiep o cuoi)
#   g[t] = so xau hop le do dai i ket thuc bang dung t so 1 (0 <= t <= k-1)
#   them '0' -> ve t = 0 ; them '1' -> t + 1 (chi khi t + 1 < k)
# De nghi ra hon, nhung n = 10^6, k = 10^6 thi qua cham. Qua subtask 1, 2 (n <= 5000).
MOD = 10**9 + 7

def main():
    data = open('DEMXAU.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    g = [0] * k
    g[0] = 1                            # xau rong: 0 so 1 o cuoi
    for _ in range(n):
        # them '0' vao bat ky xau nao -> t = 0 ; them '1' -> moi o t dich sang t + 1 (o k-1 bi bo)
        g = [sum(g) % MOD] + g[:-1]     # cat/ghep list chay trong C, nhanh hon vong for nhieu
    with open('DEMXAU.OUT', 'w') as out:
        out.write(str(sum(g) % MOD) + '\n')

main()
