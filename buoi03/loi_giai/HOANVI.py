# HOANVI: liet ke cac hoan vi KHAC NHAU cua xau S (co the lap ky tu), thu tu tu dien
# Quay lui tren mang dem: o moi vi tri thu tung ky tu (theo thu tu a..z) con so luong > 0
# -> khong bao gio sinh trung, khong can set, va ra san thu tu tu dien
def main():
    data = open('HOANVI.INP', 'rb').read().split()
    s = data[0].decode()
    n = len(s)
    chu = sorted(set(s))                 # cac ky tu khac nhau, tang dan
    con = [s.count(c) for c in chu]      # con[t] = so ky tu chu[t] chua dung
    m = len(chu)
    x = [''] * n
    kq = []

    def thu(i):
        if i == n:
            kq.append(''.join(x))
            return
        for t in range(m):
            if con[t]:
                con[t] -= 1; x[i] = chu[t]
                thu(i + 1)
                con[t] += 1              # tra lai (quen dong nay la loi hay gap nhat)

    thu(0)
    with open('HOANVI.OUT', 'w') as f:
        f.write(str(len(kq)) + '\n' + '\n'.join(kq) + '\n')

main()
