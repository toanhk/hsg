# KIEM TRA cho bai co nhieu dap an dung. Moi ham nhan (input, dap_an_mau, output_hoc_sinh) dang chuoi,
# tra ve True/False. cham_thu.py tu goi ham trung ten bai.
# Dap an mau chi dung de biet "co / khong co loi giai" (-1 hay khong); phan con lai kiem tra truc tiep.

def _canh(a, m, buoc=2, dau=2):
    return [tuple(int(x) for x in a[dau + buoc * i: dau + buoc * (i + 1)]) for i in range(m)]

def _khong_vong(n, cung):
    """Kahn: True neu do thi co huong (n dinh, danh sach cung) khong co chu trinh."""
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    for u, v in cung:
        adj[u].append(v); deg[v] += 1
    q = [u for u in range(1, n + 1) if deg[u] == 0]
    for u in q:
        for v in adj[u]:
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    return len(q) == n

def MONHOC(inp, dap_an, ra):
    a = inp.split()
    n, m = int(a[0]), int(a[1])
    b = ra.split()
    if dap_an.split() == ['-1']:
        return b == ['-1']
    try:
        p = list(map(int, b))
    except ValueError:
        return False
    if len(p) != n or sorted(p) != list(range(1, n + 1)):
        return False                       # phai la mot hoan vi cua 1..n
    vt = [0] * (n + 1)
    for i, x in enumerate(p):
        vt[x] = i
    return all(vt[u] < vt[v] for u, v in _canh(a, m))

def CHUTRINH(inp, dap_an, ra):
    a = inp.split()
    n, m = int(a[0]), int(a[1])
    b = ra.split()
    if dap_an.split() == ['-1']:
        return b == ['-1']
    try:
        k = int(b[0]); ct = list(map(int, b[1:]))
    except (ValueError, IndexError):
        return False
    if k < 1 or len(ct) != k or len(set(ct)) != k or any(not 1 <= x <= n for x in ct):
        return False
    co = set(_canh(a, m))
    return all((ct[i], ct[(i + 1) % k]) in co for i in range(k))

def DINHHUONG(inp, dap_an, ra):
    a = inp.split()
    n, m = int(a[0]), int(a[1])
    b = ra.split()
    if dap_an.split() == ['-1']:
        return b == ['-1']
    cung, vo = [], []
    for t, u, v in _canh(a, m, 3):
        (cung if t == 1 else vo).append((u, v))
    s = b[0] if b else ''
    if len(b) > 1 or len(s) != len(vo) or any(c not in '01' for c in s):
        return False
    cung += [(v, u) if c == '1' else (u, v) for c, (u, v) in zip(s, vo)]
    return _khong_vong(n, cung)
