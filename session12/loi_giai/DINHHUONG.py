# DINHHUONG: n dinh, m canh; canh "1 u v" la cung CO HUONG u -> v, canh "0 u v" la canh VO HUONG.
# Dinh huong moi canh vo huong (giu u -> v hoac doi thanh v -> u) sao cho do thi KHONG co chu trinh.
# In -1 neu khong the; nguoc lai in mot xau gom k ky tu (k = so canh vo huong, theo thu tu input):
# '0' = giu u -> v, '1' = doi thanh v -> u. Nhieu dap an -> in cach nao cung duoc. n, m <= 2*10^5
# Y tuong: chi cac cung co huong moi co the tao chu trinh "bat buoc". Neu phan co huong khong co chu
#   trinh, lay mot thu tu to-po vt[]. Huong moi canh vo huong tu dinh dung TRUOC sang dinh dung SAU
#   trong thu tu do -> moi cung (cu va moi) deu di "tien" trong thu tu -> khong the quay vong.
# Phan co huong co chu trinh -> -1 (dinh huong the nao chu trinh do van con).  O(n + m)
def main():
    data = open('DINHHUONG.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    vo = []                                   # cac canh vo huong (u, v) theo thu tu input
    for i in range(2, 2 + 3 * m, 3):
        u = int(data[i + 1]); v = int(data[i + 2])
        if data[i] == b'1':
            adj[u].append(v); deg[v] += 1
        else:
            vo.append((u, v))
    q = [u for u in range(1, n + 1) if deg[u] == 0]
    for u in q:
        for v in adj[u]:
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    if len(q) < n:
        out = '-1'
    else:
        vt = [0] * (n + 1)
        for i, u in enumerate(q):
            vt[u] = i
        out = ''.join('0' if vt[u] < vt[v] else '1' for u, v in vo)
    with open('DINHHUONG.OUT', 'w') as f:
        f.write(out + '\n')

main()
