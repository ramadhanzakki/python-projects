import random
import sys # Digunakan untuk nilai 'infinity'

def number_guessing_game():
    """
    Fungsi utama untuk menjalankan permainan tebak angka.
    Mencakup semua fitur tambahan: rentang dinamis, batas percobaan, dan skor terbaik.
    """
    # Inisialisasi skor terbaik di luar loop utama permainan.
    # float('inf') adalah cara mudah untuk memastikan percobaan pertama selalu menjadi skor terbaik.
    best_score = float('inf') 
    
    print("Selamat datang di Permainan Tebak Angka! 🎲")

    while True:
        # Menggunakan .lower() untuk menyederhanakan pengecekan input (menerima 'y' atau 'Y')
        play_game = input('\nApakah Anda ingin bermain? (y/n): ').lower()

        if play_game == 'y':
            try:
                # Meminta semua pengaturan di awal
                min_num = int(input('Masukkan angka minimum: '))
                max_num = int(input('Masukkan angka maksimum: '))
                max_attempts = int(input('Masukkan batas percobaan (misal: 5): '))
                
                # Validasi sederhana untuk rentang angka
                if min_num >= max_num:
                    print("Angka minimum harus lebih kecil dari angka maksimum. Coba lagi.")
                    continue

            except ValueError:
                print("Input tidak valid! Harap masukkan angka.")
                continue

            # Menghasilkan angka rahasia untuk ronde ini
            secret_number = random.randint(min_num, max_num)
            attempts = 0
            
            print(f"\nSaya telah memilih angka antara {min_num} dan {max_num}. Anda punya {max_attempts} percobaan.")

            # Loop utama untuk menebak
            while attempts < max_attempts:
                try:
                    guess_str = input(f"Percobaan ke-{attempts + 1}: Masukkan tebakan Anda: ")
                    user_guess = int(guess_str)
                except ValueError:
                    print("Input harus berupa angka!")
                    continue

                attempts += 1 # Tambah percobaan setelah input valid

                # Logika pengecekan tebakan
                if user_guess == secret_number:
                    print(f"🎉 Selamat! Anda berhasil menebak angka {secret_number} dalam {attempts} percobaan.")
                    
                    # Cek dan perbarui skor terbaik
                    if attempts < best_score:
                        best_score = attempts
                        print(f"✨ Skor terbaik baru! Yaitu {best_score} percobaan.")
                    
                    break # Keluar dari loop tebakan karena sudah menang
                elif user_guess < secret_number:
                    print("Terlalu rendah! Coba lagi.")
                else: # user_guess > secret_number
                    print("Terlalu tinggi! Coba lagi.")

            # Kondisi jika loop selesai tanpa menebak dengan benar (kalah)
            if user_guess != secret_number:
                print(f"\nMaaf, kesempatan Anda habis. Angka yang benar adalah {secret_number}. 😔")
        
        elif play_game == 'n':
            print("Terima kasih sudah bermain!")
            break # Keluar dari loop utama dan mengakhiri program
        
        else:
            print("Input tidak valid. Harap masukkan 'y' untuk bermain atau 'n' untuk keluar.")
        
        # Tampilkan skor terbaik saat ini jika sudah pernah menang
        if best_score != float('inf'):
            print(f"Skor terbaik Anda sejauh ini: {best_score} percobaan.")

# Menjalankan fungsi utama permainan
if __name__ == "__main__":
    number_guessing_game()