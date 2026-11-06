# HANGDOI - ban dung list: insert(0, x) va pop(0) ton O(n) -> cham khi Q lon
def main():
    data = open('HANGDOI.INP', 'rb').read().split()
    Q = int(data[0]); pos = 1
    a = []
    out = []
    for _ in range(Q):
        t = data[pos]; pos += 1
        if t == b'1':
            a.append(data[pos]); pos += 1
        elif t == b'2':
            a.insert(0, data[pos]); pos += 1
        elif t == b'3':
            out.append(a.pop(0) if a else b'-1')
        else:
            out.append(a.pop() if a else b'-1')
    with open('HANGDOI.OUT', 'wb') as f:
        f.write(b'\n'.join(out) + b'\n')

main()
