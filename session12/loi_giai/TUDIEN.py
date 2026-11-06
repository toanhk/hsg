# TUDIEN: n tu (chu thuong) da duoc sap xep theo mot bang chu cai LA. Tim thu tu cac chu cai CO MAT
# trong cac tu, phu hop voi viec sap xep; nhieu thu tu dung -> in thu tu nho nhat theo bang chu cai
# thuong (a < b < ...). Khong co thu tu nao -> in -1.  n <= 10^5, tong do dai <= 10^6
# Mo hinh: dinh = chu cai (<= 26). Hai tu KE NHAU w1, w2: o vi tri dau tien khac nhau c1 != c2 ->
#   cung c1 -> c2. Khong co vi tri khac va len(w1) > len(w2) (vi du "abc" dung truoc "ab") -> -1.
# Chi so sanh cac cap KE NHAU la du (thu tu tu dien co tinh bac cau).
# To-po nho nhat theo tu dien: Kahn voi heapq (luon lay chu nho nhat dang co bac vao 0).
import heapq

def main():
    data = open('TUDIEN.INP', 'rb').read().split()
    n = int(data[0])
    w = data[1:1 + n]                          # moi tu la bytes: duyet ra so 97..122
    co = [False] * 26
    for x in set(b''.join(w)):
        co[x - 97] = True
    ke = [set() for _ in range(26)]
    sai = False
    for i in range(n - 1):
        a, b = w[i], w[i + 1]
        for x, y in zip(a, b):
            if x != y:
                ke[x - 97].add(y - 97)          # set: cung trung chi tinh mot lan
                break
        else:
            if len(a) > len(b):
                sai = True
                break
    out = '-1'
    if not sai:
        deg = [0] * 26
        for u in range(26):
            for v in ke[u]:
                deg[v] += 1
        h = [u for u in range(26) if co[u] and deg[u] == 0]
        heapq.heapify(h)
        kq = []
        while h:
            u = heapq.heappop(h); kq.append(chr(97 + u))
            for v in ke[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    heapq.heappush(h, v)
        if len(kq) == sum(co):
            out = ''.join(kq)
    with open('TUDIEN.OUT', 'w') as f:
        f.write(out + '\n')

main()
