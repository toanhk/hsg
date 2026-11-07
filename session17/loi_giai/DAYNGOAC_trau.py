# DAYNGOAC - vet can (|S| <= 16): so ky tu phai chen = |S| - (do dai day con DUNG dai nhat cua S)
# (giu lai day con dung, moi ky tu bi bo thi chen ban ghep cua no ngay canh). Thu moi day con: 2^n.
def dung(t):
    st = []
    for c in t:
        if c in '([':
            st.append(c)
        elif not st or st.pop() != ('(' if c == ')' else '['):
            return False
    return not st

def main():
    data = open('DAYNGOAC.INP', 'rb').read().split()
    S = data[0].decode()
    n = len(S)
    best = 0
    for mask in range(1 << n):
        t = [S[i] for i in range(n) if mask >> i & 1]
        if len(t) > best and dung(t):
            best = len(t)
    with open('DAYNGOAC.OUT', 'w') as out:
        out.write(str(n - best) + '\n')

main()
