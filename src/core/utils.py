import pandas as pd
from settings import DATA_FILE


def __get_data():
    """
    Read and return as Pandas DataFrame all data in DATA_FILE
    """
    return pd.read_csv(DATA_FILE)


def _validate_filter(values, filter):
    return filter in values
