from flask import Flask, render_template
import requests 
import os
import logging 
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from dotenv import load_dotenv

load_dotenv


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)



FOREX_API_KEY = os.environ.get("FOREX_API_KEY")
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


@retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=8),
        retry=retry_if_exception_type(requests.exceptions.ConnectionError),
        reraise=True
)
def get_forex_data():
    try:
        url = f"https://v6.exchangerate-api.com/v6/{FOREX_API_KEY}/latest/USD"
        logger.info("Fetching forex data from API.")
        response = requests.get(url)
        data = response.json()
        rates = data["conversion_rates"]
        logger.info("Successfully retrieved exchange rates.")
        
        pairs = []
        for base, quote in CURRENCY_PAIRS:
            if base == "USD":
                rate = rates[quote]
                logger.debug("Calculated USD based pair.")
            else:
                rate = rates[quote] / rates[base]
                logger.debug("Calculated cross currency pair.")
        
            pairs.append({
                "pair": f"{base}/{quote}",
                "rate": round(rate, 5)
            })

        return pairs
    except requests.exceptions.ConnectionError:
        logger.error("Failed to connect to the API, check your internet connection.")
        return []
    except requests.exceptions.Timeout:
        logger.error("Request timed out, the API took too long to respond.")
        return []
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error occured: {e}")
        return []
    except Exception as e:
        logging.critical(f"Unexpected error in get_forex_data: {e}")
        return []
    


@app.route("/")

def index():
    pairs = get_forex_data()
    return render_template("index.html", pairs=pairs)

if __name__ == "__main__":
    app.run(debug=True)
