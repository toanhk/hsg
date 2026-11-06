# LIENTHONG - vet can: "lan nhan". Ban dau nhan[u] = u; lap lai: voi moi canh (u, v), ca hai
# dinh lay nhan nho hon. Khi khong con gi thay doi, hai dinh cung thanh phan <=> cung nhan.
# Moi luot O(m), co the can toi n luot -> O(n*m): chi dung cho n, m <= 1000 (subtask 1).

def main():
    data = open('LIENTHONG.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    canh = [(int(data[2 + 2 * i]), int(data[3 + 2 * i])) for i in range(m)]
    nhan = list(range(n + 1))
    doi = True
    while doi:
        doi = False
        for u, v in canh:
            if nhan[u] != nhan[v]:
                nhan[u] = nhan[v] = min(nhan[u], nhan[v])
                doi = True
    dem = {}
    for u in range(1, n + 1):
        dem[nhan[u]] = dem.get(nhan[u], 0) + 1
    with open('LIENTHONG.OUT', 'w') as out:
        out.write(f'{len(dem)} {max(dem.values())}\n')

main()
