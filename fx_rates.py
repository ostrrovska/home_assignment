import requests
import sqlite3


def init_db():
    with open('db_init.sql', 'r', encoding='utf-8') as f:
        sql_script = f.read()
    conn = sqlite3.connect('fx_rates.db')
    cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()


def get_observations():
    url = f"https://api.riksbank.se/swea/v1/Observations/Latest/ByGroup/{130}"
    response = requests.get(url)
    data = response.json()
    return data


def save_to_db(data):
    conn = sqlite3.connect('fx_rates.db')
    cursor = conn.cursor()
    for data in data:
        cursor.execute(
            "INSERT INTO rates (series_id, date, value) VALUES (?, ?, ?)",
            (data['seriesId'], data['date'], data['value']),
        )
    conn.commit()
    conn.close()


init_db()
data = get_observations()
save_to_db(data)
