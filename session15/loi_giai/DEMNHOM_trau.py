# DEMNHOM - vet can: sau moi cay cau, DFS lai toan bo do thi de dem thanh phan lien thong.
# O(m * (n + m)).

def main():
    data = open('DEMNHOM.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    ke = [[] for _ in range(n + 1)]
    out = []
    for i in range(2, 2 + 2 * m, 2):
        u, v = int(data[i]), int(data[i + 1])
        ke[u].append(v); ke[v].append(u)
        tham = [False] * (n + 1)
        nhom = lon = 0
        for s in range(1, n + 1):
            if tham[s]:
                continue
            nhom += 1
            tham[s] = True
            st = [s]; c = 0
            while st:
                x = st.pop(); c += 1
                for y in ke[x]:
                    if not tham[y]:
                        tham[y] = True; st.append(y)
            lon = max(lon, c)
        out.append(f'{nhom} {lon}')
    with open('DEMNHOM.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
