# KHONGKE - vet can: quay lui, tai moi vi tri chon (roi nhay qua o ke) hoac bo qua.
# So tap hop le ~ Fibonacci(n+2): n = 20 -> 17711 tap, n = 60 -> 4*10^12. Chi cho subtask 1.
def main():
    data = open('KHONGKE.INP', 'rb').read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    tot = 0

    def thu(i, tong):                   # da quyet dinh xong a[0..i-1]
        nonlocal tot
        if i >= n:
            if tong > tot:
                tot = tong
            return
        thu(i + 1, tong)                # bo a[i]
        thu(i + 2, tong + a[i])         # chon a[i], bat buoc bo a[i+1]

    thu(0, 0)
    with open('KHONGKE.OUT', 'w') as out:
        out.write(str(tot) + '\n')

main()
