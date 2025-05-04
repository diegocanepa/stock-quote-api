## 📈 Stock Quote API

A lightweight REST API built with **Flask** that allows you to fetch real-time quotes for stocks, bonds, or CEDEARs (Argentinian Depositary Receipts) using Yahoo Finance via the `yfinance` Python package.

---

### 🚀 Available Endpoints

#### `GET api/v1/quotes`

Fetches current market prices for one or more financial instruments.

##### 🔹 Query Parameters:

- `symbols`: a comma-separated list of symbols (e.g. `GGAL.BA,YPFD.BA,TSLA`)

##### 🔹 Example Request:

```bash
curl "http://localhost:5000/api/v1/quotes?symbols=GGAL.BA,YPFD.BA,TSLA"
```

##### 🔹 Example Response (some symbols valid):

```json
[
  {
    "symbol": "GGAL.BA",
    "price": 123.45,
    "date": "2025-05-04 14:30:00"
  },
  {
    "symbol": "TSLA",
    "price": 652.30,
    "date": "2025-05-04 14:30:00"
  }
]
```

##### 🔹 Error Responses

- If the `symbols` query param is missing:

```json
{
  "error": "Missing 'symbols' query param"
}
```

- If none of the provided symbols are valid:

```json
{
  "error": "No valid symbols found",
  "input": ["FOO", "BAR"]
}
```

---

### ⚙️ Local Setup

1. Clone the repository:

```bash
git clone https://github.com/your_username/stock-quote-api.git
cd stock-quote-api
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python -m app.main
```

---

### 🐳 Run with Docker

#### 1. Build the image:

```bash
docker build -t stock-quote-api .
```

#### 2. Run the container:

```bash
docker run -p 5000:5000 stock-quote-api
```