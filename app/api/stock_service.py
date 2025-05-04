from app.utils.stock_utils import fetch_stock_quotes

def get_stock_quotes(symbols: list[str]):
    return fetch_stock_quotes(symbols)

