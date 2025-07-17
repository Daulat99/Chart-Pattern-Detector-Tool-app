import yfinance as yf

def fetch_data(symbol, period='1d', interval='5m'):
    data = yf.download(tickers=symbol, period=period, interval=interval)
    return data
