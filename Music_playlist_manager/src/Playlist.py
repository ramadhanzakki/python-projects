from src.SongNode import SongNode

class PlayList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_song = None
        self.song_index = {}
        self.play_history = []


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


    def play_song(self, title):
        if title in self.song_index:
            node_to_play = self.song_index[title]
            self.current_song = node_to_play
            print(f'▶️ Playing {self.current_song.title}')
            self.play_history.append(self.current_song.title)

        else:
            print(f'[!] The song ‘{title}’ was not found in the playlist')


    def next_song(self):
        if self.current_song is None:
            print('[!] No songs have been played yet. Play a song first.')
            return
        
        if self.current_song.next is None:
            print('[!] You have reached the end of the playlist.')
            return
        
        self.current_song = self.current_song.next
        print(f'▶️ Next up: {self.current_song.title}')
        self.play_history.append(self.current_song.title)

    
    def prev_song(self):
        if self.current_song is None:
            print('[!] No songs have been played yet. Play a song first.')
            return
        
        if self.current_song.prev is None:
            print('[!] You have reached the end of the playlist.')
            return

        self.current_song = self.current_song.prev
        print(f'▶️ Play previous: {self.current_song.title}')
        self.play_history.append(self.current_song.title)


    def show_history(self):
        if self.play_history is None:
            print('[!] Playback history is still empty')
            return
        
        print('--- 📜 Play History (Most Recent) 📜 ---')
        for i, title in enumerate(reversed(self.play_history), start=1):
            print(f'{i}. {title}')
            