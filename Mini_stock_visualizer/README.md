# Mini Stock Visualizer 📈

A simple Command Line Interface (CLI) application to analyze and visualize stock price movements in real-time.

This project was created as an exercise in applying **Object-Oriented Programming (OOP)** and **Package Management** concepts in Python.

## 📸 Preview

![[AAPL_chart 1.png]]

## ✨ Key Features

- **Real-time Data Fetching:** Retrieves the latest stock price data (last 1 month) directly from Yahoo Finance.
    
- **Simple Analysis:** Automatically calculates the average closing price.
    
- **Data Visualization:** Generates an image file (`.png`) containing the stock price movement chart.
    
- **Interactive CLI:** Clean and colorful terminal interface.
    

## 🛠️ Tech Stack

- **Python 3.14.2**
    
- **yfinance** (To fetch stock market data)
    
- **matplotlib** (To create chart visualizations)
    
- **colorama** (For colored text in the terminal)
    

## 🚀 Installation & Setup

Make sure you have Python installed on your computer.

1. **Clone this repository**
    
    ```
    git clone [https://github.com/ramadhanzakki/python-project/Mini_Stock_Visualizer.git](https://github.com/ramadhanzakki/python-project/Mini-Stock-Visualizer.git)
    cd Mini-Stock-Visualizer
    ```
    
2. **Create a Virtual Environment** (Highly recommended to keep things clean)
    
    ```
    # For Windows
    python -m venv venv
    
    # For Mac/Linux
    python3 -m venv venv
    ```
    
3. **Activate the Virtual Environment**
    
    ```
    # For Windows
    .\venv\Scripts\activate
    
    # For Mac/Linux
    source venv/bin/activate
    ```
    
4. **Install Required Libraries** Run this command to install `yfinance`, `matplotlib`, and other dependencies at once:
    
    ```
    pip install -r requirements.txt
    ```
    
5. **Run the Application**
    
    ```
    python main.py
    ```
    

## 📖 Usage

When the program runs, enter a valid stock **Ticker Symbol**.

- **For US Stocks:** Use the standard code (e.g., `AAPL`, `TSLA`, `GOOG`).
    
- **For Indonesian Stocks:** Add `.JK` at the end (e.g., `BBCA.JK`, `TLKM.JK`, `ANTM.JK`).
    

Example output:

```
Enter Stock Code: BBCA.JK
[V] Data successfully retrieved!
Average Price: 10,250.00
[V] Chart saved as: BBCA.JK_chart.png
```

## 📂 Project Structure

```
.
├── src/
│   └── func.py        # Main logic (StockAnalyzer Class)
├── main.py            # App entry point
├── requirements.txt   # List of dependencies
├── README.md          # Project documentation
└── .gitignore         # Git ignore file
```

## 🎓 Learning Outcomes

This project was built to learn:

1. **Python OOP:** Using Classes, Methods, and Constructors.
    
2. **Package Management:** Using `pip`, `virtual environment`, and `requirements.txt`.
    
3. **External Libraries:** Leveraging open-source libraries to accelerate development.
    

_Created with ❤️ by [Muhammad Zakki Fitra Ramadhan]_