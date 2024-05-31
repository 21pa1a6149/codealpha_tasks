import yfinance as yf

class Stock:
    def __init__(self, symbol, quantity):
        self.symbol = symbol
        self.quantity = quantity
        self.data = None
    
    def fetch_data(self):
        self.data = yf.Ticker(self.symbol).history(period="1d")
    
    def current_price(self):
        if self.data is None:
            self.fetch_data()
        return self.data['Close'].iloc[-1]

class Portfolio:
    def __init__(self):
        self.stocks = {}
    
    def add_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol].quantity += quantity
        else:
            stock = Stock(symbol, quantity)
            self.stocks[symbol] = stock
    
    def remove_stock(self, symbol):
        if symbol in self.stocks:
            del self.stocks[symbol]
        else:
            print("Stock not found in portfolio.")
    
    def update_quantity(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol].quantity = quantity
        else:
            print("Stock not found in portfolio.")
    
    def current_value(self):
        total_value = 0
        for stock in self.stocks.values():
            total_value += stock.current_price() * stock.quantity
        return total_value

    def display_portfolio(self):
        print("Stock\t\tQuantity\tCurrent Price\tTotal Value")
        print("-" * 50)
        for symbol, stock in self.stocks.items():
            current_price = stock.current_price()
            total_value = current_price * stock.quantity
            print(f"{symbol}\t\t{stock.quantity}\t\t${current_price:.2f}\t\t${total_value:.2f}")
        print("-" * 50)
        print(f"Total Portfolio Value: ${self.current_value():.2f}")

if __name__ == "__main__":

    portfolio = Portfolio()
    while True:
        print("\nStock Portfolio Tracker Menu")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Update Quantity")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            symbol = input("Enter stock symbol to add: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(symbol, shares)
            print(f"Added {shares} shares of {symbol} to portfolio.")
        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ").upper()
            portfolio.remove_stock(symbol)
            print(f"{symbol} removed from portfolio.")
        elif choice == '3':
            portfolio.display_portfolio()
        elif choice == '4':
            symbol = input("Enter stock symbol to add: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.update_quantity(symbol,shares)
        elif choice == '5':
            print("Exiting the tracker.")
            break
        else:
            print("Invalid choice. Please try again.")
        
        
        
        

        

        
        
        
        
        
