# 🗿 Rock Paper Scissors ✂️

A classic, terminal-based Rock Paper Scissors game written in Python. 🐍 Play against the computer 🤖 or challenge a friend 🧑‍🤝‍🧑 in two-player mode!

## ✨ Features

- **Two Game Modes:**
    
    - **👤 vs. 💻 (Player vs. Computer):** Test your luck against a simple AI.
        
    - **👤 vs. 👤 (Two Player):** Battle it out with a friend on the same machine.
        
- **🏆 First-to-3:** The game tracks your score and plays until one player wins 3 rounds.
    
- **🖥️ Clean Interface:** Uses terminal clearing to keep the game display tidy and hide the first player's move in 2-player mode.
    
- **⌨️ Simple Inputs:** Easy-to-use 'r', 'p', 's' commands.
    

## 🚀 How to Play

### Prerequisites

- You must have **Python 3** installed on your system. 🐍
    

### Running the Game

1. Save the code as a Python file (e.g., `rps_game.py`).
    
2. Open your terminal or command prompt.
    
3. Navigate to the directory where you saved the file.
    
4. Run the game with the following command:
    
    ```
    python rps_game.py
    ```
    

### 🎮 Game Instructions

1. When you start the game, you will be asked to choose a mode:
    
    - `c` for **Player vs. Computer** 🤖
        
    - `f` for **Two Player** (friend) 🧑‍🤝‍🧑
        
2. When prompted, enter your choice for the round:
    
    - `r` for Rock 🗿
        
    - `p` for Paper 📄
        
    - `s` for Scissors ✂️
        
3. The game follows the classic rules:
    
    - Rock crushes Scissors. (🗿 > ✂️)
        
    - Paper covers Rock. (📄 > 🗿)
        
    - Scissors cuts Paper. (✂️ > 📄)
        
4. In Two Player mode, the screen will clear after Player 1 makes a choice, so Player 2 cannot see it. 🤫
    
5. The first player to reach **3 wins** is the overall champion! 🥇🎉
    

## 📂 Code Structure

The program is organized into several key functions:

- `main()`: The main game loop that handles mode selection and replay logic. 🔄
    
- `mainkan_lawan_komputer()`: Contains the game logic for the Player vs. Computer mode. 💻
    
- `mainkan_dua_pemain()`: Contains the game logic for the Two Player mode. 🧑‍🤝‍🧑
    
- `dapatkan_pilihan_pemain(nama_pemain)`: Prompts a player for their move and validates the input. ⌨️
    
- `tentukan_pemenang(pilihan1, pilihan2)`: Determines the winner of a single round. ⚖️
    
- `tampilkan_hasil_ronde(...)`: Displays the outcome of the round and the current score. 📊
    
- `bersihkan_layar()`: A utility function to clear the terminal screen for a better user experience. 🧹