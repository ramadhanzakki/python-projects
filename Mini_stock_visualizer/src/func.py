import yfinance as yf
import matplotlib.pyplot as plt
from colorama import Fore, Style, init

init(autoreset=True)

class StockAnalyzer:
    def __init__(self, ticker_symbol):
        self.symbol = ticker_symbol.upper()
        self.data = None

    def fetch_data(self, period='1mo'):
        print(f"{Fore.YELLOW} Retrieving data for {self.symbol}...")

        try:
            ticker = yf.Ticker(self.symbol)
            self.data = ticker.history(period=period)

            if self.data.empty:
                print(f'{Fore.RED} [X] Data not found! Check the stock code.')
                return False

            print(f'{Fore.GREEN} [V] Data successfully retrieved! ({len(self.data)} Trading Days).')
            return True
        
        except Exception as e:
            print(f'{Fore.RED} [X] Error: {e}')
            return False

    def show_average(self):
        if self.data is None : return

        avg_price = self.data['Close'].mean()
        print(f'{Fore.CYAN} --- Statistics {self.symbol} (Last 1 Month) ---')
        print(f'Average Price {Fore.WHITE} : {avg_price:,.2f}')

    def save_chart(self):
        if self.data is None : return

        print(f'{Fore.YELLOW} Drawing a graph...')

        plt.figure(figsize=(10, 5))
        plt.plot(self.data.index, self.data['Close'], marker='o', linestyle='-', color='b')
        plt.title(f"Pergerakan Harga Saham {self.symbol}")
        plt.xlabel("Tanggal")
        plt.ylabel("Harga (IDR/USD)")
        plt.grid(True)

        filename = f"{self.symbol}_chart.png"
        plt.savefig(filename)
        print(f"{Fore.GREEN}[V] Grafik disimpan sebagai: {filename}")
        plt.close()