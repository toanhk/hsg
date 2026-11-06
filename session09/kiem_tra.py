# KIEM TRA cho bai co nhieu dap an dung. Moi ham nhan (input, dap_an_mau, output_hoc_sinh) dang chuoi,
# tra ve True/False. cham_thu.py tu goi ham trung ten bai.

def LOTRINH(inp, dap_an, ra):
    a = inp.split()
    n, m = int(a[0]), int(a[1])
    k = int(dap_an.split()[0])
    try:
        b = list(map(int, ra.split()))
    except ValueError:
        return False
    if not b or b[0] != k:
        return False                       # sai so duong it nhat
    if k < 0:
        return len(b) == 1
    duong = b[1:]
    if len(duong) != k + 1 or duong[0] != 1 or duong[-1] != n:
        return False
    canh = set()
    for i in range(m):
        canh.add((int(a[2 + 2 * i]), int(a[3 + 2 * i])))
    return all((duong[i], duong[i + 1]) in canh for i in range(k))   # moi buoc phai la duong MOT CHIEU co that
