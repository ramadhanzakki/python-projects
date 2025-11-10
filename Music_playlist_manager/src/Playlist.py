from src.SongNode import SongNode
import random

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
            print('[!]Your playlist is currently empty')
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


    def shuffle(self):
        if self.head is None or self.head.next is None:
            print('[!] Not enough songs to shuffle')
            return
        
        current = self.head
        song_array = []

        while current:
            song_array.append(current)
            current = current.next

        random.shuffle(song_array)

        for i in range(len(song_array)):
            node = song_array[i]
            if i == 0:
                node.prev = None
            elif i > 0:
                node.prev = song_array[i - 1]

            if i == len(song_array) - 1:
                node.next = None
            elif i < len(song_array) - 1:
                node.next = song_array[i + 1]

        self.head = song_array[0]
        self.tail = song_array[-1]
        self.current_song = None


    def display_helper(self, current_node, count):
        if current_node == None:
            return
        
        print(f'{count}. {current_node.title}')
        self.display_helper(current_node.next, count + 1)


    def display_recursive(self):
        if self.head == None:
            print('[!] Playlist is Empty')
            return
        
        print("--- 🎵 Playlist (Versi Rekursif) 🎵 ---")

        self.display_helper(self.head, 1)


    def _merge_sort(self, left_arr, right_arr):
        result = []
        i = 0
        j = 0

        while i <= len(left_arr) - 1 and j <= len(right_arr)- 1:
            if left_arr[i] < right_arr[j]:
                result.append(left_arr[i])
                i += 1
            else:
                result.append(right_arr[j])
                j += 1

        result.extend(left_arr[i:])
        result.extend(right_arr[j:])

        return result


    def sorted_titles(self, arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2

        left_half = arr[:mid]
        right_half = arr[mid:]

        sorted_left = self.sorted_titles(left_half)
        sorted_right = self.sorted_titles(right_half)

        return self._merge_sort(sorted_left,sorted_right)


    def display_sorted(self):
        title_array = []

        current = self.head
        while current:
            title_array.append(current.title)
            current = current.next

        sort_titles = self.sorted_titles(title_array)

        print("--- 🎵 Playlist (Terurut A-Z) 🎵 ---")

        for i, title in enumerate(sort_titles, start=1):
            print(f'{i}. {title}')
