import sys
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
            "INSERT OR IGNORE INTO rates (series_id, date, value) VALUES (?, ?, ?)",
            (data['seriesId'], data['date'], data['value']),
        )
    conn.commit()
    conn.close()


def main():
    try:
        print("Starting the FX rates update process...")
        init_db()
        data = get_observations()
        if data:
            save_to_db(data)
            print("FX rates updated successfully!")
        else:
            print("No new FX rates found.")

    except sqlite3.Error as e:
        print(f"An error with database occurred: {e}")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"A network error occurred while fetching data: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

    print("Process completed.")


if __name__ == "__main__":
    main()
