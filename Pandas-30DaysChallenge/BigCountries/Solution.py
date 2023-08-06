import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    big_df = world[["name", "population", "area"]]
    result_df = big_df[(big_df["area"] >= 3000000) | (big_df["population"] >= 25000000)]
    return result_df
