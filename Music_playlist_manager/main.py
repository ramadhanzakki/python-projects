from src.Playlist import PlayList
# --- TEMPELKAN KODE INI DI BAGIAN BAWAH FILE-MU ---

print("========================================")
print(" 🚀 MEMULAI PENGUJIAN FITUR SORTING 🚀")
print("========================================")

# 1. Buat playlist tes
playlist_tes = PlayList()

# -----------------------------------------------------------------
print("\n--- Tes 1: Playlist Kosong (Edge Case) ---")
print("Memanggil 'display_sorted' pada playlist kosong...")
playlist_tes.display_sorted()
### HARAPAN:
# (Seharusnya tidak crash, mungkin hanya mencetak header)
# --- 🎵 Playlist (Terurut A-Z) 🎵 ---
# (Tidak ada lagu di bawahnya)
# -----------------------------------------------------------------

# 2. Tambahkan satu lagu
print("\n--- Tes 2: Playlist Satu Lagu (Base Case Sort) ---")
playlist_tes.add_song("Lagu Cuma Satu")
print("\nMemanggil 'display_sorted'...")
playlist_tes.display_sorted()
### HARAPAN:
# --- 🎵 Playlist (Terurut A-Z) 🎵 ---
# 1. Lagu Cuma Satu
# -----------------------------------------------------------------

# 3. Buat playlist baru yang tidak terurut
playlist_tes_2 = PlayList()
print("\n--- Tes 3: Playlist Tidak Terurut (Normal Case) ---")
playlist_tes_2.add_song("Zebra")
playlist_tes_2.add_song("Apple")
playlist_tes_2.add_song("Mango")
playlist_tes_2.add_song("Banana")
playlist_tes_2.add_song("Xylophone")

print("\nMemanggil 'display_sorted'...")
playlist_tes_2.display_sorted()
### HARAPAN: (Harus Terurut A-Z)
# --- 🎵 Playlist (Terurut A-Z) 🎵 ---
# 1. Apple
# 2. Banana
# 3. Mango
# 4. Xylophone
# 5. Zebra
# -----------------------------------------------------------------

print("\n--- Tes 4: Playlist Terurut Terbalik (Worst Case) ---")
playlist_tes_3 = PlayList()
playlist_tes_3.add_song("Song D")
playlist_tes_3.add_song("Song C")
playlist_tes_3.add_song("Song B")
playlist_tes_3.add_song("Song A")

print("\nMemanggil 'display_sorted'...")
playlist_tes_3.display_sorted()
### HARAPAN: (Harus Terurut A-Z)
# --- 🎵 Playlist (Terurut A-Z) 🎵 ---
# 1. Song A
# 2. Song B
# 3. Song C
# 4. Song D
# -----------------------------------------------------------------

print("\n--- Tes 5: Cek Integritas Playlist Asli (SANGAT PENTING) ---")
print("Memanggil 'display' (NON-sorted) pada playlist Tes 3...")
playlist_tes_2.display()
### HARAPAN: (Urutan asli TIDAK BOLEH berubah)
# --- 🎵 My Playlist 🎵 ---
# 1. Zebra
# 2. Apple
# 3. Mango
# 4. Banana
# 5. Xylophone
# --------------------------
# (Jika ini cocok, kamu berhasil! Kamu tidak merusak playlist aslinya)
# -----------------------------------------------------------------

print("\n========================================")
print("      🏁 PENGUJIAN SORTING SELESAI 🏁")
print("========================================")