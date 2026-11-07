# SOAT BAI truoc khi nop (buoi 23): bat cac loi "mat diem oan" hay gap nhat MA KHONG CAN biet thuat toan.
#   - sai ten file chuong trinh (TONGCON.py, khong phai tongcon.py / TongCon.py / TONGCON (1).py)
#   - doc/ghi sai ten file du lieu (phai dung 'TONGCON.INP' / 'TONGCON.OUT', viet HOA, dung duoi)
#   - dung input()/print() ra man hinh thay vi doc/ghi file
#   - ham de quy (de tran ngan xep Python voi n lon), thieu main()
#   - chay thu tren test vi du (test/BAI/Test01): co tao file .OUT khong, dung khong, mat bao lau
# Chay:  python soat_bai.py               -> soat thu muc bai_lam/ voi cac bai co trong test/
#        python soat_bai.py loi_giai       -> soat thu muc khac (vi du loi giai mau)
import ast, os, shutil, subprocess, sys, tempfile, time

def de_quy(cay):
    """Tra ve ten cac ham tu goi chinh no (de quy truc tiep)."""
    ten = []
    for nut in ast.walk(cay):
        if isinstance(nut, ast.FunctionDef):
            for con in ast.walk(nut):
                if isinstance(con, ast.Call) and isinstance(con.func, ast.Name) and con.func.id == nut.name:
                    ten.append(nut.name); break
    return ten

def soat(thu_muc, bai):
    print(f'=== {bai}')
    file = os.path.join(thu_muc, bai + '.py')
    if not os.path.exists(file):
        gan = [f for f in os.listdir(thu_muc) if f.lower().startswith(bai.lower())]
        print(f'  [LOI] Khong co file {bai}.py' + (f' (co: {", ".join(gan)} -> doi ten cho dung!)' if gan else ''))
        return
    src = open(file, encoding='utf-8', errors='replace').read()
    canh_bao = []
    for duoi in ('.INP', '.OUT'):
        if f"'{bai}{duoi}'" not in src and f'"{bai}{duoi}"' not in src:
            canh_bao.append(f'[LOI] Khong thay chuoi "{bai}{duoi}" dung chinh ta (viet hoa, dung ten bai)')
    for sai in (bai.lower() + '.inp', bai.lower() + '.out', bai + '.IN"', bai + '.TXT'):
        if sai in src:
            canh_bao.append(f'[LOI] Co ten file sai "{sai}"')
    try:
        cay = ast.parse(src)
    except SyntaxError as e:
        print(f'  [LOI] Loi cu phap dong {e.lineno}: {e.msg}')
        return
    goi = {n.func.id for n in ast.walk(cay) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}
    if 'input' in goi:
        canh_bao.append('[CANH BAO] Dung input(): de doc file phai dung open(...).read(); input() doc ban phim va cham')
    if 'print' in goi and f'{bai}.OUT' not in src:
        canh_bao.append('[LOI] Chi print() ra man hinh, khong ghi file .OUT')
    for f in de_quy(cay):
        canh_bao.append(f'[CANH BAO] Ham {f}() de quy: n lon co the tran ngan xep / cham -> viet bang vong lap')
    if not any(isinstance(n, ast.FunctionDef) and n.name == 'main' for n in cay.body):
        canh_bao.append('[GOI Y] Khong co main(): code o muc module cham hon ~2 lan')
    for c in canh_bao:
        print('  ' + c)
    vd = os.path.join('test', bai, 'Test01')
    if not os.path.isdir(vd):
        return
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copy(os.path.join(vd, bai + '.INP'), tmp)
        t0 = time.perf_counter()
        try:
            r = subprocess.run([sys.executable, os.path.abspath(file)], cwd=tmp, timeout=5, stdin=subprocess.DEVNULL,
                               capture_output=True, text=True)
        except subprocess.TimeoutExpired:
            print('  [LOI] Chay vi du qua 5 giay (dang cho doc ban phim? vong lap vo han?)')
            return
        tg = time.perf_counter() - t0
        if r.returncode != 0:
            print('  [LOI] Chay vi du bi loi:', r.stderr.strip().splitlines()[-1] if r.stderr.strip() else '')
            return
        ra = os.path.join(tmp, bai + '.OUT')
        if not os.path.exists(ra):
            print(f'  [LOI] Chay xong nhung khong co file {bai}.OUT trong thu muc hien tai')
            return
        dung = open(ra).read().split() == open(os.path.join(vd, bai + '.OUT')).read().split()
        print(f'  Vi du: {"DUNG" if dung else "SAI"} ({tg:.2f} s)')
    if not canh_bao:
        print('  Khong thay loi hinh thuc.')

def main():
    thu_muc = sys.argv[1] if len(sys.argv) > 1 else 'bai_lam'
    if not os.path.isdir(thu_muc):
        print(f'Khong co thu muc {thu_muc}/ - tao thu muc va chep bai lam vao (TONGCON.py, ...)')
        return
    for bai in sorted(os.listdir('test')):
        soat(thu_muc, bai)

main()
