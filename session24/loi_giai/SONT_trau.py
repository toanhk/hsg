# SONT - vet can: chia thu tung so trong doan (subtask 1: R <= 1000, Q <= 100).
def la_nt(x):
    if x < 2:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

def main():
    data = open('SONT.INP', 'rb').read().split()
    q = int(data[0])
    out = []
    for k in range(q):
        L, R = int(data[1 + 2 * k]), int(data[2 + 2 * k])
        out.append(sum(la_nt(x) for x in range(L, R + 1)))
    with open('SONT.OUT', 'w') as f:
        f.write('\n'.join(map(str, out)) + '\n')

main()
