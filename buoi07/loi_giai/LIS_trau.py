# LIS - vet can: quay lui, moi phan tu chon hoac bo, chi chon khi lon hon phan tu da chon cuoi cung
# Toi da 2^n nhanh: chi qua subtask 1 (n <= 20)
def main():
    data = open('LIS.INP', 'rb').read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    tot = 0
    # ngan xep tuong minh: (vi tri dang xet, phan tu cuoi da chon, do dai)
    st = [(0, None, 0)]
    while st:
        i, cuoi, dai = st.pop()
        if i == n:
            if dai > tot:
                tot = dai
            continue
        st.append((i + 1, cuoi, dai))                     # bo a[i]
        if cuoi is None or a[i] > cuoi:
            st.append((i + 1, a[i], dai + 1))             # chon a[i]
    with open('LIS.OUT', 'w') as out:
        out.write(str(tot) + '\n')

main()
