from flask import Blueprint, jsonify, request
from app.api.stock_service import get_stock_quotes

stock_api = Blueprint('stock_api', __name__)

@stock_api.route("/quotes", methods=["GET"])
def get_quotes():
    symbols_param = request.args.get("symbols")
    if not symbols_param:
        return jsonify({"error": "Missing 'symbols' query param"}), 400

    symbols = [s.strip().upper() for s in symbols_param.split(",")]
    quotes = get_stock_quotes(symbols)

    if not quotes:
        return jsonify({
            "error": "No valid symbols found",
            "input": symbols
        }), 404

    return jsonify(quotes)