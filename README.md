Forex Price Dashboard

A live forex dashboard that displays real-time exchange rates for 7 currency pairs in a clean web interface.

What it does
Pulls live currency pair prices from the ExchangeRate API and displays them on a auto-refreshing webpage. Built with Python and Flask, deployed with Gunicorn.

Currency pairs
- USD/EUR
- USD/GBP
- USD/JPY
- USD/CAD
- USD/AUD
- EUR/GBP
- GBP/JPY

Tech used
- Python
- Flask
- Gunicorn
- ExchangeRate API
- HTML/CSS

How to run locally
1. Clone the repo
git clone https://github.com/dashya-bit9/forex-dashboard

cd forex-dashboard

2. Install dependencies
pip install -r requirements.txt

3. Add your API key
Create a .env file and add :
FOREX_API_KEY=your_key_here

4. Run the app
python app.py (or python3 for some people)

5. Open your browser and go to 'http://localhost:5000'


Deployment
Deployed using Gunicorn on Render.

Use case
Useful for trader, fintech apps, or any project needing live currency displayed in a simple dashboard. Can be extended to support more pairs, historical charts, or price alerts.
