# KHUNG BAI THI - doi TEN thanh ten bai trong de (vi du 'NUMBER')
import sys

TEN = 'TENBAI'

def main():
    # 1) Doc toan bo input mot lan, tach thanh cac "tu" (kieu bytes)
    try:
        data = open(TEN + '.INP', 'rb').read().split()
        ghi_file = True
    except FileNotFoundError:            # khong co file -> doc ban phim/stdin (de tu thu)
        data = sys.stdin.buffer.read().split()
        ghi_file = False
    pos = 0                              # con tro: tu tiep theo can doc

    n = int(data[pos]); pos += 1
    a = list(map(int, data[pos:pos + n])); pos += n

    # 2) Giai bai - gom ket qua vao list out (moi phan tu la mot dong)
    out = []
    out.append(str(sum(a)))

    # 3) Ghi mot lan
    res = '\n'.join(out) + '\n'
    if ghi_file:
        with open(TEN + '.OUT', 'w') as f:
            f.write(res)
    else:
        sys.stdout.write(res)

main()
