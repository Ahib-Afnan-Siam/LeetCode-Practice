import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    pivoted = weather.pivot(index='month', columns='city', values='temperature')
    pivoted.columns.name = None
    return pivoted