import random
from src.Playlist import PlayList
print("========================================")
print("       🚀 FEATURES TEST STARTES 🚀     ")
print("========================================")


# Buat playlist tes baru
playlist_tes = PlayList()

# -----------------------------------------------------------------
print("\n--- Tes 1: Shuffle Empty Playlist (Edge Case) ---")
playlist_tes.shuffle()
playlist_tes.display()
# EXPECTATION:
# [!] Not enough songs to shuffle
# [!]Your playlist is currently empty
# -----------------------------------------------------------------

# Adding a song
playlist_tes.add_song("Golden - HUNTRX/EJAE, Rei Ami, Audrey Nuna")

print("\n--- Tes 2: Shuffle Playlist With a Song (Edge Case) ---")
playlist_tes.shuffle()
playlist_tes.display()
# EXPECTATION:
# [!] Not enough songs to shuffle
# --- 🎵 My Playlist 🎵 ---
# 1. Golden - HUNTRX/EJAE, Rei Ami, Audrey Nuna
# -----------------------------------------------------------------

# Adding more song
playlist_tes.add_song("In Another World - EJAE")
playlist_tes.add_song("STYLE - Hearts2Hearts")
playlist_tes.add_song("FOCUS - Hearts2hearts")
playlist_tes.add_song("That's So True - Grachie Abrams")

print("\n--- Tes 3: Shuffle Normal (Shuffle Playlist) ---")
print("--- BEFORE SHUFFLE ---")
playlist_tes.display()
# EXPECTATION (BEFORE):
# --- 🎵 My Playlist 🎵 ---
# 1. Golden - HUNTRX/EJAE, Rei Ami, Audrey Nuna
# 2. In Another World - EJAE
# 3. STYLE - Hearts2Hearts
# 4. FOCUS - Hearts2hearts
# 5. That's So True - Grachie Abrams
# --------------------------

print("\n--- (Running Shuffle) ---")
playlist_tes.shuffle()

print("\n--- AFTER SHUFFLE ---")
playlist_tes.display()
# EXPECTATION (AFTER):
# --- 🎵 Isi Playlist 🎵 ---
# 1. [Random Song, Example: FOCUS - Hearts2hearts]
# 2. [Random Song, Example: Golden - HUNTRX/EJAE, Rei Ami, Audrey Nuna]
# 3. [Random Song, Example: That's So True - Grachie Abrams]
# 4. [Random Song, Example: STYLE - Hearts2Hearts]
# 5. [Random Song, Example: In Another World - EJAE]
# (The order MUST be different from before, unless it happens to be the same.)
# -----------------------------------------------------------------

print("\n--- Tes 4: Reset Check 'current_song' ---")
# The algorithm should set self.current_song to None.
# So, ‘next’ or ‘prev’ should fail with the correct message.
playlist_tes.next_song()
# EXPECTATION:
# [[!] No songs have been played yet. Play a song first.
# -----------------------------------------------------------------

print("\n--- Tes 5: Check Hash Table Integrity (VERY IMPORTANT) ---")
# Does ‘play_song’ still work after shuffle?
# Let's try playing “STYLE - Hearts2Hearts” (whose new position we don't know).
playlist_tes.play_song("STYLE - Hearts2Hearts")
# EXPECTATION:
# ▶️ Playiing: STYLE - Hearts2Hearts
# (If this works, your Hash Table is still valid!)
# -----------------------------------------------------------------

print("\n--- Tes 6: Check Pointer Integrity (Navigation) ---")
# Our 'current_song' is now “STYLE - Hearts2Hearts”.
# Let's try ‘next’ and ‘prev’ on the shuffled playlist
print("Play the next song from ‘STYLE - Hearts2Hearts’ (in the new order)...")
playlist_tes.next_song()

print("Play the previous song (return to ‘STYLE - Hearts2Hearts’)...")
playlist_tes.prev_song()
# EXPECTATION:
# ▶️ Next Up: [Any song AFTER ‘STYLE - Hearts2Hearts’ in random order]
# ▶️ Play Previous: STYLE - Hearts2Hearts
# (If this works, your .next and .prev pointers are correctly reconnected.)
# -----------------------------------------------------------------

print("\n========================================")
print("        🏁 TESTING IS FINNISED 🏁      ")
print("========================================")
