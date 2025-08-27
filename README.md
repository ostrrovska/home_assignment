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
python fx_rates.py
```