from src.Playlist import PlayList
# --- TEMPELKAN KODE INI DI BAGIAN BAWAH FILE-MU ---

print("========================================")
print(" 🚀 MEMULAI PENGUJIAN FITUR REKURSIF 🚀")
print("========================================")

# 1. Buat playlist tes
playlist_tes = PlayList()

# -----------------------------------------------------------------
print("\n--- Tes 1: Playlist Kosong (Edge Case) ---")
print("Memanggil 'display_recursive' pada playlist kosong...")
playlist_tes.display_recursive()
### HARAPAN:
# [!] Playlist is Empty
# -----------------------------------------------------------------

# 2. Tambahkan beberapa lagu
print("\n--- Tes 2: Playlist Terisi (Normal Case) ---")
playlist_tes.add_song("Lagu A: Rekursi Mulai")
playlist_tes.add_song("Lagu B: Panggil Diri Sendiri")
playlist_tes.add_song("Lagu C: Menuju Base Case")
playlist_tes.add_song("Lagu D: Selesai")

print("\nMemanggil 'display_recursive' pada playlist terisi...")
playlist_tes.display_recursive()
### HARAPAN:
# --- 🎵 Playlist (Versi Rekursif) 🎵 ---
# 1. Lagu A: Rekursi Mulai
# 2. Lagu B: Panggil Diri Sendiri
# 3. Lagu C: Menuju Base Case
# 4. Lagu D: Selesai
# -----------------------------------------------------------------

print("\n--- Tes 3: Perbandingan dgn Versi Iteratif (Sanity Check) ---")
print("Memanggil 'display' (non-rekursif) untuk perbandingan...")
playlist_tes.display()
### HARAPAN:
# --- 🎵 My Playlist 🎵 ---
# 1. Lagu A: Rekursi Mulai
# 2. Lagu B: Panggil Diri Sendiri
# 3. Lagu C: Menuju Base Case
# 4. Lagu D: Selesai
# --------------------------
# (Outputnya harus identik, kecuali header-nya)
# -----------------------------------------------------------------

print("\n========================================")
print("      🏁 PENGUJIAN REKURSIF SELESAI 🏁")
print("========================================")