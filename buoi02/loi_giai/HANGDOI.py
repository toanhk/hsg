# HANGDOI: mo phong hang doi hai dau. Q <= 10^6 lenh. deque: moi lenh O(1)
from collections import deque

def main():
    data = open('HANGDOI.INP', 'rb').read().split()
    Q = int(data[0]); pos = 1
    dq = deque()
    out = []
    for _ in range(Q):
        t = data[pos]; pos += 1          # so sanh bytes, khong can doi sang int
        if t == b'1':                    # 1 x: them x vao cuoi
            dq.append(data[pos]); pos += 1     # giu nguyen bytes, khoi int/str
        elif t == b'2':                  # 2 x: them x vao dau
            dq.appendleft(data[pos]); pos += 1
        elif t == b'3':                  # 3: lay ra o dau
            out.append(dq.popleft() if dq else b'-1')
        else:                            # 4: lay ra o cuoi
            out.append(dq.pop() if dq else b'-1')
    with open('HANGDOI.OUT', 'wb') as f:
        f.write(b'\n'.join(out) + b'\n')

main()
