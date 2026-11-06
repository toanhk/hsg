# XEPHANG: n doi, m ket qua "u v" nghia la doi u xep TREN doi v. In bang xep hang (n so, tu cao xuong
# thap) neu no duoc xac dinh DUY NHAT; in 0 neu co nhieu hon mot bang hop le; in -1 neu cac ket qua mau
# thuan (khong co bang nao).  n <= 10^5, m <= 2*10^5
# Mo hinh: cung u -> v. Bang xep hang hop le = thu tu to-po.
#   - Kahn khong lay du n doi -> co chu trinh -> -1.
#   - Thu tu DUY NHAT <=> moi luc hang doi co DUNG MOT doi. Neu co luc 2 doi cung bac vao 0 thi hai doi
#     do doi cho cho nhau van hop le -> nhieu bang. (Tuong duong: moi cap ke nhau trong thu tu deu co cung.)
# Chu y: thay mot luc co >= 2 doi chua duoc ket luan 0 ngay - phai chay Kahn het de con biet co -1 khong.
def main():
    data = open('XEPHANG.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    for i in range(2, 2 + 2 * m, 2):
        u = int(data[i]); v = int(data[i + 1])
        adj[u].append(v); deg[v] += 1
    q = [u for u in range(1, n + 1) if deg[u] == 0]
    duy_nhat = True
    dau = 0                                  # q[dau:] la phan "dang cho" cua hang doi
    while dau < len(q):
        if len(q) - dau > 1:
            duy_nhat = False
        u = q[dau]; dau += 1
        for v in adj[u]:
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    with open('XEPHANG.OUT', 'w') as f:
        if len(q) < n:
            f.write('-1\n')
        elif not duy_nhat:
            f.write('0\n')
        else:
            f.write(' '.join(map(str, q)) + '\n')

main()
