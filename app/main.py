import logging
from flask import Flask
from app.api.stock_routes import stock_api

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

API_VERSION="v1"

def create_app():
    app = Flask(__name__)
    app.register_blueprint(stock_api, url_prefix=f"/api/{API_VERSION}")
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
