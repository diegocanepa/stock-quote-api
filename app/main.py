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

# Create the Flask application
app = Flask(__name__)

# Register routes
app.register_blueprint(stock_api, url_prefix=f"/api/{API_VERSION}")

if __name__ == "__main__":
    app.run(debug=True)
    
    
