# Blueprint semua barang yang ada di toko
class barang:
    def __init__(self, nama: str, stok: int, harga: float):
        self.nama = nama
        self.stok = stok
        self.harga = harga

    def tampilkan_info(self):
        print(f'- {self.nama}, stok = {self.stok} unit, harga = Rp {self.harga}')

    def tambah_stok(self, jumlah):
        if jumlah >= 0:
            self.stok += jumlah
        else:
            print('Error! tidak bisa menambahkan kurang dari 0')

    def jual(self, jumlah):
        if jumlah >= self.stok:
            print(
                f'Warning! stok barang kurang. Stok tinggal {self.stok} unit')
        elif jumlah <= 0:
            print("Error! pembelian tidak bisa dibawah 0")
        else:
            self.stok -= jumlah
            print(
                f"berhasil menjual {jumlah} unit '{self.nama}' dengan harga: Rp {self.harga * jumlah}. Stok tersisa {self.stok}")


def main():
    buku = barang('Buku Tulis', 20, 2500)
    bolpoin = barang('Bolpoin', 31, 1000)
    tipex = barang('Tip Ex', 17, 1500)
    On_transaksi = True

    print('=======================================')
    print('       TOKO ALAT TULIS ALKAUTSAR       ')
    print('=======================================')

    while On_transaksi == True:
        print('\n --- Invertaris ---')
        buku.tampilkan_info()
        bolpoin.tampilkan_info()
        tipex.tampilkan_info()

        while True:
            user_transaksi = input('beli atau tidak? (y/n): ').lower()

            if user_transaksi == 'y':
                print('\n --- Dijual ---')
                print(f'1. {buku.nama}')
                print(f'2. {bolpoin.nama}')
                print(f'3. {tipex.nama}')

                try:
                    user_input = int(input('Pilih nomor: '))
                except ValueError:
                    print('Input harus angka')
                    continue

                if user_input == 1:
                    try:
                        jumlah_beli = int(input('Beli berapa: '))
                    except ValueError:
                        print('Warning! Masukan angka')

                    buku.jual(jumlah_beli)
                    break
                elif user_input == 2:
                    try:
                        jumlah_beli = int(input('Beli berapa: '))
                    except ValueError:
                        print('Warning! Masukan angka')

                    bolpoin.jual(jumlah_beli)
                    break
                elif user_input == 3:
                    try:
                        jumlah_beli = int(input('Beli berapa: '))
                    except ValueError:
                        print('Warning! Masukan angka')

                    tipex.jual(jumlah_beli)
                    break

            elif user_transaksi == 'n':
                break
            else:
                print('Input harus y atau n')

        user_continue = input('Lanjut atau tidak? (y/n)').lower()
        if user_continue == 'n':
            On_transaksi = False
        elif user_continue != 'y' and user_continue != 'n':
            print('Error Value')

if __name__ == "__main__":
    main()
