# CHUTRINH - ban SAI de chua tren lop: "thay chu trinh la dung DFS luon cho nhanh".
# Loi: dung giua chung thi phan con lai cua thanh phan CHUA duoc danh dau tham. Vong for ben
# ngoai se gap lai chung va tuong do la thanh phan MOI -> mot thanh phan bi dem nhieu lan.
# Bai hoc: DFS dem thanh phan phai tham HET thanh phan, ke ca khi da biet dap an cua no.
# Thu tay: canh 1-2, 2-3, 3-1, 3-4 -> dap an 1, ban nay in 2 (dinh 4 bi bo lai, sau do canh 4-3
# bi coi la chu trinh vi cha[4] = 0). Nhung K4 (6 canh) thi van ra dung 1: test ngau nhien moi bat duoc.

def main():
    data = open('CHUTRINH.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + 2 * m]))
    ke = [[] for _ in range(n + 1)]
    for u, v in zip(a[0::2], a[1::2]):
        ke[u].append(v)
        ke[v].append(u)
    tham = [False] * (n + 1)
    cha = [0] * (n + 1)
    dem = 0
    for s in range(1, n + 1):
        if tham[s]:
            continue
        tham[s] = True
        st = [s]
        co = False
        while st and not co:                   # SAI: dung ngay khi thay chu trinh
            u = st.pop()
            for v in ke[u]:
                if not tham[v]:
                    tham[v] = True
                    cha[v] = u
                    st.append(v)
                elif v != cha[u]:
                    co = True
                    break
        dem += co
    with open('CHUTRINH.OUT', 'w') as out:
        out.write(str(dem) + '\n')

main()
