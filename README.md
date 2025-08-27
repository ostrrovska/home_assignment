# FX Rates Fetcher

Fetches the latest FX rates from the Swedish Riksbank API and stores them in a local SQLite database.

## Requirements

- Python 3.10.8
- [Poetry](https://python-poetry.org/) for dependency management
- Internet connection to access the Riksbank API

## Setup

1. Clone this repository:

```bash
git clone https://github.com/ostrrovska/home_assignment.git
cd home_assignment
```

2. Install dependencies with Poetry:

```bash
poetry install
```

3. Run the script

```bash
poetry run python fx_rates.py
```

## Viewing the Database

The script creates a local SQLite database file named `fx_rates.db`. You can inspect its contents using the `sqlite3` command-line tool, which typically comes with Python.

1.  Open a terminal in the project directory and connect to the database:
    ```bash
    sqlite3 fx_rates.db
    ```

2.  Once you are inside the SQLite prompt, you can use the following commands.

    *   To see the structure (schema) of the `rates` table:
        ```sql
        .schema rates
        ```

    *   For a more readable, table-like output, it's best to first enable headers and set the output mode to `column`:
        ```sql
        .headers on
        .mode column
        ```

    *   Now, to see all the data stored in the `rates` table:
        ```sql
        SELECT * FROM rates;
        ```

    *   If the table contains many entries, you can limit the output to the first 10 rows:
        ```sql
        SELECT * FROM rates LIMIT 10;
        ```

3.  To exit the SQLite prompt, simply type:
    ```sql
    .quit
    ```