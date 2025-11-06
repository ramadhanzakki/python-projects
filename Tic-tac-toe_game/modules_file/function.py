def cek_seri(papan):
    for row in papan:
        for cell in row:
           if cell == ' ':
                return False
    return True


def cek_pemenang(papan, pemain):
    for row in range(3):
        if papan[row][0] == papan[row][1] == papan[row][2] == pemain:
            return True
    for coloumn in range(3):
        if papan[0][coloumn] == papan[1][coloumn] == papan[2][coloumn] == pemain:
            return True
    if papan[0][0] == papan[1][1] == papan[2][2] == pemain:
        return True
    if papan[0][2] == papan[1][1] == papan[2][0] == pemain:
        return True
    return False


def buat_papan_kosong():
    papan_baru = [[' ' for _ in range(3)] for _ in range(3)]
    return papan_baru


def tampilkan_papan(papan):
    for i, row in enumerate(papan):
        print('  | '.join(row))
        if i < 2:
            print('---+----+---')
    print()


def cek_langkah_valid(papan, baris, kolom):
    if baris >= 0 and baris <= 2 and kolom >= 0 and kolom <= 2:
        if papan[baris][kolom] == ' ':
            return True
    else:
        return False
    