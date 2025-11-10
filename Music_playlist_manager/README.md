# PyPlaylist: A DSA-Powered Music Playlist Manager

**PyPlaylist** is a terminal-based music playlist management system built in Python. It serves as a practical implementation of fundamental Data Structures and Algorithms (DSA), demonstrating how different structures can work together to solve real-world problems efficiently.

This project was developed as a capstone exercise to master core computer science concepts including Linked Lists, Hash Tables, Stacks, Recursion, and Sorting Algorithms.

## 🚀 Key Features & DSA Implementation

PyPlaylist goes beyond a simple list of songs by leveraging specialized data structures for each feature to ensure optimal performance.

|Feature|Description|Underlying DSA|Time Complexity|
|---|---|---|---|
|**Add Song**|Appends a new song to the end of the playlist.|**Doubly Linked List** (Tail Pointer)|O(1)|
|**Play Song**|Instantly finds and plays a song by its title.|**Hash Table** (Python Dictionary)|O(1) Average|
|**Next/Prev**|Navigates to adjacent songs in the playlist.|**Doubly Linked List** (Pointers)|O(1)|
|**Play History**|Tracks recently played songs in LIFO order.|**Stack** (Python List)|O(1) Push/Pop|
|**Shuffle**|Randomizes the playlist order efficiently.|**Array** + Fisher-Yates Shuffle|O(N)|
|**Sort (A-Z)**|Displays songs alphabetically without altering the original playlist.|**Merge Sort Algorithm**|O(N log N)|
|**Recursive Display**|Prints the playlist using a functional recursion approach.|**Recursion**|O(N)|

## 🛠️ Tech Stack

- **Language:** Python 3.x
    
- **Libraries:** `random` (standard library only, no external dependencies)
    

## 📂 Project Structure

```
PyPlaylist/
├── src/
│   ├── SongNode.py       # Class representing a single song (Node)
│   └── Playlist.py       # Main class managing the playlist logic
├── main.py               # Entry point and testing script
└── README.md             # Project documentation
```

## 🧩 Detailed Component Breakdown

### 1. Doubly Linked List (`SongNode` & `Playlist`)

The core of the playlist is a Doubly Linked List. Unlike a standard array, this allows for efficient insertion and deletion of songs from any position without shifting elements. The `prev` and `next` pointers enable seamless bidirectional navigation (`next_song()` and `prev_song()`).

### 2. Hash Table Index (`song_index`)

To avoid O(N) search times when a user wants to play a specific song, PyPlaylist maintains a Hash Table mapping song titles directly to their corresponding `SongNode` objects in memory. This enables instant (O(1)) access to any song, regardless of playlist size.

### 3. Play History Stack (`play_history`)

A Stack data structure is used to implement the "Recently Played" feature. As songs are played, they are pushed onto the stack. When viewing history, songs are popped (displayed) in Last-In, First-Out (LIFO) order, showing the most recent tracks first.

### 4. Merge Sort (`display_sorted`)

To display songs alphabetically, the project implements the **Merge Sort** algorithm from scratch. This stable, divide-and-conquer algorithm efficiently sorts a copy of the playlist titles in O(N log N) time, leaving the original playback order intact.

## 🏁 Getting Started

1. **Clone the repository:**
    
    ```
    git clone [https://github.com/yourusername/PyPlaylist.git](https://github.com/yourusername/PyPlaylist.git)
    ```
    
2. **Navigate to the project directory:**
    
    ```
    cd PyPlaylist
    ```
    
3. **Run the application (demo/test script):**
    
    ```
    python main.py
    ```
    

## 🧪 Testing

The `main.py` file includes a comprehensive suite of test cases that validate:

- Adding and displaying songs.
    
- Navigating with next/previous.
    
- Correct LIFO behavior of the play history.
    
- Integrity of the playlist after shuffling.
    
- Accuracy of the Merge Sort implementation.
    
- Correctness of the recursive display function.
    

_Built with ❤️ as a learning journey into Data Structures and Algorithms._
