from src.SongNode import SongNode
from src.Playlist import PlayList

my_playlist = PlayList()

my_playlist.add_song('Golden - HUNTRX/EJAE, Audrey Nuna, Rei Ami')
my_playlist.add_song('In Another World - EJAE')
my_playlist.add_song('FOCUS - Hearts2Hearts')

my_playlist.display()

print("\n--- 🔍 Intip isi Hash Table (song_index) ---")
for title, node in my_playlist.song_index.items():
    print(f"Key: '{title}'")
    print(f"   -> Value: <SongNode object di memori, Title: {node.title}>")