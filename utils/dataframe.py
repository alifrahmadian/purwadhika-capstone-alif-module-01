import pandas as pd

def convert_to_dataframe(rows, description):
    columns = [col[0] for col in description]
    return pd.DataFrame(rows, columns=columns)