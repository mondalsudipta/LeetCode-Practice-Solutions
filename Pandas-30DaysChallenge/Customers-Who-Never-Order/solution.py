import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    merge_df = customers.merge(orders, left_on="id", right_on="customerId", how="left")
    result_df = merge_df[merge_df["customerId"].isnull()]
    result_df.rename(columns={"name": "Customers"}, inplace=True)

    return result_df[["Customers"]]
