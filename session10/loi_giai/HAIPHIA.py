# HAIPHIA: T bo test, moi bo la mot do thi vo huong. Hoi do thi co phai do thi HAI PHIA khong
# (to moi dinh mau 0 hoac 1 sao cho moi canh noi hai dinh KHAC mau). Tong n <= 2*10^5, tong m <= 2*10^5.
# Y tuong: DFS bang ngan xep, to dinh goc mau 0, dinh ke chua to thi to mau nguoc lai (1 - mau[u]);
# gap dinh ke DA TO trung mau voi u -> co chu trinh le -> KHONG hai phia.
# Phai lam cho TUNG thanh phan lien thong (moi thanh phan to doc lap).
# Bay hay gap: (1) quen RESET mang mau giua cac bo test (xem HAIPHIA_sai.py);
#              (2) gap mau thuan thi dung bo test do duoc, nhung con tro pos phai nhay qua du 2*m so
#                  cua bo test (o day nhay ngay luc doc, truoc khi giai).
# O(tong n + tong m).

def main():
    data = open('HAIPHIA.INP', 'rb').read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        a = list(map(int, data[pos + 2:pos + 2 + 2 * m]))
        pos += 2 + 2 * m
        ke = [[] for _ in range(n + 1)]
        for u, v in zip(a[0::2], a[1::2]):
            ke[u].append(v)
            ke[v].append(u)

        mau = [-1] * (n + 1)                   # TAO MOI cho moi bo test (-1 = chua to)
        ok = True
        for s in range(1, n + 1):
            if mau[s] != -1:
                continue
            mau[s] = 0
            st = [s]
            while st and ok:
                u = st.pop()
                khac = 1 - mau[u]
                for v in ke[u]:
                    if mau[v] == -1:
                        mau[v] = khac
                        st.append(v)
                    elif mau[v] != khac:       # cung mau voi u -> chu trinh le
                        ok = False
                        break
            if not ok:
                break
        out.append('YES' if ok else 'NO')

    with open('HAIPHIA.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
