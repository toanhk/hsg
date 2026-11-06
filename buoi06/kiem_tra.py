# KIEM TRA cho bai co nhieu dap an dung. Moi ham nhan (input, dap_an_mau, output_hoc_sinh) dang chuoi,
# tra ve True/False. cham_thu.py tu goi ham trung ten bai.

def TRUYVET(inp, dap_an, ra):
    a = inp.split()
    n, W = int(a[0]), int(a[1])
    w = [int(a[2 + 2 * i]) for i in range(n)]
    v = [int(a[3 + 2 * i]) for i in range(n)]
    tot_nhat = int(dap_an.split()[0])
    try:
        b = list(map(int, ra.split()))
        gt, k, chon = b[0], b[1], b[2:]
    except (ValueError, IndexError):
        return False
    if gt != tot_nhat or k != len(chon) or len(set(chon)) != k:
        return False                       # sai gia tri, sai so luong, hoac lap vat
    if any(not 1 <= i <= n for i in chon):
        return False
    if sum(w[i - 1] for i in chon) > W:
        return False                       # qua tai
    return sum(v[i - 1] for i in chon) == gt   # tap in ra phai dat dung gia tri da khai
