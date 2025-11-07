from src.SongNode import SongNode

class PlayList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_song = None
        self.song_index = {}


    def add_song(self, title):
        new_song = SongNode(title)

        if self.head is None:
            self.head = new_song
            self.tail = new_song
        else:
            self.tail.next = new_song
            new_song.prev = self.tail
            self.tail = new_song

        self.song_index[title] = new_song
        print(f'[+] The song {title} has been successfully added in playlist')


    def display(self):
        if self.head is None:
            print('Your playlist is currently empty')
            return
        
        print('--- 🎵 My Playlist 🎵 ---')
        current = self.head
        count = 1
        while current:
            print(f'{count}. {current.title}')
            current = current.next
            count += 1

        print('--------------------------')