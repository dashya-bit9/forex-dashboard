import sqlite3
import logging
from datetime import datetime


logger = logging.getLogger(__name__)


def init_db():
    conn = sqlite3.connect("forex_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pair TEXT NOT NULL, 
            rate REAL NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    logger.info("Database initialized successfully.")



def save_rates(pairs):
    conn = sqlite3.connect("forex_data.db")
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for pair in pairs:
        cursor.execute("""
            INSERT INTO rates (pair, rate, timestamp)
            VALUES (?, ?, ?)
        """, (pair["pair"], pair["rate"], timestamp))
        logger.debug(f"Saved {pair['pair']} at rate {pair['rate']}")
    
    conn.commit()
    conn.close()
    logger.info(f"Saved {len(pairs)} pairs to database.")