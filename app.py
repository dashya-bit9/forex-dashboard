from flask import Flask, render_template
import requests 
from config import FOREX_API_KEY

app = Flask(__name__)

CURRENCY_PAIRS = [
    ("USD", "EUR"),
    ("USD", "GBP"),
    ("USD", "JPY"),
    ("USD", "CAD"),
    ("USD", "AUD"),
    ("EUR", "GBP"),
    ("GBP", "JPY"),
]


def get_forex_data():
    url = f"https://v6.exchangerate-api.com/v6/{FOREX_API_KEY}/latest/USD"
    response = requests.get(url)
    data = response.json()
    rates = data["conversion_rates"]
    
    pairs = []
    for base, quote in CURRENCY_PAIRS:
        if base == "USD":
            rate = rates[quote]
        else:
            rate = rates[quote] / rates[base]
        
        pairs.append({
            "pair": f"{base}/{quote}",
            "rate": round(rate, 5)
        })

    return pairs


@app.route("/")

def index():
    pairs = get_forex_data()
    return render_template("index.html", pairs=pairs)

if __name__ == "__main__":
    app.run(debug=True)
