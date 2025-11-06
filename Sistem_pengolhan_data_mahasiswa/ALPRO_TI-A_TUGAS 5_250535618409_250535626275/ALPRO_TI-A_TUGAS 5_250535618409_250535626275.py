#Program Data Mahasiswa Sederhana
#Fungsi untuk menambah data mahasiswa
def tambahMahasiswa():
    print("\n=== Tambah Data Mahasiswa ===")
    
    #Buka file untuk membaca data yang sudah ada
    file = open('mahasiswa.txt', 'r')
    isiFile = file.read()
    file.close()
    
    #Input data dari user
    while True:
        nim = input("Masukkan NIM (12 angka): ")
        if not nim.isdigit():
            print("❌ NIM hanya boleh berisi angka!")
        elif len(nim) != 12:
            print("❌ NIM harus 12 angka!")
        elif nim in isiFile:
            print("❌ NIM sudah terdaftar!")
            return
        else:
            break    
    
    #Input nama dan jurusan
    nama = input("Masukkan Nama: ")
    jurusan = input("Masukkan Jurusan: ")
    
    #Tulis data ke file
    file = open('mahasiswa.txt', 'a') #Mode 'a' agar tidak menimpa data lama
    file.write(nim + "," + nama + "," + jurusan + "\n")
    file.close()
    
    print("Data berhasil ditambahkan!")

#Fungsi untuk menampilkan semua data mahasiswa
def tampilkanMahasiswa():
    print("\n=== Data Mahasiswa ===")
    
    #Buka file untuk dibaca
    file = open('mahasiswa.txt', 'r')
    data = file.readlines()
    file.close()
    
    #Cek apakah ada data
    if len(data) == 0: 
        print("Tidak ada data!")
        return
    
    #Tampilkan data dengan format yang rapi
    print(f"{'No':<5} {'NIM':<15} {'Nama':<20} {'Jurusan':<20}")
    print("-" * 70)
    
    nomor = 1
    for baris in data:
        if baris.strip() != "":  # Abaikan baris kosong
            pisah = baris.split(",")
            nim = pisah[0]
            nama = pisah[1]
            jurusan = pisah[2].strip()
            
            # Format output agar rapi dan sejajar
            print(f"{nomor:<5} {nim:<15} {nama:<25} {jurusan:<20}")
            nomor += 1
    
    print("-" * 70)

#Fungsi untuk menghapus data mahasiswa
def hapusMahasiswa():
    print("\n=== Hapus Data Mahasiswa ===")
    
    #Baca semua data
    file = open('mahasiswa.txt', 'r')
    data = file.readlines()
    file.close()
    
    nim = input("Masukkan NIM yang akan dihapus: ")
    
    #Cari dan hapus data
    dataBaru = [] #list untuk menyimpan data yang tidak dihapus
    ketemu = False
    
    for baris in data:
        pisah = baris.split(",")
        if pisah[0] != nim:
            dataBaru.append(baris)
        else:
            ketemu = True
            print("Data ditemukan:")
            print("NIM:", pisah[0])
            print("Nama:", pisah[1])
            print("Jurusan:", pisah[2].strip())
    
    if ketemu:
        yakin = input("Yakin ingin menghapus? (y/n): ")
        if yakin == 'y':
            #Tulis ulang data tanpa yang dihapus
            file = open('mahasiswa.txt', 'w')
            for baris in dataBaru:
                file.write(baris)
            file.close()
            print("Data berhasil dihapus!")
        else:
            print("Penghapusan dibatalkan")
    else:
        print("NIM tidak ditemukan!")

#Program utama
print("=" * 50)
print("PROGRAM DATA MAHASISWA")
print("=" * 50)

#Cek apakah file ada, kalau tidak buat file baru
try:
    file = open('mahasiswa.txt', 'r')
    file.close()
except:
    file = open('mahasiswa.txt', 'w')
    file.close()
    print("File baru dibuat")

#Loop menu utama
while True:
    print("\n=== MENU UTAMA ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Keluar")
    
    pilihan = input("Pilih menu (1-4): ")
    
    if pilihan == '1':
        tambahMahasiswa()
    elif pilihan == '2':
        tampilkanMahasiswa()
    elif pilihan == '3':
        hapusMahasiswa()
    elif pilihan == '4':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!")