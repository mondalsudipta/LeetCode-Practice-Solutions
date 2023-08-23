import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].str.title()
    return users.sort_values("user_id")
