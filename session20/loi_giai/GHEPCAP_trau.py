# GHEPCAP - vet can (n <= 12): quay lui, ban chua xep nho nhat ghep voi tung ban con lai.
# So cach xep = (n-1)!! (n = 12: 10395 cach). Ngan xep thay de quy.
def main():
    data = open('GHEPCAP.INP', 'rb').read().split()
    n = int(data[0])
    a = [list(map(int, data[1 + i * n:1 + (i + 1) * n])) for i in range(n)]
    best = 0
    st = [(tuple(range(n)), 0)]               # (cac ban con lai, tong hien tai)
    while st:
        con, t = st.pop()
        if not con:
            best = max(best, t)
            continue
        i = con[0]
        for k in range(1, len(con)):
            st.append((con[1:k] + con[k + 1:], t + a[i][con[k]]))
    with open('GHEPCAP.OUT', 'w') as f:
        f.write(str(best) + '\n')

main()
