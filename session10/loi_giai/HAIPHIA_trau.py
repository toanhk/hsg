# HAIPHIA - vet can: thu moi cach to 2^n mau, kiem tra tung canh. O(2^n * m): n <= 15 (subtask 1).

def main():
    data = open('HAIPHIA.INP', 'rb').read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        canh = [(int(data[pos + 2 + 2 * i]) - 1, int(data[pos + 3 + 2 * i]) - 1) for i in range(m)]
        pos += 2 + 2 * m
        ok = False
        for mask in range(1 << n):             # bit u cua mask = mau cua dinh u
            if all((mask >> u & 1) != (mask >> v & 1) for u, v in canh):
                ok = True
                break
        out.append('YES' if ok else 'NO')
    with open('HAIPHIA.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
