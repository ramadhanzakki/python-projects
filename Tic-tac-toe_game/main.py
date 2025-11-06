from modules_file import function as md

# ===== FUNGSI UTAMA (MAIN) =====


def main():
    # Inisialisasi
    papan = md.buat_papan_kosong()
    pemain_sekarang = 'X'
    game_berjalan = True

    # Loop Permainan Utama
    while game_berjalan:
        md.tampilkan_papan(papan)
        print(f'giliran pemain: {pemain_sekarang}')

        # Dapatkan Input Pemain
        input_baris = int(input('Masukan baris (0-2): '))
        input_kolom = int(input('Masukan kolom (0-2): '))

        # Validasi Langkah
        if md.cek_langkah_valid(papan, input_baris, input_kolom):

            # Update Papan
            papan[input_baris][input_kolom] = pemain_sekarang

            # Cek Kondisi Menang
            if md.cek_pemenang(papan, pemain_sekarang):
                md.tampilkan_papan(papan)
                print(f'Selamat! pemain {pemain_sekarang} menang')
                game_berjalan = False

            # Cek Kondisi Seri
            elif md.cek_seri(papan):
                md.tampilkan_papan(papan)
                print(f'Permainan berakhir seri')
                game_berjalan = False

            # Ganti Giliran Pemain
            else:
                if pemain_sekarang == 'X':
                    pemain_sekarang = 'O'
                else:
                    pemain_sekarang = 'X'
        else:
            print(
                'Langkah tidak valid. Kotak sudah terisi atau di luar papan. Coba lagi.')

        print('Permainan Selesai')


# Baris ini memastikan fungsi main() dijalankan saat script dieksekusi
if __name__ == "__main__":
    main()