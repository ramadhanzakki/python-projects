# 📦 Inventory Product Search Simulator

A simple Python console application 🐍 to visually demonstrate and compare the performance of different searching algorithms. 📊

This project was built to understand the core concepts of:

- **Linear Search**
    
- **Binary Search**
    
- **Interpolation Search**
    

...and to see how their performance (in steps and time) differs in a real-world scenario.

## ✨ Features

- 🚶 **Linear Search:** The classic, one-by-one check, perfect for unsorted data.
    
- 📚 **Binary Search:** The efficient "divide and conquer" method for sorted data.
    
- 🔭 **Interpolation Search:** A "smarter" version of Binary Search, optimized for uniformly distributed data.
    
- ⏱️ **Performance Comparison:** See exactly how many steps and milliseconds each algorithm takes to find a product.
    
- 🧹 **Clean Code:** The project is structured with Separation of Concerns, splitting logic (`src/function.py`), presentation (`src/visual.py`), and data (`data/input/inventory.py`).
    

## 📁 Project Structure

The project is organized in a clean and easy-to-understand structure:

```
Inventory-Product-Search/
├── 📂 data/
│   └── 📂 input/
│       └── 📜 inventory.py  (The list of products 📦)
├── 📂 src/
│   ├── 📜 function.py     (Contains all search algorithm logic 🧠)
│   └── 📜 visual.py       (Handles printing tables and results 🎨)
└── 📜 main.py           (The main entry point of the application 🚀)
```

## 🚀 How to Use

1. **Clone the repository:**
    
    ```
    git clone [https://github.com/ramadhanzakki/Inventory-Product-Search.git](https://github.com/ramadhanzakki/Inventory-Product-Search.git)
    ```
    
2. **Navigate to the project directory:**
    
    ```
    cd Inventory-Product-Search
    ```
    
3. **Run the application:**
    
    ```
    python main.py
    ```
    
4. **Follow the on-screen prompts:**
    
    - You will see the full inventory list.
        
    - Enter a Product ID you want to find (e.g., `180`).
        
    - Choose which algorithm (1, 2, or 3) you want to use.
        
    - The app will show you the product details and the performance results!
        

## 💻 Technologies Used

- **Python 3**
    
- Standard libraries (`time`, `sys`)
    

Feel free to contribute or suggest improvements!
