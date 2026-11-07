# KIEM TRA cho bai co nhieu dap an dung. Moi ham nhan (input, dap_an_mau, output_hoc_sinh) dang chuoi,
# tra ve True/False. cham_thu.py tu goi ham trung ten bai.

def HANHTRINH(inp, dap_an, ra):
    """Dung neu: cung do dai D voi dap an mau, duong di bat dau o 1, ket thuc o n, moi buoc la mot canh
    co that, va tong trong so (lay canh nho nhat giua hai dinh neu co canh trung) dung bang D."""
    a = inp.split()
    n, m = int(a[0]), int(a[1])
    mau = dap_an.split()
    b = ra.split()
    if mau == ['-1']:
        return b == ['-1']
    try:
        D = int(b[0]); k = int(b[1]); p = list(map(int, b[2:]))
    except (ValueError, IndexError):
        return False
    if D != int(mau[0]) or k != len(p) or k < 1 or p[0] != 1 or p[-1] != n:
        return False
    w = {}
    for i in range(m):
        u, v, c = int(a[2 + 3 * i]), int(a[3 + 3 * i]), int(a[4 + 3 * i])
        if u > v: u, v = v, u
        if c < w.get((u, v), 1 << 62):
            w[(u, v)] = c
    tong = 0
    for x, y in zip(p, p[1:]):
        e = (x, y) if x < y else (y, x)
        if e not in w:
            return False
        tong += w[e]
    return tong == D
