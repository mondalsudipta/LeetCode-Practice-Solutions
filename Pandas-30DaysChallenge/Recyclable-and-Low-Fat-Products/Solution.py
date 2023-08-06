import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products[["product_id", "low_fats", "recyclable"]]
    result_df = df[(df["low_fats"] == "Y") & (df["recyclable"] == "Y")]
    return result_df[["product_id"]]
