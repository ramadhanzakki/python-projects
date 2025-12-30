import os
from colorama import Fore, Style, init
from src.func import StockAnalyzer

init()

if __name__ == "__main__":
    os.system('cls')
    print(f"{Fore.BLUE} === Smple Stock Analysis Application ===")

    code = input("Enter Stock Code (example: BBCA.JK, TLKM.JK, or AAPL): ")

    app = StockAnalyzer(code)

    success = app.fetch_data()

    if success:
        app.show_average()
        app.save_chart()

    print(f'\n{Fore.MAGENTA}Done. Check your project folder to see the image!')