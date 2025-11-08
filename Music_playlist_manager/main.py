from src.SongNode import SongNode
from src.Playlist import PlayList

print("========================================")
print("    🚀 STARTING FEATURES TESTING 🚀    ")
print("========================================")

my_playlist = PlayList()
my_playlist.add_song('Golden - HUNTRX/EJAE, Audrey Nuna, Rei Ami')
my_playlist.add_song('In Another World - EJAE')
my_playlist.add_song('FOCUS - Hearts2Hearts')
my_playlist.add_song('House Party - VVUP')

print("\n--- 🎵 Initial Playlist Created 🎵 ---")
my_playlist.display()

print('\n--- Test 1: Test Empty History ---')
my_playlist.show_history()

print('\n--- Test 2: Play Song ---')
my_playlist.play_song('Golden - HUNTRX/EJAE, Audrey Nuna, Rei Ami')
my_playlist.show_history()

print('\n--- Test 3: Play next song ---')
my_playlist.next_song()
my_playlist.next_song()
my_playlist.next_song()
my_playlist.show_history()

print('\n--- Test 4: Play Previous Song ---')
my_playlist.prev_song()
my_playlist.show_history()

print('\n--- Test 5: Failed Action ---')
my_playlist.play_song('House Party - VVUP')
my_playlist.next_song()
my_playlist.show_history()

print("\n========================================")
print("       🏁 TESTING IS FINNISED        🏁")
print("========================================")