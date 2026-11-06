# HAIPHIA - ban SAI de chua tren lop: QUEN RESET giua cac bo test.
# Hoc sinh tao mang mau MOT lan (du lon cho moi bo test) o ngoai vong lap bo test.
# Bo test sau thay mau cu cua bo truoc, tuong dinh "da to" -> bo qua hoac bao mau thuan sai.
# Test nho bat loi: 2 bo test; bo 1: canh 1-2; bo 2: canh 1-3, 3-2 ... (mau cu: 1->0, 2->1;
# bo 2 to 3 mau 1 tu dinh 1, roi 2 mau cu 1 trung mau 3 -> NO, trong khi dap an YES).

def main():
    data = open('HAIPHIA.INP', 'rb').read().split()
    t = int(data[0])
    pos = 1
    out = []
    mau = [-1] * (2 * 10**5 + 1)               # SAI: chi tao mot lan cho moi bo test
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        a = list(map(int, data[pos + 2:pos + 2 + 2 * m]))
        pos += 2 + 2 * m
        ke = [[] for _ in range(n + 1)]
        for u, v in zip(a[0::2], a[1::2]):
            ke[u].append(v)
            ke[v].append(u)
        ok = True
        for s in range(1, n + 1):
            if mau[s] != -1:
                continue
            mau[s] = 0
            st = [s]
            while st and ok:
                u = st.pop()
                for v in ke[u]:
                    if mau[v] == -1:
                        mau[v] = 1 - mau[u]
                        st.append(v)
                    elif mau[v] == mau[u]:
                        ok = False
                        break
            if not ok:
                break
        out.append('YES' if ok else 'NO')
    with open('HAIPHIA.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
