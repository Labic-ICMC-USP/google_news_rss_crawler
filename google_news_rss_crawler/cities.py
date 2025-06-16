import pandas as pd

def load_cities(csv_path):
    """
    Load city data from a CSV file.
    Expected columns: City, State, Country, LATITUDE, LONGITUDE
    """
    return pd.read_csv(csv_path)
