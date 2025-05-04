import logging
import yfinance as yf

logger = logging.getLogger(__name__)

def fetch_stock_quotes(symbols: list[str]):
    quotes = []
    for symbol in symbols:
        quote = fetch_stock_quote(symbol)
        if quote:
            quotes.append(quote)
    logger.info(f"Successfully fetched {len(quotes)} quotes from {len(symbols)} requested symbols")
    return quotes

def fetch_stock_quote(symbol: str):
    try:
        ticker = yf.Ticker(symbol)
        history = ticker.history(period="1d")

        if history.empty:
            logger.error(f"Invalid or no data for symbol: {symbol}")
            return None

        latest_data = history.iloc[-1]
        return {
            "symbol": symbol,
            "price": latest_data["Close"],
            "date": latest_data.name.strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as e:
        logger.exception(f"Error fetching data for symbol: {symbol} — {e}")
        return None