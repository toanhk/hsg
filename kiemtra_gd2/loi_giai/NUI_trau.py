# NUI - vet can: thu moi tap cay giu lai (2^n), kiem tra dang nui. Subtask 1 (n <= 15).
def la_nui(d):
    i = 1
    while i < len(d) and d[i - 1] < d[i]:
        i += 1
    while i < len(d) and d[i - 1] > d[i]:
        i += 1
    return i == len(d)

def main():
    data = open('NUI.INP', 'rb').read().split()
    n = int(data[0])
    h = list(map(int, data[1:1 + n]))
    best = 0
    for mask in range(1, 1 << n):
        d = [h[i] for i in range(n) if mask >> i & 1]
        if len(d) > best and la_nui(d):
            best = len(d)
    with open('NUI.OUT', 'w') as f:
        f.write(str(n - best) + '\n')

main()
